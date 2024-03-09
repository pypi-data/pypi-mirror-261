"""RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7079,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_RING_PINS_TO_DISC_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.cycloidal import _2343
    from mastapy.system_model.analyses_and_results.static_loads import _6947
    from mastapy.system_model.analyses_and_results.system_deflections import _2797
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7048,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation"
)


class RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation(
    _7079.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
):
    """RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _RING_PINS_TO_DISC_CONNECTION_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
            parent: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7079.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7079.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def ring_pins_to_disc_connection_advanced_time_stepping_analysis_for_modulation(
            self: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
        ) -> "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2343.RingPinsToDiscConnection":
        """mastapy.system_model.connections_and_sockets.cycloidal.RingPinsToDiscConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6947.RingPinsToDiscConnectionLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.RingPinsToDiscConnectionLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2797.RingPinsToDiscConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.RingPinsToDiscConnectionSystemDeflection

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
    ) -> "RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_RingPinsToDiscConnectionAdvancedTimeSteppingAnalysisForModulation(
            self
        )
