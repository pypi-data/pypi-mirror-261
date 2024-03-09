"""StraightBevelPlanetGearStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3877
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StraightBevelPlanetGearStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2551
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3783,
        _3771,
        _3799,
        _3827,
        _3844,
        _3790,
        _3846,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelPlanetGearStabilityAnalysis")


class StraightBevelPlanetGearStabilityAnalysis(
    _3877.StraightBevelDiffGearStabilityAnalysis
):
    """StraightBevelPlanetGearStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelPlanetGearStabilityAnalysis"
    )

    class _Cast_StraightBevelPlanetGearStabilityAnalysis:
        """Special nested class for casting StraightBevelPlanetGearStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
            parent: "StraightBevelPlanetGearStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3877.StraightBevelDiffGearStabilityAnalysis":
            return self._parent._cast(_3877.StraightBevelDiffGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3783.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.BevelGearStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3771.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3799.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.ConicalGearStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3827.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.GearStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3844.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.MountableComponentStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3790.ComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3790,
            )

            return self._parent._cast(_3790.ComponentStabilityAnalysis)

        @property
        def part_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3846,
            )

            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
        ) -> "StraightBevelPlanetGearStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelPlanetGearStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2551.StraightBevelPlanetGear":
        """mastapy.system_model.part_model.gears.StraightBevelPlanetGear

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
    ) -> "StraightBevelPlanetGearStabilityAnalysis._Cast_StraightBevelPlanetGearStabilityAnalysis":
        return self._Cast_StraightBevelPlanetGearStabilityAnalysis(self)
