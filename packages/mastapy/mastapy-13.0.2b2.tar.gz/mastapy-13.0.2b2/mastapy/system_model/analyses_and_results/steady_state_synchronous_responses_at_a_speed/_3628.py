"""UnbalancedMassSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
    _3629,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed",
    "UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.static_loads import _6983
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3583,
        _3531,
        _3585,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar("Self", bound="UnbalancedMassSteadyStateSynchronousResponseAtASpeed")


class UnbalancedMassSteadyStateSynchronousResponseAtASpeed(
    _3629.VirtualComponentSteadyStateSynchronousResponseAtASpeed
):
    """UnbalancedMassSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed"
    )

    class _Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting UnbalancedMassSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
            parent: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def virtual_component_steady_state_synchronous_response_at_a_speed(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3629.VirtualComponentSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3629.VirtualComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_steady_state_synchronous_response_at_a_speed(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3583.MountableComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3583,
            )

            return self._parent._cast(
                _3583.MountableComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_steady_state_synchronous_response_at_a_speed(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3531.ComponentSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3531,
            )

            return self._parent._cast(
                _3531.ComponentSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_steady_state_synchronous_response_at_a_speed(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3585.PartSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
                _3585,
            )

            return self._parent._cast(_3585.PartSteadyStateSynchronousResponseAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def unbalanced_mass_steady_state_synchronous_response_at_a_speed(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
        ) -> "UnbalancedMassSteadyStateSynchronousResponseAtASpeed":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "UnbalancedMassSteadyStateSynchronousResponseAtASpeed.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6983.UnbalancedMassLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.UnbalancedMassLoadCase

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
    ) -> "UnbalancedMassSteadyStateSynchronousResponseAtASpeed._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_UnbalancedMassSteadyStateSynchronousResponseAtASpeed(self)
