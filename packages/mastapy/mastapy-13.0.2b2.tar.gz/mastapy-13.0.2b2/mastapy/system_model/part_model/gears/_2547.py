"""StraightBevelDiffGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2521
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel.Gears", "StraightBevelDiffGear"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.straight_bevel_diff import _966
    from mastapy.system_model.part_model.gears import _2551, _2552, _2515, _2525, _2532
    from mastapy.system_model.part_model import _2466, _2446, _2470
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGear",)


Self = TypeVar("Self", bound="StraightBevelDiffGear")


class StraightBevelDiffGear(_2521.BevelGear):
    """StraightBevelDiffGear

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGear")

    class _Cast_StraightBevelDiffGear:
        """Special nested class for casting StraightBevelDiffGear to subclasses."""

        def __init__(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
            parent: "StraightBevelDiffGear",
        ):
            self._parent = parent

        @property
        def bevel_gear(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "_2521.BevelGear":
            return self._parent._cast(_2521.BevelGear)

        @property
        def agma_gleason_conical_gear(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "_2515.AGMAGleasonConicalGear":
            from mastapy.system_model.part_model.gears import _2515

            return self._parent._cast(_2515.AGMAGleasonConicalGear)

        @property
        def conical_gear(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "_2525.ConicalGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.ConicalGear)

        @property
        def gear(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "_2532.Gear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.Gear)

        @property
        def mountable_component(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "_2466.MountableComponent":
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.MountableComponent)

        @property
        def component(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "_2446.Component":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Component)

        @property
        def part(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "_2470.Part":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.Part)

        @property
        def design_entity(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def straight_bevel_planet_gear(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "_2551.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "_2552.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.StraightBevelSunGear)

        @property
        def straight_bevel_diff_gear(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear",
        ) -> "StraightBevelDiffGear":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGear._Cast_StraightBevelDiffGear", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelDiffGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def bevel_gear_design(self: Self) -> "_966.StraightBevelDiffGearDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def straight_bevel_diff_gear_design(
        self: Self,
    ) -> "_966.StraightBevelDiffGearDesign":
        """mastapy.gears.gear_designs.straight_bevel_diff.StraightBevelDiffGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelDiffGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "StraightBevelDiffGear._Cast_StraightBevelDiffGear":
        return self._Cast_StraightBevelDiffGear(self)
