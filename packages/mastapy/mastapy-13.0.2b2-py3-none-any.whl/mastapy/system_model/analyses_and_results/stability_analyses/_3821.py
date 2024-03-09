"""FaceGearSetStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses import _3826
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_SET_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "FaceGearSetStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2531
    from mastapy.system_model.analyses_and_results.static_loads import _6889
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3822,
        _3820,
        _3865,
        _3765,
        _3846,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearSetStabilityAnalysis",)


Self = TypeVar("Self", bound="FaceGearSetStabilityAnalysis")


class FaceGearSetStabilityAnalysis(_3826.GearSetStabilityAnalysis):
    """FaceGearSetStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_SET_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearSetStabilityAnalysis")

    class _Cast_FaceGearSetStabilityAnalysis:
        """Special nested class for casting FaceGearSetStabilityAnalysis to subclasses."""

        def __init__(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
            parent: "FaceGearSetStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_3826.GearSetStabilityAnalysis":
            return self._parent._cast(_3826.GearSetStabilityAnalysis)

        @property
        def specialised_assembly_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_3865.SpecialisedAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3865,
            )

            return self._parent._cast(_3865.SpecialisedAssemblyStabilityAnalysis)

        @property
        def abstract_assembly_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_3765.AbstractAssemblyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3765,
            )

            return self._parent._cast(_3765.AbstractAssemblyStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def face_gear_set_stability_analysis(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
        ) -> "FaceGearSetStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearSetStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2531.FaceGearSet":
        """mastapy.system_model.part_model.gears.FaceGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6889.FaceGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def face_gears_stability_analysis(
        self: Self,
    ) -> "List[_3822.FaceGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FaceGearStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceGearsStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def face_meshes_stability_analysis(
        self: Self,
    ) -> "List[_3820.FaceGearMeshStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FaceGearMeshStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.FaceMeshesStabilityAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "FaceGearSetStabilityAnalysis._Cast_FaceGearSetStabilityAnalysis":
        return self._Cast_FaceGearSetStabilityAnalysis(self)
