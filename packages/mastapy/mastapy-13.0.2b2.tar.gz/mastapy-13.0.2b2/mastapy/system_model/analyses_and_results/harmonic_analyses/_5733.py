"""DatumHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5707
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_DATUM_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "DatumHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2450
    from mastapy.system_model.analyses_and_results.static_loads import _6872
    from mastapy.system_model.analyses_and_results.system_deflections import _2753
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5790
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("DatumHarmonicAnalysis",)


Self = TypeVar("Self", bound="DatumHarmonicAnalysis")


class DatumHarmonicAnalysis(_5707.ComponentHarmonicAnalysis):
    """DatumHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _DATUM_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_DatumHarmonicAnalysis")

    class _Cast_DatumHarmonicAnalysis:
        """Special nested class for casting DatumHarmonicAnalysis to subclasses."""

        def __init__(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
            parent: "DatumHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def component_harmonic_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_5707.ComponentHarmonicAnalysis":
            return self._parent._cast(_5707.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_5790.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def datum_harmonic_analysis(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis",
        ) -> "DatumHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "DatumHarmonicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2450.Datum":
        """mastapy.system_model.part_model.Datum

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6872.DatumLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.DatumLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2753.DatumSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.DatumSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "DatumHarmonicAnalysis._Cast_DatumHarmonicAnalysis":
        return self._Cast_DatumHarmonicAnalysis(self)
