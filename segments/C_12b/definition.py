# -*- encoding: utf-8 -*-
from abjad import *
from plague_water import makers
from plague_water.segments import C_palette

### BASE SEGMENT MAKER ###

base_segment_maker = C_palette.segment_maker

### SEGMENT PARAMETERS ###

segment_id = '12b'
denominator = 106
numerator = 7
outer_numerator = 12
segment_name = 'Segment {} ({}:{}) ({}:{})'.format(
    segment_id,
    outer_numerator,
    denominator,
    numerator,
    outer_numerator,
    )

segment_tempo = indicatortools.Tempo(durationtools.Duration(1, 4), 40)
target_segment_duration = makers.SegmentMaker.get_segment_target_duration(
    denominator=denominator,
    numerator=numerator,
    tempo=segment_tempo,
    total_duration_in_seconds=480,
    )

### CONTEXT MAP ###

context_map = base_segment_maker.context_map.copy()

### BRUSHES ###

cursor_transform = makers.CursorTransform(
    increment=40,
    reverse=True,
    )

guitar_timespan_maker = new(
    base_segment_maker['Guitar Voice'].transform_cursors(cursor_transform),
    )

saxophone_timespan_maker = new(
    base_segment_maker['Saxophone Voice'].transform_cursors(cursor_transform),
    )

piano_rh_timespan_maker = new(
    base_segment_maker['Piano RH Voice'].transform_cursors(cursor_transform),
    )

piano_lh_timespan_maker = new(
    base_segment_maker['Piano LH Voice'].transform_cursors(cursor_transform),
    )

percussion_rh_timespan_maker = new(
    base_segment_maker['Percussion RH Voice'].transform_cursors(cursor_transform),
    )

percussion_lh_timespan_maker = new(
    base_segment_maker['Percussion LH Voice'].transform_cursors(cursor_transform),
    )

### SEGMENT DEFINITION ###

segment_maker = new(
    base_segment_maker,
    context_map=context_map,
    segment_id=segment_id,
    segment_name=segment_name,
    segment_tempo=segment_tempo,
    target_segment_duration=target_segment_duration,
    timespan_makers=(
        guitar_timespan_maker,
        percussion_lh_timespan_maker,
        percussion_rh_timespan_maker,
        piano_lh_timespan_maker,
        piano_rh_timespan_maker,
        saxophone_timespan_maker,
        )
    )

### MAIN ###

if __name__ == '__main__':
    segment_maker.build_and_persist(__file__)
