"""CoaxialConnectionCompoundStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.stability_analyses.compound import _3996
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COAXIAL_CONNECTION_COMPOUND_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses.Compound",
    "CoaxialConnectionCompoundStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2271
    from mastapy.system_model.analyses_and_results.stability_analyses import _3789
    from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
        _3943,
        _3902,
        _3934,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CoaxialConnectionCompoundStabilityAnalysis",)


Self = TypeVar("Self", bound="CoaxialConnectionCompoundStabilityAnalysis")


class CoaxialConnectionCompoundStabilityAnalysis(
    _3996.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
):
    """CoaxialConnectionCompoundStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COAXIAL_CONNECTION_COMPOUND_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CoaxialConnectionCompoundStabilityAnalysis"
    )

    class _Cast_CoaxialConnectionCompoundStabilityAnalysis:
        """Special nested class for casting CoaxialConnectionCompoundStabilityAnalysis to subclasses."""

        def __init__(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
            parent: "CoaxialConnectionCompoundStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_3996.ShaftToMountableComponentConnectionCompoundStabilityAnalysis":
            return self._parent._cast(
                _3996.ShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_stability_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> (
            "_3902.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3902,
            )

            return self._parent._cast(
                _3902.AbstractShaftToMountableComponentConnectionCompoundStabilityAnalysis
            )

        @property
        def connection_compound_stability_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_3934.ConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3934,
            )

            return self._parent._cast(_3934.ConnectionCompoundStabilityAnalysis)

        @property
        def connection_compound_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_stability_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "_3943.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses.compound import (
                _3943,
            )

            return self._parent._cast(
                _3943.CycloidalDiscCentralBearingConnectionCompoundStabilityAnalysis
            )

        @property
        def coaxial_connection_compound_stability_analysis(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
        ) -> "CoaxialConnectionCompoundStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis",
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
        self: Self, instance_to_wrap: "CoaxialConnectionCompoundStabilityAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2271.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2271.CoaxialConnection":
        """mastapy.system_model.connections_and_sockets.CoaxialConnection

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
    ) -> "List[_3789.CoaxialConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CoaxialConnectionStabilityAnalysis]

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
    ) -> "List[_3789.CoaxialConnectionStabilityAnalysis]":
        """List[mastapy.system_model.analyses_and_results.stability_analyses.CoaxialConnectionStabilityAnalysis]

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
    ) -> "CoaxialConnectionCompoundStabilityAnalysis._Cast_CoaxialConnectionCompoundStabilityAnalysis":
        return self._Cast_CoaxialConnectionCompoundStabilityAnalysis(self)
