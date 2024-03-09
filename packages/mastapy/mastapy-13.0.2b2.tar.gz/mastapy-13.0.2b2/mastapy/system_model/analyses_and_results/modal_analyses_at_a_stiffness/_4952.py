"""RollingRingAssemblyModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
    _4959,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness",
    "RollingRingAssemblyModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.static_loads import _6948
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4859,
        _4940,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="RollingRingAssemblyModalAnalysisAtAStiffness")


class RollingRingAssemblyModalAnalysisAtAStiffness(
    _4959.SpecialisedAssemblyModalAnalysisAtAStiffness
):
    """RollingRingAssemblyModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RollingRingAssemblyModalAnalysisAtAStiffness"
    )

    class _Cast_RollingRingAssemblyModalAnalysisAtAStiffness:
        """Special nested class for casting RollingRingAssemblyModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
            parent: "RollingRingAssemblyModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def specialised_assembly_modal_analysis_at_a_stiffness(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
        ) -> "_4959.SpecialisedAssemblyModalAnalysisAtAStiffness":
            return self._parent._cast(
                _4959.SpecialisedAssemblyModalAnalysisAtAStiffness
            )

        @property
        def abstract_assembly_modal_analysis_at_a_stiffness(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
        ) -> "_4859.AbstractAssemblyModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4859,
            )

            return self._parent._cast(_4859.AbstractAssemblyModalAnalysisAtAStiffness)

        @property
        def part_modal_analysis_at_a_stiffness(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
        ) -> "_4940.PartModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
                _4940,
            )

            return self._parent._cast(_4940.PartModalAnalysisAtAStiffness)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis_at_a_stiffness(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
        ) -> "RollingRingAssemblyModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness",
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
        instance_to_wrap: "RollingRingAssemblyModalAnalysisAtAStiffness.TYPE",
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
    ) -> "RollingRingAssemblyModalAnalysisAtAStiffness._Cast_RollingRingAssemblyModalAnalysisAtAStiffness":
        return self._Cast_RollingRingAssemblyModalAnalysisAtAStiffness(self)
