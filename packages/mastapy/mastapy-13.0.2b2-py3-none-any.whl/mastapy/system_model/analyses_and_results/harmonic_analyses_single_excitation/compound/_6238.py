"""ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
    _6144,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation.Compound",
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6109,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
        _6165,
        _6185,
        _6224,
        _6176,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = (
    "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


Self = TypeVar(
    "Self",
    bound="ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
)


class ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation(
    _6144.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
):
    """ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_COMPOUND_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
            parent: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6144.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6144.AbstractShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6176.ConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6176,
            )

            return self._parent._cast(
                _6176.ConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def coaxial_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6165.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6165,
            )

            return self._parent._cast(
                _6165.CoaxialConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cycloidal_disc_central_bearing_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6185.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6185,
            )

            return self._parent._cast(
                _6185.CycloidalDiscCentralBearingConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planetary_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "_6224.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.compound import (
                _6224,
            )

            return self._parent._cast(
                _6224.PlanetaryConnectionCompoundHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_to_mountable_component_connection_compound_harmonic_analysis_of_single_excitation(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
        ) -> "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_6109.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_6109.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ShaftToMountableComponentConnectionHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: Self,
    ) -> "ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ShaftToMountableComponentConnectionCompoundHarmonicAnalysisOfSingleExcitation(
            self
        )
