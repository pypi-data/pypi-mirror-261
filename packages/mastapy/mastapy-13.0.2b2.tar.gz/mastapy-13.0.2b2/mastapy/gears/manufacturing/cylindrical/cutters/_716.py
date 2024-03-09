"""CylindricalGearShaverDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical import _610
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SHAVER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalGearShaverDatabase",
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1830, _1833, _1826


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearShaverDatabase",)


Self = TypeVar("Self", bound="CylindricalGearShaverDatabase")


class CylindricalGearShaverDatabase(
    _610.CylindricalCutterDatabase["_715.CylindricalGearShaver"]
):
    """CylindricalGearShaverDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SHAVER_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearShaverDatabase")

    class _Cast_CylindricalGearShaverDatabase:
        """Special nested class for casting CylindricalGearShaverDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearShaverDatabase._Cast_CylindricalGearShaverDatabase",
            parent: "CylindricalGearShaverDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_cutter_database(
            self: "CylindricalGearShaverDatabase._Cast_CylindricalGearShaverDatabase",
        ) -> "_610.CylindricalCutterDatabase":
            return self._parent._cast(_610.CylindricalCutterDatabase)

        @property
        def named_database(
            self: "CylindricalGearShaverDatabase._Cast_CylindricalGearShaverDatabase",
        ) -> "_1830.NamedDatabase":
            from mastapy.utility.databases import _1830

            return self._parent._cast(_1830.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearShaverDatabase._Cast_CylindricalGearShaverDatabase",
        ) -> "_1833.SQLDatabase":
            pass

            from mastapy.utility.databases import _1833

            return self._parent._cast(_1833.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearShaverDatabase._Cast_CylindricalGearShaverDatabase",
        ) -> "_1826.Database":
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.Database)

        @property
        def cylindrical_gear_shaver_database(
            self: "CylindricalGearShaverDatabase._Cast_CylindricalGearShaverDatabase",
        ) -> "CylindricalGearShaverDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearShaverDatabase._Cast_CylindricalGearShaverDatabase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CylindricalGearShaverDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearShaverDatabase._Cast_CylindricalGearShaverDatabase":
        return self._Cast_CylindricalGearShaverDatabase(self)
