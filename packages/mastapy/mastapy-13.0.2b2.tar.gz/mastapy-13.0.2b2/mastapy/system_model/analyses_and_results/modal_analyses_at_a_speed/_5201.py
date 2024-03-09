"""PartToPartShearCouplingHalfModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5157
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "PartToPartShearCouplingHalfModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5197,
        _5144,
        _5199,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfModalAnalysisAtASpeed")


class PartToPartShearCouplingHalfModalAnalysisAtASpeed(
    _5157.CouplingHalfModalAnalysisAtASpeed
):
    """PartToPartShearCouplingHalfModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed"
    )

    class _Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed:
        """Special nested class for casting PartToPartShearCouplingHalfModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
            parent: "PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ) -> "_5157.CouplingHalfModalAnalysisAtASpeed":
            return self._parent._cast(_5157.CouplingHalfModalAnalysisAtASpeed)

        @property
        def mountable_component_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ) -> "_5197.MountableComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5197,
            )

            return self._parent._cast(_5197.MountableComponentModalAnalysisAtASpeed)

        @property
        def component_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ) -> "_5144.ComponentModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5144,
            )

            return self._parent._cast(_5144.ComponentModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ) -> "_5199.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis_at_a_speed(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
        ) -> "PartToPartShearCouplingHalfModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed",
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
        instance_to_wrap: "PartToPartShearCouplingHalfModalAnalysisAtASpeed.TYPE",
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
    ) -> "PartToPartShearCouplingHalfModalAnalysisAtASpeed._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed":
        return self._Cast_PartToPartShearCouplingHalfModalAnalysisAtASpeed(self)
