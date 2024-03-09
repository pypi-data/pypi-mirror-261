"""ShaftCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4170
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "ShaftCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2484
    from mastapy.system_model.analyses_and_results.power_flows import _4135
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4171,
        _4194,
        _4248,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ShaftCompoundPowerFlow",)


Self = TypeVar("Self", bound="ShaftCompoundPowerFlow")


class ShaftCompoundPowerFlow(_4170.AbstractShaftCompoundPowerFlow):
    """ShaftCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _SHAFT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ShaftCompoundPowerFlow")

    class _Cast_ShaftCompoundPowerFlow:
        """Special nested class for casting ShaftCompoundPowerFlow to subclasses."""

        def __init__(
            self: "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow",
            parent: "ShaftCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def abstract_shaft_compound_power_flow(
            self: "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow",
        ) -> "_4170.AbstractShaftCompoundPowerFlow":
            return self._parent._cast(_4170.AbstractShaftCompoundPowerFlow)

        @property
        def abstract_shaft_or_housing_compound_power_flow(
            self: "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow",
        ) -> "_4171.AbstractShaftOrHousingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4171,
            )

            return self._parent._cast(_4171.AbstractShaftOrHousingCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow",
        ) -> "_4194.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow",
        ) -> "_4248.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def shaft_compound_power_flow(
            self: "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow",
        ) -> "ShaftCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ShaftCompoundPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(self: Self) -> "List[_4135.ShaftPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ShaftPowerFlow]

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
    def component_analysis_cases(self: Self) -> "List[_4135.ShaftPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.ShaftPowerFlow]

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
    def cast_to(self: Self) -> "ShaftCompoundPowerFlow._Cast_ShaftCompoundPowerFlow":
        return self._Cast_ShaftCompoundPowerFlow(self)
