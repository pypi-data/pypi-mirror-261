"""ZerolBevelGearSetSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3002,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
    "ZerolBevelGearSetSteadyStateSynchronousResponse",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2556
    from mastapy.system_model.analyses_and_results.static_loads import _6990
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3117,
        _3115,
        _2990,
        _3018,
        _3045,
        _3084,
        _2985,
        _3065,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearSetSteadyStateSynchronousResponse",)


Self = TypeVar("Self", bound="ZerolBevelGearSetSteadyStateSynchronousResponse")


class ZerolBevelGearSetSteadyStateSynchronousResponse(
    _3002.BevelGearSetSteadyStateSynchronousResponse
):
    """ZerolBevelGearSetSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearSetSteadyStateSynchronousResponse"
    )

    class _Cast_ZerolBevelGearSetSteadyStateSynchronousResponse:
        """Special nested class for casting ZerolBevelGearSetSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
            parent: "ZerolBevelGearSetSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_steady_state_synchronous_response(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_3002.BevelGearSetSteadyStateSynchronousResponse":
            return self._parent._cast(_3002.BevelGearSetSteadyStateSynchronousResponse)

        @property
        def agma_gleason_conical_gear_set_steady_state_synchronous_response(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_2990.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2990,
            )

            return self._parent._cast(
                _2990.AGMAGleasonConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_set_steady_state_synchronous_response(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_3018.ConicalGearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3018,
            )

            return self._parent._cast(
                _3018.ConicalGearSetSteadyStateSynchronousResponse
            )

        @property
        def gear_set_steady_state_synchronous_response(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_3045.GearSetSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3045,
            )

            return self._parent._cast(_3045.GearSetSteadyStateSynchronousResponse)

        @property
        def specialised_assembly_steady_state_synchronous_response(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_3084.SpecialisedAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3084,
            )

            return self._parent._cast(
                _3084.SpecialisedAssemblySteadyStateSynchronousResponse
            )

        @property
        def abstract_assembly_steady_state_synchronous_response(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_2985.AbstractAssemblySteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _2985,
            )

            return self._parent._cast(
                _2985.AbstractAssemblySteadyStateSynchronousResponse
            )

        @property
        def part_steady_state_synchronous_response(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_3065.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_set_steady_state_synchronous_response(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
        ) -> "ZerolBevelGearSetSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse",
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
        instance_to_wrap: "ZerolBevelGearSetSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2556.ZerolBevelGearSet":
        """mastapy.system_model.part_model.gears.ZerolBevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6990.ZerolBevelGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def zerol_bevel_gears_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3117.ZerolBevelGearSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ZerolBevelGearSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelGearsSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def zerol_bevel_meshes_steady_state_synchronous_response(
        self: Self,
    ) -> "List[_3115.ZerolBevelGearMeshSteadyStateSynchronousResponse]":
        """List[mastapy.system_model.analyses_and_results.steady_state_synchronous_responses.ZerolBevelGearMeshSteadyStateSynchronousResponse]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ZerolBevelMeshesSteadyStateSynchronousResponse

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearSetSteadyStateSynchronousResponse._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse":
        return self._Cast_ZerolBevelGearSetSteadyStateSynchronousResponse(self)
