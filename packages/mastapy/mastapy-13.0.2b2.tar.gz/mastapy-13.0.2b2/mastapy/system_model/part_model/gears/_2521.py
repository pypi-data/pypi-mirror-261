"""BevelGear"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.part_model.gears import _2515
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR = python_net_import("SMT.MastaAPI.SystemModel.PartModel.Gears", "BevelGear")

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.bevel import _1181
    from mastapy.system_model.part_model.gears import (
        _2517,
        _2519,
        _2520,
        _2545,
        _2547,
        _2549,
        _2551,
        _2552,
        _2555,
        _2525,
        _2532,
    )
    from mastapy.system_model.part_model import _2466, _2446, _2470
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("BevelGear",)


Self = TypeVar("Self", bound="BevelGear")


class BevelGear(_2515.AGMAGleasonConicalGear):
    """BevelGear

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGear")

    class _Cast_BevelGear:
        """Special nested class for casting BevelGear to subclasses."""

        def __init__(self: "BevelGear._Cast_BevelGear", parent: "BevelGear"):
            self._parent = parent

        @property
        def agma_gleason_conical_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2515.AGMAGleasonConicalGear":
            return self._parent._cast(_2515.AGMAGleasonConicalGear)

        @property
        def conical_gear(self: "BevelGear._Cast_BevelGear") -> "_2525.ConicalGear":
            from mastapy.system_model.part_model.gears import _2525

            return self._parent._cast(_2525.ConicalGear)

        @property
        def gear(self: "BevelGear._Cast_BevelGear") -> "_2532.Gear":
            from mastapy.system_model.part_model.gears import _2532

            return self._parent._cast(_2532.Gear)

        @property
        def mountable_component(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2466.MountableComponent":
            from mastapy.system_model.part_model import _2466

            return self._parent._cast(_2466.MountableComponent)

        @property
        def component(self: "BevelGear._Cast_BevelGear") -> "_2446.Component":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Component)

        @property
        def part(self: "BevelGear._Cast_BevelGear") -> "_2470.Part":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.Part)

        @property
        def design_entity(self: "BevelGear._Cast_BevelGear") -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def bevel_differential_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2517.BevelDifferentialGear":
            from mastapy.system_model.part_model.gears import _2517

            return self._parent._cast(_2517.BevelDifferentialGear)

        @property
        def bevel_differential_planet_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2519.BevelDifferentialPlanetGear":
            from mastapy.system_model.part_model.gears import _2519

            return self._parent._cast(_2519.BevelDifferentialPlanetGear)

        @property
        def bevel_differential_sun_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2520.BevelDifferentialSunGear":
            from mastapy.system_model.part_model.gears import _2520

            return self._parent._cast(_2520.BevelDifferentialSunGear)

        @property
        def spiral_bevel_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2545.SpiralBevelGear":
            from mastapy.system_model.part_model.gears import _2545

            return self._parent._cast(_2545.SpiralBevelGear)

        @property
        def straight_bevel_diff_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2547.StraightBevelDiffGear":
            from mastapy.system_model.part_model.gears import _2547

            return self._parent._cast(_2547.StraightBevelDiffGear)

        @property
        def straight_bevel_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2549.StraightBevelGear":
            from mastapy.system_model.part_model.gears import _2549

            return self._parent._cast(_2549.StraightBevelGear)

        @property
        def straight_bevel_planet_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2551.StraightBevelPlanetGear":
            from mastapy.system_model.part_model.gears import _2551

            return self._parent._cast(_2551.StraightBevelPlanetGear)

        @property
        def straight_bevel_sun_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2552.StraightBevelSunGear":
            from mastapy.system_model.part_model.gears import _2552

            return self._parent._cast(_2552.StraightBevelSunGear)

        @property
        def zerol_bevel_gear(
            self: "BevelGear._Cast_BevelGear",
        ) -> "_2555.ZerolBevelGear":
            from mastapy.system_model.part_model.gears import _2555

            return self._parent._cast(_2555.ZerolBevelGear)

        @property
        def bevel_gear(self: "BevelGear._Cast_BevelGear") -> "BevelGear":
            return self._parent

        def __getattr__(self: "BevelGear._Cast_BevelGear", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGear.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def conical_gear_design(self: Self) -> "_1181.BevelGearDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConicalGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_gear_design(self: Self) -> "_1181.BevelGearDesign":
        """mastapy.gears.gear_designs.bevel.BevelGearDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelGearDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGear._Cast_BevelGear":
        return self._Cast_BevelGear(self)
