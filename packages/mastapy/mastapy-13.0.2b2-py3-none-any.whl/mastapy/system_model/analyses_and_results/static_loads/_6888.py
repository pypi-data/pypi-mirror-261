"""FaceGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6895
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_FACE_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "FaceGearMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2313
    from mastapy.system_model.analyses_and_results.static_loads import _6914, _6852
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("FaceGearMeshLoadCase",)


Self = TypeVar("Self", bound="FaceGearMeshLoadCase")


class FaceGearMeshLoadCase(_6895.GearMeshLoadCase):
    """FaceGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _FACE_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_FaceGearMeshLoadCase")

    class _Cast_FaceGearMeshLoadCase:
        """Special nested class for casting FaceGearMeshLoadCase to subclasses."""

        def __init__(
            self: "FaceGearMeshLoadCase._Cast_FaceGearMeshLoadCase",
            parent: "FaceGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def gear_mesh_load_case(
            self: "FaceGearMeshLoadCase._Cast_FaceGearMeshLoadCase",
        ) -> "_6895.GearMeshLoadCase":
            return self._parent._cast(_6895.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "FaceGearMeshLoadCase._Cast_FaceGearMeshLoadCase",
        ) -> "_6914.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "FaceGearMeshLoadCase._Cast_FaceGearMeshLoadCase",
        ) -> "_6852.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "FaceGearMeshLoadCase._Cast_FaceGearMeshLoadCase",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "FaceGearMeshLoadCase._Cast_FaceGearMeshLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "FaceGearMeshLoadCase._Cast_FaceGearMeshLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def face_gear_mesh_load_case(
            self: "FaceGearMeshLoadCase._Cast_FaceGearMeshLoadCase",
        ) -> "FaceGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "FaceGearMeshLoadCase._Cast_FaceGearMeshLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "FaceGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(self: Self) -> "FaceGearMeshLoadCase._Cast_FaceGearMeshLoadCase":
        return self._Cast_FaceGearMeshLoadCase(self)
