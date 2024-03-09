"""KlingelnbergCycloPalloidSpiralBevelGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6915
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2542
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6847,
        _6893,
        _6927,
        _6840,
        _6931,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidSpiralBevelGearLoadCase",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidSpiralBevelGearLoadCase")


class KlingelnbergCycloPalloidSpiralBevelGearLoadCase(
    _6915.KlingelnbergCycloPalloidConicalGearLoadCase
):
    """KlingelnbergCycloPalloidSpiralBevelGearLoadCase

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_SPIRAL_BEVEL_GEAR_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase"
    )

    class _Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase:
        """Special nested class for casting KlingelnbergCycloPalloidSpiralBevelGearLoadCase to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
            parent: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ) -> "_6915.KlingelnbergCycloPalloidConicalGearLoadCase":
            return self._parent._cast(_6915.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ) -> "_6847.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.ConicalGearLoadCase)

        @property
        def gear_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ) -> "_6893.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ) -> "_6927.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ) -> "_6840.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ComponentLoadCase)

        @property
        def part_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ) -> "_6931.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
        ) -> "KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase",
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
        self: Self,
        instance_to_wrap: "KlingelnbergCycloPalloidSpiralBevelGearLoadCase.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2542.KlingelnbergCycloPalloidSpiralBevelGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidSpiralBevelGear

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
    ) -> "KlingelnbergCycloPalloidSpiralBevelGearLoadCase._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
        return self._Cast_KlingelnbergCycloPalloidSpiralBevelGearLoadCase(self)
