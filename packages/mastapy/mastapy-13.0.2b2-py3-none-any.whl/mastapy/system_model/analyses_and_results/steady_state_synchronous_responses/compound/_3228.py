"""StraightBevelGearSetCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3136,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2550
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3098,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3226,
        _3227,
        _3124,
        _3152,
        _3178,
        _3216,
        _3118,
        _3197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="StraightBevelGearSetCompoundSteadyStateSynchronousResponse"
)


class StraightBevelGearSetCompoundSteadyStateSynchronousResponse(
    _3136.BevelGearSetCompoundSteadyStateSynchronousResponse
):
    """StraightBevelGearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
    )

    class _Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting StraightBevelGearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
            parent: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3136.BevelGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3136.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3124.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3152.ConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3178.GearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3178,
            )

            return self._parent._cast(
                _3178.GearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3216,
            )

            return self._parent._cast(
                _3216.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3118.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3118,
            )

            return self._parent._cast(
                _3118.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
        ) -> "StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "StraightBevelGearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2550.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2550.StraightBevelGearSet":
        """mastapy.system_model.part_model.gears.StraightBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3098.StraightBevelGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_gears_compound_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3226.StraightBevelGearCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.StraightBevelGearCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelGearsCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def straight_bevel_meshes_compound_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3227.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound.StraightBevelGearMeshCompoundSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.StraightBevelMeshesCompoundSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3098.StraightBevelGearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.StraightBevelGearSetSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearSetCompoundSteadyStateSynchronousResponse._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
        return self._Cast_StraightBevelGearSetCompoundSteadyStateSynchronousResponse(
            self
        )
