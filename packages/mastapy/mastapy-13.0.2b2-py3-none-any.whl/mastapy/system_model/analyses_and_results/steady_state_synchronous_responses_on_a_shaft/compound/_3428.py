"""DatumCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3402,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "DatumCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3298,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3456,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("DatumCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="DatumCompoundSteadyStateSynchronousResponseOnAShaft")


class DatumCompoundSteadyStateSynchronousResponseOnAShaft(
    _3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
):
    """DatumCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _DATUM_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting DatumCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "DatumCompoundSteadyStateSynchronousResponseOnAShaft._Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "DatumCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DatumCompoundSteadyStateSynchronousResponseOnAShaft._Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DatumCompoundSteadyStateSynchronousResponseOnAShaft._Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3456.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "DatumCompoundSteadyStateSynchronousResponseOnAShaft._Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "DatumCompoundSteadyStateSynchronousResponseOnAShaft._Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumCompoundSteadyStateSynchronousResponseOnAShaft._Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def datum_compound_steady_state_synchronous_response_on_a_shaft(
            self: "DatumCompoundSteadyStateSynchronousResponseOnAShaft._Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "DatumCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "DatumCompoundSteadyStateSynchronousResponseOnAShaft._Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "DatumCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2450.Datum":
        """mastapy.system_model.part_model.Datum

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
    ) -> "List[_3298.DatumSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.DatumSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "List[_3298.DatumSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.DatumSteadyStateSynchronousResponseOnAShaft]

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
    ) -> "DatumCompoundSteadyStateSynchronousResponseOnAShaft._Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_DatumCompoundSteadyStateSynchronousResponseOnAShaft(self)
