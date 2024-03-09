"""MagnetMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.materials import _270
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MAGNET_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "MagnetMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1830, _1833, _1826


__docformat__ = "restructuredtext en"
__all__ = ("MagnetMaterialDatabase",)


Self = TypeVar("Self", bound="MagnetMaterialDatabase")


class MagnetMaterialDatabase(_270.MaterialDatabase["_1285.MagnetMaterial"]):
    """MagnetMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _MAGNET_MATERIAL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MagnetMaterialDatabase")

    class _Cast_MagnetMaterialDatabase:
        """Special nested class for casting MagnetMaterialDatabase to subclasses."""

        def __init__(
            self: "MagnetMaterialDatabase._Cast_MagnetMaterialDatabase",
            parent: "MagnetMaterialDatabase",
        ):
            self._parent = parent

        @property
        def material_database(
            self: "MagnetMaterialDatabase._Cast_MagnetMaterialDatabase",
        ) -> "_270.MaterialDatabase":
            return self._parent._cast(_270.MaterialDatabase)

        @property
        def named_database(
            self: "MagnetMaterialDatabase._Cast_MagnetMaterialDatabase",
        ) -> "_1830.NamedDatabase":
            from mastapy.utility.databases import _1830

            return self._parent._cast(_1830.NamedDatabase)

        @property
        def sql_database(
            self: "MagnetMaterialDatabase._Cast_MagnetMaterialDatabase",
        ) -> "_1833.SQLDatabase":
            pass

            from mastapy.utility.databases import _1833

            return self._parent._cast(_1833.SQLDatabase)

        @property
        def database(
            self: "MagnetMaterialDatabase._Cast_MagnetMaterialDatabase",
        ) -> "_1826.Database":
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.Database)

        @property
        def magnet_material_database(
            self: "MagnetMaterialDatabase._Cast_MagnetMaterialDatabase",
        ) -> "MagnetMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "MagnetMaterialDatabase._Cast_MagnetMaterialDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "MagnetMaterialDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "MagnetMaterialDatabase._Cast_MagnetMaterialDatabase":
        return self._Cast_MagnetMaterialDatabase(self)
