"""GenericMatrix"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List, Generic

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import conversion
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GENERIC_MATRIX = python_net_import("SMT.MastaAPI.MathUtility", "GenericMatrix")

if TYPE_CHECKING:
    from mastapy.math_utility import (
        _1496,
        _1498,
        _1499,
        _1500,
        _1511,
        _1526,
        _1527,
        _1528,
        _1533,
        _1538,
    )


__docformat__ = "restructuredtext en"
__all__ = ("GenericMatrix",)


Self = TypeVar("Self", bound="GenericMatrix")
TElement = TypeVar("TElement", bound="object")
TMatrix = TypeVar("TMatrix", bound="GenericMatrix")


class GenericMatrix(_0.APIBase, Generic[TElement, TMatrix]):
    """GenericMatrix

    This is a mastapy class.

    Generic Types:
        TElement
        TMatrix
    """

    TYPE = _GENERIC_MATRIX
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GenericMatrix")

    class _Cast_GenericMatrix:
        """Special nested class for casting GenericMatrix to subclasses."""

        def __init__(
            self: "GenericMatrix._Cast_GenericMatrix", parent: "GenericMatrix"
        ):
            self._parent = parent

        @property
        def complex_matrix(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1496.ComplexMatrix":
            from mastapy.math_utility import _1496

            return self._parent._cast(_1496.ComplexMatrix)

        @property
        def complex_vector(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1498.ComplexVector":
            from mastapy.math_utility import _1498

            return self._parent._cast(_1498.ComplexVector)

        @property
        def complex_vector_3d(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1499.ComplexVector3D":
            from mastapy.math_utility import _1499

            return self._parent._cast(_1499.ComplexVector3D)

        @property
        def complex_vector_6d(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1500.ComplexVector6D":
            from mastapy.math_utility import _1500

            return self._parent._cast(_1500.ComplexVector6D)

        @property
        def euler_parameters(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1511.EulerParameters":
            from mastapy.math_utility import _1511

            return self._parent._cast(_1511.EulerParameters)

        @property
        def quaternion(self: "GenericMatrix._Cast_GenericMatrix") -> "_1526.Quaternion":
            from mastapy.math_utility import _1526

            return self._parent._cast(_1526.Quaternion)

        @property
        def real_matrix(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1527.RealMatrix":
            from mastapy.math_utility import _1527

            return self._parent._cast(_1527.RealMatrix)

        @property
        def real_vector(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1528.RealVector":
            from mastapy.math_utility import _1528

            return self._parent._cast(_1528.RealVector)

        @property
        def square_matrix(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "_1533.SquareMatrix":
            from mastapy.math_utility import _1533

            return self._parent._cast(_1533.SquareMatrix)

        @property
        def vector_6d(self: "GenericMatrix._Cast_GenericMatrix") -> "_1538.Vector6D":
            from mastapy.math_utility import _1538

            return self._parent._cast(_1538.Vector6D)

        @property
        def generic_matrix(
            self: "GenericMatrix._Cast_GenericMatrix",
        ) -> "GenericMatrix":
            return self._parent

        def __getattr__(self: "GenericMatrix._Cast_GenericMatrix", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GenericMatrix.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def number_of_columns(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfColumns

        if temp is None:
            return 0

        return temp

    @property
    def number_of_entries(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfEntries

        if temp is None:
            return 0

        return temp

    @property
    def number_of_rows(self: Self) -> "int":
        """int

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NumberOfRows

        if temp is None:
            return 0

        return temp

    @property
    def data(self: Self) -> "List[TElement]":
        """List[TElement]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Data

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @enforce_parameter_types
    def get_column_at(self: Self, index: "int") -> "List[TElement]":
        """List[TElement]

        Args:
            index (int)
        """
        index = int(index)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetColumnAt(index if index else 0)
        )

    @enforce_parameter_types
    def get_row_at(self: Self, row_index: "int") -> "List[TElement]":
        """List[TElement]

        Args:
            row_index (int)
        """
        row_index = int(row_index)
        return conversion.pn_to_mp_objects_in_list(
            self.wrapped.GetRowAt(row_index if row_index else 0)
        )

    @property
    def cast_to(self: Self) -> "GenericMatrix._Cast_GenericMatrix":
        return self._Cast_GenericMatrix(self)
