"""RootAssemblyPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4041
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "RootAssemblyPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4124,
        _4034,
        _4116,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyPowerFlow",)


Self = TypeVar("Self", bound="RootAssemblyPowerFlow")


class RootAssemblyPowerFlow(_4041.AssemblyPowerFlow):
    """RootAssemblyPowerFlow

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RootAssemblyPowerFlow")

    class _Cast_RootAssemblyPowerFlow:
        """Special nested class for casting RootAssemblyPowerFlow to subclasses."""

        def __init__(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
            parent: "RootAssemblyPowerFlow",
        ):
            self._parent = parent

        @property
        def assembly_power_flow(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_4041.AssemblyPowerFlow":
            return self._parent._cast(_4041.AssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_4034.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def root_assembly_power_flow(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow",
        ) -> "RootAssemblyPowerFlow":
            return self._parent

        def __getattr__(
            self: "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RootAssemblyPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2476.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_inputs(self: Self) -> "_4124.PowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "RootAssemblyPowerFlow._Cast_RootAssemblyPowerFlow":
        return self._Cast_RootAssemblyPowerFlow(self)
