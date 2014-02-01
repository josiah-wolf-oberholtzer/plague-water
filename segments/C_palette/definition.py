# -*- encoding: utf-8 -*-
from abjad import new
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import indicatortools
from plague_water import makers
from plague_water import materials
from plague_water import score_templates

### SEGMENT PARAMETERS ###

measure_segmentation_talea = (1,)
permitted_time_signatures = materials.square_time_signatures
segment_tempo = indicatortools.Tempo(durationtools.Duration(1, 4), 80)

### CONTEXT MAP ###

score_template = score_templates.PlagueWaterScoreTemplate()
score = score_template()
context_map = datastructuretools.ContextMap(score_template)
context_map[score]['minimum_timespan_duration'] = durationtools.Duration(1, 8)
context_map[score]['pitch_class_maker'] = makers.PitchClassMaker(
    pitch_class_ratio=(1, 1, 1),
    pitch_class_talea=(
        [0, 3, 2, 5, 11, 1],
        [2, 8, 10, 11],
        [1, 4],
        ),
    transform_ratio=None,
    transform_talea=None,
    )

### BRUSHES ###

guitar_brush = makers.Brush(
    music_makers=[
        makers.MusicMaker(
            leading_rest_durations=materials.short_durations(1),
            playing_durations=materials.short_durations(2),
            playing_groupings=materials.short_groupings(3),
            ),
        ],
    )

saxophone_brush = makers.Brush(
    initial_music_maker=makers.MusicMaker(
        leading_rest_durations=materials.short_durations(4),
        playing_durations=materials.long_durations(10),
        playing_groupings=materials.short_groupings(5),
        ),
    music_makers=[
        makers.MusicMaker(
            leading_rest_durations=materials.short_durations(6),
            playing_durations=materials.long_durations(7),
            playing_groupings=materials.medium_groupings(8),
            ),
        ],
    )

piano_rh_brush = makers.Brush(
    music_makers=[
        makers.MusicMaker(
            leading_rest_durations=materials.medium_durations(9),
            playing_durations=materials.very_short_durations(10),
            playing_groupings=materials.short_groupings(11),
            ),
        ],
    )

piano_lh_brush = makers.Brush(
    music_makers=[
        makers.MusicMaker(
            leading_rest_durations=materials.medium_durations(12),
            playing_durations=materials.very_short_durations(13),
            playing_groupings=materials.short_groupings(14),
            ),
        ],
    )

percussion_rh_brush = makers.Brush(
    music_makers=[
        makers.MusicMaker(
            leading_rest_durations=materials.medium_durations(15),
            playing_durations=materials.short_durations(16),
            playing_groupings=materials.short_groupings(17),
            ),
        ],
    )

percussion_lh_brush = makers.Brush(
    initial_music_maker=makers.MusicMaker(
        leading_rest_durations=materials.short_durations(18),
        playing_durations=materials.long_durations(12),
        playing_groupings=materials.short_groupings(19),
        ),
    music_makers=[
        makers.MusicMaker(
            leading_rest_durations=materials.short_durations(20),
            playing_durations=materials.long_durations(21),
            playing_groupings=materials.medium_groupings(22),
            ),
        ],
    )

### SEGMENT DEFINITION ###

segment_maker = makers.SegmentMaker(
    context_map=context_map,
    guitar_brush=guitar_brush,
    is_final_segment=False,
    measure_segmentation_talea=measure_segmentation_talea,
    percussion_rh_brush=percussion_rh_brush,
    percussion_lh_brush=percussion_lh_brush,
    permitted_time_signatures=permitted_time_signatures,
    piano_lh_brush=piano_lh_brush,
    piano_rh_brush=piano_rh_brush,
    saxophone_brush=saxophone_brush,
    segment_tempo=segment_tempo,
    )
