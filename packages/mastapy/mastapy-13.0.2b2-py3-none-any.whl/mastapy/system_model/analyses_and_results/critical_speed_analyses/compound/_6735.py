"""GearCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6754,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "GearCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6606
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6681,
        _6688,
        _6691,
        _6692,
        _6693,
        _6706,
        _6709,
        _6724,
        _6727,
        _6730,
        _6739,
        _6743,
        _6746,
        _6749,
        _6776,
        _6782,
        _6785,
        _6788,
        _6789,
        _6800,
        _6803,
        _6702,
        _6756,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("GearCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="GearCompoundCriticalSpeedAnalysis")


class GearCompoundCriticalSpeedAnalysis(
    _6754.MountableComponentCompoundCriticalSpeedAnalysis
):
    """GearCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearCompoundCriticalSpeedAnalysis")

    class _Cast_GearCompoundCriticalSpeedAnalysis:
        """Special nested class for casting GearCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
            parent: "GearCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6754.MountableComponentCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6754.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6702.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(_6702.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6756.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(_6756.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6681.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6681,
            )

            return self._parent._cast(
                _6681.AGMAGleasonConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6688.BevelDifferentialGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6688,
            )

            return self._parent._cast(
                _6688.BevelDifferentialGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6691.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6691,
            )

            return self._parent._cast(
                _6691.BevelDifferentialPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6692.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6692,
            )

            return self._parent._cast(
                _6692.BevelDifferentialSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6693.BevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6693,
            )

            return self._parent._cast(_6693.BevelGearCompoundCriticalSpeedAnalysis)

        @property
        def concept_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6706.ConceptGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6706,
            )

            return self._parent._cast(_6706.ConceptGearCompoundCriticalSpeedAnalysis)

        @property
        def conical_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6709.ConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6709,
            )

            return self._parent._cast(_6709.ConicalGearCompoundCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6724.CylindricalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6724,
            )

            return self._parent._cast(
                _6724.CylindricalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6727.CylindricalPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6727,
            )

            return self._parent._cast(
                _6727.CylindricalPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def face_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6730.FaceGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6730,
            )

            return self._parent._cast(_6730.FaceGearCompoundCriticalSpeedAnalysis)

        @property
        def hypoid_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6739.HypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6739,
            )

            return self._parent._cast(_6739.HypoidGearCompoundCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6743.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6743,
            )

            return self._parent._cast(
                _6743.KlingelnbergCycloPalloidConicalGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6746.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6746,
            )

            return self._parent._cast(
                _6746.KlingelnbergCycloPalloidHypoidGearCompoundCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> (
            "_6749.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6749,
            )

            return self._parent._cast(
                _6749.KlingelnbergCycloPalloidSpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6776.SpiralBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6776,
            )

            return self._parent._cast(
                _6776.SpiralBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6782.StraightBevelDiffGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6782,
            )

            return self._parent._cast(
                _6782.StraightBevelDiffGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6785.StraightBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6785,
            )

            return self._parent._cast(
                _6785.StraightBevelGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6788.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6788,
            )

            return self._parent._cast(
                _6788.StraightBevelPlanetGearCompoundCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6789.StraightBevelSunGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6789,
            )

            return self._parent._cast(
                _6789.StraightBevelSunGearCompoundCriticalSpeedAnalysis
            )

        @property
        def worm_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6800.WormGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6800,
            )

            return self._parent._cast(_6800.WormGearCompoundCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "_6803.ZerolBevelGearCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6803,
            )

            return self._parent._cast(_6803.ZerolBevelGearCompoundCriticalSpeedAnalysis)

        @property
        def gear_compound_critical_speed_analysis(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
        ) -> "GearCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "GearCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_6606.GearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearCriticalSpeedAnalysis]

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
    ) -> "List[_6606.GearCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.GearCriticalSpeedAnalysis]

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
    ) -> "GearCompoundCriticalSpeedAnalysis._Cast_GearCompoundCriticalSpeedAnalysis":
        return self._Cast_GearCompoundCriticalSpeedAnalysis(self)
