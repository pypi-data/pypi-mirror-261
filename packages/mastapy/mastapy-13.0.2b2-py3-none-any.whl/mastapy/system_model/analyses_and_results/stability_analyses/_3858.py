"""RollingRingAssemblyStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3865
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROLLING_RING_ASSEMBLY_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "RollingRingAssemblyStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2599
    from mastapy.system_model.analyses_and_results.static_loads import _6948
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3765,
        _3846,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("RollingRingAssemblyStabilityAnalysis",)


Self = TypeVar("Self", bound="RollingRingAssemblyStabilityAnalysis")


class RollingRingAssemblyStabilityAnalysis(_3865.SpecialisedAssemblyStabilityAnalysis):
    """RollingRingAssemblyStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _ROLLING_RING_ASSEMBLY_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_RollingRingAssemblyStabilityAnalysis")

    class _Cast_RollingRingAssemblyStabilityAnalysis:
        """Special nested class for casting RollingRingAssemblyStabilityAnalysis to subclasses."""

        def __init__(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
            parent: "RollingRingAssemblyStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_3865.SpecialisedAssemblyStabilityAnalysis":
            return self._parent._cast(_3865.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_3765.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def rolling_ring_assembly_stability_analysis(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
        ) -> "RollingRingAssemblyStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis",
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
        self: Self, instance_to_wrap: "RollingRingAssemblyStabilityAnalysis.TYPE"
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
    ) -> "RollingRingAssemblyStabilityAnalysis._Cast_RollingRingAssemblyStabilityAnalysis":
        return self._Cast_RollingRingAssemblyStabilityAnalysis(self)
