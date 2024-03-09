"""SynchroniserPartCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3938
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_PART_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "SynchroniserPartCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.stability_analyses import _3884
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _4013,
        _4015,
        _3976,
        _3924,
        _3978,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserPartCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="SynchroniserPartCompoundStabilityAnalysis")


class SynchroniserPartCompoundStabilityAnalysis(
    _3938.CouplingHalfCompoundStabilityAnalysis
):
    """SynchroniserPartCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_PART_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SynchroniserPartCompoundStabilityAnalysis"
    )

    class _Cast_SynchroniserPartCompoundStabilityAnalysis:
        """Special nested class for casting SynchroniserPartCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
            parent: "SynchroniserPartCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def coupling_half_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_3938.CouplingHalfCompoundStabilityAnalysis":
            return self._parent._cast(_3938.CouplingHalfCompoundStabilityAnalysis)

        @property
        def mountable_component_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_3976.MountableComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3976,
            )

            return self._parent._cast(_3976.MountableComponentCompoundStabilityAnalysis)

        @property
        def component_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_3924.ComponentCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3924,
            )

            return self._parent._cast(_3924.ComponentCompoundStabilityAnalysis)

        @property
        def part_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_3978.PartCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3978,
            )

            return self._parent._cast(_3978.PartCompoundStabilityAnalysis)

        @property
        def part_compound_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def synchroniser_half_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_4013.SynchroniserHalfCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4013,
            )

            return self._parent._cast(_4013.SynchroniserHalfCompoundStabilityAnalysis)

        @property
        def synchroniser_sleeve_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "_4015.SynchroniserSleeveCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _4015,
            )

            return self._parent._cast(_4015.SynchroniserSleeveCompoundStabilityAnalysis)

        @property
        def synchroniser_part_compound_stability_analysis(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
        ) -> "SynchroniserPartCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "SynchroniserPartCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_3884.SynchroniserPartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SynchroniserPartStabilityAnalysis]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_3884.SynchroniserPartStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.SynchroniserPartStabilityAnalysis]

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
    def cast_to(
        self: Self,
    ) -> "SynchroniserPartCompoundStabilityAnalysis._Cast_SynchroniserPartCompoundStabilityAnalysis":
        return self._Cast_SynchroniserPartCompoundStabilityAnalysis(self)
