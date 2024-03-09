"""HypoidGearMeshSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2989,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "HypoidGearMeshSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2317
    from mastapy.system_model.analyses_and_results.static_loads import _6909
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3017,
        _3044,
        _3051,
        _3020,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMeshSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="HypoidGearMeshSteadyStateSynchronousResponse")


class HypoidGearMeshSteadyStateSynchronousResponse(
    _2989.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
):
    """HypoidGearMeshSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_HypoidGearMeshSteadyStateSynchronousResponse"
    )

    class _Cast_HypoidGearMeshSteadyStateSynchronousResponse:
        """Special nested class for casting HypoidGearMeshSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
            parent: "HypoidGearMeshSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "_2989.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse":
            return self._parent._cast(
                _2989.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "_3017.ConicalGearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3017,
            )

            return self._parent._cast(
                _3017.ConicalGearMeshSteadyStateSynchronousResponse
            )

        @property
        def gear_mesh_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "_3044.GearMeshSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3044,
            )

            return self._parent._cast(_3044.GearMeshSteadyStateSynchronousResponse)

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "_3051.InterMountableComponentConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3051,
            )

            return self._parent._cast(
                _3051.InterMountableComponentConnectionSteadyStateSynchronousResponse
            )

        @property
        def connection_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "_3020.ConnectionSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3020,
            )

            return self._parent._cast(_3020.ConnectionSteadyStateSynchronousResponse)

        @property
        def connection_static_load_analysis_case(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
        ) -> "HypoidGearMeshSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse",
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
        instance_to_wrap: "HypoidGearMeshSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2317.HypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.HypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6909.HypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.HypoidGearMeshLoadCase

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
    ) -> "HypoidGearMeshSteadyStateSynchronousResponse._Cast_HypoidGearMeshSteadyStateSynchronousResponse":
        return self._Cast_HypoidGearMeshSteadyStateSynchronousResponse(self)
