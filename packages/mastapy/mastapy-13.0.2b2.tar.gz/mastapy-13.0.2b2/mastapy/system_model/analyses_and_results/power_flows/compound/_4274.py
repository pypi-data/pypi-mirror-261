"""StraightBevelDiffGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4185
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "StraightBevelDiffGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2547
    from mastapy.system_model.analyses_and_results.power_flows import _4145
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4280,
        _4281,
        _4173,
        _4201,
        _4227,
        _4246,
        _4194,
        _4248,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="StraightBevelDiffGearCompoundPowerFlow")


class StraightBevelDiffGearCompoundPowerFlow(_4185.BevelGearCompoundPowerFlow):
    """StraightBevelDiffGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearCompoundPowerFlow"
    )

    class _Cast_StraightBevelDiffGearCompoundPowerFlow:
        """Special nested class for casting StraightBevelDiffGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
            parent: "StraightBevelDiffGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_4185.BevelGearCompoundPowerFlow":
            return self._parent._cast(_4185.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_4173.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_4201.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_4227.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_4246.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_4194.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_4248.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_4280.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "_4281.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4281,
            )

            return self._parent._cast(_4281.StraightBevelSunGearCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
        ) -> "StraightBevelDiffGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2547.StraightBevelDiffGear":
        """mastapy.system_model.part_model.gears.StraightBevelDiffGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4145.StraightBevelDiffGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4145.StraightBevelDiffGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.StraightBevelDiffGearPowerFlow]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelDiffGearCompoundPowerFlow._Cast_StraightBevelDiffGearCompoundPowerFlow":
        return self._Cast_StraightBevelDiffGearCompoundPowerFlow(self)
