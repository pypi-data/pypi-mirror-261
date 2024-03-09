"""KlingelnbergConicalGearMaterialDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.materials import _595
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CONICAL_GEAR_MATERIAL_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Materials", "KlingelnbergConicalGearMaterialDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1830, _1833, _1826


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergConicalGearMaterialDatabase",)


Self = TypeVar("Self", bound="KlingelnbergConicalGearMaterialDatabase")


class KlingelnbergConicalGearMaterialDatabase(
    _595.GearMaterialDatabase["_601.KlingelnbergCycloPalloidConicalGearMaterial"]
):
    """KlingelnbergConicalGearMaterialDatabase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CONICAL_GEAR_MATERIAL_DATABASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergConicalGearMaterialDatabase"
    )

    class _Cast_KlingelnbergConicalGearMaterialDatabase:
        """Special nested class for casting KlingelnbergConicalGearMaterialDatabase to subclasses."""

        def __init__(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
            parent: "KlingelnbergConicalGearMaterialDatabase",
        ):
            self._parent = parent

        @property
        def gear_material_database(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
        ) -> "_595.GearMaterialDatabase":
            return self._parent._cast(_595.GearMaterialDatabase)

        @property
        def named_database(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
        ) -> "_1830.NamedDatabase":
            from mastapy.utility.databases import _1830

            return self._parent._cast(_1830.NamedDatabase)

        @property
        def sql_database(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
        ) -> "_1833.SQLDatabase":
            pass

            from mastapy.utility.databases import _1833

            return self._parent._cast(_1833.SQLDatabase)

        @property
        def database(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
        ) -> "_1826.Database":
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.Database)

        @property
        def klingelnberg_conical_gear_material_database(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
        ) -> "KlingelnbergConicalGearMaterialDatabase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase",
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
        self: Self, instance_to_wrap: "KlingelnbergConicalGearMaterialDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergConicalGearMaterialDatabase._Cast_KlingelnbergConicalGearMaterialDatabase":
        return self._Cast_KlingelnbergConicalGearMaterialDatabase(self)
