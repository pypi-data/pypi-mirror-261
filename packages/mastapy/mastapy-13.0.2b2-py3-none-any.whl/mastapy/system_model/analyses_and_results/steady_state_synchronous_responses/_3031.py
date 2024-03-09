"""CycloidalDiscSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _2987,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "CycloidalDiscSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2571
    from mastapy.system_model.analyses_and_results.static_loads import _6862
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _2986,
        _3010,
        _3065,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="CycloidalDiscSteadyStateSynchronousResponse")


class CycloidalDiscSteadyStateSynchronousResponse(
    _2987.AbstractShaftSteadyStateSynchronousResponse
):
    """CycloidalDiscSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CycloidalDiscSteadyStateSynchronousResponse"
    )

    class _Cast_CycloidalDiscSteadyStateSynchronousResponse:
        """Special nested class for casting CycloidalDiscSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
            parent: "CycloidalDiscSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def abstract_shaft_steady_state_synchronous_response(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_2987.AbstractShaftSteadyStateSynchronousResponse":
            return self._parent._cast(_2987.AbstractShaftSteadyStateSynchronousResponse)

        @property
        def abstract_shaft_or_housing_steady_state_synchronous_response(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_2986.AbstractShaftOrHousingSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2986,
            )

            return self._parent._cast(
                _2986.AbstractShaftOrHousingSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_3010.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(_3010.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_3065.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_steady_state_synchronous_response(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
        ) -> "CycloidalDiscSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse",
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
        self: Self, instance_to_wrap: "CycloidalDiscSteadyStateSynchronousResponse.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2571.CycloidalDisc":
        """mastapy.system_model.part_model.cycloidal.CycloidalDisc

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6862.CycloidalDiscLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscLoadCase

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
    ) -> "CycloidalDiscSteadyStateSynchronousResponse._Cast_CycloidalDiscSteadyStateSynchronousResponse":
        return self._Cast_CycloidalDiscSteadyStateSynchronousResponse(self)
