"""PartToPartShearCouplingHalfModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4613
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "PartToPartShearCouplingHalfModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.system_deflections import _2789
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4660,
        _4599,
        _4664,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfModalAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfModalAnalysis")


class PartToPartShearCouplingHalfModalAnalysis(_4613.CouplingHalfModalAnalysis):
    """PartToPartShearCouplingHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfModalAnalysis"
    )

    class _Cast_PartToPartShearCouplingHalfModalAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfModalAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
            parent: "PartToPartShearCouplingHalfModalAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_modal_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
        ) -> "_4613.CouplingHalfModalAnalysis":
            return self._parent._cast(_4613.CouplingHalfModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
        ) -> "_4660.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
        ) -> "_4599.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
        ) -> "_4664.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
        ) -> "PartToPartShearCouplingHalfModalAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingHalfModalAnalysis.TYPE"
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
    def system_deflection_results(
        self: Self,
    ) -> "_2789.PartToPartShearCouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection

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
    ) -> "PartToPartShearCouplingHalfModalAnalysis._Cast_PartToPartShearCouplingHalfModalAnalysis":
        return self._Cast_PartToPartShearCouplingHalfModalAnalysis(self)
