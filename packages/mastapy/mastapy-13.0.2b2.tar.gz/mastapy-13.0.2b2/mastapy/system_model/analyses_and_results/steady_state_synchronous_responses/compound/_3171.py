"""FaceGearCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3176,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "FaceGearCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3041,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3195,
        _3143,
        _3197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="FaceGearCompoundSteadyStateSynchronousResponse")


class FaceGearCompoundSteadyStateSynchronousResponse(
    _3176.GearCompoundSteadyStateSynchronousResponse
):
    """FaceGearCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_FaceGearCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting FaceGearCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
            parent: "FaceGearCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def gear_compound_steady_state_synchronous_response(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3176.GearCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(_3176.GearCompoundSteadyStateSynchronousResponse)

        @property
        def mountable_component_compound_steady_state_synchronous_response(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3195.MountableComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3195,
            )

            return self._parent._cast(
                _3195.MountableComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def component_compound_steady_state_synchronous_response(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3143.ComponentCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3143,
            )

            return self._parent._cast(
                _3143.ComponentCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def face_gear_compound_steady_state_synchronous_response(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
        ) -> "FaceGearCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "FaceGearCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2530.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

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
    ) -> "List[_3041.FaceGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.FaceGearSteadyStateSynchronousResponse]

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
    ) -> "List[_3041.FaceGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.FaceGearSteadyStateSynchronousResponse]

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
    ) -> "FaceGearCompoundSteadyStateSynchronousResponse._Cast_FaceGearCompoundSteadyStateSynchronousResponse":
        return self._Cast_FaceGearCompoundSteadyStateSynchronousResponse(self)
