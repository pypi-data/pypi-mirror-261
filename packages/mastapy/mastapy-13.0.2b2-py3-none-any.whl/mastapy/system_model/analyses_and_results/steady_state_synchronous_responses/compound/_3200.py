"""PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3157,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3067,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3195,
        _3143,
        _3197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse"
)


class PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse(
    _3157.CouplingHalfCompoundSteadyStateSynchronousResponse
):
    """PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
            parent: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3157.CouplingHalfCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3157.CouplingHalfCompoundSteadyStateSynchronousResponse
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(
                _3195.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3143.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3143,
            )

            return self._parent._cast(
                _3143.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
        ) -> "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse.TYPE",
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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3067.PartToPartShearCouplingHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PartToPartShearCouplingHalfSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3067.PartToPartShearCouplingHalfSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.PartToPartShearCouplingHalfSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse":
        return self._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponse(
            self
        )
