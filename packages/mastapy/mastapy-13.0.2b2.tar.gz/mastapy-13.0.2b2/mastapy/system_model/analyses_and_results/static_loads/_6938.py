"""PlanetCarrierLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6927
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANET_CARRIER_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "PlanetCarrierLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2471
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6937,
        _6840,
        _6931,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PlanetCarrierLoadCase",)


Self = TypeVar("Self", bound="PlanetCarrierLoadCase")


class PlanetCarrierLoadCase(_6927.MountableComponentLoadCase):
    """PlanetCarrierLoadCase

    This is a mastapy class.
    """

    TYPE = _PLANET_CARRIER_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PlanetCarrierLoadCase")

    class _Cast_PlanetCarrierLoadCase:
        """Special nested class for casting PlanetCarrierLoadCase to subclasses."""

        def __init__(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
            parent: "PlanetCarrierLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_6927.MountableComponentLoadCase":
            return self._parent._cast(_6927.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_6840.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ComponentLoadCase)

        @property
        def part_load_case(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_6931.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def planet_carrier_load_case(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase",
        ) -> "PlanetCarrierLoadCase":
            return self._parent

        def __getattr__(
            self: "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PlanetCarrierLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2471.PlanetCarrier":
        """mastapy.system_model.part_model.PlanetCarrier

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planet_manufacture_errors(
        self: Self,
    ) -> "List[_6937.PlanetarySocketManufactureError]":
        """List[mastapy.system_model.analyses_and_results.static_loads.PlanetarySocketManufactureError]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PlanetManufactureErrors

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "PlanetCarrierLoadCase._Cast_PlanetCarrierLoadCase":
        return self._Cast_PlanetCarrierLoadCase(self)
