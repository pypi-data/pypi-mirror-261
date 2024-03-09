"""KlingelnbergCycloPalloidSpiralBevelGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2538
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears",
    "KlingelnbergCycloPalloidSpiralBevelGear",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _974
    from mastapy.system_model.part_model.gears import _2525, _2532
    from mastapy.system_model.part_model import _2466, _2446, _2470
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGear",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGear")


class KlingelnbergCycloPalloidSpiralBevelGear(
    _2538.KlingelnbergCycloPalloidConicalGear
):
    """KlingelnbergCycloPalloidSpiralBevelGear

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGear"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGear:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGear to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
            parent: "KlingelnbergCycloPalloidSpiralBevelGear",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2538.KlingelnbergCycloPalloidConicalGear":
            return self._parent._cast(_2538.KlingelnbergCycloPalloidConicalGear)

        @property
        def conical_gear(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2525.ConicalGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.ConicalGear)

        @property
        def gear(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2532.Gear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.Gear)

        @property
        def mountable_component(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2466.MountableComponent":
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.MountableComponent)

        @property
        def component(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2446.Component":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Component)

        @property
        def part(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2470.Part":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.Part)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGear":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGear.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(
        self: Self,
    ) -> "_974.KlingelnbergCycloPalloidSpiralBevelGearDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
        self: Self,
    ) -> "_974.KlingelnbergCycloPalloidSpiralBevelGearDesign":
        """mastapy.gears.gear_designs.klingelnberg_spiral_bevel.KlingelnbergCycloPalloidSpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidSpiralBevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidSpiralBevelGear._Cast_KlingelnbergCycloPalloidSpiralBevelGear":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGear(self)
