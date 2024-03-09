"""HypoidGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2301
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears", "HypoidGearMesh"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.hypoid import _987
    from mastapy.system_model.connections_and_sockets.gears import _2309, _2315
    from mastapy.system_model.connections_and_sockets import _2283, _2274
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("HypoidGearMesh",)


Self = TypeVar("Self", bound="HypoidGearMesh")


class HypoidGearMesh(_2301.AGMAGleasonConicalGearMesh):
    """HypoidGearMesh

    This is a mastapy class.
    """

    TYPE = _HYPOID_GEAR_MESH
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_HypoidGearMesh")

    class _Cast_HypoidGearMesh:
        """Special nested class for casting HypoidGearMesh to subclasses."""

        def __init__(
            self: "HypoidGearMesh._Cast_HypoidGearMesh", parent: "HypoidGearMesh"
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "_2301.AGMAGleasonConicalGearMesh":
            return self._parent._cast(_2301.AGMAGleasonConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "_2309.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2309

            return self._parent._cast(_2309.ConicalGearMesh)

        @property
        def gear_mesh(self: "HypoidGearMesh._Cast_HypoidGearMesh") -> "_2315.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2315

            return self._parent._cast(_2315.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "_2283.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.InterMountableComponentConnection)

        @property
        def connection(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "_2274.Connection":
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.Connection)

        @property
        def design_entity(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def hypoid_gear_mesh(
            self: "HypoidGearMesh._Cast_HypoidGearMesh",
        ) -> "HypoidGearMesh":
            return self._parent

        def __getattr__(self: "HypoidGearMesh._Cast_HypoidGearMesh", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "HypoidGearMesh.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_mesh_design(self: Self) -> "_987.HypoidGearMeshDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def hypoid_gear_mesh_design(self: Self) -> "_987.HypoidGearMeshDesign":
        """mastapy.gears.gear_designs.hypoid.HypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HypoidGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "HypoidGearMesh._Cast_HypoidGearMesh":
        return self._Cast_HypoidGearMesh(self)
