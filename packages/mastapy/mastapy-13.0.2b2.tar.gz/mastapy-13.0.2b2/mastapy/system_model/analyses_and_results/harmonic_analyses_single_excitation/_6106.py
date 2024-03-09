"""RootAssemblyHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6017,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "RootAssemblyHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2476
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6072,
        _6010,
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="RootAssemblyHarmonicAnalysisOfSingleExcitation")


class RootAssemblyHarmonicAnalysisOfSingleExcitation(
    _6017.AssemblyHarmonicAnalysisOfSingleExcitation
):
    """RootAssemblyHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting RootAssemblyHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
            parent: "RootAssemblyHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def assembly_harmonic_analysis_of_single_excitation(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6017.AssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6017.AssemblyHarmonicAnalysisOfSingleExcitation)

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6010.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6010,
            )

            return self._parent._cast(
                _6010.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def root_assembly_harmonic_analysis_of_single_excitation(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
        ) -> "RootAssemblyHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "RootAssemblyHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2476.RootAssembly":
        """mastapy.system_model.part_model.RootAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_of_single_excitation_inputs(
        self: Self,
    ) -> "_6072.HarmonicAnalysisOfSingleExcitation":
        """mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOfSingleExcitationInputs

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyHarmonicAnalysisOfSingleExcitation._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation":
        return self._Cast_RootAssemblyHarmonicAnalysisOfSingleExcitation(self)
