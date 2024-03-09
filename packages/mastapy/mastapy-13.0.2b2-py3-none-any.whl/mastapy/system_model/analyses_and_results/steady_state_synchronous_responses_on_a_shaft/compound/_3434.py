"""FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3475,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FLEXIBLE_PIN_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2456
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3304,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3377,
        _3456,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft"
)


class FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft(
    _3475.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
):
    """FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _FLEXIBLE_PIN_ASSEMBLY_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3475.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3475.SpecialisedAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3377.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3377,
            )

            return self._parent._cast(
                _3377.AbstractAssemblyCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3456.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def flexible_pin_assembly_compound_steady_state_synchronous_response_on_a_shaft(
            self: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft",
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
        self: Self,
        instance_to_wrap: "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2456.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2456.FlexiblePinAssembly":
        """mastapy.system_model.part_model.FlexiblePinAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3304.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3304.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.FlexiblePinAssemblySteadyStateSynchronousResponseOnAShaft]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_FlexiblePinAssemblyCompoundSteadyStateSynchronousResponseOnAShaft(
            self
        )
