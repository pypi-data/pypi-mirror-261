"""BevelDifferentialGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5697
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "BevelDifferentialGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517
    from mastapy.system_model.analyses_and_results.static_loads import _6825
    from mastapy.system_model.analyses_and_results.system_deflections import _2705
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5695,
        _5696,
        _5685,
        _5714,
        _5755,
        _5788,
        _5707,
        _5790,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearHarmonicAnalysis")


class BevelDifferentialGearHarmonicAnalysis(_5697.BevelGearHarmonicAnalysis):
    """BevelDifferentialGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearHarmonicAnalysis"
    )

    class _Cast_BevelDifferentialGearHarmonicAnalysis:
        """Special nested class for casting BevelDifferentialGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
            parent: "BevelDifferentialGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_5697.BevelGearHarmonicAnalysis":
            return self._parent._cast(_5697.BevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_5685.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5685,
            )

            return self._parent._cast(_5685.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_5714.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_5755.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(_5755.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_5788.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_5707.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_5790.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_5695.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "_5696.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5696,
            )

            return self._parent._cast(_5696.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
        ) -> "BevelDifferentialGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2517.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6825.BevelDifferentialGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2705.BevelDifferentialGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearHarmonicAnalysis._Cast_BevelDifferentialGearHarmonicAnalysis":
        return self._Cast_BevelDifferentialGearHarmonicAnalysis(self)
