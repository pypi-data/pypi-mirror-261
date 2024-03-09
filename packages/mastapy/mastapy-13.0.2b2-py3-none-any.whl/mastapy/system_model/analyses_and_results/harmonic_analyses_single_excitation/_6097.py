"""PlanetCarrierHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6089,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "PlanetCarrierHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import _6938
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6035,
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="PlanetCarrierHarmonicAnalysisOfSingleExcitation")


class PlanetCarrierHarmonicAnalysisOfSingleExcitation(
    _6089.MountableComponentHarmonicAnalysisOfSingleExcitation
):
    """PlanetCarrierHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting PlanetCarrierHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
            parent: "PlanetCarrierHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.MountableComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6089.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
        ) -> "_6035.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(_6035.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
        ) -> "PlanetCarrierHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "PlanetCarrierHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6938.PlanetCarrierLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PlanetCarrierLoadCase

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
    ) -> "PlanetCarrierHarmonicAnalysisOfSingleExcitation._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation":
        return self._Cast_PlanetCarrierHarmonicAnalysisOfSingleExcitation(self)
