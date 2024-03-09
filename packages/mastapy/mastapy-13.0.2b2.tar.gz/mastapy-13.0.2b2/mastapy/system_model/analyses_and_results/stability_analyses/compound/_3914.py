"""BevelDifferentialSunGearCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3910
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "BevelDifferentialSunGearCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3780
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
__all__ = ("BevelDifferentialSunGearCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialSunGearCompoundStabilityAnalysis")


class BevelDifferentialSunGearCompoundStabilityAnalysis(
    _3910.BevelDifferentialGearCompoundStabilityAnalysis
):
    """BevelDifferentialSunGearCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_SUN_GEAR_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialSunGearCompoundStabilityAnalysis"
    )

    class _Cast_BevelDifferentialSunGearCompoundStabilityAnalysis:
        """Special nested class for casting BevelDifferentialSunGearCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
            parent: "BevelDifferentialSunGearCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_differential_gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_3910.BevelDifferentialGearCompoundStabilityAnalysis":
            return self._parent._cast(
                _3910.BevelDifferentialGearCompoundStabilityAnalysis
            )

        @property
        def bevel_gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_3915.BevelGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3915,
            )

            return self._parent._cast(_3915.BevelGearCompoundStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_3903.AGMAGleasonConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3903,
            )

            return self._parent._cast(
                _3903.AGMAGleasonConicalGearCompoundStabilityAnalysis
            )

        @property
        def conical_gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_3931.ConicalGearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3931,
            )

            return self._parent._cast(_3931.ConicalGearCompoundStabilityAnalysis)

        @property
        def gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_3957.GearCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3957,
            )

            return self._parent._cast(_3957.GearCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_3976.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_3924.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(_3924.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_3978.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_sun_gear_compound_stability_analysis(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
        ) -> "BevelDifferentialSunGearCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis",
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
        instance_to_wrap: "BevelDifferentialSunGearCompoundStabilityAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3780.BevelDifferentialSunGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialSunGearStabilityAnalysis]

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
    ) -> "List[_3780.BevelDifferentialSunGearStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.BevelDifferentialSunGearStabilityAnalysis]

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
    ) -> "BevelDifferentialSunGearCompoundStabilityAnalysis._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis":
        return self._Cast_BevelDifferentialSunGearCompoundStabilityAnalysis(self)
