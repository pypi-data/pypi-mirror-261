"""KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5947
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_HARMONIC_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
        "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5783
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5913,
        _5939,
        _5958,
        _5906,
        _5960,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis"
)


class KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis(
    _5947.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
):
    """KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5947.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis":
            return self._parent._cast(
                _5947.KlingelnbergCycloPalloidConicalGearCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5913.ConicalGearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5913,
            )

            return self._parent._cast(_5913.ConicalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5939.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5958.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5906.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(_5906.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_5960.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_harmonic_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5783.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]

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
    ) -> "List[_5783.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis]

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis":
        return (
            self._Cast_KlingelnbergCycloPalloidSpiralBevelGearCompoundHarmonicAnalysis(
                self
            )
        )
