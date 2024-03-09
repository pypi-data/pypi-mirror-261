"""BevelDifferentialPlanetGearCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3910
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BevelDifferentialPlanetGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3779
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3915,
        _3903,
        _3931,
        _3957,
        _3976,
        _3924,
        _3978,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialPlanetGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialPlanetGearCompoundStabilityAnalysis")


class BevelDifferentialPlanetGearCompoundStabilityAnalysis(
    _3910.BevelDifferentialGearCompoundStabilityAnalysis
):
    """BevelDifferentialPlanetGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_PLANET_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis"
    )

    class _Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis:
        """Special nested class for casting BevelDifferentialPlanetGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
            parent: "BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_3910.BevelDifferentialGearCompoundStabilityAnalysis":
            return self._parent._cast(
                _3910.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_3915.BevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_3903.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3903,
            )

            return self._parent._cast(
                _3903.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_3931.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(_3931.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_3957.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_3976.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_3924.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(_3924.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_3978.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_stability_analysis(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
        ) -> "BevelDifferentialPlanetGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "BevelDifferentialPlanetGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3779.BevelDifferentialPlanetGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialPlanetGearStabilityAnalysis]

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
    ) -> "List[_3779.BevelDifferentialPlanetGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialPlanetGearStabilityAnalysis]

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
    ) -> "BevelDifferentialPlanetGearCompoundStabilityAnalysis._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis":
        return self._Cast_BevelDifferentialPlanetGearCompoundStabilityAnalysis(self)
