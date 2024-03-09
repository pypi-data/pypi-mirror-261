"""GearSetCompoundSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
    _3216,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses.Compound",
    "GearSetCompoundSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3045,
    )
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
        _3124,
        _3131,
        _3136,
        _3149,
        _3152,
        _3167,
        _3173,
        _3182,
        _3186,
        _3189,
        _3192,
        _3202,
        _3219,
        _3225,
        _3228,
        _3243,
        _3246,
        _3118,
        _3197,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("GearSetCompoundSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="GearSetCompoundSteadyStateSynchronousResponse")


class GearSetCompoundSteadyStateSynchronousResponse(
    _3216.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
):
    """GearSetCompoundSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _GEAR_SET_COMPOUND_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GearSetCompoundSteadyStateSynchronousResponse"
    )

    class _Cast_GearSetCompoundSteadyStateSynchronousResponse:
        """Special nested class for casting GearSetCompoundSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
            parent: "GearSetCompoundSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3216.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3216.SpecialisedAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3118.AbstractAssemblyCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3118,
            )

            return self._parent._cast(
                _3118.AbstractAssemblyCompoundSteadyStateSynchronousResponse
            )

        @property
        def part_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3197.PartCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3197,
            )

            return self._parent._cast(_3197.PartCompoundSteadyStateSynchronousResponse)

        @property
        def part_compound_analysis(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3124.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3124,
            )

            return self._parent._cast(
                _3124.AGMAGleasonConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_differential_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3131.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3131,
            )

            return self._parent._cast(
                _3131.BevelDifferentialGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def bevel_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3136.BevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3136,
            )

            return self._parent._cast(
                _3136.BevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def concept_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3149.ConceptGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3149,
            )

            return self._parent._cast(
                _3149.ConceptGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3152.ConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3152,
            )

            return self._parent._cast(
                _3152.ConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def cylindrical_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3167.CylindricalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3167,
            )

            return self._parent._cast(
                _3167.CylindricalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def face_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3173.FaceGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3173,
            )

            return self._parent._cast(
                _3173.FaceGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3182.HypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3182,
            )

            return self._parent._cast(
                _3182.HypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3186.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3186,
            )

            return self._parent._cast(
                _3186.KlingelnbergCycloPalloidConicalGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3189.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3189,
            )

            return self._parent._cast(
                _3189.KlingelnbergCycloPalloidHypoidGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3192.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3192,
            )

            return self._parent._cast(
                _3192.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def planetary_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3202.PlanetaryGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3202,
            )

            return self._parent._cast(
                _3202.PlanetaryGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def spiral_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3219.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3219,
            )

            return self._parent._cast(
                _3219.SpiralBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_diff_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3225.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3225,
            )

            return self._parent._cast(
                _3225.StraightBevelDiffGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def straight_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3228.StraightBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3228,
            )

            return self._parent._cast(
                _3228.StraightBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def worm_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3243.WormGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3243,
            )

            return self._parent._cast(
                _3243.WormGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def zerol_bevel_gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "_3246.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.compound import (
                _3246,
            )

            return self._parent._cast(
                _3246.ZerolBevelGearSetCompoundSteadyStateSynchronousResponse
            )

        @property
        def gear_set_compound_steady_state_synchronous_response(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
        ) -> "GearSetCompoundSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse",
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
        instance_to_wrap: "GearSetCompoundSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_3045.GearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.GearSetSteadyStateSynchronousResponse]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_3045.GearSetSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.GearSetSteadyStateSynchronousResponse]

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
    def cast_to(
        self: Self,
    ) -> "GearSetCompoundSteadyStateSynchronousResponse._Cast_GearSetCompoundSteadyStateSynchronousResponse":
        return self._Cast_GearSetCompoundSteadyStateSynchronousResponse(self)
