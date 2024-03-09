"""AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7175,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7016,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7154,
        _7157,
        _7158,
        _7159,
        _7205,
        _7242,
        _7248,
        _7251,
        _7254,
        _7255,
        _7269,
        _7201,
        _7220,
        _7168,
        _7222,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self",
    bound="AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7175.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7175.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7175.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7201.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7201,
            )

            return self._parent._cast(
                _7201.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7220.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7168,
            )

            return self._parent._cast(
                _7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7154.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7154,
            )

            return self._parent._cast(
                _7154.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7157.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7157,
            )

            return self._parent._cast(
                _7157.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7158.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7158,
            )

            return self._parent._cast(
                _7158.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7159.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7159,
            )

            return self._parent._cast(
                _7159.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7205.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7205,
            )

            return self._parent._cast(
                _7205.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7242.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7242,
            )

            return self._parent._cast(
                _7242.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7248.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7248,
            )

            return self._parent._cast(
                _7248.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7251.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7251,
            )

            return self._parent._cast(
                _7251.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7254.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7254,
            )

            return self._parent._cast(
                _7254.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7255.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7255,
            )

            return self._parent._cast(
                _7255.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7269.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7269,
            )

            return self._parent._cast(
                _7269.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7016.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7016.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
