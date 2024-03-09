"""AGMAGleasonConicalGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3799
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "AGMAGleasonConicalGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3778,
        _3779,
        _3780,
        _3783,
        _3831,
        _3868,
        _3877,
        _3880,
        _3881,
        _3882,
        _3898,
        _3827,
        _3844,
        _3790,
        _3846,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearStabilityAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearStabilityAnalysis")


class AGMAGleasonConicalGearStabilityAnalysis(_3799.ConicalGearStabilityAnalysis):
    """AGMAGleasonConicalGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearStabilityAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearStabilityAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
            parent: "AGMAGleasonConicalGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3799.ConicalGearStabilityAnalysis":
            return self._parent._cast(_3799.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3827.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3844.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3790.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3778.BevelDifferentialGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3779.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3779,
            )

            return self._parent._cast(
                _3779.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3780.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3780,
            )

            return self._parent._cast(_3780.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3783.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.BevelGearStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3831.HypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(_3831.HypoidGearStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3868.SpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(_3868.SpiralBevelGearStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3877.StraightBevelDiffGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3880.StraightBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3881.StraightBevelPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3882.StraightBevelSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.StraightBevelSunGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "_3898.ZerolBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3898,
            )

            return self._parent._cast(_3898.ZerolBevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
        ) -> "AGMAGleasonConicalGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2515.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearStabilityAnalysis._Cast_AGMAGleasonConicalGearStabilityAnalysis":
        return self._Cast_AGMAGleasonConicalGearStabilityAnalysis(self)
