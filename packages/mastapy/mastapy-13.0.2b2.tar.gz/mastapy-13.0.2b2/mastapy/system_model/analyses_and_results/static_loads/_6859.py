"""CVTPulleyLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6943
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CVT_PULLEY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "CVTPulleyLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2589
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6855,
        _6927,
        _6840,
        _6931,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CVTPulleyLoadCase",)


Self = TypeVar("Self", bound="CVTPulleyLoadCase")


class CVTPulleyLoadCase(_6943.PulleyLoadCase):
    """CVTPulleyLoadCase

    This is a mastapy class.
    """

    TYPE = _CVT_PULLEY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CVTPulleyLoadCase")

    class _Cast_CVTPulleyLoadCase:
        """Special nested class for casting CVTPulleyLoadCase to subclasses."""

        def __init__(
            self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase",
            parent: "CVTPulleyLoadCase",
        ):
            self._parent = parent

        @property
        def pulley_load_case(
            self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase",
        ) -> "_6943.PulleyLoadCase":
            return self._parent._cast(_6943.PulleyLoadCase)

        @property
        def coupling_half_load_case(
            self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase",
        ) -> "_6855.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase",
        ) -> "_6927.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase",
        ) -> "_6840.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ComponentLoadCase)

        @property
        def part_load_case(
            self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase",
        ) -> "_6931.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cvt_pulley_load_case(
            self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase",
        ) -> "CVTPulleyLoadCase":
            return self._parent

        def __getattr__(self: "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CVTPulleyLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def clamping_force(self: Self) -> "float":
        """float"""
        temp = self.wrapped.ClampingForce

        if temp is None:
            return 0.0

        return temp

    @clamping_force.setter
    @enforce_parameter_types
    def clamping_force(self: Self, value: "float"):
        self.wrapped.ClampingForce = float(value) if value is not None else 0.0

    @property
    def effective_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EffectiveDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def number_of_nodes(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfNodes

        if temp is None:
            return 0

        return temp

    @number_of_nodes.setter
    @enforce_parameter_types
    def number_of_nodes(self: Self, value: "int"):
        self.wrapped.NumberOfNodes = int(value) if value is not None else 0

    @property
    def component_design(self: Self) -> "_2589.CVTPulley":
        """mastapy.system_model.part_model.couplings.CVTPulley

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CVTPulleyLoadCase._Cast_CVTPulleyLoadCase":
        return self._Cast_CVTPulleyLoadCase(self)
