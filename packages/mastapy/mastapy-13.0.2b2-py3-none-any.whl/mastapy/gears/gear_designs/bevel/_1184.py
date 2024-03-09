"""BevelMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.agma_gleason_conical import _1197
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Bevel", "BevelMeshedGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _956
    from mastapy.gears.gear_designs.straight_bevel import _965
    from mastapy.gears.gear_designs.straight_bevel_diff import _969
    from mastapy.gears.gear_designs.spiral_bevel import _973
    from mastapy.gears.gear_designs.conical import _1160
    from mastapy.gears.gear_designs import _949


__docformat__ = "restructuredtext en"
__all__ = ("BevelMeshedGearDesign",)


Self = TypeVar("Self", bound="BevelMeshedGearDesign")


class BevelMeshedGearDesign(_1197.AGMAGleasonConicalMeshedGearDesign):
    """BevelMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _BEVEL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelMeshedGearDesign")

    class _Cast_BevelMeshedGearDesign:
        """Special nested class for casting BevelMeshedGearDesign to subclasses."""

        def __init__(
            self: "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign",
            parent: "BevelMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign",
        ) -> "_1197.AGMAGleasonConicalMeshedGearDesign":
            return self._parent._cast(_1197.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign",
        ) -> "_1160.ConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.conical import _1160

            return self._parent._cast(_1160.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign",
        ) -> "_949.GearDesignComponent":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.GearDesignComponent)

        @property
        def zerol_bevel_meshed_gear_design(
            self: "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign",
        ) -> "_956.ZerolBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _956

            return self._parent._cast(_956.ZerolBevelMeshedGearDesign)

        @property
        def straight_bevel_meshed_gear_design(
            self: "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign",
        ) -> "_965.StraightBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _965

            return self._parent._cast(_965.StraightBevelMeshedGearDesign)

        @property
        def straight_bevel_diff_meshed_gear_design(
            self: "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign",
        ) -> "_969.StraightBevelDiffMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _969

            return self._parent._cast(_969.StraightBevelDiffMeshedGearDesign)

        @property
        def spiral_bevel_meshed_gear_design(
            self: "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign",
        ) -> "_973.SpiralBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _973

            return self._parent._cast(_973.SpiralBevelMeshedGearDesign)

        @property
        def bevel_meshed_gear_design(
            self: "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign",
        ) -> "BevelMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelMeshedGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bending_strength_geometry_factor_concave(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStrengthGeometryFactorConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def bending_strength_geometry_factor_convex(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BendingStrengthGeometryFactorConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def distance_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DistanceFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def durability_factor_agma(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DurabilityFactorAGMA

        if temp is None:
            return 0.0

        return temp

    @property
    def durability_factor_gleason(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DurabilityFactorGleason

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_j_concave(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorJConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def geometry_factor_j_convex(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GeometryFactorJConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_root_fillet_radius(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumRootFilletRadius

        if temp is None:
            return 0.0

        return temp

    @property
    def normal_chordal_thickness_at_mean_of_contact(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NormalChordalThicknessAtMeanOfContact

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_factor_concave(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthFactorConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def strength_factor_convex(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StrengthFactorConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(self: Self) -> "BevelMeshedGearDesign._Cast_BevelMeshedGearDesign":
        return self._Cast_BevelMeshedGearDesign(self)
