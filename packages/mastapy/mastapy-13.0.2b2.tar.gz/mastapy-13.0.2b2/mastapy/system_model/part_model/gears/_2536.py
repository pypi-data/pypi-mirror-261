"""HypoidGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "HypoidGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _986
    from mastapy.system_model.part_model.gears import _2525, _2532
    from mastapy.system_model.part_model import _2466, _2446, _2470
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGear",)


Self = TypeVar("Self", bound="HypoidGear")


class HypoidGear(_2515.AGMAGleasonConicalGear):
    """HypoidGear

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGear")

    class _Cast_HypoidGear:
        """Special nested class for casting HypoidGear to subclasses."""

        def __init__(self: "HypoidGear._Cast_HypoidGear", parent: "HypoidGear"):
            self._parent = parent

        @property
        def agma_gleason_conical_gear(
            self: "HypoidGear._Cast_HypoidGear",
        ) -> "_2515.AGMAGleasonConicalGear":
            return self._parent._cast(_2515.AGMAGleasonConicalGear)

        @property
        def conical_gear(self: "HypoidGear._Cast_HypoidGear") -> "_2525.ConicalGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.ConicalGear)

        @property
        def gear(self: "HypoidGear._Cast_HypoidGear") -> "_2532.Gear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.Gear)

        @property
        def mountable_component(
            self: "HypoidGear._Cast_HypoidGear",
        ) -> "_2466.MountableComponent":
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.MountableComponent)

        @property
        def component(self: "HypoidGear._Cast_HypoidGear") -> "_2446.Component":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Component)

        @property
        def part(self: "HypoidGear._Cast_HypoidGear") -> "_2470.Part":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.Part)

        @property
        def design_entity(self: "HypoidGear._Cast_HypoidGear") -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def hypoid_gear(self: "HypoidGear._Cast_HypoidGear") -> "HypoidGear":
            return self._parent

        def __getattr__(self: "HypoidGear._Cast_HypoidGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(self: Self) -> "_986.HypoidGearDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_design(self: Self) -> "_986.HypoidGearDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGear._Cast_HypoidGear":
        return self._Cast_HypoidGear(self)
