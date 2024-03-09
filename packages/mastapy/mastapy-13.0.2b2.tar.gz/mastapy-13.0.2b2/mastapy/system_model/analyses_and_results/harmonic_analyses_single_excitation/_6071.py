"""GuideDxfModelHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6035,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GUIDE_DXF_MODEL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "GuideDxfModelHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2457
    from mastapy.system_model.analyses_and_results.static_loads import _6899
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("GuideDxfModelHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="GuideDxfModelHarmonicAnalysisOfSingleExcitation")


class GuideDxfModelHarmonicAnalysisOfSingleExcitation(
    _6035.ComponentHarmonicAnalysisOfSingleExcitation
):
    """GuideDxfModelHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _GUIDE_DXF_MODEL_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting GuideDxfModelHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
            parent: "GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_6035.ComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6035.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
        ) -> "GuideDxfModelHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "GuideDxfModelHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2457.GuideDxfModel":
        """mastapy.system_model.part_model.GuideDxfModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6899.GuideDxfModelLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.GuideDxfModelLoadCase

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
    ) -> "GuideDxfModelHarmonicAnalysisOfSingleExcitation._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation":
        return self._Cast_GuideDxfModelHarmonicAnalysisOfSingleExcitation(self)
