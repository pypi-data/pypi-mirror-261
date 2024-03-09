"""PartToPartShearCouplingHalfDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "PartToPartShearCouplingHalfDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6358,
        _6304,
        _6360,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfDynamicAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfDynamicAnalysis")


class PartToPartShearCouplingHalfDynamicAnalysis(_6318.CouplingHalfDynamicAnalysis):
    """PartToPartShearCouplingHalfDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfDynamicAnalysis"
    )

    class _Cast_PartToPartShearCouplingHalfDynamicAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfDynamicAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
            parent: "PartToPartShearCouplingHalfDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_dynamic_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_6318.CouplingHalfDynamicAnalysis":
            return self._parent._cast(_6318.CouplingHalfDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_6358.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_6304.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_6360.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
        ) -> "PartToPartShearCouplingHalfDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis",
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
        self: Self, instance_to_wrap: "PartToPartShearCouplingHalfDynamicAnalysis.TYPE"
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
    ) -> "PartToPartShearCouplingHalfDynamicAnalysis._Cast_PartToPartShearCouplingHalfDynamicAnalysis":
        return self._Cast_PartToPartShearCouplingHalfDynamicAnalysis(self)
