"""BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7208,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BELT_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2270
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7022,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7183,
        _7178,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7208.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _BELT_CONNECTION_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7208.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7208.InterMountableComponentConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7178.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7178,
            )

            return self._parent._cast(
                _7178.ConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_compound_analysis(
            self: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7183.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7183,
            )

            return self._parent._cast(
                _7183.CVTBeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def belt_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2270.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2270.BeltConnection":
        """mastapy.system_model.connections_and_sockets.BeltConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_7022.BeltConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BeltConnectionAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_7022.BeltConnectionAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.BeltConnectionAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_BeltConnectionCompoundAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
