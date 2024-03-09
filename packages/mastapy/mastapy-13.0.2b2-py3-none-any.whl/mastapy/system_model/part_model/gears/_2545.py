"""SpiralBevelGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2521
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "SpiralBevelGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.spiral_bevel import _970
    from mastapy.system_model.part_model.gears import _2515, _2525, _2532
    from mastapy.system_model.part_model import _2466, _2446, _2470
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGear",)


Self = TypeVar("Self", bound="SpiralBevelGear")


class SpiralBevelGear(_2521.BevelGear):
    """SpiralBevelGear

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGear")

    class _Cast_SpiralBevelGear:
        """Special nested class for casting SpiralBevelGear to subclasses."""

        def __init__(
            self: "SpiralBevelGear._Cast_SpiralBevelGear", parent: "SpiralBevelGear"
        ):
            self._parent = parent

        @property
        def bevel_gear(
            self: "SpiralBevelGear._Cast_SpiralBevelGear",
        ) -> "_2521.BevelGear":
            return self._parent._cast(_2521.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "SpiralBevelGear._Cast_SpiralBevelGear",
        ) -> "_2515.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "SpiralBevelGear._Cast_SpiralBevelGear",
        ) -> "_2525.ConicalGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.ConicalGear)

        @property
        def gear(self: "SpiralBevelGear._Cast_SpiralBevelGear") -> "_2532.Gear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.Gear)

        @property
        def mountable_component(
            self: "SpiralBevelGear._Cast_SpiralBevelGear",
        ) -> "_2466.MountableComponent":
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.MountableComponent)

        @property
        def component(
            self: "SpiralBevelGear._Cast_SpiralBevelGear",
        ) -> "_2446.Component":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Component)

        @property
        def part(self: "SpiralBevelGear._Cast_SpiralBevelGear") -> "_2470.Part":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.Part)

        @property
        def design_entity(
            self: "SpiralBevelGear._Cast_SpiralBevelGear",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def spiral_bevel_gear(
            self: "SpiralBevelGear._Cast_SpiralBevelGear",
        ) -> "SpiralBevelGear":
            return self._parent

        def __getattr__(self: "SpiralBevelGear._Cast_SpiralBevelGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_design(self: Self) -> "_970.SpiralBevelGearDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def spiral_bevel_gear_design(self: Self) -> "_970.SpiralBevelGearDesign":
        """mastapy.gears.gear_designs.spiral_bevel.SpiralBevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SpiralBevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SpiralBevelGear._Cast_SpiralBevelGear":
        return self._Cast_SpiralBevelGear(self)
