"""CylindricalManufacturedGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1220
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_MANUFACTURED_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Cylindrical",
    "CylindricalManufacturedGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.gears.analysis import _1219, _1216


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalManufacturedGearLoadCase",)


Self = TypeVar("Self", bound="CylindricalManufacturedGearLoadCase")


class CylindricalManufacturedGearLoadCase(_1220.GearImplementationAnalysis):
    """CylindricalManufacturedGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_MANUFACTURED_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalManufacturedGearLoadCase")

    class _Cast_CylindricalManufacturedGearLoadCase:
        """Special nested class for casting CylindricalManufacturedGearLoadCase to subclasses."""

        def __init__(
            self: "CylindricalManufacturedGearLoadCase._Cast_CylindricalManufacturedGearLoadCase",
            parent: "CylindricalManufacturedGearLoadCase",
        ):
            self._parent = parent

        @property
        def gear_implementation_analysis(
            self: "CylindricalManufacturedGearLoadCase._Cast_CylindricalManufacturedGearLoadCase",
        ) -> "_1220.GearImplementationAnalysis":
            return self._parent._cast(_1220.GearImplementationAnalysis)

        @property
        def gear_design_analysis(
            self: "CylindricalManufacturedGearLoadCase._Cast_CylindricalManufacturedGearLoadCase",
        ) -> "_1219.GearDesignAnalysis":
            from mastapy.gears.analysis import _1219

            return self._parent._cast(_1219.GearDesignAnalysis)

        @property
        def abstract_gear_analysis(
            self: "CylindricalManufacturedGearLoadCase._Cast_CylindricalManufacturedGearLoadCase",
        ) -> "_1216.AbstractGearAnalysis":
            from mastapy.gears.analysis import _1216

            return self._parent._cast(_1216.AbstractGearAnalysis)

        @property
        def cylindrical_manufactured_gear_load_case(
            self: "CylindricalManufacturedGearLoadCase._Cast_CylindricalManufacturedGearLoadCase",
        ) -> "CylindricalManufacturedGearLoadCase":
            return self._parent

        def __getattr__(
            self: "CylindricalManufacturedGearLoadCase._Cast_CylindricalManufacturedGearLoadCase",
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
        self: Self, instance_to_wrap: "CylindricalManufacturedGearLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> (
        "CylindricalManufacturedGearLoadCase._Cast_CylindricalManufacturedGearLoadCase"
    ):
        return self._Cast_CylindricalManufacturedGearLoadCase(self)
