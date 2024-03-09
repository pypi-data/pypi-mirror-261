"""MeasurementComponentSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3111,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "MeasurementComponentSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.static_loads import _6925
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3063,
        _3010,
        _3065,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="MeasurementComponentSteadyStateSynchronousResponse")


class MeasurementComponentSteadyStateSynchronousResponse(
    _3111.VirtualComponentSteadyStateSynchronousResponse
):
    """MeasurementComponentSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentSteadyStateSynchronousResponse"
    )

    class _Cast_MeasurementComponentSteadyStateSynchronousResponse:
        """Special nested class for casting MeasurementComponentSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
            parent: "MeasurementComponentSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def virtual_component_steady_state_synchronous_response(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_3111.VirtualComponentSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3111.VirtualComponentSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_3063.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(
                _3063.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_3010.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(_3010.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_3065.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def measurement_component_steady_state_synchronous_response(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
        ) -> "MeasurementComponentSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse",
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
        instance_to_wrap: "MeasurementComponentSteadyStateSynchronousResponse.TYPE",
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
    ) -> "MeasurementComponentSteadyStateSynchronousResponse._Cast_MeasurementComponentSteadyStateSynchronousResponse":
        return self._Cast_MeasurementComponentSteadyStateSynchronousResponse(self)
