"""TorqueConverterTurbineCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4208
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "TorqueConverterTurbineCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612
    from mastapy.system_model.analyses_and_results.power_flows import _4160
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4246,
        _4194,
        _4248,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineCompoundPowerFlow",)


Self = TypeVar("Self", bound="TorqueConverterTurbineCompoundPowerFlow")


class TorqueConverterTurbineCompoundPowerFlow(_4208.CouplingHalfCompoundPowerFlow):
    """TorqueConverterTurbineCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_TorqueConverterTurbineCompoundPowerFlow"
    )

    class _Cast_TorqueConverterTurbineCompoundPowerFlow:
        """Special nested class for casting TorqueConverterTurbineCompoundPowerFlow to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
            parent: "TorqueConverterTurbineCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_power_flow(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ) -> "_4208.CouplingHalfCompoundPowerFlow":
            return self._parent._cast(_4208.CouplingHalfCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ) -> "_4246.MountableComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4246,
            )

            return self._parent._cast(_4246.MountableComponentCompoundPowerFlow)

        @property
        def component_compound_power_flow(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ) -> "_4194.ComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4194,
            )

            return self._parent._cast(_4194.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ) -> "_4248.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
        ) -> "TorqueConverterTurbineCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "TorqueConverterTurbineCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2612.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

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
    ) -> "List[_4160.TorqueConverterTurbinePowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.TorqueConverterTurbinePowerFlow]

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
    ) -> "List[_4160.TorqueConverterTurbinePowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.TorqueConverterTurbinePowerFlow]

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
    ) -> "TorqueConverterTurbineCompoundPowerFlow._Cast_TorqueConverterTurbineCompoundPowerFlow":
        return self._Cast_TorqueConverterTurbineCompoundPowerFlow(self)
