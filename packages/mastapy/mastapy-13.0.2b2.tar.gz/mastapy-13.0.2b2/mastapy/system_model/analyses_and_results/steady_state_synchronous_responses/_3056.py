"""KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3053,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2541
    from mastapy.system_model.analyses_and_results.static_loads import _6920
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3057,
        _3055,
        _3018,
        _3045,
        _3084,
        _2985,
        _3065,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse"
)


class KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse(
    _3053.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> (
            "_3053.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse"
        ):
            return self._parent._cast(
                _3053.KlingelnbergCycloPalloidConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_3018.ConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_3045.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_3084.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_2985.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2985,
            )

            return self._parent._cast(
                _2985.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_3065.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
        ) -> "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2541.KlingelnbergCycloPalloidHypoidGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidHypoidGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(
        self: Self,
    ) -> "_6920.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3057.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidHypoidGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidGearsSteadyStateSynchronousResponse
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def klingelnberg_cyclo_palloid_hypoid_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3055.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.KlingelnbergCycloPalloidHypoidGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = (
            self.wrapped.KlingelnbergCycloPalloidHypoidMeshesSteadyStateSynchronousResponse
        )

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearSetSteadyStateSynchronousResponse(
            self
        )
