"""SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3362,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3285,
        _3324,
        _3272,
        _3326,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft")


class SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft(
    _3362.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
):
    """SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
            parent: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def synchroniser_part_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3362.SynchroniserPartSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3362.SynchroniserPartSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def coupling_half_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3285.CouplingHalfSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3285,
            )

            return self._parent._cast(
                _3285.CouplingHalfSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3272.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3326.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(_3326.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response_on_a_shaft(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
        ) -> "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6973.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

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
    ) -> "SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_SynchroniserSleeveSteadyStateSynchronousResponseOnAShaft(self)
