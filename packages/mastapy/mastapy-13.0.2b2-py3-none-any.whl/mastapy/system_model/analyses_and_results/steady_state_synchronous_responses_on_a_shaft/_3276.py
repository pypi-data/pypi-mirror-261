"""ConceptGearMeshSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3305,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONCEPT_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2307
    from mastapy.system_model.analyses_and_results.static_loads import _6845
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3312,
        _3282,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="ConceptGearMeshSteadyStateSynchronousResponseOnAShaft")


class ConceptGearMeshSteadyStateSynchronousResponseOnAShaft(
    _3305.GearMeshSteadyStateSynchronousResponseOnAShaft
):
    """ConceptGearMeshSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _CONCEPT_GEAR_MESH_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft"
    )

    class _Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting ConceptGearMeshSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
            parent: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3305.GearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3305.GearMeshSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def inter_mountable_component_connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3312.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3312,
            )

            return self._parent._cast(
                _3312.InterMountableComponentConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3282.ConnectionSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3282,
            )

            return self._parent._cast(
                _3282.ConnectionSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def connection_static_load_analysis_case(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def concept_gear_mesh_steady_state_synchronous_response_on_a_shaft(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
        ) -> "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2307.ConceptGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConceptGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6845.ConceptGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ConceptGearMeshLoadCase

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
    ) -> "ConceptGearMeshSteadyStateSynchronousResponseOnAShaft._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_ConceptGearMeshSteadyStateSynchronousResponseOnAShaft(self)
