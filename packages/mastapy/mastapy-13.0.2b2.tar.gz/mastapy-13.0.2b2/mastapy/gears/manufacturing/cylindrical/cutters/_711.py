"""CylindricalGearPlungeShaverDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.manufacturing.cylindrical import _610
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_PLUNGE_SHAVER_DATABASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical.Cutters",
    "CylindricalGearPlungeShaverDatabase",
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1830, _1833, _1826


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearPlungeShaverDatabase",)


Self = TypeVar("Self", bound="CylindricalGearPlungeShaverDatabase")


class CylindricalGearPlungeShaverDatabase(
    _610.CylindricalCutterDatabase["_710.CylindricalGearPlungeShaver"]
):
    """CylindricalGearPlungeShaverDatabase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_PLUNGE_SHAVER_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearPlungeShaverDatabase")

    class _Cast_CylindricalGearPlungeShaverDatabase:
        """Special nested class for casting CylindricalGearPlungeShaverDatabase to subclasses."""

        def __init__(
            self: "CylindricalGearPlungeShaverDatabase._Cast_CylindricalGearPlungeShaverDatabase",
            parent: "CylindricalGearPlungeShaverDatabase",
        ):
            self._parent = parent

        @property
        def cylindrical_cutter_database(
            self: "CylindricalGearPlungeShaverDatabase._Cast_CylindricalGearPlungeShaverDatabase",
        ) -> "_610.CylindricalCutterDatabase":
            return self._parent._cast(_610.CylindricalCutterDatabase)

        @property
        def named_database(
            self: "CylindricalGearPlungeShaverDatabase._Cast_CylindricalGearPlungeShaverDatabase",
        ) -> "_1830.NamedDatabase":
            from mastapy.utility.databases import _1830

            return self._parent._cast(_1830.NamedDatabase)

        @property
        def sql_database(
            self: "CylindricalGearPlungeShaverDatabase._Cast_CylindricalGearPlungeShaverDatabase",
        ) -> "_1833.SQLDatabase":
            pass

            from mastapy.utility.databases import _1833

            return self._parent._cast(_1833.SQLDatabase)

        @property
        def database(
            self: "CylindricalGearPlungeShaverDatabase._Cast_CylindricalGearPlungeShaverDatabase",
        ) -> "_1826.Database":
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.Database)

        @property
        def cylindrical_gear_plunge_shaver_database(
            self: "CylindricalGearPlungeShaverDatabase._Cast_CylindricalGearPlungeShaverDatabase",
        ) -> "CylindricalGearPlungeShaverDatabase":
            return self._parent

        def __getattr__(
            self: "CylindricalGearPlungeShaverDatabase._Cast_CylindricalGearPlungeShaverDatabase",
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
        self: Self, instance_to_wrap: "CylindricalGearPlungeShaverDatabase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalGearPlungeShaverDatabase._Cast_CylindricalGearPlungeShaverDatabase"
    ):
        return self._Cast_CylindricalGearPlungeShaverDatabase(self)
