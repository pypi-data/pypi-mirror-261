"""BeltDriveStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3865
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_DRIVE_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BeltDriveStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2578
    from mastapy.system_model.analyses_and_results.static_loads import _6824
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3808,
        _3765,
        _3846,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BeltDriveStabilityAnalysis",)


Self = TypeVar("Self", bound="BeltDriveStabilityAnalysis")


class BeltDriveStabilityAnalysis(_3865.SpecialisedAssemblyStabilityAnalysis):
    """BeltDriveStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BELT_DRIVE_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BeltDriveStabilityAnalysis")

    class _Cast_BeltDriveStabilityAnalysis:
        """Special nested class for casting BeltDriveStabilityAnalysis to subclasses."""

        def __init__(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
            parent: "BeltDriveStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_stability_analysis(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
        ) -> "_3865.SpecialisedAssemblyStabilityAnalysis":
            return self._parent._cast(_3865.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
        ) -> "_3765.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_stability_analysis(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
        ) -> "_3808.CVTStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3808,
            )

            return self._parent._cast(_3808.CVTStabilityAnalysis)

        @property
        def belt_drive_stability_analysis(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
        ) -> "BeltDriveStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BeltDriveStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2578.BeltDrive":
        """mastapy.system_model.part_model.couplings.BeltDrive

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6824.BeltDriveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BeltDriveLoadCase

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
    ) -> "BeltDriveStabilityAnalysis._Cast_BeltDriveStabilityAnalysis":
        return self._Cast_BeltDriveStabilityAnalysis(self)
