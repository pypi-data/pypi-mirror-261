"""ConceptCouplingPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4073
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "ConceptCouplingPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2583
    from mastapy.system_model.analyses_and_results.static_loads import _6843
    from mastapy.system_model.analyses_and_results.power_flows import (
        _4137,
        _4034,
        _4116,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingPowerFlow",)


Self = TypeVar("Self", bound="ConceptCouplingPowerFlow")


class ConceptCouplingPowerFlow(_4073.CouplingPowerFlow):
    """ConceptCouplingPowerFlow

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConceptCouplingPowerFlow")

    class _Cast_ConceptCouplingPowerFlow:
        """Special nested class for casting ConceptCouplingPowerFlow to subclasses."""

        def __init__(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
            parent: "ConceptCouplingPowerFlow",
        ):
            self._parent = parent

        @property
        def coupling_power_flow(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "_4073.CouplingPowerFlow":
            return self._parent._cast(_4073.CouplingPowerFlow)

        @property
        def specialised_assembly_power_flow(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "_4137.SpecialisedAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4137

            return self._parent._cast(_4137.SpecialisedAssemblyPowerFlow)

        @property
        def abstract_assembly_power_flow(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "_4034.AbstractAssemblyPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4034

            return self._parent._cast(_4034.AbstractAssemblyPowerFlow)

        @property
        def part_power_flow(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "_4116.PartPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4116

            return self._parent._cast(_4116.PartPowerFlow)

        @property
        def part_static_load_analysis_case(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def concept_coupling_power_flow(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow",
        ) -> "ConceptCouplingPowerFlow":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConceptCouplingPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2583.ConceptCoupling":
        """mastapy.system_model.part_model.couplings.ConceptCoupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6843.ConceptCouplingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptCouplingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingPowerFlow._Cast_ConceptCouplingPowerFlow":
        return self._Cast_ConceptCouplingPowerFlow(self)
