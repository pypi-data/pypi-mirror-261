"""SynchroniserSleeveSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3103,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "SynchroniserSleeveSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3023,
        _3063,
        _3010,
        _3065,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="SynchroniserSleeveSteadyStateSynchronousResponse")


class SynchroniserSleeveSteadyStateSynchronousResponse(
    _3103.SynchroniserPartSteadyStateSynchronousResponse
):
    """SynchroniserSleeveSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserSleeveSteadyStateSynchronousResponse"
    )

    class _Cast_SynchroniserSleeveSteadyStateSynchronousResponse:
        """Special nested class for casting SynchroniserSleeveSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
            parent: "SynchroniserSleeveSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def synchroniser_part_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_3103.SynchroniserPartSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3103.SynchroniserPartSteadyStateSynchronousResponse
            )

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_3023.CouplingHalfSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3023,
            )

            return self._parent._cast(_3023.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_3063.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(
                _3063.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_3010.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(_3010.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_3065.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_steady_state_synchronous_response(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
        ) -> "SynchroniserSleeveSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse",
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
        instance_to_wrap: "SynchroniserSleeveSteadyStateSynchronousResponse.TYPE",
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
    ) -> "SynchroniserSleeveSteadyStateSynchronousResponse._Cast_SynchroniserSleeveSteadyStateSynchronousResponse":
        return self._Cast_SynchroniserSleeveSteadyStateSynchronousResponse(self)
