"""SynchroniserHalfModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4701
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "SynchroniserHalfModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.static_loads import _6970
    from mastapy.system_model.analyses_and_results.system_deflections import _2823
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4613,
        _4660,
        _4599,
        _4664,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfModalAnalysis",)


Self = TypeVar("Self", bound="SynchroniserHalfModalAnalysis")


class SynchroniserHalfModalAnalysis(_4701.SynchroniserPartModalAnalysis):
    """SynchroniserHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserHalfModalAnalysis")

    class _Cast_SynchroniserHalfModalAnalysis:
        """Special nested class for casting SynchroniserHalfModalAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
            parent: "SynchroniserHalfModalAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "_4701.SynchroniserPartModalAnalysis":
            return self._parent._cast(_4701.SynchroniserPartModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "_4613.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "_4660.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "_4599.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "_4664.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
        ) -> "SynchroniserHalfModalAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserHalfModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6970.SynchroniserHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2823.SynchroniserHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SynchroniserHalfSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserHalfModalAnalysis._Cast_SynchroniserHalfModalAnalysis":
        return self._Cast_SynchroniserHalfModalAnalysis(self)
