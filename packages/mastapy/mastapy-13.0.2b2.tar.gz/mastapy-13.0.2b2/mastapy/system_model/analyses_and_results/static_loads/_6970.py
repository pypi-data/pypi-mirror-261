"""SynchroniserHalfLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6972
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_HALF_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "SynchroniserHalfLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2606
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6855,
        _6927,
        _6840,
        _6931,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserHalfLoadCase",)


Self = TypeVar("Self", bound="SynchroniserHalfLoadCase")


class SynchroniserHalfLoadCase(_6972.SynchroniserPartLoadCase):
    """SynchroniserHalfLoadCase

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_HALF_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserHalfLoadCase")

    class _Cast_SynchroniserHalfLoadCase:
        """Special nested class for casting SynchroniserHalfLoadCase to subclasses."""

        def __init__(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase",
            parent: "SynchroniserHalfLoadCase",
        ):
            self._parent = parent

        @property
        def synchroniser_part_load_case(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase",
        ) -> "_6972.SynchroniserPartLoadCase":
            return self._parent._cast(_6972.SynchroniserPartLoadCase)

        @property
        def coupling_half_load_case(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase",
        ) -> "_6855.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.CouplingHalfLoadCase)

        @property
        def mountable_component_load_case(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase",
        ) -> "_6927.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase",
        ) -> "_6840.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ComponentLoadCase)

        @property
        def part_load_case(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase",
        ) -> "_6931.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def synchroniser_half_load_case(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase",
        ) -> "SynchroniserHalfLoadCase":
            return self._parent

        def __getattr__(
            self: "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SynchroniserHalfLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2606.SynchroniserHalf":
        """mastapy.system_model.part_model.couplings.SynchroniserHalf

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
    ) -> "SynchroniserHalfLoadCase._Cast_SynchroniserHalfLoadCase":
        return self._Cast_SynchroniserHalfLoadCase(self)
