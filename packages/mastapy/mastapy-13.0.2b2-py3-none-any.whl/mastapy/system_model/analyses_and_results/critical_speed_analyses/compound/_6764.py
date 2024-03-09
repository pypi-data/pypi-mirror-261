"""PowerLoadCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6799,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_POWER_LOAD_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "PowerLoadCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2474
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6635
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6754,
        _6702,
        _6756,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PowerLoadCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="PowerLoadCompoundCriticalSpeedAnalysis")


class PowerLoadCompoundCriticalSpeedAnalysis(
    _6799.VirtualComponentCompoundCriticalSpeedAnalysis
):
    """PowerLoadCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _POWER_LOAD_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PowerLoadCompoundCriticalSpeedAnalysis"
    )

    class _Cast_PowerLoadCompoundCriticalSpeedAnalysis:
        """Special nested class for casting PowerLoadCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis",
            parent: "PowerLoadCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis",
        ) -> "_6799.VirtualComponentCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6799.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis",
        ) -> "_6754.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(
                _6754.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis",
        ) -> "_6702.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(_6702.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis",
        ) -> "_6756.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(_6756.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def power_load_compound_critical_speed_analysis(
            self: "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis",
        ) -> "PowerLoadCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "PowerLoadCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2474.PowerLoad":
        """mastapy.system_model.part_model.PowerLoad

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
    ) -> "List[_6635.PowerLoadCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.PowerLoadCriticalSpeedAnalysis]

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
    ) -> "List[_6635.PowerLoadCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.PowerLoadCriticalSpeedAnalysis]

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
    ) -> "PowerLoadCompoundCriticalSpeedAnalysis._Cast_PowerLoadCompoundCriticalSpeedAnalysis":
        return self._Cast_PowerLoadCompoundCriticalSpeedAnalysis(self)
