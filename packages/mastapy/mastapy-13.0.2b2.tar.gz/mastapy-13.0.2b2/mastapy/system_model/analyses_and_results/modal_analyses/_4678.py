"""RollingRingModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses import _4613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "RollingRingModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2598
    from mastapy.system_model.analyses_and_results.static_loads import _6950
    from mastapy.system_model.analyses_and_results.system_deflections import _2801
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4660,
        _4599,
        _4664,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingModalAnalysis",)


Self = TypeVar("Self", bound="RollingRingModalAnalysis")


class RollingRingModalAnalysis(_4613.CouplingHalfModalAnalysis):
    """RollingRingModalAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingModalAnalysis")

    class _Cast_RollingRingModalAnalysis:
        """Special nested class for casting RollingRingModalAnalysis to subclasses."""

        def __init__(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
            parent: "RollingRingModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_4613.CouplingHalfModalAnalysis":
            return self._parent._cast(_4613.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_4660.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_4599.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_4664.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis",
        ) -> "RollingRingModalAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "RollingRingModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2598.RollingRing":
        """mastapy.system_model.part_model.couplings.RollingRing

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6950.RollingRingLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RollingRingLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2801.RollingRingSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RollingRingSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[RollingRingModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.RollingRingModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RollingRingModalAnalysis._Cast_RollingRingModalAnalysis":
        return self._Cast_RollingRingModalAnalysis(self)
