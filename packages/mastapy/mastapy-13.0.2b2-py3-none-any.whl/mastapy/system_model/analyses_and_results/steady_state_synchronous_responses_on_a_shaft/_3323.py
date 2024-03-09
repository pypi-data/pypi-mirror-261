"""MeasurementComponentSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3370,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.static_loads import _6925
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3324,
        _3272,
        _3326,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar(
    "Self", bound="MeasurementComponentSteadyStateSynchronousResponseOnAShaft"
)


class MeasurementComponentSteadyStateSynchronousResponseOnAShaft(
    _3370.VirtualComponentSteadyStateSynchronousResponseOnAShaft
):
    """MeasurementComponentSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting MeasurementComponentSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
            parent: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def virtual_component_steady_state_synchronous_response_on_a_shaft(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3370.VirtualComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3370.VirtualComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def mountable_component_steady_state_synchronous_response_on_a_shaft(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3324.MountableComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3324,
            )

            return self._parent._cast(
                _3324.MountableComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def component_steady_state_synchronous_response_on_a_shaft(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3272.ComponentSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3272,
            )

            return self._parent._cast(
                _3272.ComponentSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3326.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(_3326.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def measurement_component_steady_state_synchronous_response_on_a_shaft(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
        ) -> "MeasurementComponentSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "MeasurementComponentSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2465.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6925.MeasurementComponentLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.MeasurementComponentLoadCase

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
    ) -> "MeasurementComponentSteadyStateSynchronousResponseOnAShaft._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_MeasurementComponentSteadyStateSynchronousResponseOnAShaft(
            self
        )
