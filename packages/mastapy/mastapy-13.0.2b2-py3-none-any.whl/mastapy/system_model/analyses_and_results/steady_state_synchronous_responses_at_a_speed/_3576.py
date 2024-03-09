"""KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3573,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6920
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3577,
        _3575,
        _3539,
        _3565,
        _3604,
        _3506,
        _3585,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = (
    "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
)


class KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed(
    _3573.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
):
    """KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
            parent: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3573.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3573.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3539.ConicalGearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3539,
            )

            return self._parent._cast(
                _3539.ConicalGearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_set_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3565.GearSetSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3565,
            )

            return self._parent._cast(
                _3565.GearSetSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3604.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3604,
            )

            return self._parent._cast(
                _3604.SpecialisedAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3506.AbstractAssemblySteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3506,
            )

            return self._parent._cast(
                _3506.AbstractAssemblySteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(_3585.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2541.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6920.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3577.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidGearsSteadyStateSynchronousResponseAtASpeed
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_steady_state_synchronous_response_at_a_speed(
        self: Self,
    ) -> "List[_3575.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponseAtASpeed]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidMeshesSteadyStateSynchronousResponseAtASpeed
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponseAtASpeed(
            self
        )
