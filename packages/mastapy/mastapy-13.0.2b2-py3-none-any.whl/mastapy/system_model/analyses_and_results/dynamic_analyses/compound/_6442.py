"""ConicalGearCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6468
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "ConicalGearCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6414,
        _6421,
        _6424,
        _6425,
        _6426,
        _6472,
        _6476,
        _6479,
        _6482,
        _6509,
        _6515,
        _6518,
        _6521,
        _6522,
        _6536,
        _6487,
        _6435,
        _6489,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="ConicalGearCompoundDynamicAnalysis")


class ConicalGearCompoundDynamicAnalysis(_6468.GearCompoundDynamicAnalysis):
    """ConicalGearCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearCompoundDynamicAnalysis")

    class _Cast_ConicalGearCompoundDynamicAnalysis:
        """Special nested class for casting ConicalGearCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
            parent: "ConicalGearCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6468.GearCompoundDynamicAnalysis":
            return self._parent._cast(_6468.GearCompoundDynamicAnalysis)

        @property
        def mountable_component_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6487.MountableComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6487,
            )

            return self._parent._cast(_6487.MountableComponentCompoundDynamicAnalysis)

        @property
        def component_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6435.ComponentCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6435,
            )

            return self._parent._cast(_6435.ComponentCompoundDynamicAnalysis)

        @property
        def part_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6489.PartCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6489,
            )

            return self._parent._cast(_6489.PartCompoundDynamicAnalysis)

        @property
        def part_compound_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6414.AGMAGleasonConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6414,
            )

            return self._parent._cast(
                _6414.AGMAGleasonConicalGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6421.BevelDifferentialGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6421,
            )

            return self._parent._cast(
                _6421.BevelDifferentialGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6424.BevelDifferentialPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6424,
            )

            return self._parent._cast(
                _6424.BevelDifferentialPlanetGearCompoundDynamicAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6425.BevelDifferentialSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6425,
            )

            return self._parent._cast(
                _6425.BevelDifferentialSunGearCompoundDynamicAnalysis
            )

        @property
        def bevel_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6426.BevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6426,
            )

            return self._parent._cast(_6426.BevelGearCompoundDynamicAnalysis)

        @property
        def hypoid_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6472.HypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6472,
            )

            return self._parent._cast(_6472.HypoidGearCompoundDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6476.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6476,
            )

            return self._parent._cast(
                _6476.KlingelnbergCycloPalloidConicalGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6479.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6479,
            )

            return self._parent._cast(
                _6479.KlingelnbergCycloPalloidHypoidGearCompoundDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6482.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6482,
            )

            return self._parent._cast(
                _6482.KlingelnbergCycloPalloidSpiralBevelGearCompoundDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6509.SpiralBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6509,
            )

            return self._parent._cast(_6509.SpiralBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6515.StraightBevelDiffGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6515,
            )

            return self._parent._cast(
                _6515.StraightBevelDiffGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6518.StraightBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6518,
            )

            return self._parent._cast(_6518.StraightBevelGearCompoundDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6521.StraightBevelPlanetGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6521,
            )

            return self._parent._cast(
                _6521.StraightBevelPlanetGearCompoundDynamicAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6522.StraightBevelSunGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6522,
            )

            return self._parent._cast(_6522.StraightBevelSunGearCompoundDynamicAnalysis)

        @property
        def zerol_bevel_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "_6536.ZerolBevelGearCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6536,
            )

            return self._parent._cast(_6536.ZerolBevelGearCompoundDynamicAnalysis)

        @property
        def conical_gear_compound_dynamic_analysis(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
        ) -> "ConicalGearCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "ConicalGearCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def planetaries(self: Self) -> "List[ConicalGearCompoundDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.compound.ConicalGearCompoundDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6311.ConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearDynamicAnalysis]

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
    ) -> "List[_6311.ConicalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.ConicalGearDynamicAnalysis]

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
    ) -> "ConicalGearCompoundDynamicAnalysis._Cast_ConicalGearCompoundDynamicAnalysis":
        return self._Cast_ConicalGearCompoundDynamicAnalysis(self)
