"""ShaftHubConnectionCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3154,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HUB_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2600
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3081,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3195,
        _3143,
        _3197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHubConnectionCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ShaftHubConnectionCompoundSteadyStateSynchronousResponse")


class ShaftHubConnectionCompoundSteadyStateSynchronousResponse(
    _3154.ConnectorCompoundSteadyStateSynchronousResponse
):
    """ShaftHubConnectionCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SHAFT_HUB_CONNECTION_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting ShaftHubConnectionCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
            parent: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def connector_compound_steady_state_synchronous_response(
            self: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3154.ConnectorCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3154.ConnectorCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(
                _3195.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3143.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3143,
            )

            return self._parent._cast(
                _3143.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def shaft_hub_connection_compound_steady_state_synchronous_response(
            self: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
        ) -> "ShaftHubConnectionCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ShaftHubConnectionCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2600.ShaftHubConnection":
        """mastapy.system_model.part_model.couplings.ShaftHubConnection

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
    ) -> "List[_3081.ShaftHubConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ShaftHubConnectionSteadyStateSynchronousResponse]

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
    def planetaries(
        self: Self,
    ) -> "List[ShaftHubConnectionCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.ShaftHubConnectionCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3081.ShaftHubConnectionSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ShaftHubConnectionSteadyStateSynchronousResponse]

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
    ) -> "ShaftHubConnectionCompoundSteadyStateSynchronousResponse._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse":
        return self._Cast_ShaftHubConnectionCompoundSteadyStateSynchronousResponse(self)
