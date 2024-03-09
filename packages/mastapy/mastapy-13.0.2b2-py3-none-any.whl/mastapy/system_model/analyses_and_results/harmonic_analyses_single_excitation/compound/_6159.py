"""BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6147,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6028,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6154,
        _6242,
        _6248,
        _6251,
        _6269,
        _6175,
        _6201,
        _6239,
        _6141,
        _6220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation")


class BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation(
    _6147.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
):
    """BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6147.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation"
        ):
            return self._parent._cast(
                _6147.AGMAGleasonConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6175.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6175,
            )

            return self._parent._cast(
                _6175.ConicalGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6201.GearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6201,
            )

            return self._parent._cast(
                _6201.GearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6141.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6141,
            )

            return self._parent._cast(
                _6141.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6220.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6154.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6154,
            )

            return self._parent._cast(
                _6154.BevelDifferentialGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6242.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6242,
            )

            return self._parent._cast(
                _6242.SpiralBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6248.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6248,
            )

            return self._parent._cast(
                _6248.StraightBevelDiffGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6251.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6251,
            )

            return self._parent._cast(
                _6251.StraightBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def zerol_bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6269.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6269,
            )

            return self._parent._cast(
                _6269.ZerolBevelGearSetCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_set_compound_harmonic_analysis_of_single_excitation(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6028.BevelGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BevelGearSetHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6028.BevelGearSetHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BevelGearSetHarmonicAnalysisOfSingleExcitation]

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
    ) -> "BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BevelGearSetCompoundHarmonicAnalysisOfSingleExcitation(self)
