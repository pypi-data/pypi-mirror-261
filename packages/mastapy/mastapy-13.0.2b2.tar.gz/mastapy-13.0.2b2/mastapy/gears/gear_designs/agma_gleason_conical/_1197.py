"""AGMAGleasonConicalMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.conical import _1160
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.AGMAGleasonConical",
    "AGMAGleasonConicalMeshedGearDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _956
    from mastapy.gears.gear_designs.straight_bevel import _965
    from mastapy.gears.gear_designs.straight_bevel_diff import _969
    from mastapy.gears.gear_designs.spiral_bevel import _973
    from mastapy.gears.gear_designs.hypoid import _989
    from mastapy.gears.gear_designs.bevel import _1184
    from mastapy.gears.gear_designs import _949


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalMeshedGearDesign",)


Self = TypeVar("Self", bound="AGMAGleasonConicalMeshedGearDesign")


class AGMAGleasonConicalMeshedGearDesign(_1160.ConicalMeshedGearDesign):
    """AGMAGleasonConicalMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AGMAGleasonConicalMeshedGearDesign")

    class _Cast_AGMAGleasonConicalMeshedGearDesign:
        """Special nested class for casting AGMAGleasonConicalMeshedGearDesign to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
            parent: "AGMAGleasonConicalMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def conical_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_1160.ConicalMeshedGearDesign":
            return self._parent._cast(_1160.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_949.GearDesignComponent":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.GearDesignComponent)

        @property
        def zerol_bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_956.ZerolBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _956

            return self._parent._cast(_956.ZerolBevelMeshedGearDesign)

        @property
        def straight_bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_965.StraightBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _965

            return self._parent._cast(_965.StraightBevelMeshedGearDesign)

        @property
        def straight_bevel_diff_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_969.StraightBevelDiffMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _969

            return self._parent._cast(_969.StraightBevelDiffMeshedGearDesign)

        @property
        def spiral_bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_973.SpiralBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _973

            return self._parent._cast(_973.SpiralBevelMeshedGearDesign)

        @property
        def hypoid_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_989.HypoidMeshedGearDesign":
            from mastapy.gears.gear_designs.hypoid import _989

            return self._parent._cast(_989.HypoidMeshedGearDesign)

        @property
        def bevel_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "_1184.BevelMeshedGearDesign":
            from mastapy.gears.gear_designs.bevel import _1184

            return self._parent._cast(_1184.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
        ) -> "AGMAGleasonConicalMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(
        self: Self, instance_to_wrap: "AGMAGleasonConicalMeshedGearDesign.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mean_normal_topland(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MeanNormalTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_topland_to_module_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumToplandToModuleFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def required_mean_normal_topland(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RequiredMeanNormalTopland

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalMeshedGearDesign._Cast_AGMAGleasonConicalMeshedGearDesign":
        return self._Cast_AGMAGleasonConicalMeshedGearDesign(self)
