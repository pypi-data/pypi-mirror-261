"""SpiralBevelGearCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6561
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SpiralBevelGearCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2545
    from mastapy.system_model.analyses_and_results.static_loads import _6956
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6549,
        _6577,
        _6606,
        _6625,
        _6570,
        _6627,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearCriticalSpeedAnalysis")


class SpiralBevelGearCriticalSpeedAnalysis(_6561.BevelGearCriticalSpeedAnalysis):
    """SpiralBevelGearCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpiralBevelGearCriticalSpeedAnalysis")

    class _Cast_SpiralBevelGearCriticalSpeedAnalysis:
        """Special nested class for casting SpiralBevelGearCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
            parent: "SpiralBevelGearCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6561.BevelGearCriticalSpeedAnalysis":
            return self._parent._cast(_6561.BevelGearCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6549.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6549,
            )

            return self._parent._cast(_6549.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6577.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.ConicalGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6606.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.GearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6625.MountableComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6625,
            )

            return self._parent._cast(_6625.MountableComponentCriticalSpeedAnalysis)

        @property
        def component_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6570.ComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6570,
            )

            return self._parent._cast(_6570.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_6627.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
        ) -> "SpiralBevelGearCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2545.SpiralBevelGear":
        """mastapy.system_model.part_model.gears.SpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6956.SpiralBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearLoadCase

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
    ) -> "SpiralBevelGearCriticalSpeedAnalysis._Cast_SpiralBevelGearCriticalSpeedAnalysis":
        return self._Cast_SpiralBevelGearCriticalSpeedAnalysis(self)
