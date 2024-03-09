"""ConnectorCompoundSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
    _3454,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTOR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft.Compound",
    "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3283,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
        _3385,
        _3455,
        _3473,
        _3402,
        _3456,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ConnectorCompoundSteadyStateSynchronousResponseOnAShaft")


class ConnectorCompoundSteadyStateSynchronousResponseOnAShaft(
    _3454.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
):
    """ConnectorCompoundSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONNECTOR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConnectorCompoundSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
            parent: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3454.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3454.MountableComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3402,
            )

            return self._parent._cast(
                _3402.ComponentCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3456.PartCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3456,
            )

            return self._parent._cast(
                _3456.PartCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_compound_analysis(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bearing_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3385.BearingCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3385,
            )

            return self._parent._cast(
                _3385.BearingCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def oil_seal_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3455.OilSealCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3455,
            )

            return self._parent._cast(
                _3455.OilSealCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3473.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.compound import (
                _3473,
            )

            return self._parent._cast(
                _3473.ShaftHubConnectionCompoundSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connector_compound_steady_state_synchronous_response_on_a_shaft(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3283.ConnectorSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConnectorSteadyStateSynchronousResponseOnAShaft]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3283.ConnectorSteadyStateSynchronousResponseOnAShaft]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft.ConnectorSteadyStateSynchronousResponseOnAShaft]

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
    def cast_to(
        self: Self,
    ) -> "ConnectorCompoundSteadyStateSynchronousResponseOnAShaft._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConnectorCompoundSteadyStateSynchronousResponseOnAShaft(self)
