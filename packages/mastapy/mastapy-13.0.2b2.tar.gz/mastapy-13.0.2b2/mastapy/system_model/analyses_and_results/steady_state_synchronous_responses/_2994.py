"""BeltConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3051,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "BeltConnectionSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.static_loads import _6823
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3025,
        _3020,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="BeltConnectionSteadyStateSynchronousResponse")


class BeltConnectionSteadyStateSynchronousResponse(
    _3051.InterMountableComponentConnectionSteadyStateSynchronousResponse
):
    """BeltConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BeltConnectionSteadyStateSynchronousResponse"
    )

    class _Cast_BeltConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting BeltConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
            parent: "BeltConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_3051.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3051.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_3020.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(_3020.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_steady_state_synchronous_response(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "_3025.CVTBeltConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3025,
            )

            return self._parent._cast(
                _3025.CVTBeltConnectionSteadyStateSynchronousResponse
            )

        @property
        def belt_connection_steady_state_synchronous_response(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
        ) -> "BeltConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "BeltConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2270.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6823.BeltConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BeltConnectionSteadyStateSynchronousResponse._Cast_BeltConnectionSteadyStateSynchronousResponse":
        return self._Cast_BeltConnectionSteadyStateSynchronousResponse(self)
