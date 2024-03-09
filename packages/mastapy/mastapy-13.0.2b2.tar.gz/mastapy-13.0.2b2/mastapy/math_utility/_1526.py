"""Quaternion"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.math_utility import _1528
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_QUATERNION = python_net_import("SMT.MastaAPI.MathUtility", "Quaternion")

if TYPE_CHECKING:
    from mastapy.math_utility import _1527, _1516


__docformat__ = "restructuredtext en"
__all__ = ("Quaternion",)


Self = TypeVar("Self", bound="Quaternion")


class Quaternion(_1528.RealVector):
    """Quaternion

    This is a mastapy class.
    """

    TYPE = _QUATERNION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_Quaternion")

    class _Cast_Quaternion:
        """Special nested class for casting Quaternion to subclasses."""

        def __init__(self: "Quaternion._Cast_Quaternion", parent: "Quaternion"):
            self._parent = parent

        @property
        def real_vector(self: "Quaternion._Cast_Quaternion") -> "_1528.RealVector":
            return self._parent._cast(_1528.RealVector)

        @property
        def real_matrix(self: "Quaternion._Cast_Quaternion") -> "_1527.RealMatrix":
            from mastapy.math_utility import _1527

            return self._parent._cast(_1527.RealMatrix)

        @property
        def generic_matrix(
            self: "Quaternion._Cast_Quaternion",
        ) -> "_1516.GenericMatrix":
            from mastapy.math_utility import _1516

            return self._parent._cast(_1516.GenericMatrix)

        @property
        def quaternion(self: "Quaternion._Cast_Quaternion") -> "Quaternion":
            return self._parent

        def __getattr__(self: "Quaternion._Cast_Quaternion", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "Quaternion.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "Quaternion._Cast_Quaternion":
        return self._Cast_Quaternion(self)
