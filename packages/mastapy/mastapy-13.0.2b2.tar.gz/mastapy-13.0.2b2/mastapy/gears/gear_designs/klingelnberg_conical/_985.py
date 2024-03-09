"""KlingelnbergConicalMeshedGearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.gear_designs.conical import _1160
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_MESHED_GEAR_DESIGN = python_net_import(
    "SMT.MastaAPI.Gears.GearDesigns.KlingelnbergConical",
    "KlingelnbergConicalMeshedGearDesign",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _981
    from mastapy.gears.gear_designs import _949


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergConicalMeshedGearDesign",)


Self = TypeVar("Self", bound="KlingelnbergConicalMeshedGearDesign")


class KlingelnbergConicalMeshedGearDesign(_1160.ConicalMeshedGearDesign):
    """KlingelnbergConicalMeshedGearDesign

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_MESHED_GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_KlingelnbergConicalMeshedGearDesign")

    class _Cast_KlingelnbergConicalMeshedGearDesign:
        """Special nested class for casting KlingelnbergConicalMeshedGearDesign to subclasses."""

        def __init__(
            self: "KlingelnbergConicalMeshedGearDesign._Cast_KlingelnbergConicalMeshedGearDesign",
            parent: "KlingelnbergConicalMeshedGearDesign",
        ):
            self._parent = parent

        @property
        def conical_meshed_gear_design(
            self: "KlingelnbergConicalMeshedGearDesign._Cast_KlingelnbergConicalMeshedGearDesign",
        ) -> "_1160.ConicalMeshedGearDesign":
            return self._parent._cast(_1160.ConicalMeshedGearDesign)

        @property
        def gear_design_component(
            self: "KlingelnbergConicalMeshedGearDesign._Cast_KlingelnbergConicalMeshedGearDesign",
        ) -> "_949.GearDesignComponent":
            from mastapy.gears.gear_designs import _949

            return self._parent._cast(_949.GearDesignComponent)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_meshed_gear_design(
            self: "KlingelnbergConicalMeshedGearDesign._Cast_KlingelnbergConicalMeshedGearDesign",
        ) -> "_977.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _977

            return self._parent._cast(
                _977.KlingelnbergCycloPalloidSpiralBevelMeshedGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_meshed_gear_design(
            self: "KlingelnbergConicalMeshedGearDesign._Cast_KlingelnbergConicalMeshedGearDesign",
        ) -> "_981.KlingelnbergCycloPalloidHypoidMeshedGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _981

            return self._parent._cast(
                _981.KlingelnbergCycloPalloidHypoidMeshedGearDesign
            )

        @property
        def klingelnberg_conical_meshed_gear_design(
            self: "KlingelnbergConicalMeshedGearDesign._Cast_KlingelnbergConicalMeshedGearDesign",
        ) -> "KlingelnbergConicalMeshedGearDesign":
            return self._parent

        def __getattr__(
            self: "KlingelnbergConicalMeshedGearDesign._Cast_KlingelnbergConicalMeshedGearDesign",
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
        self: Self, instance_to_wrap: "KlingelnbergConicalMeshedGearDesign.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "KlingelnbergConicalMeshedGearDesign._Cast_KlingelnbergConicalMeshedGearDesign"
    ):
        return self._Cast_KlingelnbergConicalMeshedGearDesign(self)
