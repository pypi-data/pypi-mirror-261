"""KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
    _3054,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponses",
        "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import _6921
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
        _3019,
        _3046,
        _3063,
        _3010,
        _3065,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
)


class KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse(
    _3054.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
):
    """KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse

    This is a mastapy class.
    """

    TYPE = (
        _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_STEADY_STATE_SYNCHRONOUS_RESPONSE
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_3054.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse":
            return self._parent._cast(
                _3054.KlingelnbergCycloPalloidConicalGearSteadyStateSynchronousResponse
            )

        @property
        def conical_gear_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_3019.ConicalGearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3019,
            )

            return self._parent._cast(_3019.ConicalGearSteadyStateSynchronousResponse)

        @property
        def gear_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_3046.GearSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3046,
            )

            return self._parent._cast(_3046.GearSteadyStateSynchronousResponse)

        @property
        def mountable_component_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_3063.MountableComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3063,
            )

            return self._parent._cast(
                _3063.MountableComponentSteadyStateSynchronousResponse
            )

        @property
        def component_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_3010.ComponentSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3010,
            )

            return self._parent._cast(_3010.ComponentSteadyStateSynchronousResponse)

        @property
        def part_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_3065.PartSteadyStateSynchronousResponse":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses import (
                _3065,
            )

            return self._parent._cast(_3065.PartSteadyStateSynchronousResponse)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_steady_state_synchronous_response(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(
        self: Self,
    ) -> "_6921.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidSpiralBevelGearLoadCase

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearSteadyStateSynchronousResponse(
            self
        )
