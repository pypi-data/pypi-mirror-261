"""FaceGearMeshPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.power_flows import _4095
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows", "FaceGearMeshPowerFlow"
)

if TYPE_CHECKING:
    from mastapy.gears.rating.face import _447
    from mastapy.system_model.connections_and_sockets.gears import _2313
    from mastapy.system_model.analyses_and_results.static_loads import _6888
    from mastapy.system_model.analyses_and_results.power_flows import _4102, _4069
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshPowerFlow",)


Self = TypeVar("Self", bound="FaceGearMeshPowerFlow")


class FaceGearMeshPowerFlow(_4095.GearMeshPowerFlow):
    """FaceGearMeshPowerFlow

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshPowerFlow")

    class _Cast_FaceGearMeshPowerFlow:
        """Special nested class for casting FaceGearMeshPowerFlow to subclasses."""

        def __init__(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow",
            parent: "FaceGearMeshPowerFlow",
        ):
            self._parent = parent

        @property
        def gear_mesh_power_flow(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow",
        ) -> "_4095.GearMeshPowerFlow":
            return self._parent._cast(_4095.GearMeshPowerFlow)

        @property
        def inter_mountable_component_connection_power_flow(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow",
        ) -> "_4102.InterMountableComponentConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4102

            return self._parent._cast(_4102.InterMountableComponentConnectionPowerFlow)

        @property
        def connection_power_flow(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow",
        ) -> "_4069.ConnectionPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows import _4069

            return self._parent._cast(_4069.ConnectionPowerFlow)

        @property
        def connection_static_load_analysis_case(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def face_gear_mesh_power_flow(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow",
        ) -> "FaceGearMeshPowerFlow":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearMeshPowerFlow.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def rating(self: Self) -> "_447.FaceGearMeshRating":
        """mastapy.gears.rating.face.FaceGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_447.FaceGearMeshRating":
        """mastapy.gears.rating.face.FaceGearMeshRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2313.FaceGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.FaceGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6888.FaceGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.FaceGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "FaceGearMeshPowerFlow._Cast_FaceGearMeshPowerFlow":
        return self._Cast_FaceGearMeshPowerFlow(self)
