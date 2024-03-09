"""BearingCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6177,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEARING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "BearingCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2441
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6018,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6218,
        _6166,
        _6220,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BearingCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="BearingCompoundHarmonicAnalysisOfSingleExcitation")


class BearingCompoundHarmonicAnalysisOfSingleExcitation(
    _6177.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
):
    """BearingCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEARING_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BearingCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "BearingCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connector_compound_harmonic_analysis_of_single_excitation(
            self: "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6177.ConnectorCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6177.ConnectorCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_compound_harmonic_analysis_of_single_excitation(
            self: "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6218.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6218,
            )

            return self._parent._cast(
                _6218.MountableComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_compound_harmonic_analysis_of_single_excitation(
            self: "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6166.ComponentCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6166,
            )

            return self._parent._cast(
                _6166.ComponentCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_harmonic_analysis_of_single_excitation(
            self: "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6220.PartCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6220,
            )

            return self._parent._cast(
                _6220.PartCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_compound_analysis(
            self: "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bearing_compound_harmonic_analysis_of_single_excitation(
            self: "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "BearingCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BearingCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2441.Bearing":
        """mastapy.system_model.part_model.Bearing

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
    ) -> "List[_6018.BearingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BearingHarmonicAnalysisOfSingleExcitation]

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
    def planetaries(
        self: Self,
    ) -> "List[BearingCompoundHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound.BearingCompoundHarmonicAnalysisOfSingleExcitation]

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
    ) -> "List[_6018.BearingHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.BearingHarmonicAnalysisOfSingleExcitation]

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
    ) -> "BearingCompoundHarmonicAnalysisOfSingleExcitation._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BearingCompoundHarmonicAnalysisOfSingleExcitation(self)
