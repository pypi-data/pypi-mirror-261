"""CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5381
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
        "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2340
    from mastapy.system_model.analyses_and_results.static_loads import _6863
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5416
    from mastapy.system_model.analyses_and_results.analysis_cases import _7544, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",)


Self = TypeVar(
    "Self", bound="CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis"
)


class CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis(
    _5381.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
):
    """CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _CYCLOIDAL_DISC_PLANETARY_BEARING_CONNECTION_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
    )

    class _Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis:
        """Special nested class for casting CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
            parent: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> (
            "_5381.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            return self._parent._cast(
                _5381.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_5416.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7544.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
        ) -> "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2340.CycloidalDiscPlanetaryBearingConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.CycloidalDiscPlanetaryBearingConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6863.CycloidalDiscPlanetaryBearingConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CycloidalDiscPlanetaryBearingConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
        return (
            self._Cast_CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis(
                self
            )
        )
