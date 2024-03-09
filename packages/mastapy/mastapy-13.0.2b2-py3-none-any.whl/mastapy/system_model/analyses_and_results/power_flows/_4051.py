"""BevelGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4039
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "BevelGearPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4046,
        _4048,
        _4049,
        _4139,
        _4145,
        _4148,
        _4150,
        _4151,
        _4167,
        _4067,
        _4096,
        _4114,
        _4059,
        _4116,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearPowerFlow",)


Self = TypeVar("Self", bound="BevelGearPowerFlow")


class BevelGearPowerFlow(_4039.AGMAGleasonConicalGearPowerFlow):
    """BevelGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearPowerFlow")

    class _Cast_BevelGearPowerFlow:
        """Special nested class for casting BevelGearPowerFlow to subclasses."""

        def __init__(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
            parent: "BevelGearPowerFlow",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4039.AGMAGleasonConicalGearPowerFlow":
            return self._parent._cast(_4039.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4067.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4096.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4114.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4059.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4046.BevelDifferentialGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4046

            return self._parent._cast(_4046.BevelDifferentialGearPowerFlow)

        @property
        def bevel_differential_planet_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4048.BevelDifferentialPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4048

            return self._parent._cast(_4048.BevelDifferentialPlanetGearPowerFlow)

        @property
        def bevel_differential_sun_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4049.BevelDifferentialSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4049

            return self._parent._cast(_4049.BevelDifferentialSunGearPowerFlow)

        @property
        def spiral_bevel_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4139.SpiralBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4139

            return self._parent._cast(_4139.SpiralBevelGearPowerFlow)

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4145.StraightBevelDiffGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4145

            return self._parent._cast(_4145.StraightBevelDiffGearPowerFlow)

        @property
        def straight_bevel_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4148.StraightBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4148

            return self._parent._cast(_4148.StraightBevelGearPowerFlow)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4150.StraightBevelPlanetGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4150

            return self._parent._cast(_4150.StraightBevelPlanetGearPowerFlow)

        @property
        def straight_bevel_sun_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4151.StraightBevelSunGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4151

            return self._parent._cast(_4151.StraightBevelSunGearPowerFlow)

        @property
        def zerol_bevel_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "_4167.ZerolBevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4167

            return self._parent._cast(_4167.ZerolBevelGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow",
        ) -> "BevelGearPowerFlow":
            return self._parent

        def __getattr__(self: "BevelGearPowerFlow._Cast_BevelGearPowerFlow", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2521.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearPowerFlow._Cast_BevelGearPowerFlow":
        return self._Cast_BevelGearPowerFlow(self)
