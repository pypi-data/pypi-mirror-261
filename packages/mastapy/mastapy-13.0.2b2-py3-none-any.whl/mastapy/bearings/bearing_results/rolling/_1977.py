"""ISO14179SettingsDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility.databases import _1830
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ISO14179_SETTINGS_DATABASE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling", "ISO14179SettingsDatabase"
)

if TYPE_CHECKING:
    from mastapy.utility.databases import _1833, _1826


__docformat__ = "restructuredtext en"
__all__ = ("ISO14179SettingsDatabase",)


Self = TypeVar("Self", bound="ISO14179SettingsDatabase")


class ISO14179SettingsDatabase(_1830.NamedDatabase["_1976.ISO14179Settings"]):
    """ISO14179SettingsDatabase

    This is a mastapy class.
    """

    TYPE = _ISO14179_SETTINGS_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ISO14179SettingsDatabase")

    class _Cast_ISO14179SettingsDatabase:
        """Special nested class for casting ISO14179SettingsDatabase to subclasses."""

        def __init__(
            self: "ISO14179SettingsDatabase._Cast_ISO14179SettingsDatabase",
            parent: "ISO14179SettingsDatabase",
        ):
            self._parent = parent

        @property
        def named_database(
            self: "ISO14179SettingsDatabase._Cast_ISO14179SettingsDatabase",
        ) -> "_1830.NamedDatabase":
            return self._parent._cast(_1830.NamedDatabase)

        @property
        def sql_database(
            self: "ISO14179SettingsDatabase._Cast_ISO14179SettingsDatabase",
        ) -> "_1833.SQLDatabase":
            pass

            from mastapy.utility.databases import _1833

            return self._parent._cast(_1833.SQLDatabase)

        @property
        def database(
            self: "ISO14179SettingsDatabase._Cast_ISO14179SettingsDatabase",
        ) -> "_1826.Database":
            pass

            from mastapy.utility.databases import _1826

            return self._parent._cast(_1826.Database)

        @property
        def iso14179_settings_database(
            self: "ISO14179SettingsDatabase._Cast_ISO14179SettingsDatabase",
        ) -> "ISO14179SettingsDatabase":
            return self._parent

        def __getattr__(
            self: "ISO14179SettingsDatabase._Cast_ISO14179SettingsDatabase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ISO14179SettingsDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ISO14179SettingsDatabase._Cast_ISO14179SettingsDatabase":
        return self._Cast_ISO14179SettingsDatabase(self)
