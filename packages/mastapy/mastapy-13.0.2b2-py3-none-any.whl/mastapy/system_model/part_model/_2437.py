"""AbstractShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.part_model import _2438
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.PartModel", "AbstractShaft"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.shaft_model import _2484
    from mastapy.system_model.part_model.cycloidal import _2571
    from mastapy.system_model.part_model import _2446, _2470
    from mastapy.system_model import _2205


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaft",)


Self = TypeVar("Self", bound="AbstractShaft")


class AbstractShaft(_2438.AbstractShaftOrHousing):
    """AbstractShaft

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractShaft")

    class _Cast_AbstractShaft:
        """Special nested class for casting AbstractShaft to subclasses."""

        def __init__(
            self: "AbstractShaft._Cast_AbstractShaft", parent: "AbstractShaft"
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing(
            self: "AbstractShaft._Cast_AbstractShaft",
        ) -> "_2438.AbstractShaftOrHousing":
            return self._parent._cast(_2438.AbstractShaftOrHousing)

        @property
        def component(self: "AbstractShaft._Cast_AbstractShaft") -> "_2446.Component":
            from mastapy.system_model.part_model import _2446

            return self._parent._cast(_2446.Component)

        @property
        def part(self: "AbstractShaft._Cast_AbstractShaft") -> "_2470.Part":
            from mastapy.system_model.part_model import _2470

            return self._parent._cast(_2470.Part)

        @property
        def design_entity(
            self: "AbstractShaft._Cast_AbstractShaft",
        ) -> "_2205.DesignEntity":
            from mastapy.system_model import _2205

            return self._parent._cast(_2205.DesignEntity)

        @property
        def shaft(self: "AbstractShaft._Cast_AbstractShaft") -> "_2484.Shaft":
            from mastapy.system_model.part_model.shaft_model import _2484

            return self._parent._cast(_2484.Shaft)

        @property
        def cycloidal_disc(
            self: "AbstractShaft._Cast_AbstractShaft",
        ) -> "_2571.CycloidalDisc":
            from mastapy.system_model.part_model.cycloidal import _2571

            return self._parent._cast(_2571.CycloidalDisc)

        @property
        def abstract_shaft(
            self: "AbstractShaft._Cast_AbstractShaft",
        ) -> "AbstractShaft":
            return self._parent

        def __getattr__(self: "AbstractShaft._Cast_AbstractShaft", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractShaft.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "AbstractShaft._Cast_AbstractShaft":
        return self._Cast_AbstractShaft(self)
