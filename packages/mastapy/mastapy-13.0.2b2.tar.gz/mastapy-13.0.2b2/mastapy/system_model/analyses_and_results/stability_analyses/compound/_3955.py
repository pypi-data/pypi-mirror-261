"""FEPartCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3901
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FE_PART_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "FEPartCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2455
    from mastapy.system_model.analyses_and_results.stability_analyses import _3823
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3924,
        _3978,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("FEPartCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="FEPartCompoundStabilityAnalysis")


class FEPartCompoundStabilityAnalysis(
    _3901.AbstractShaftOrHousingCompoundStabilityAnalysis
):
    """FEPartCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _FE_PART_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FEPartCompoundStabilityAnalysis")

    class _Cast_FEPartCompoundStabilityAnalysis:
        """Special nested class for casting FEPartCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "FEPartCompoundStabilityAnalysis._Cast_FEPartCompoundStabilityAnalysis",
            parent: "FEPartCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_stability_analysis(
            self: "FEPartCompoundStabilityAnalysis._Cast_FEPartCompoundStabilityAnalysis",
        ) -> "_3901.AbstractShaftOrHousingCompoundStabilityAnalysis":
            return self._parent._cast(
                _3901.AbstractShaftOrHousingCompoundStabilityAnalysis
            )

        @property
        def component_compound_stability_analysis(
            self: "FEPartCompoundStabilityAnalysis._Cast_FEPartCompoundStabilityAnalysis",
        ) -> "_3924.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(_3924.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "FEPartCompoundStabilityAnalysis._Cast_FEPartCompoundStabilityAnalysis",
        ) -> "_3978.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "FEPartCompoundStabilityAnalysis._Cast_FEPartCompoundStabilityAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "FEPartCompoundStabilityAnalysis._Cast_FEPartCompoundStabilityAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "FEPartCompoundStabilityAnalysis._Cast_FEPartCompoundStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def fe_part_compound_stability_analysis(
            self: "FEPartCompoundStabilityAnalysis._Cast_FEPartCompoundStabilityAnalysis",
        ) -> "FEPartCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "FEPartCompoundStabilityAnalysis._Cast_FEPartCompoundStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FEPartCompoundStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2455.FEPart":
        """mastapy.system_model.part_model.FEPart

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3823.FEPartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FEPartStabilityAnalysis]

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
    def planetaries(self: Self) -> "List[FEPartCompoundStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.compound.FEPartCompoundStabilityAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases(self: Self) -> "List[_3823.FEPartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.FEPartStabilityAnalysis]

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
    ) -> "FEPartCompoundStabilityAnalysis._Cast_FEPartCompoundStabilityAnalysis":
        return self._Cast_FEPartCompoundStabilityAnalysis(self)
