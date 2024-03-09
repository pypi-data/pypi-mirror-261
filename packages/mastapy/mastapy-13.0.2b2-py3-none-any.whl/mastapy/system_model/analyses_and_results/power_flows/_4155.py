"""SynchroniserSleevePowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4153
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows",
    "SynchroniserSleevePowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4072,
        _4114,
        _4059,
        _4116,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleevePowerFlow",)


Self = TypeVar("Self", bound="SynchroniserSleevePowerFlow")


class SynchroniserSleevePowerFlow(_4153.SynchroniserPartPowerFlow):
    """SynchroniserSleevePowerFlow

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleevePowerFlow")

    class _Cast_SynchroniserSleevePowerFlow:
        """Special nested class for casting SynchroniserSleevePowerFlow to subclasses."""

        def __init__(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
            parent: "SynchroniserSleevePowerFlow",
        ):
            self._parent = parent

        @property
        def synchroniser_part_power_flow(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "_4153.SynchroniserPartPowerFlow":
            return self._parent._cast(_4153.SynchroniserPartPowerFlow)

        @property
        def coupling_half_power_flow(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "_4072.CouplingHalfPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4072

            return self._parent._cast(_4072.CouplingHalfPowerFlow)

        @property
        def mountable_component_power_flow(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "_4114.MountableComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4114

            return self._parent._cast(_4114.MountableComponentPowerFlow)

        @property
        def component_power_flow(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "_4059.ComponentPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4059

            return self._parent._cast(_4059.ComponentPowerFlow)

        @property
        def part_power_flow(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_power_flow(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
        ) -> "SynchroniserSleevePowerFlow":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserSleevePowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6973.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserSleevePowerFlow._Cast_SynchroniserSleevePowerFlow":
        return self._Cast_SynchroniserSleevePowerFlow(self)
