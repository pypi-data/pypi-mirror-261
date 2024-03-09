"""AbstractShaftCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6679,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "AbstractShaftCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6546
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6722,
        _6772,
        _6702,
        _6756,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="AbstractShaftCompoundCriticalSpeedAnalysis")


class AbstractShaftCompoundCriticalSpeedAnalysis(
    _6679.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
):
    """AbstractShaftCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftCompoundCriticalSpeedAnalysis"
    )

    class _Cast_AbstractShaftCompoundCriticalSpeedAnalysis:
        """Special nested class for casting AbstractShaftCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
            parent: "AbstractShaftCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_6679.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6679.AbstractShaftOrHousingCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_6702.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(_6702.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_6756.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(_6756.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_6722.CycloidalDiscCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6722,
            )

            return self._parent._cast(_6722.CycloidalDiscCompoundCriticalSpeedAnalysis)

        @property
        def shaft_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "_6772.ShaftCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6772,
            )

            return self._parent._cast(_6772.ShaftCompoundCriticalSpeedAnalysis)

        @property
        def abstract_shaft_compound_critical_speed_analysis(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
        ) -> "AbstractShaftCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "AbstractShaftCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_6546.AbstractShaftCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractShaftCriticalSpeedAnalysis]

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
    ) -> "List[_6546.AbstractShaftCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.AbstractShaftCriticalSpeedAnalysis]

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
    ) -> "AbstractShaftCompoundCriticalSpeedAnalysis._Cast_AbstractShaftCompoundCriticalSpeedAnalysis":
        return self._Cast_AbstractShaftCompoundCriticalSpeedAnalysis(self)
