"""SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7258,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7130,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7182,
        _7220,
        _7168,
        _7222,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7258.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7258.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7258.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7182.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7182,
            )

            return self._parent._cast(
                _7182.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7220.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7220,
            )

            return self._parent._cast(
                _7220.MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7168,
            )

            return self._parent._cast(
                _7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

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
    ) -> "List[_7130.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "List[_7130.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation]

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
    ) -> "SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
