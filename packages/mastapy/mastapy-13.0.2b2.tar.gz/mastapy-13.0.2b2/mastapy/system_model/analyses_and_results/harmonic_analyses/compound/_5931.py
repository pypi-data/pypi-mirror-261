"""CylindricalPlanetGearCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5928
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "CylindricalPlanetGearCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5732
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5939,
        _5958,
        _5906,
        _5960,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalPlanetGearCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="CylindricalPlanetGearCompoundHarmonicAnalysis")


class CylindricalPlanetGearCompoundHarmonicAnalysis(
    _5928.CylindricalGearCompoundHarmonicAnalysis
):
    """CylindricalPlanetGearCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_PLANET_GEAR_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalPlanetGearCompoundHarmonicAnalysis"
    )

    class _Cast_CylindricalPlanetGearCompoundHarmonicAnalysis:
        """Special nested class for casting CylindricalPlanetGearCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
            parent: "CylindricalPlanetGearCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_compound_harmonic_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5928.CylindricalGearCompoundHarmonicAnalysis":
            return self._parent._cast(_5928.CylindricalGearCompoundHarmonicAnalysis)

        @property
        def gear_compound_harmonic_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5939.GearCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5939,
            )

            return self._parent._cast(_5939.GearCompoundHarmonicAnalysis)

        @property
        def mountable_component_compound_harmonic_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5958.MountableComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5958,
            )

            return self._parent._cast(_5958.MountableComponentCompoundHarmonicAnalysis)

        @property
        def component_compound_harmonic_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5906.ComponentCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5906,
            )

            return self._parent._cast(_5906.ComponentCompoundHarmonicAnalysis)

        @property
        def part_compound_harmonic_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
        ) -> "_5960.PartCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5960,
            )

            return self._parent._cast(_5960.PartCompoundHarmonicAnalysis)

        @property
        def part_compound_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_harmonic_analysis(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
        ) -> "CylindricalPlanetGearCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis",
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
        instance_to_wrap: "CylindricalPlanetGearCompoundHarmonicAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_5732.CylindricalPlanetGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalPlanetGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5732.CylindricalPlanetGearHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.CylindricalPlanetGearHarmonicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalPlanetGearCompoundHarmonicAnalysis._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis":
        return self._Cast_CylindricalPlanetGearCompoundHarmonicAnalysis(self)
