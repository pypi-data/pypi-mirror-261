"""AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5915
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5687
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5894,
        _5899,
        _5945,
        _5982,
        _5988,
        _5991,
        _6009,
        _5941,
        _5979,
        _5881,
        _5960,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearSetCompoundHarmonicAnalysis")


class AGMAGleasonConicalGearSetCompoundHarmonicAnalysis(
    _5915.ConicalGearSetCompoundHarmonicAnalysis
):
    """AGMAGleasonConicalGearSetCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
            parent: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5915.ConicalGearSetCompoundHarmonicAnalysis":
            return self._parent._cast(_5915.ConicalGearSetCompoundHarmonicAnalysis)

        @property
        def gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5941.GearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5941,
            )

            return self._parent._cast(_5941.GearSetCompoundHarmonicAnalysis)

        @property
        def specialised_assembly_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5979.SpecialisedAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5979,
            )

            return self._parent._cast(_5979.SpecialisedAssemblyCompoundHarmonicAnalysis)

        @property
        def abstract_assembly_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5881.AbstractAssemblyCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5881,
            )

            return self._parent._cast(_5881.AbstractAssemblyCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5960.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5894.BevelDifferentialGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5894,
            )

            return self._parent._cast(
                _5894.BevelDifferentialGearSetCompoundHarmonicAnalysis
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5899.BevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5899,
            )

            return self._parent._cast(_5899.BevelGearSetCompoundHarmonicAnalysis)

        @property
        def hypoid_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5945.HypoidGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5945,
            )

            return self._parent._cast(_5945.HypoidGearSetCompoundHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5982.SpiralBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5982,
            )

            return self._parent._cast(_5982.SpiralBevelGearSetCompoundHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5988.StraightBevelDiffGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5988,
            )

            return self._parent._cast(
                _5988.StraightBevelDiffGearSetCompoundHarmonicAnalysis
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_5991.StraightBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5991,
            )

            return self._parent._cast(
                _5991.StraightBevelGearSetCompoundHarmonicAnalysis
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "_6009.ZerolBevelGearSetCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _6009,
            )

            return self._parent._cast(_6009.ZerolBevelGearSetCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
        ) -> "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_5687.AGMAGleasonConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearSetHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_5687.AGMAGleasonConicalGearSetHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.AGMAGleasonConicalGearSetHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCompoundHarmonicAnalysis._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis":
        return self._Cast_AGMAGleasonConicalGearSetCompoundHarmonicAnalysis(self)
