"""SynchroniserSleeveStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3884
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "SynchroniserSleeveStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3803,
        _3844,
        _3790,
        _3846,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveStabilityAnalysis",)


Self = TypeVar("Self", bound="SynchroniserSleeveStabilityAnalysis")


class SynchroniserSleeveStabilityAnalysis(_3884.SynchroniserPartStabilityAnalysis):
    """SynchroniserSleeveStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeveStabilityAnalysis")

    class _Cast_SynchroniserSleeveStabilityAnalysis:
        """Special nested class for casting SynchroniserSleeveStabilityAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
            parent: "SynchroniserSleeveStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def synchroniser_part_stability_analysis(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "_3884.SynchroniserPartStabilityAnalysis":
            return self._parent._cast(_3884.SynchroniserPartStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "_3803.CouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.CouplingHalfStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "_3844.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "_3790.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
        ) -> "SynchroniserSleeveStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6973.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

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
    ) -> (
        "SynchroniserSleeveStabilityAnalysis._Cast_SynchroniserSleeveStabilityAnalysis"
    ):
        return self._Cast_SynchroniserSleeveStabilityAnalysis(self)
