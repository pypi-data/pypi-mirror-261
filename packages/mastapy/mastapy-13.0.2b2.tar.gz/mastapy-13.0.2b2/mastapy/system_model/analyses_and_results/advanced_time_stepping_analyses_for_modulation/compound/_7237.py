"""RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7150,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ROOT_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7108,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7143,
        _7222,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7150.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ROOT_ASSEMBLY_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7150.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7150.AssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7143.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7143,
            )

            return self._parent._cast(
                _7143.AbstractAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def root_assembly_compound_advanced_time_stepping_analysis_for_modulation(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7108.RootAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.RootAssemblyAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7108.RootAssemblyAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.RootAssemblyAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_RootAssemblyCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
