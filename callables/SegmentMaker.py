#-*- encoding: utf-8 -*-
import collections
import os
from abjad import *
from plague_water import plague_water_configuration
from plague_water import score_templates


class SegmentMaker(abctools.AbjadObject):

    ### SCORE-LEVEL VARIABLES ###

    measure_segmentation_talea = None

    minimum_timespan_duration = None

    permitted_time_signatures = None

    segment_name = None

    segment_target_duration = None

    tempo = None

    ### VOICE-LEVEL VARIABLES ###

    guitar_brush = None

    piano_right_hand_brush = None

    piano_left_hand_brush = None

    percussion_right_hand_brush = None

    percussion_left_hand_brush = None

    saxophone_brush = None

    ### INITIALIZER ###

    def __init__(self):
        from plague_water import callables
        assert isinstance(self.guitar_brush,
            (callables.Brush, type(None)))
        assert isinstance(self.measure_segmentation_talea,
            collections.Iterable) and \
            all(isinstance(x, int) and 0 < x
                for x in self.measure_segmentation_talea)
        assert isinstance(self.minimum_timespan_duration, Duration) and \
            0 < self.minimum_timespan_duration < 1
        assert isinstance(self.percussion_left_hand_brush,
            (callables.Brush, type(None)))
        assert isinstance(self.percussion_right_hand_brush,
            (callables.Brush, type(None)))
        assert isinstance(self.permitted_time_signatures,
            collections.Iterable) and \
            self.permitted_time_signatures and \
            all(isinstance(x, TimeSignature)
                for x in self.permitted_time_signatures)
        assert isinstance(self.piano_left_hand_brush,
            (callables.Brush, type(None)))
        assert isinstance(self.piano_right_hand_brush,
            (callables.Brush, type(None)))
        assert isinstance(self.saxophone_brush,
            (callables.Brush, type(None)))
        assert isinstance(self.segment_target_duration, Duration) and \
            1 <= self.segment_target_duration
        assert isinstance(self.segment_name, str) and self.segment_name
        assert isinstance(self.tempo, Tempo)

    ### SPECIAL METHODS ###

    def __call__(self):
        template = score_templates.PlagueWaterScoreTemplate()
        self.score = template()
        self.meters, self.time_signatures, self.timespan_mapping = \
            self.build_meters_time_signatures_and_timespan_mapping()
        self.populate_time_signature_context()
        self.populate_semantic_voice_contexts()
        self.configure_score(self.score)
        self.lilypond_file = lilypondfiletools.make_basic_lilypond_file(
            self.score)
        self.configure_lilypond_file(self.lilypond_file)
        return self.lilypond_file

    def __repr__(self):
        return '<Segment: {!r}>'.format(self.segment_name)

    ### PUBLIC METHODS ###

    @classmethod
    def build_and_persist(class_, current_file_path):
        segment = class_()
        lilypond_file = segment()
        current_directory_path = os.path.dirname(os.path.abspath(
            os.path.expanduser(current_file_path)))
        lilypond_file_path = os.path.join(current_directory_path, 'output.ly')
        persist(lilypond_file).as_ly(lilypond_file_path)
        pdf_file_path = os.path.join(current_directory_path, 'output.pdf')
        persist(lilypond_file).as_pdf(pdf_file_path)

    def build_meters_time_signatures_and_timespan_mapping(self):
        timespan_mapping = {}
        offset_counter = datastructuretools.TypedCounter(
            item_class=Offset,
            )
        for voice in iterate(self.score).by_class(Voice):
            timespan_inventory = timespantools.TimespanInventory()
            timespan_mapping[voice.name] = timespan_inventory
            current_offset = Offset(0)
            while current_offset < self.segment_target_duration:
                rest_duration = self.resting_duration_cursor()[0]
                current_offset += rest_duration
                if self.segment_target_duration <= current_offset:
                    break
                play_grouping = self.playing_grouping_cursor()[0]
                for play_duration in self.playing_duration_cursor(
                    play_grouping):
                    next_offset = current_offset + play_duration
                    if self.segment_target_duration <= next_offset:
                        break
                    timespan = timespantools.Timespan(
                        start_offset=current_offset,
                        stop_offset=next_offset,
                        )
                    offset_counter[current_offset] += 1
                    offset_counter[next_offset] += 1
                    timespan_inventory.append(timespan)
                    current_offset = next_offset
        meters = metertools.Meter.fit_meters_to_expr(
            offset_counter,
            self.permitted_time_signatures,
            )
        meters = tuple(meters)
        time_signatures = tuple(x.implied_time_signature for x in meters)
        if self.measure_segmentation_talea:
            current_offset = Offset(0)
            groups = sequencetools.partition_sequence_by_counts(
                time_signatures,
                self.measure_segmentation_talea,
                cyclic=True,
                overhang=True,
                )
            for group in groups:
                current_offset += sum(x.duration for x in group)
                for voice_name, timespan_inventory in timespan_mapping.items():
                    new_timespan_inventory = \
                        timespantools.TimespanInventory()
                    for shard in timespan_inventory.split_at_offset(
                        current_offset):
                        new_timespan_inventory.extend(shard)
                    timespan_mapping[voice_name] = new_timespan_inventory
        for voice_name, timespan_inventory in timespan_mapping.items():
            timespan_inventory[:] = [x for x in timespan_inventory
                if self.minimum_timespan_duration <= x.duration]
        return meters, time_signatures, timespan_mapping

    def configure_score(self, score):
        override(score).horizontal_bracket.color = 'red'
        rehearsal_mark = indicatortools.LilyPondCommand(r'mark \default')
        attach(rehearsal_mark, score['TimeSignatureContext'][0],
            scope=scoretools.Context)
        attach(self.tempo, score['TimeSignatureContext'][0])
        score.add_double_bar()
        right_column = markuptools.MarkupCommand(
            'right-column', [
                ' ',
                ' ',
                ' ',
                'Jamaica Plain',
                'December 2013 - February 2014',
                ],
            )
        italic = markuptools.MarkupCommand(
            'italic',
            right_column,
            )
        final_markup = Markup(italic, 'down')
        score.add_final_markup(final_markup)

    def configure_lilypond_file(self, lilypond_file):
        #title = 'Plague Water ({})'.format(self.segment_name)
        #lilypond_file.header_block.title = Markup(title)
        lilypond_file.remove(lilypond_file.header_block)
        lilypond_file.remove(lilypond_file.layout_block)
        lilypond_file.remove(lilypond_file.paper_block)
        for file_path in plague_water_configuration.stylesheets_file_paths:
            lilypond_file.file_initial_user_includes.append(file_path)
        lilypond_file.default_paper_size = '11x17', 'landscape'
        lilypond_file.global_staff_size = 14

    def populate_semantic_voice_contexts(self):
        measure_durations = [x.duration for x in self.time_signatures]
        measure_offsets = mathtools.cumulative_sums(
            measure_durations)
        actual_segment_target_duration = sum(measure_durations)
        note_maker = rhythmmakertools.NoteRhythmMaker()
        rest_maker = rhythmmakertools.RestRhythmMaker()
        for voice_name, timespan_inventory in self.timespan_mapping.items():
            message = 'VOICE: {}'.format(voice_name)
            plague_water_configuration.debug(message)
            voice = self.score[voice_name]
            current_offset = Offset(0)
            for group in timespan_inventory.partition(
                include_tangent_timespans=True):
                group_start_offset = group[0].start_offset
                group_stop_offset = group[-1].stop_offset
                rest_duration = group_start_offset - current_offset
                if rest_duration:
                    rests = sequencetools.flatten_sequence(
                        rest_maker((rest_duration,)))
                    rest_container = Container(rests)
                    voice.append(rest_container)
                notes = note_maker((x.duration for x in group))
                note_containers = [Container(x) for x in notes]
                bracket = spannertools.HorizontalBracketSpanner()
                attach(bracket, note_containers)
                voice.extend(note_containers)
                current_offset = group_stop_offset
            rest_duration = actual_segment_target_duration - current_offset
            if rest_duration:
                rests = sequencetools.flatten_sequence(
                    rest_maker((rest_duration,)))
                rest_container = Container(rests)
                voice.append(rest_container)
            for i, shard in enumerate(mutate(voice[:]).split(
                measure_durations)):
                message = '\tSHARD: {}'.format(shard)
                plague_water_configuration.debug(message)
                meter = self.meters[i]
                measure_offset = measure_offsets[i]
                for cell in shard:
                    cell_timespan = inspect(cell).get_timespan()
                    cell_start_offset = cell_timespan.start_offset
                    relative_offset = cell_start_offset - measure_offset
                    message = '\t\tCELL: {} @ {}'.format(cell, relative_offset)
                    plague_water_configuration.debug(message)
                    mutate(cell[:]).rewrite_meter(
                        meter,
                        #boundary_depth=1,
                        initial_offset=relative_offset,
                        )
            beam = spannertools.MeasuredComplexBeam()
            attach(beam, voice.select_leaves())

    def populate_time_signature_context(self):
        measures = scoretools.make_spacer_skip_measures(
            self.time_signatures)
        self.score['TimeSignatureContext'].extend(measures)
