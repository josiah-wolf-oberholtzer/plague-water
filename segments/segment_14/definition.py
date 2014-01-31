# -*- encoding: utf-8 -*-
from abjad import *
from plague_water import makers
from plague_water.segments import palette_d

### BASE SEGMENT MAKER ###

base_segment_maker = palette_d.segment_maker

### SEGMENT PARAMETERS ###

segment_id = 14
numerator = 9
denominator = 106
segment_name = 'Segment {} ({}:{})'.format(
    segment_id,
    numerator,
    denominator,
    )

target_segment_duration = makers.SegmentMaker.get_segment_target_duration(
    denominator=denominator,
    numerator=numerator,
    tempo=base_segment_maker.segment_tempo,
    total_duration_in_seconds=480,
    )

### CONTEXT MAP ###

context_map = base_segment_maker.context_map.copy()

### BRUSHES ###

cursor_transform = None

guitar_brush = new(
    base_segment_maker.guitar_brush.transform_cursors(cursor_transform),
    )

saxophone_brush = new(
    base_segment_maker.saxophone_brush.transform_cursors(cursor_transform),
    )

piano_rh_brush = new(
    base_segment_maker.piano_rh_brush.transform_cursors(cursor_transform),
    )

piano_lh_brush = new(
    base_segment_maker.piano_lh_brush.transform_cursors(cursor_transform),
    )

percussion_rh_brush = new(
    base_segment_maker.percussion_rh_brush.transform_cursors(cursor_transform),
    )

percussion_lh_brush = new(
    base_segment_maker.percussion_lh_brush.transform_cursors(cursor_transform),
    )

### SEGMENT DEFINITION ###

segment_maker = new(
    base_segment_maker,
    guitar_brush=guitar_brush,
    percussion_lh_brush=percussion_lh_brush,
    percussion_rh_brush=percussion_rh_brush,
    piano_lh_brush=piano_lh_brush,
    piano_rh_brush=piano_rh_brush,
    saxophone_brush=saxophone_brush,
    segment_id=segment_id,
    segment_name=segment_name,
    target_segment_duration=target_segment_duration,
    )

### MAIN ###

if __name__ == '__main__':
    segment_maker.build_and_persist(__file__)
