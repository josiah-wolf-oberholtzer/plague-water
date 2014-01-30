# -*- encoding: utf-8 -*-
from abjad.tools import datastructuretools
from abjad.tools import durationtools
from abjad.tools import systemtools
from abjad.tools import timespantools
from plague_water.makers.Maker import Maker


class Brush(Maker):

    ### CLASS VARIABLES ###

    __slots__ = (
        '_initial_music_maker',
        '_music_maker_indices',
        '_music_makers',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        initial_music_maker=None,
        music_maker_indices=None,
        music_makers=None,
        ):
        from plague_water import makers
        assert isinstance(initial_music_maker, (makers.MusicMaker, type(None)))
        self._initial_music_maker = initial_music_maker
        if music_maker_indices is not None:
            music_maker_indices = tuple(int(x) for x in music_maker_indices)
        self._music_maker_indices = music_maker_indices
        if music_makers is not None:
            assert initial_music_maker or len(music_makers)
            assert all(isinstance(x, makers.MusicMaker)
                for x in music_makers)
            music_makers = tuple(music_makers)
        self._music_makers = music_makers

    ### SPECIAL METHODS ###

    def __call__(
        self,
        target_segment_duration,
        context_map=None,
        context_name=None,
        ):
        current_offset = durationtools.Offset(0)
        timespan_inventory = timespantools.TimespanInventory()
        message = '\t\t{}'.format(context_name)
        with systemtools.ProgressIndicator(message) as progress_indicator:
            if self.initial_music_maker is not None:
                music_maker_timespan_inventory, current_offset = \
                    self.initial_music_maker.create_timespans(
                        current_offset,
                        target_segment_duration,
                        )
                timespan_inventory.extend(music_maker_timespan_inventory)
                progress_indicator.advance()
            if self.music_makers:
                music_makers = datastructuretools.CyclicTuple(
                    self.music_makers)
                if not self.music_maker_indices:
                    music_maker_indices = datastructuretools.CyclicTuple(
                        range(len(self.music_makers)))
                else:
                    music_maker_indices = datastructuretools.CyclicTuple(
                        self.music_maker_indices)
                counter = 0
                while current_offset < target_segment_duration:
                    music_maker_index = music_maker_indices[counter]
                    music_maker = music_makers[music_maker_index]
                    music_maker_timespan_inventory, current_offset = \
                        music_maker.create_timespans(
                            current_offset,
                            target_segment_duration,
                            )
                    timespan_inventory.extend(music_maker_timespan_inventory)
                    counter += 1
                    progress_indicator.advance()
        return timespan_inventory

    ### PUBLIC PROPERTIES ###

    @property
    def initial_music_maker(self):
        return self._initial_music_maker

    @property
    def music_maker_indices(self):
        return self._music_maker_indices

    @property
    def music_makers(self):
        return self._music_makers
