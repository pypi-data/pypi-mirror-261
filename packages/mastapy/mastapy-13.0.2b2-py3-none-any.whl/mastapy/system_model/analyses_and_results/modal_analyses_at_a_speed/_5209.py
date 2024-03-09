"""RingPinsModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5197
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "RingPinsModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.cycloidal import _2572
    from mastapy.system_model.analyses_and_results.static_loads import _6946
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5144,
        _5199,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="RingPinsModalAnalysisAtASpeed")


class RingPinsModalAnalysisAtASpeed(_5197.MountableComponentModalAnalysisAtASpeed):
    """RingPinsModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _RING_PINS_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RingPinsModalAnalysisAtASpeed")

    class _Cast_RingPinsModalAnalysisAtASpeed:
        """Special nested class for casting RingPinsModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
            parent: "RingPinsModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
        ) -> "_5197.MountableComponentModalAnalysisAtASpeed":
            return self._parent._cast(_5197.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
        ) -> "_5144.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
        ) -> "_5199.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def ring_pins_modal_analysis_at_a_speed(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
        ) -> "RingPinsModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RingPinsModalAnalysisAtASpeed.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2572.RingPins":
        """mastapy.system_model.part_model.cycloidal.RingPins

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6946.RingPinsLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsLoadCase

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
    ) -> "RingPinsModalAnalysisAtASpeed._Cast_RingPinsModalAnalysisAtASpeed":
        return self._Cast_RingPinsModalAnalysisAtASpeed(self)
