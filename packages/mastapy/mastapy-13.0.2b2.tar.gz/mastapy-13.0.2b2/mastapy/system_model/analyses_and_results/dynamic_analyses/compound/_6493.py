"""PlanetaryConnectionCompoundDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import _6507
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses.Compound",
    "PlanetaryConnectionCompoundDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2289
    from mastapy.system_model.analyses_and_results.dynamic_analyses import _6364
    from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
        _6413,
        _6445,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryConnectionCompoundDynamicAnalysis",)


Self = TypeVar("Self", bound="PlanetaryConnectionCompoundDynamicAnalysis")


class PlanetaryConnectionCompoundDynamicAnalysis(
    _6507.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
):
    """PlanetaryConnectionCompoundDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _PLANETARY_CONNECTION_COMPOUND_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PlanetaryConnectionCompoundDynamicAnalysis"
    )

    class _Cast_PlanetaryConnectionCompoundDynamicAnalysis:
        """Special nested class for casting PlanetaryConnectionCompoundDynamicAnalysis to subclasses."""

        def __init__(
            self: "PlanetaryConnectionCompoundDynamicAnalysis._Cast_PlanetaryConnectionCompoundDynamicAnalysis",
            parent: "PlanetaryConnectionCompoundDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "PlanetaryConnectionCompoundDynamicAnalysis._Cast_PlanetaryConnectionCompoundDynamicAnalysis",
        ) -> "_6507.ShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            return self._parent._cast(
                _6507.ShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_dynamic_analysis(
            self: "PlanetaryConnectionCompoundDynamicAnalysis._Cast_PlanetaryConnectionCompoundDynamicAnalysis",
        ) -> "_6413.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6413,
            )

            return self._parent._cast(
                _6413.AbstractShaftToMountableComponentConnectionCompoundDynamicAnalysis
            )

        @property
        def connection_compound_dynamic_analysis(
            self: "PlanetaryConnectionCompoundDynamicAnalysis._Cast_PlanetaryConnectionCompoundDynamicAnalysis",
        ) -> "_6445.ConnectionCompoundDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses.compound import (
                _6445,
            )

            return self._parent._cast(_6445.ConnectionCompoundDynamicAnalysis)

        @property
        def connection_compound_analysis(
            self: "PlanetaryConnectionCompoundDynamicAnalysis._Cast_PlanetaryConnectionCompoundDynamicAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PlanetaryConnectionCompoundDynamicAnalysis._Cast_PlanetaryConnectionCompoundDynamicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryConnectionCompoundDynamicAnalysis._Cast_PlanetaryConnectionCompoundDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def planetary_connection_compound_dynamic_analysis(
            self: "PlanetaryConnectionCompoundDynamicAnalysis._Cast_PlanetaryConnectionCompoundDynamicAnalysis",
        ) -> "PlanetaryConnectionCompoundDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "PlanetaryConnectionCompoundDynamicAnalysis._Cast_PlanetaryConnectionCompoundDynamicAnalysis",
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
        self: Self, instance_to_wrap: "PlanetaryConnectionCompoundDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2289.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2289.PlanetaryConnection":
        """mastapy.system_model.connections_and_sockets.PlanetaryConnection

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
    ) -> "List[_6364.PlanetaryConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryConnectionDynamicAnalysis]

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
    ) -> "List[_6364.PlanetaryConnectionDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.PlanetaryConnectionDynamicAnalysis]

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
    ) -> "PlanetaryConnectionCompoundDynamicAnalysis._Cast_PlanetaryConnectionCompoundDynamicAnalysis":
        return self._Cast_PlanetaryConnectionCompoundDynamicAnalysis(self)
