"""CVTHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6020,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CVTHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2588
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6110,
        _6010,
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CVTHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CVTHarmonicAnalysisOfSingleExcitation")


class CVTHarmonicAnalysisOfSingleExcitation(
    _6020.BeltDriveHarmonicAnalysisOfSingleExcitation
):
    """CVTHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CVT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CVTHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CVTHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CVTHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
            parent: "CVTHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def belt_drive_harmonic_analysis_of_single_excitation(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "_6020.BeltDriveHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6020.BeltDriveHarmonicAnalysisOfSingleExcitation)

        @property
        def specialised_assembly_harmonic_analysis_of_single_excitation(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "_6110.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6110,
            )

            return self._parent._cast(
                _6110.SpecialisedAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_assembly_harmonic_analysis_of_single_excitation(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "_6010.AbstractAssemblyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6010,
            )

            return self._parent._cast(
                _6010.AbstractAssemblyHarmonicAnalysisOfSingleExcitation
            )

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_harmonic_analysis_of_single_excitation(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
        ) -> "CVTHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "CVTHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2588.CVT":
        """mastapy.system_model.part_model.couplings.CVT

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CVTHarmonicAnalysisOfSingleExcitation._Cast_CVTHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CVTHarmonicAnalysisOfSingleExcitation(self)
