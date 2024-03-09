"""PartToPartShearCouplingHalfSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3023,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3063,
        _3010,
        _3065,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingHalfSteadyStateSynchronousResponse"
)


class PartToPartShearCouplingHalfSteadyStateSynchronousResponse(
    _3023.CouplingHalfSteadyStateSynchronousResponse
):
    """PartToPartShearCouplingHalfSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
    )

    class _Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse:
        """Special nested class for casting PartToPartShearCouplingHalfSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
            parent: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3023.CouplingHalfSteadyStateSynchronousResponse":
            return self._parent._cast(_3023.CouplingHalfSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3063.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(
                _3063.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3010.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(_3010.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_3065.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
        ) -> "PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PartToPartShearCouplingHalfSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2591.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6933.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

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
    ) -> "PartToPartShearCouplingHalfSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse":
        return self._Cast_PartToPartShearCouplingHalfSteadyStateSynchronousResponse(
            self
        )
