"""ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3156,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2346
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3011,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3183,
        _3153,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse"
)


class ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse(
    _3156.CouplingConnectionCompoundSteadyStateSynchronousResponse
):
    """ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CONCEPT_COUPLING_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
            parent: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_steady_state_synchronous_response(
            self: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3156.CouplingConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3156.CouplingConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def inter_mountable_component_connection_compound_steady_state_synchronous_response(
            self: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3183.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3183,
            )

            return self._parent._cast(
                _3183.InterMountableComponentConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_steady_state_synchronous_response(
            self: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3153.ConnectionCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3153,
            )

            return self._parent._cast(
                _3153.ConnectionCompoundSteadyStateSynchronousResponse
            )

        @property
        def connection_compound_analysis(
            self: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def concept_coupling_connection_compound_steady_state_synchronous_response(
            self: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2346.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2346.ConceptCouplingConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ConceptCouplingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_3011.ConceptCouplingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptCouplingConnectionSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_3011.ConceptCouplingConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ConceptCouplingConnectionSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse":
        return (
            self._Cast_ConceptCouplingConnectionCompoundSteadyStateSynchronousResponse(
                self
            )
        )
