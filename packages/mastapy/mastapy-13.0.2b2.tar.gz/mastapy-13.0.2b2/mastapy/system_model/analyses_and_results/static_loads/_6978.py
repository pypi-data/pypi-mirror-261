"""TorqueConverterTurbineLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6855
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_TORQUE_CONVERTER_TURBINE_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "TorqueConverterTurbineLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2612
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6927,
        _6840,
        _6931,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("TorqueConverterTurbineLoadCase",)


Self = TypeVar("Self", bound="TorqueConverterTurbineLoadCase")


class TorqueConverterTurbineLoadCase(_6855.CouplingHalfLoadCase):
    """TorqueConverterTurbineLoadCase

    This is a mastapy class.
    """

    TYPE = _TORQUE_CONVERTER_TURBINE_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_TorqueConverterTurbineLoadCase")

    class _Cast_TorqueConverterTurbineLoadCase:
        """Special nested class for casting TorqueConverterTurbineLoadCase to subclasses."""

        def __init__(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
            parent: "TorqueConverterTurbineLoadCase",
        ):
            self._parent = parent

        @property
        def coupling_half_load_case(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_6855.CouplingHalfLoadCase":
            return self._parent._cast(_6855.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_6927.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_6840.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ComponentLoadCase)

        @property
        def part_load_case(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_6931.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def torque_converter_turbine_load_case(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
        ) -> "TorqueConverterTurbineLoadCase":
            return self._parent

        def __getattr__(
            self: "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "TorqueConverterTurbineLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2612.TorqueConverterTurbine":
        """mastapy.system_model.part_model.couplings.TorqueConverterTurbine

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "TorqueConverterTurbineLoadCase._Cast_TorqueConverterTurbineLoadCase":
        return self._Cast_TorqueConverterTurbineLoadCase(self)
