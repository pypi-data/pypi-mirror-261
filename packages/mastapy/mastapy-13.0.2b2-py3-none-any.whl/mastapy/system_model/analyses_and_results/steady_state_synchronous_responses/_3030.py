"""CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2988,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2340
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3020,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
)


class CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse(
    _2988.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
):
    """CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = (
        _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_STEADY_STATE_SYNCHRONOUS_RESPONSE
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
            parent: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_steady_state_synchronous_response(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_2988.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse":
            return self._parent._cast(
                _2988.AbstractShaftToMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_3020.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(_3020.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_steady_state_synchronous_response(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
        ) -> "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2340.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6863.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

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
    ) -> "CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse":
        return self._Cast_CycloidalDiscPlanetaryBearingConnectionSteadyStateSynchronousResponse(
            self
        )
