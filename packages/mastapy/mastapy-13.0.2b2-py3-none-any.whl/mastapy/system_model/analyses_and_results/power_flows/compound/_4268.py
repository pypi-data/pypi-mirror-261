"""SpiralBevelGearCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4185
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "SpiralBevelGearCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.power_flows import _4139
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
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
__all__ = ("SpiralBevelGearCompoundPowerFlow",)


Self = TypeVar("Self", bound="SpiralBevelGearCompoundPowerFlow")


class SpiralBevelGearCompoundPowerFlow(_4185.BevelGearCompoundPowerFlow):
    """SpiralBevelGearCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearCompoundPowerFlow")

    class _Cast_SpiralBevelGearCompoundPowerFlow:
        """Special nested class for casting SpiralBevelGearCompoundPowerFlow to subclasses."""

        def __init__(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
            parent: "SpiralBevelGearCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4185.BevelGearCompoundPowerFlow":
            return self._parent._cast(_4185.BevelGearCompoundPowerFlow)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4173.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4201.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConicalGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4227.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.GearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4246.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4194.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_4248.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
        ) -> "SpiralBevelGearCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpiralBevelGearCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

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
    ) -> "List[_4139.SpiralBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4139.SpiralBevelGearPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.SpiralBevelGearPowerFlow]

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
    ) -> "SpiralBevelGearCompoundPowerFlow._Cast_SpiralBevelGearCompoundPowerFlow":
        return self._Cast_SpiralBevelGearCompoundPowerFlow(self)
