"""ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6179,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CLUTCH_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.couplings import _2344
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6031,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6206,
        _6176,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation"
)


class ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6179.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CLUTCH_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def coupling_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6179.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6179.CouplingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6206.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6206,
            )

            return self._parent._cast(
                _6206.InterMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6176.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2344.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2344.ClutchConnection":
        """mastapy.system_model.connections_and_sockets.couplings.ClutchConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6031.ClutchConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ClutchConnectionHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6031.ClutchConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ClutchConnectionHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ClutchConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
