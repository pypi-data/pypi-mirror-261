"""PartToPartShearCouplingHalfStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3803
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "PartToPartShearCouplingHalfStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3844,
        _3790,
        _3846,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfStabilityAnalysis",)


Self = TypeVar("Self", bound="PartToPartShearCouplingHalfStabilityAnalysis")


class PartToPartShearCouplingHalfStabilityAnalysis(_3803.CouplingHalfStabilityAnalysis):
    """PartToPartShearCouplingHalfStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_TO_PART_SHEAR_COUPLING_HALF_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartToPartShearCouplingHalfStabilityAnalysis"
    )

    class _Cast_PartToPartShearCouplingHalfStabilityAnalysis:
        """Special nested class for casting PartToPartShearCouplingHalfStabilityAnalysis to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
            parent: "PartToPartShearCouplingHalfStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_stability_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_3803.CouplingHalfStabilityAnalysis":
            return self._parent._cast(_3803.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_3844.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_3790.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
        ) -> "PartToPartShearCouplingHalfStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis",
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
        instance_to_wrap: "PartToPartShearCouplingHalfStabilityAnalysis.TYPE",
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
    ) -> "PartToPartShearCouplingHalfStabilityAnalysis._Cast_PartToPartShearCouplingHalfStabilityAnalysis":
        return self._Cast_PartToPartShearCouplingHalfStabilityAnalysis(self)
