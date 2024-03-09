"""OilSealHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6046,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_OIL_SEAL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "OilSealHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2468
    from mastapy.system_model.analyses_and_results.static_loads import _6929
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6089,
        _6035,
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("OilSealHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="OilSealHarmonicAnalysisOfSingleExcitation")


class OilSealHarmonicAnalysisOfSingleExcitation(
    _6046.ConnectorHarmonicAnalysisOfSingleExcitation
):
    """OilSealHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _OIL_SEAL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_OilSealHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_OilSealHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting OilSealHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
            parent: "OilSealHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.ConnectorHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6046.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(
                _6089.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "_6035.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(_6035.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
        ) -> "OilSealHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "OilSealHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2468.OilSeal":
        """mastapy.system_model.part_model.OilSeal

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6929.OilSealLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.OilSealLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "OilSealHarmonicAnalysisOfSingleExcitation._Cast_OilSealHarmonicAnalysisOfSingleExcitation":
        return self._Cast_OilSealHarmonicAnalysisOfSingleExcitation(self)
