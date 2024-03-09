"""ShaftToMountableComponentConnectionModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4577
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ShaftToMountableComponentConnectionModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2297
    from mastapy.system_model.analyses_and_results.system_deflections import _2807
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4598,
        _4619,
        _4668,
        _4609,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ShaftToMountableComponentConnectionModalAnalysis",)


Self = TypeVar("Self", bound="ShaftToMountableComponentConnectionModalAnalysis")


class ShaftToMountableComponentConnectionModalAnalysis(
    _4577.AbstractShaftToMountableComponentConnectionModalAnalysis
):
    """ShaftToMountableComponentConnectionModalAnalysis

    This is a mastapy class.
    """

    TYPE = _SHAFT_TO_MOUNTABLE_COMPONENT_CONNECTION_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ShaftToMountableComponentConnectionModalAnalysis"
    )

    class _Cast_ShaftToMountableComponentConnectionModalAnalysis:
        """Special nested class for casting ShaftToMountableComponentConnectionModalAnalysis to subclasses."""

        def __init__(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
            parent: "ShaftToMountableComponentConnectionModalAnalysis",
        ):
            self._parent = parent

        @property
        def abstract_shaft_to_mountable_component_connection_modal_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "_4577.AbstractShaftToMountableComponentConnectionModalAnalysis":
            return self._parent._cast(
                _4577.AbstractShaftToMountableComponentConnectionModalAnalysis
            )

        @property
        def connection_modal_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "_4609.ConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4609

            return self._parent._cast(_4609.ConnectionModalAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def coaxial_connection_modal_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "_4598.CoaxialConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4598

            return self._parent._cast(_4598.CoaxialConnectionModalAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_modal_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "_4619.CycloidalDiscCentralBearingConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4619

            return self._parent._cast(
                _4619.CycloidalDiscCentralBearingConnectionModalAnalysis
            )

        @property
        def planetary_connection_modal_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "_4668.PlanetaryConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4668

            return self._parent._cast(_4668.PlanetaryConnectionModalAnalysis)

        @property
        def shaft_to_mountable_component_connection_modal_analysis(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
        ) -> "ShaftToMountableComponentConnectionModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis",
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
        instance_to_wrap: "ShaftToMountableComponentConnectionModalAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2297.ShaftToMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.ShaftToMountableComponentConnection

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
    ) -> "_2807.ShaftToMountableComponentConnectionSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ShaftToMountableComponentConnectionSystemDeflection

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
    ) -> "ShaftToMountableComponentConnectionModalAnalysis._Cast_ShaftToMountableComponentConnectionModalAnalysis":
        return self._Cast_ShaftToMountableComponentConnectionModalAnalysis(self)
