# -*- encoding: utf-8 -*-
from abjad import *


class PitchClassTransformExpression(abctools.AbjadObject):
    r'''A pitch-class transform expression.

    ::

        >>> from plague_water import makers
        >>> pitch_class_transform= makers.PitchClassTransformExpression(
        ...     inversion=True,
        ...     transposition=3,
        ...     )
        >>> print format(pitch_class_transform)
        makers.PitchClassTransformExpression(
            inversion=True,
            transposition=3,
            )

    ::

        >>> pitch_classes = pitchtools.PitchClassSegment([0, 1, 4])
        >>> pitch_class_transform(pitch_classes)
        PitchClassSegment([3, 2, 11])

    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        '_inversion',
        '_retrogression',
        '_rotation',
        '_transposition',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        inversion=None,
        retrogression=None,
        rotation=None,
        transposition=None,
        ):
        assert inversion in (True, False, None)
        assert retrogression in (True, False, None)
        assert isinstance(rotation, (int, type(None)))
        assert isinstance(transposition, (int, type(None)))
        if transposition is not None:
            assert -12 < transposition < 12
        self._inversion = inversion
        self._retrogression = retrogression
        self._rotation = rotation
        self._transposition = transposition

    ### SPECIAL METHODS ###

    def __call__(self, pitch_classes):
        assert isinstance(pitch_classes, pitchtools.PitchClassSegment)
        if self.rotation:
            pitch_classes = pitch_classes.rotate(self.rotation, transpose=True)
        if self.inversion:
            pitch_classes = pitch_classes.invert()
        if self.transposition is not None:
            pitch_classes = pitch_classes.transpose(self.transposition)
        if self.retrogression:
            pitch_classes = pitch_classes.retrograde()
        return pitch_classes

    def __eq__(self, expr):
        return systemtools.StorageFormatManager.compare(self, expr)

    def __hash__(self):
        hash_values = systemtools.StorageFormatManager.get_hash_values(self)
        return hash(hash_values)

    ### PUBLIC PROPERTIES ###

    @property
    def inversion(self):
        return self._inversion

    @property
    def retrogression(self):
        return self._retrogression

    @property
    def rotation(self):
        return self._rotation

    @property
    def transposition(self):
        return self._transposition
