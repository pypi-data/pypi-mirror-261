"""BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6021,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2519
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6026,
        _6014,
        _6042,
        _6068,
        _6089,
        _6035,
        _6091,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self", bound="BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation"
)


class BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation(
    _6021.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
):
    """BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
            parent: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6021.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6021.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6026.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6026,
            )

            return self._parent._cast(_6026.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6014.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6014,
            )

            return self._parent._cast(
                _6014.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6042.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6068.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(_6068.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(
                _6089.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6035.ComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6035,
            )

            return self._parent._cast(_6035.ComponentHarmonicAnalysisOfSingleExcitation)

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6091,
            )

            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
        ) -> "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2519.BevelDifferentialPlanetGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialPlanetGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
        return self._Cast_BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation(
            self
        )
