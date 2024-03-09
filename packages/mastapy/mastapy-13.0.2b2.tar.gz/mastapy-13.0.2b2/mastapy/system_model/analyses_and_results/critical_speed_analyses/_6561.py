"""BevelGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6549
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BevelGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2521
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6556,
        _6559,
        _6560,
        _6647,
        _6653,
        _6656,
        _6659,
        _6660,
        _6674,
        _6577,
        _6606,
        _6625,
        _6570,
        _6627,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelGearCriticalSpeedAnalysis")


class BevelGearCriticalSpeedAnalysis(_6549.AGMAGleasonConicalGearCriticalSpeedAnalysis):
    """BevelGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearCriticalSpeedAnalysis")

    class _Cast_BevelGearCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
            parent: "BevelGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6549.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            return self._parent._cast(_6549.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6577.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6606.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6625.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6570.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6627.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6556.BevelDifferentialGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(_6556.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6559.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6559,
            )

            return self._parent._cast(
                _6559.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6560.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6560,
            )

            return self._parent._cast(
                _6560.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6647.SpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6653.StraightBevelDiffGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(_6653.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6656.StraightBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6659.StraightBevelPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(
                _6659.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6660.StraightBevelSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(_6660.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "_6674.ZerolBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6674,
            )

            return self._parent._cast(_6674.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def bevel_gear_critical_speed_analysis(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
        ) -> "BevelGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearCriticalSpeedAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2521.BevelGear":
        """mastapy.system_model.part_model.gears.BevelGear

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
    ) -> "BevelGearCriticalSpeedAnalysis._Cast_BevelGearCriticalSpeedAnalysis":
        return self._Cast_BevelGearCriticalSpeedAnalysis(self)
