"""AGMAGleasonConicalGearHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses import _5714
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "AGMAGleasonConicalGearHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2515
    from mastapy.system_model.analyses_and_results.system_deflections import _2693
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5692,
        _5695,
        _5696,
        _5697,
        _5773,
        _5814,
        _5821,
        _5824,
        _5827,
        _5828,
        _5843,
        _5755,
        _5788,
        _5707,
        _5790,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearHarmonicAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearHarmonicAnalysis")


class AGMAGleasonConicalGearHarmonicAnalysis(_5714.ConicalGearHarmonicAnalysis):
    """AGMAGleasonConicalGearHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearHarmonicAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearHarmonicAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearHarmonicAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
            parent: "AGMAGleasonConicalGearHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5714.ConicalGearHarmonicAnalysis":
            return self._parent._cast(_5714.ConicalGearHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5755.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(_5755.GearHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5788.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.MountableComponentHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5707.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ComponentHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5790.PartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5790,
            )

            return self._parent._cast(_5790.PartHarmonicAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5692.BevelDifferentialGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5692,
            )

            return self._parent._cast(_5692.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5695.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5696.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5696,
            )

            return self._parent._cast(_5696.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5697.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.BevelGearHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5773.HypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(_5773.HypoidGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5814.SpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.SpiralBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5821.StraightBevelDiffGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5824.StraightBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5827.StraightBevelPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5827,
            )

            return self._parent._cast(_5827.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5828.StraightBevelSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.StraightBevelSunGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "_5843.ZerolBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.ZerolBevelGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
        ) -> "AGMAGleasonConicalGearHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "AGMAGleasonConicalGearHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2515.AGMAGleasonConicalGear":
        """mastapy.system_model.part_model.gears.AGMAGleasonConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2693.AGMAGleasonConicalGearSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AGMAGleasonConicalGearSystemDeflection

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
    ) -> "AGMAGleasonConicalGearHarmonicAnalysis._Cast_AGMAGleasonConicalGearHarmonicAnalysis":
        return self._Cast_AGMAGleasonConicalGearHarmonicAnalysis(self)
