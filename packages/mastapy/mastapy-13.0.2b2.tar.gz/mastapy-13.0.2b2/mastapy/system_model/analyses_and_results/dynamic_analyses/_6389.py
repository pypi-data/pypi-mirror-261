"""StraightBevelGearDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "StraightBevelGearDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2549
    from mastapy.system_model.analyses_and_results.static_loads import _6965
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6283,
        _6311,
        _6339,
        _6358,
        _6304,
        _6360,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearDynamicAnalysis",)


Self = TypeVar("Self", bound="StraightBevelGearDynamicAnalysis")


class StraightBevelGearDynamicAnalysis(_6295.BevelGearDynamicAnalysis):
    """StraightBevelGearDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelGearDynamicAnalysis")

    class _Cast_StraightBevelGearDynamicAnalysis:
        """Special nested class for casting StraightBevelGearDynamicAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
            parent: "StraightBevelGearDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_dynamic_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_6295.BevelGearDynamicAnalysis":
            return self._parent._cast(_6295.BevelGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_6283.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_6311.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConicalGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_6339.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.GearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_6358.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.MountableComponentDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_6304.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_6360.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
        ) -> "StraightBevelGearDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "StraightBevelGearDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2549.StraightBevelGear":
        """mastapy.system_model.part_model.gears.StraightBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6965.StraightBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearLoadCase

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
    ) -> "StraightBevelGearDynamicAnalysis._Cast_StraightBevelGearDynamicAnalysis":
        return self._Cast_StraightBevelGearDynamicAnalysis(self)
