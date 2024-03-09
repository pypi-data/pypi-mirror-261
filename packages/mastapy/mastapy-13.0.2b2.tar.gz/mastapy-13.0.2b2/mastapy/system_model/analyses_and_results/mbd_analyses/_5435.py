"""FaceGearMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5441
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "FaceGearMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.static_loads import _6887
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5466,
        _5406,
        _5469,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7551, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="FaceGearMultibodyDynamicsAnalysis")


class FaceGearMultibodyDynamicsAnalysis(_5441.GearMultibodyDynamicsAnalysis):
    """FaceGearMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMultibodyDynamicsAnalysis")

    class _Cast_FaceGearMultibodyDynamicsAnalysis:
        """Special nested class for casting FaceGearMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
            parent: "FaceGearMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_multibody_dynamics_analysis(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
        ) -> "_5441.GearMultibodyDynamicsAnalysis":
            return self._parent._cast(_5441.GearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
        ) -> "_5466.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
        ) -> "_5406.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
        ) -> "_5469.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(_5469.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
        ) -> "_7551.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
        ) -> "FaceGearMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "FaceGearMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2530.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6887.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

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
    ) -> "FaceGearMultibodyDynamicsAnalysis._Cast_FaceGearMultibodyDynamicsAnalysis":
        return self._Cast_FaceGearMultibodyDynamicsAnalysis(self)
