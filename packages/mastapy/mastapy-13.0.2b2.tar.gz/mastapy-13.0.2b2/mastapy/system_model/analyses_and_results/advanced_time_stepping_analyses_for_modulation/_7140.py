"""ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7029,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2555
    from mastapy.system_model.analyses_and_results.static_loads import _6988
    from mastapy.system_model.analyses_and_results.system_deflections import _2843
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7016,
        _7045,
        _7071,
        _7091,
        _7038,
        _7093,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar("Self", bound="ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation")


class ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation(
    _7029.BevelGearAdvancedTimeSteppingAnalysisForModulation
):
    """ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
            parent: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7029.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7029.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7016.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7016,
            )

            return self._parent._cast(
                _7016.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7045.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7071.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7071,
            )

            return self._parent._cast(
                _7071.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7038.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7038,
            )

            return self._parent._cast(
                _7038.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7093.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
        ) -> "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2555.ZerolBevelGear":
        """mastapy.system_model.part_model.gears.ZerolBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6988.ZerolBevelGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2843.ZerolBevelGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ZerolBevelGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation(self)
