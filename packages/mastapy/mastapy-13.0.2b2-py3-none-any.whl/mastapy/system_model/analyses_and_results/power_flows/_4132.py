"""RollingRingPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4072
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "RollingRingPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6950
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4114,
        _4059,
        _4116,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingPowerFlow",)


Self = TypeVar("Self", bound="RollingRingPowerFlow")


class RollingRingPowerFlow(_4072.CouplingHalfPowerFlow):
    """RollingRingPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingPowerFlow")

    class _Cast_RollingRingPowerFlow:
        """Special nested class for casting RollingRingPowerFlow to subclasses."""

        def __init__(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
            parent: "RollingRingPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_power_flow(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
        ) -> "_4072.CouplingHalfPowerFlow":
            return self._parent._cast(_4072.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
        ) -> "_4114.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
        ) -> "_4059.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def rolling_ring_power_flow(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow",
        ) -> "RollingRingPowerFlow":
            return self._parent

        def __getattr__(
            self: "RollingRingPowerFlow._Cast_RollingRingPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6950.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RollingRingPowerFlow._Cast_RollingRingPowerFlow":
        return self._Cast_RollingRingPowerFlow(self)
