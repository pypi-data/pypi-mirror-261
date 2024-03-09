"""KlingelnbergCycloPalloidHypoidGearMesh"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.connections_and_sockets.gears import _2320
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Gears",
    "KlingelnbergCycloPalloidHypoidGearMesh",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _979
    from mastapy.system_model.connections_and_sockets.gears import _2309, _2315
    from mastapy.system_model.connections_and_sockets import _2283, _2274
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMesh",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidHypoidGearMesh")


class KlingelnbergCycloPalloidHypoidGearMesh(
    _2320.KlingelnbergCycloPalloidConicalGearMesh
):
    """KlingelnbergCycloPalloidHypoidGearMesh

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidHypoidGearMesh"
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMesh:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMesh to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
            parent: "KlingelnbergCycloPalloidHypoidGearMesh",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ) -> "_2320.KlingelnbergCycloPalloidConicalGearMesh":
            return self._parent._cast(_2320.KlingelnbergCycloPalloidConicalGearMesh)

        @property
        def conical_gear_mesh(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ) -> "_2309.ConicalGearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2309

            return self._parent._cast(_2309.ConicalGearMesh)

        @property
        def gear_mesh(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ) -> "_2315.GearMesh":
            from mastapy.system_model.connections_and_sockets.gears import _2315

            return self._parent._cast(_2315.GearMesh)

        @property
        def inter_mountable_component_connection(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ) -> "_2283.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.InterMountableComponentConnection)

        @property
        def connection(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ) -> "_2274.Connection":
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.Connection)

        @property
        def design_entity(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
        ) -> "KlingelnbergCycloPalloidHypoidGearMesh":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh",
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
        self: Self, instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMesh.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def active_gear_mesh_design(
        self: Self,
    ) -> "_979.KlingelnbergCycloPalloidHypoidGearMeshDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ActiveGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def klingelnberg_cyclo_palloid_hypoid_gear_mesh_design(
        self: Self,
    ) -> "_979.KlingelnbergCycloPalloidHypoidGearMeshDesign":
        """mastapy.gears.gear_designs.klingelnberg_hypoid.KlingelnbergCycloPalloidHypoidGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.KlingelnbergCycloPalloidHypoidGearMeshDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidHypoidGearMesh._Cast_KlingelnbergCycloPalloidHypoidGearMesh":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMesh(self)
