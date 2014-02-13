# -*- encoding: utf-8 -*-
from abjad import new
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import indicatortools
from abjad.tools import spannertools
from plague_water import makers
from plague_water import materials
from plague_water import score_templates

### SEGMENT PARAMETERS ###

measure_segmentation_talea = (1,)
permitted_time_signatures = materials.square_time_signatures
segment_tempo = indicatortools.Tempo(durationtools.Duration(1, 4), 72)

### CONTEXT MAP ###

score_template = score_templates.PlagueWaterScoreTemplate()
score = score_template()
context_map = datastructuretools.ContextMap(score_template)
context_map[score]['minimum_timespan_duration'] = durationtools.Duration(1, 8)
context_map[score]['pitch_agent'] = makers.PitchClassAgent(
    pitch_class_ratio=(1, 1, 1),
    pitch_class_talea=(
        [0, 3, 2, 5, 11, 1],
        [2, 8, 10, 11],
        [1, 4],
        ),
    transform_ratio=None,
    transform_talea=None,
    )

### SEMANTIC CONTEXT MAKERS ###

guitar_context_maker = makers.ContextMaker(
    context_name='Guitar Voice',
    music_makers=[
        makers.MusicMaker(
            dynamic_agent=materials.background_dynamic_agent,
            grace_maker=makers.GraceAgent(
                lengths=(0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1),
                ),
            indicator_agent=makers.IndicatorAgent(
                last_leaf_indicators=(
                    indicatortools.BendAfter(-4),
                    indicatortools.BendAfter(4),
                    ),
                ),
            rhythm_maker=materials.pointillist_rhythm_maker,
            timespan_agent=new(
                materials.pointillist_sparse_timespan_agent,
                playing_durations=materials.short_durations,
                ),
            ).transform_cursors(5),
        ],
    )

saxophone_context_maker = makers.ContextMaker(
    context_name='Saxophone Voice',
    music_makers=[
        makers.MusicMaker(
            dynamic_agent=materials.foreground_dynamic_agent,
            grace_maker=makers.GraceAgent(
                lengths=(0, 0, 2, 1, 3, 1, 1, 0, 2, 1),
                ),
            rhythm_maker=materials.flowing_rhythm_maker,
            spanner_agent=materials.trilling_sparsely_spanner_agent,
            timespan_agent=materials.sustained_long_timespan_agent,
            ).transform_cursors(2),
        ],
    )

piano_rh_context_maker = makers.ContextMaker(
    context_name='Piano RH Voice',
    music_makers=[
        makers.MusicMaker(
            dynamic_agent=materials.background_dynamic_agent,
            labels='pedaled',
            rhythm_maker=materials.pointillist_rhythm_maker,
            spanner_agent=materials.trilling_constantly_spanner_agent,
            timespan_agent=new(
                materials.pointillist_sparse_timespan_agent,
                playing_durations=materials.very_short_durations,
                playing_groupings=[1],
                ),
            ).transform_cursors(6),
        ],
    )

piano_lh_context_maker = makers.ContextMaker(
    context_name='Piano LH Voice',
    music_makers=[
        makers.MusicMaker(
            dynamic_agent=materials.background_dynamic_agent,
            labels='pedaled',
            rhythm_maker=materials.pointillist_rhythm_maker,
            spanner_agent=materials.trilling_constantly_spanner_agent,
            timespan_agent=new(
                materials.pointillist_sparse_timespan_agent,
                playing_durations=materials.very_short_durations,
                playing_groupings=[1],
                ),
            ).transform_cursors(4),
        ],
    )

percussion_shaker_context_maker = makers.ContextMaker(
    context_name='Percussion Shaker Voice',
    music_makers=[
        materials.silent_music_maker,
        ],
    )

percussion_woodblock_context_maker = makers.ContextMaker(
    context_name='Percussion Woodblock Voice',
    music_makers=[
        makers.MusicMaker(
            dynamic_agent=materials.midground_dynamic_agent,
            grace_maker=makers.GraceAgent(
                lengths=(0, 0, 0, 1, 0, 1, 1, 0, 1, 1),
                ),
            indicator_agent=makers.IndicatorAgent(
                first_leaf_indicators=('accent',),
                inner_leaf_indicators=('staccato',),
                ),
            pitch_agent=new(
                materials.woodblock_pitch_agent,
                talea=(0, 2, 4, 2, 3, 0, 1, 2),
                ),
            rhythm_maker=materials.pointillist_rhythm_maker,
            timespan_agent=new(
                materials.pointillist_sparse_timespan_agent,
                playing_durations=materials.short_durations,
                ),
            ).transform_cursors(5),
        ],
    )

percussion_drum_context_maker = makers.ContextMaker(
    context_name='Percussion Drum Voice',
    music_makers=[
        makers.MusicMaker(
            dynamic_agent=materials.midground_dynamic_agent,
            grace_maker=makers.GraceAgent(
                lengths=(0, 0, 0, 1, 0, 1, 1, 0, 1, 1),
                ),
            indicator_agent=makers.IndicatorAgent(
                first_leaf_indicators=('accent',),
                ),
            pitch_agent=new(
                materials.drum_pitch_agent,
                talea=(0, 2, 1, 2, 0, 1, 2),
                ),
            rhythm_maker=materials.flowing_rhythm_maker,
            spanner_agent=makers.SpannerAgent(
                cyclical_logical_tie_spanners=(
                    makers.StemTremoloSpanner(),
                    makers.StemTremoloSpanner(),
                    None,
                    ),
                minimum_logical_tie_duration=durationtools.Duration(1, 8),
                ),
            timespan_agent=materials.sustained_long_timespan_agent,
            ).transform_cursors(1),
        ],
    )

### DEPENDENT CONTEXT MAKERS ###

piano_pedals_context_maker = makers.ContextMaker(
    context_dependencies=(
        'Piano LH Voice',
        'Piano RH Voice',
        ),
    context_name='Piano Pedals',
    music_makers=[
        new(materials.piano_pedals_music_maker,
            spanner_agent=makers.SpannerAgent(
                cyclical_output_spanners=(
                    makers.ComplexPianoPedalSpanner(
                        include_inner_leaves=False,
                        let_vibrate=True,
                        ),
                    ),
                ),
            ),
        ],
    )

### SEGMENT DEFINITION ###

segment_maker = makers.SegmentMaker(
    context_map=context_map,
    is_final_segment=False,
    measure_segmentation_talea=measure_segmentation_talea,
    permitted_time_signatures=permitted_time_signatures,
    segment_tempo=segment_tempo,
    context_makers=(
        guitar_context_maker,
        percussion_drum_context_maker,
        percussion_shaker_context_maker,
        percussion_woodblock_context_maker,
        piano_lh_context_maker,
        piano_pedals_context_maker,
        piano_rh_context_maker,
        saxophone_context_maker,
        )
    )
