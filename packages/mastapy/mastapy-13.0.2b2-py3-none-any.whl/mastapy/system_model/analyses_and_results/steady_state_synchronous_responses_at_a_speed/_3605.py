"""SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3522,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3510,
        _3538,
        _3564,
        _3571,
        _3541,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self", bound="SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed"
)


class SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed(
    _3522.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
):
    """SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
            parent: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3522.BevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3522.BevelGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3510.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3510,
            )

            return self._parent._cast(
                _3510.AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3538.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3538,
            )

            return self._parent._cast(
                _3538.ConicalGearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3564.GearMeshSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3564,
            )

            return self._parent._cast(
                _3564.GearMeshSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3571.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3571,
            )

            return self._parent._cast(
                _3571.InterMountableComponentConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3541.ConnectionSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3541,
            )

            return self._parent._cast(
                _3541.ConnectionSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_at_a_speed(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
        ) -> "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2325.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6957.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

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
    ) -> "SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_SpiralBevelGearMeshSteadyStateSynchronousResponseAtASpeed(
            self
        )
