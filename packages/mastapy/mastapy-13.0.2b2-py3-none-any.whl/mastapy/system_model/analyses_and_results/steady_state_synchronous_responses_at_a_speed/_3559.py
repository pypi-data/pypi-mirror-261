"""FaceGearMeshSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3564,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2313
    from mastapy.system_model.analyses_and_results.static_loads import _6888
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3571,
        _3541,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="FaceGearMeshSteadyStateSynchronousResponseAtASpeed")


class FaceGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3564.GearMeshSteadyStateSynchronousResponseAtASpeed
):
    """FaceGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting FaceGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3564.GearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3564.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3571.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3541.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3541,
            )

            return self._parent._cast(
                _3541.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def face_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "FaceGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "FaceGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2313.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6888.FaceGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

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
    ) -> "FaceGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_FaceGearMeshSteadyStateSynchronousResponseAtASpeed(self)
