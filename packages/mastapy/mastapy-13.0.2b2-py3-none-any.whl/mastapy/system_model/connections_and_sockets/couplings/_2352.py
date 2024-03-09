"""SpringDamperConnection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.connections_and_sockets.couplings import _2348
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPRING_DAMPER_CONNECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.ConnectionsAndSockets.Couplings", "SpringDamperConnection"
)

if TYPE_CHECKING:
    from mastapy.system_model import _2203, _2205
    from mastapy.nodal_analysis import _72
    from mastapy.system_model.connections_and_sockets import _2283, _2274


__docformat__ = "restructuredtext en"
__all__ = ("SpringDamperConnection",)


Self = TypeVar("Self", bound="SpringDamperConnection")


class SpringDamperConnection(_2348.CouplingConnection):
    """SpringDamperConnection

    This is a mastapy class.
    """

    TYPE = _SPRING_DAMPER_CONNECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SpringDamperConnection")

    class _Cast_SpringDamperConnection:
        """Special nested class for casting SpringDamperConnection to subclasses."""

        def __init__(
            self: "SpringDamperConnection._Cast_SpringDamperConnection",
            parent: "SpringDamperConnection",
        ):
            self._parent = parent

        @property
        def coupling_connection(
            self: "SpringDamperConnection._Cast_SpringDamperConnection",
        ) -> "_2348.CouplingConnection":
            return self._parent._cast(_2348.CouplingConnection)

        @property
        def inter_mountable_component_connection(
            self: "SpringDamperConnection._Cast_SpringDamperConnection",
        ) -> "_2283.InterMountableComponentConnection":
            from mastapy.system_model.connections_and_sockets import _2283

            return self._parent._cast(_2283.InterMountableComponentConnection)

        @property
        def connection(
            self: "SpringDamperConnection._Cast_SpringDamperConnection",
        ) -> "_2274.Connection":
            from mastapy.system_model.connections_and_sockets import _2274

            return self._parent._cast(_2274.Connection)

        @property
        def design_entity(
            self: "SpringDamperConnection._Cast_SpringDamperConnection",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def spring_damper_connection(
            self: "SpringDamperConnection._Cast_SpringDamperConnection",
        ) -> "SpringDamperConnection":
            return self._parent

        def __getattr__(
            self: "SpringDamperConnection._Cast_SpringDamperConnection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SpringDamperConnection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def damping_option(self: Self) -> "_2203.ComponentDampingOption":
        """mastapy.system_model.ComponentDampingOption"""
        temp = self.wrapped.DampingOption

        if temp is None:
            return None

        value = conversion.pn_to_mp_enum(
            temp, "SMT.MastaAPI.SystemModel.ComponentDampingOption"
        )

        if value is None:
            return None

        return constructor.new_from_mastapy(
            "mastapy.system_model._2203", "ComponentDampingOption"
        )(value)

    @damping_option.setter
    @enforce_parameter_types
    def damping_option(self: Self, value: "_2203.ComponentDampingOption"):
        value = conversion.mp_to_pn_enum(
            value, "SMT.MastaAPI.SystemModel.ComponentDampingOption"
        )
        self.wrapped.DampingOption = value

    @property
    def damping(self: Self) -> "_72.LinearDampingConnectionProperties":
        """mastapy.nodal_analysis.LinearDampingConnectionProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Damping

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "SpringDamperConnection._Cast_SpringDamperConnection":
        return self._Cast_SpringDamperConnection(self)
