"""ConicalMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.gears.gear_designs import _949
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.Conical", "ConicalMeshedGearDesign"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.zerol_bevel import _956
    from mastapy.gears.gear_designs.straight_bevel import _965
    from mastapy.gears.gear_designs.straight_bevel_diff import _969
    from mastapy.gears.gear_designs.spiral_bevel import _973
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _981
    from mastapy.gears.gear_designs.klingelnberg_conical import _985
    from mastapy.gears.gear_designs.hypoid import _989
    from mastapy.gears.gear_designs.bevel import _1184
    from mastapy.gears.gear_designs.agma_gleason_conical import _1197


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshedGearDesign",)


Self = TypeVar("Self", bound="ConicalMeshedGearDesign")


class ConicalMeshedGearDesign(_949.GearDesignComponent):
    """ConicalMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshedGearDesign")

    class _Cast_ConicalMeshedGearDesign:
        """Special nested class for casting ConicalMeshedGearDesign to subclasses."""

        def __init__(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
            parent: "ConicalMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def gear_design_component(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_949.GearDesignComponent":
            return self._parent._cast(_949.GearDesignComponent)

        @property
        def zerol_bevel_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_956.ZerolBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _956

            return self._parent._cast(_956.ZerolBevelMeshedGearDesign)

        @property
        def straight_bevel_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_965.StraightBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _965

            return self._parent._cast(_965.StraightBevelMeshedGearDesign)

        @property
        def straight_bevel_diff_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_969.StraightBevelDiffMeshedGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _969

            return self._parent._cast(_969.StraightBevelDiffMeshedGearDesign)

        @property
        def spiral_bevel_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_973.SpiralBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _973

            return self._parent._cast(_973.SpiralBevelMeshedGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_977.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977

            return self._parent._cast(
                _977.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_981.KlingelnbergCycloPalloidHypoidMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _981

            return self._parent._cast(
                _981.KlingelnbergCycloPalloidHypoidMeshedGearDesign
            )

        @property
        def klingelnberg_conical_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_985.KlingelnbergConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _985

            return self._parent._cast(_985.KlingelnbergConicalMeshedGearDesign)

        @property
        def hypoid_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_989.HypoidMeshedGearDesign":
            from mastapy.gears.gear_designs.hypoid import _989

            return self._parent._cast(_989.HypoidMeshedGearDesign)

        @property
        def bevel_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_1184.BevelMeshedGearDesign":
            from mastapy.gears.gear_designs.bevel import _1184

            return self._parent._cast(_1184.BevelMeshedGearDesign)

        @property
        def agma_gleason_conical_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "_1197.AGMAGleasonConicalMeshedGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1197

            return self._parent._cast(_1197.AGMAGleasonConicalMeshedGearDesign)

        @property
        def conical_meshed_gear_design(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign",
        ) -> "ConicalMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalMeshedGearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def axial_force_type(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialForceType

        if temp is None:
            return ""

        return temp

    @property
    def axial_force_type_convex(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AxialForceTypeConvex

        if temp is None:
            return ""

        return temp

    @property
    def gleason_axial_factor_concave(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonAxialFactorConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_axial_factor_convex(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonAxialFactorConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_separating_factor_concave(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonSeparatingFactorConcave

        if temp is None:
            return 0.0

        return temp

    @property
    def gleason_separating_factor_convex(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GleasonSeparatingFactorConvex

        if temp is None:
            return 0.0

        return temp

    @property
    def module(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Module

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str"""
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @name.setter
    @enforce_parameter_types
    def name(self: Self, value: "str"):
        self.wrapped.Name = str(value) if value is not None else ""

    @property
    def pitch_angle(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PitchAngle

        if temp is None:
            return 0.0

        return temp

    @property
    def radial_force_type_concave(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialForceTypeConcave

        if temp is None:
            return ""

        return temp

    @property
    def radial_force_type_convex(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RadialForceTypeConvex

        if temp is None:
            return ""

        return temp

    @property
    def cast_to(self: Self) -> "ConicalMeshedGearDesign._Cast_ConicalMeshedGearDesign":
        return self._Cast_ConicalMeshedGearDesign(self)
