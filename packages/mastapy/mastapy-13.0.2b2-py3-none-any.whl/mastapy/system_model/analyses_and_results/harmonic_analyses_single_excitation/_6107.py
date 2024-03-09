"""ShaftHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6011,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ShaftHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2484
    from mastapy.system_model.analyses_and_results.static_loads import _6953
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6012,
        _6035,
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ShaftHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ShaftHarmonicAnalysisOfSingleExcitation")


class ShaftHarmonicAnalysisOfSingleExcitation(
    _6011.AbstractShaftHarmonicAnalysisOfSingleExcitation
):
    """ShaftHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _SHAFT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ShaftHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ShaftHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
            parent: "ShaftHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6011.AbstractShaftHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6011.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6012.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(
                _6012.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6035.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(_6035.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
        ) -> "ShaftHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "ShaftHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2484.Shaft":
        """mastapy.system_model.part_model.shaft_model.Shaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6953.ShaftLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ShaftLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ShaftHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.ShaftHarmonicAnalysisOfSingleExcitation]

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
    def cast_to(
        self: Self,
    ) -> "ShaftHarmonicAnalysisOfSingleExcitation._Cast_ShaftHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ShaftHarmonicAnalysisOfSingleExcitation(self)
