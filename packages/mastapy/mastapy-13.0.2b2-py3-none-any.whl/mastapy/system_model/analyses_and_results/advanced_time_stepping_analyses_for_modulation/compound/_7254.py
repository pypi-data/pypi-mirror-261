"""StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7248,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7125,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7159,
        _7147,
        _7175,
        _7201,
        _7220,
        _7168,
        _7222,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self",
    bound="StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
)


class StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7248.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_PLANET_GEAR_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7248.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7248.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7159.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7159,
            )

            return self._parent._cast(
                _7159.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7147.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7147,
            )

            return self._parent._cast(
                _7147.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7175.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7175,
            )

            return self._parent._cast(
                _7175.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7201.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7201,
            )

            return self._parent._cast(
                _7201.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
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
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7168,
            )

            return self._parent._cast(
                _7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7125.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7125.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation]

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
    def cast_to(
        self: Self,
    ) -> "StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
