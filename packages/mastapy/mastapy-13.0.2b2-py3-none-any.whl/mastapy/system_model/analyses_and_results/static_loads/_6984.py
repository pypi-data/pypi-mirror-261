"""VirtualComponentLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6927
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "VirtualComponentLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2481
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6924,
        _6925,
        _6941,
        _6942,
        _6983,
        _6840,
        _6931,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentLoadCase",)


Self = TypeVar("Self", bound="VirtualComponentLoadCase")


class VirtualComponentLoadCase(_6927.MountableComponentLoadCase):
    """VirtualComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_VirtualComponentLoadCase")

    class _Cast_VirtualComponentLoadCase:
        """Special nested class for casting VirtualComponentLoadCase to subclasses."""

        def __init__(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
            parent: "VirtualComponentLoadCase",
        ):
            self._parent = parent

        @property
        def mountable_component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6927.MountableComponentLoadCase":
            return self._parent._cast(_6927.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6840.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ComponentLoadCase)

        @property
        def part_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6931.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def mass_disc_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6924.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6925.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.MeasurementComponentLoadCase)

        @property
        def point_load_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6941.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(_6941.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6942.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.PowerLoadLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "_6983.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase",
        ) -> "VirtualComponentLoadCase":
            return self._parent

        def __getattr__(
            self: "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "VirtualComponentLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2481.VirtualComponent":
        """mastapy.system_model.part_model.VirtualComponent

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
    ) -> "VirtualComponentLoadCase._Cast_VirtualComponentLoadCase":
        return self._Cast_VirtualComponentLoadCase(self)
