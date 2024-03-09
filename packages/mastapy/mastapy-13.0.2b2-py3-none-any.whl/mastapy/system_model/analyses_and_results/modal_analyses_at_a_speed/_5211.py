"""RollingRingAssemblyModalAnalysisAtASpeed"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import _5218
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtASpeed",
    "RollingRingAssemblyModalAnalysisAtASpeed",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.static_loads import _6948
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
        _5119,
        _5199,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyModalAnalysisAtASpeed",)


Self = TypeVar("Self", bound="RollingRingAssemblyModalAnalysisAtASpeed")


class RollingRingAssemblyModalAnalysisAtASpeed(
    _5218.SpecialisedAssemblyModalAnalysisAtASpeed
):
    """RollingRingAssemblyModalAnalysisAtASpeed

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_MODAL_ANALYSIS_AT_A_SPEED
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyModalAnalysisAtASpeed"
    )

    class _Cast_RollingRingAssemblyModalAnalysisAtASpeed:
        """Special nested class for casting RollingRingAssemblyModalAnalysisAtASpeed to subclasses."""

        def __init__(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
            parent: "RollingRingAssemblyModalAnalysisAtASpeed",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_speed(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ) -> "_5218.SpecialisedAssemblyModalAnalysisAtASpeed":
            return self._parent._cast(_5218.SpecialisedAssemblyModalAnalysisAtASpeed)

        @property
        def abstract_assembly_modal_analysis_at_a_speed(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ) -> "_5119.AbstractAssemblyModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5119,
            )

            return self._parent._cast(_5119.AbstractAssemblyModalAnalysisAtASpeed)

        @property
        def part_modal_analysis_at_a_speed(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ) -> "_5199.PartModalAnalysisAtASpeed":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_speed import (
                _5199,
            )

            return self._parent._cast(_5199.PartModalAnalysisAtASpeed)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_speed(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
        ) -> "RollingRingAssemblyModalAnalysisAtASpeed":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyModalAnalysisAtASpeed.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2599.RollingRingAssembly":
        """mastapy.system_model.part_model.couplings.RollingRingAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6948.RollingRingAssemblyLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingAssemblyLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingAssemblyModalAnalysisAtASpeed._Cast_RollingRingAssemblyModalAnalysisAtASpeed":
        return self._Cast_RollingRingAssemblyModalAnalysisAtASpeed(self)
