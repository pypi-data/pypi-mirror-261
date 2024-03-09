"""StraightBevelPlanetGearPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4145
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "StraightBevelPlanetGearPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4051,
        _4039,
        _4067,
        _4096,
        _4114,
        _4059,
        _4116,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearPowerFlow")


class StraightBevelPlanetGearPowerFlow(_4145.StraightBevelDiffGearPowerFlow):
    """StraightBevelPlanetGearPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelPlanetGearPowerFlow")

    class _Cast_StraightBevelPlanetGearPowerFlow:
        """Special nested class for casting StraightBevelPlanetGearPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
            parent: "StraightBevelPlanetGearPowerFlow",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_power_flow(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_4145.StraightBevelDiffGearPowerFlow":
            return self._parent._cast(_4145.StraightBevelDiffGearPowerFlow)

        @property
        def bevel_gear_power_flow(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_4051.BevelGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4051

            return self._parent._cast(_4051.BevelGearPowerFlow)

        @property
        def agma_gleason_conical_gear_power_flow(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_4039.AGMAGleasonConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4039

            return self._parent._cast(_4039.AGMAGleasonConicalGearPowerFlow)

        @property
        def conical_gear_power_flow(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_4067.ConicalGearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4067

            return self._parent._cast(_4067.ConicalGearPowerFlow)

        @property
        def gear_power_flow(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_4096.GearPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4096

            return self._parent._cast(_4096.GearPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_4114.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_4059.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_power_flow(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
        ) -> "StraightBevelPlanetGearPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelPlanetGearPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearPowerFlow._Cast_StraightBevelPlanetGearPowerFlow":
        return self._Cast_StraightBevelPlanetGearPowerFlow(self)
