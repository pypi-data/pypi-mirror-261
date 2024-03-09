"""AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3279,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3258,
        _3263,
        _3309,
        _3346,
        _3353,
        _3356,
        _3374,
        _3305,
        _3312,
        _3282,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft"
)


class AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3279.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
):
    """AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3279.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3279.ConicalGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3305.GearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3305,
            )

            return self._parent._cast(
                _3305.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3312.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3282.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3282,
            )

            return self._parent._cast(
                _3282.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3258.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3258,
            )

            return self._parent._cast(
                _3258.BevelDifferentialGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3263.BevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3263,
            )

            return self._parent._cast(
                _3263.BevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def hypoid_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3309.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3309,
            )

            return self._parent._cast(
                _3309.HypoidGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def spiral_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3346.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3346,
            )

            return self._parent._cast(
                _3346.SpiralBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_diff_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3353.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3353,
            )

            return self._parent._cast(
                _3353.StraightBevelDiffGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def straight_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3356.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3356,
            )

            return self._parent._cast(
                _3356.StraightBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def zerol_bevel_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3374.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3374,
            )

            return self._parent._cast(
                _3374.ZerolBevelGearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def agma_gleason_conical_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2301.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft":
        return (
            self._Cast_AGMAGleasonConicalGearMeshSteadyStateSynchronousResponseOnAShaft(
                self
            )
        )
