"""PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
    _3675,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesAtASpeed.Compound",
    "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed import (
        _3587,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
        _3713,
        _3661,
        _3715,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",)


Self = TypeVar(
    "Self",
    bound="PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
)


class PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(
    _3675.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
):
    """PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
    )

    class _Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed:
        """Special nested class for casting PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
            parent: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3675.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
            return self._parent._cast(
                _3675.CouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def mountable_component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3713.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3713,
            )

            return self._parent._cast(
                _3713.MountableComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def component_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3661.ComponentCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3661,
            )

            return self._parent._cast(
                _3661.ComponentCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_3715.PartCompoundSteadyStateSynchronousResponseAtASpeed":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.compound import (
                _3715,
            )

            return self._parent._cast(
                _3715.PartCompoundSteadyStateSynchronousResponseAtASpeed
            )

        @property
        def part_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_steady_state_synchronous_response_at_a_speed(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
        ) -> (
            "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed"
        ):
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed",
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
        instance_to_wrap: "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed.TYPE",
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
    ) -> (
        "List[_3587.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed]

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
    ) -> (
        "List[_3587.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed]"
    ):
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_at_a_speed.PartToPartShearCouplingHalfSteadyStateSynchronousResponseAtASpeed]

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
    ) -> "PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed":
        return self._Cast_PartToPartShearCouplingHalfCompoundSteadyStateSynchronousResponseAtASpeed(
            self
        )
