"""FaceGearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6068,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "FaceGearHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2530
    from mastapy.system_model.analyses_and_results.static_loads import _6887
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6089,
        _6035,
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="FaceGearHarmonicAnalysisOfSingleExcitation")


class FaceGearHarmonicAnalysisOfSingleExcitation(
    _6068.GearHarmonicAnalysisOfSingleExcitation
):
    """FaceGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_FaceGearHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_FaceGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting FaceGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
            parent: "FaceGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6068.GearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6068.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(
                _6089.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6035.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(_6035.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
        ) -> "FaceGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "FaceGearHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2530.FaceGear":
        """mastapy.system_model.part_model.gears.FaceGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6887.FaceGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearLoadCase

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
    ) -> "FaceGearHarmonicAnalysisOfSingleExcitation._Cast_FaceGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_FaceGearHarmonicAnalysisOfSingleExcitation(self)
