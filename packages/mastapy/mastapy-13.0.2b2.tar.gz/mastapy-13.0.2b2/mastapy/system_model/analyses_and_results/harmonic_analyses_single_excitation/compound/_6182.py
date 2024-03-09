"""CVTCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6151,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "CVTCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6051,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6239,
        _6141,
        _6220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CVTCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CVTCompoundHarmonicAnalysisOfSingleExcitation")


class CVTCompoundHarmonicAnalysisOfSingleExcitation(
    _6151.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
):
    """CVTCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CVT_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CVTCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "CVTCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def belt_drive_compound_harmonic_analysis_of_single_excitation(
            self: "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6151.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6151.BeltDriveCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def specialised_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6239.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6239,
            )

            return self._parent._cast(
                _6239.SpecialisedAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_compound_harmonic_analysis_of_single_excitation(
            self: "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6141.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6141,
            )

            return self._parent._cast(
                _6141.AbstractAssemblyCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6220.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_compound_harmonic_analysis_of_single_excitation(
            self: "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "CVTCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CVTCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_6051.CVTHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CVTHarmonicAnalysisOfSingleExcitation]

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
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_6051.CVTHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CVTHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: Self,
    ) -> "CVTCompoundHarmonicAnalysisOfSingleExcitation._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CVTCompoundHarmonicAnalysisOfSingleExcitation(self)
