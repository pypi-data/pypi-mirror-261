"""CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5555
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
        "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5425
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5628,
        _5534,
        _5566,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self",
    bound="CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
)


class CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis(
    _5555.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
):
    """CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = (
        _CYCLOIDAL_DISC_CENTRAL_BEARING_CONNECTION_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
    )

    class _Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
            parent: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def coaxial_connection_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5555.CoaxialConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(
                _5555.CoaxialConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5628.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5628,
            )

            return self._parent._cast(
                _5628.ShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def abstract_shaft_to_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5534.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5534,
            )

            return self._parent._cast(
                _5534.AbstractShaftToMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_5566.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(_5566.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_compound_multibody_dynamics_analysis(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
        ) -> "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5425.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]

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
    ) -> "List[_5425.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis]

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
    ) -> "CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis":
        return self._Cast_CycloidalDiscCentralBearingConnectionCompoundMultibodyDynamicsAnalysis(
            self
        )
