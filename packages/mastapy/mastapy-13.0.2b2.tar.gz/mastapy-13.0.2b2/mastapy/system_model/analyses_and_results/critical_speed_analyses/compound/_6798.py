"""UnbalancedMassCompoundCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
    _6799,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_UNBALANCED_MASS_COMPOUND_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses.Compound",
    "UnbalancedMassCompoundCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2479
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6669
    from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
        _6754,
        _6702,
        _6756,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("UnbalancedMassCompoundCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="UnbalancedMassCompoundCriticalSpeedAnalysis")


class UnbalancedMassCompoundCriticalSpeedAnalysis(
    _6799.VirtualComponentCompoundCriticalSpeedAnalysis
):
    """UnbalancedMassCompoundCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _UNBALANCED_MASS_COMPOUND_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_UnbalancedMassCompoundCriticalSpeedAnalysis"
    )

    class _Cast_UnbalancedMassCompoundCriticalSpeedAnalysis:
        """Special nested class for casting UnbalancedMassCompoundCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
            parent: "UnbalancedMassCompoundCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_6799.VirtualComponentCompoundCriticalSpeedAnalysis":
            return self._parent._cast(
                _6799.VirtualComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def mountable_component_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_6754.MountableComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6754,
            )

            return self._parent._cast(
                _6754.MountableComponentCompoundCriticalSpeedAnalysis
            )

        @property
        def component_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_6702.ComponentCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6702,
            )

            return self._parent._cast(_6702.ComponentCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_6756.PartCompoundCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses.compound import (
                _6756,
            )

            return self._parent._cast(_6756.PartCompoundCriticalSpeedAnalysis)

        @property
        def part_compound_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def unbalanced_mass_compound_critical_speed_analysis(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
        ) -> "UnbalancedMassCompoundCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "UnbalancedMassCompoundCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2479.UnbalancedMass":
        """mastapy.system_model.part_model.UnbalancedMass

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
    ) -> "List[_6669.UnbalancedMassCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.UnbalancedMassCriticalSpeedAnalysis]

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
    ) -> "List[_6669.UnbalancedMassCriticalSpeedAnalysis]":
        """List[mastapy.system_model.analyses_and_results.critical_speed_analyses.UnbalancedMassCriticalSpeedAnalysis]

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
    ) -> "UnbalancedMassCompoundCriticalSpeedAnalysis._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis":
        return self._Cast_UnbalancedMassCompoundCriticalSpeedAnalysis(self)
