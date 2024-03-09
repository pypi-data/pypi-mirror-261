"""KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3574,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2540
    from mastapy.system_model.analyses_and_results.static_loads import _6918
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3540,
        _3566,
        _3583,
        _3531,
        _3585,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
)


class KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed(
    _3574.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
):
    """KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
            parent: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3574.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3574.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def conical_gear_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3540.ConicalGearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3540,
            )

            return self._parent._cast(
                _3540.ConicalGearSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def gear_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3566.GearSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3566,
            )

            return self._parent._cast(_3566.GearSteadyStateSynchronousResponseAtASpeed)

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(_3585.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_steady_state_synchronous_response_at_a_speed(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
        ) -> "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2540.KlingelnbergCycloPalloidHypoidGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6918.KlingelnbergCycloPalloidHypoidGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponseAtASpeed(
            self
        )
