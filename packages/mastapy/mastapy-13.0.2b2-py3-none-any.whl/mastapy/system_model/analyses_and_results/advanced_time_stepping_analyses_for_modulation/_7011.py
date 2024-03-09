"""AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7048,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2267
    from mastapy.system_model.analyses_and_results.system_deflections import _2690
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7037,
        _7058,
        _7059,
        _7097,
        _7111,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = (
    "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)


Self = TypeVar(
    "Self",
    bound="AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
)


class AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7048.ConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7048.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def coaxial_connection_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7037.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7037,
            )

            return self._parent._cast(
                _7037.CoaxialConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_central_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7058.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7058,
            )

            return self._parent._cast(
                _7058.CycloidalDiscCentralBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7059.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7059,
            )

            return self._parent._cast(
                _7059.CycloidalDiscPlanetaryBearingConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planetary_connection_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7097.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7097,
            )

            return self._parent._cast(
                _7097.PlanetaryConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7111.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7111,
            )

            return self._parent._cast(
                _7111.ShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def abstract_shaft_to_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(
        self: Self,
    ) -> "_2267.AbstractShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.AbstractShaftToMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2690.AbstractShaftToMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.AbstractShaftToMountableComponentConnectionSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_AbstractShaftToMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
