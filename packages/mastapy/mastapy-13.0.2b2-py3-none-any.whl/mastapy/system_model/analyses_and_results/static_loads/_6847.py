"""ConicalGearLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6893
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2525
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6848,
        _6816,
        _6825,
        _6828,
        _6829,
        _6830,
        _6908,
        _6915,
        _6918,
        _6921,
        _6956,
        _6962,
        _6965,
        _6968,
        _6969,
        _6988,
        _6927,
        _6840,
        _6931,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearLoadCase",)


Self = TypeVar("Self", bound="ConicalGearLoadCase")


class ConicalGearLoadCase(_6893.GearLoadCase):
    """ConicalGearLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearLoadCase")

    class _Cast_ConicalGearLoadCase:
        """Special nested class for casting ConicalGearLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
            parent: "ConicalGearLoadCase",
        ):
            self._parent = parent

        @property
        def gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6893.GearLoadCase":
            return self._parent._cast(_6893.GearLoadCase)

        @property
        def mountable_component_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6927.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.MountableComponentLoadCase)

        @property
        def component_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6840.ComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6840

            return self._parent._cast(_6840.ComponentLoadCase)

        @property
        def part_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6931.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6816.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6816

            return self._parent._cast(_6816.AGMAGleasonConicalGearLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6825.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6828.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6829.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6830.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.BevelGearLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6908.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6908

            return self._parent._cast(_6908.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6915.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(_6915.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6918.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(_6918.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6921.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(
                _6921.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def spiral_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6956.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.SpiralBevelGearLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6962.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6965.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6968.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6969.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.StraightBevelSunGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "_6988.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.ZerolBevelGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase",
        ) -> "ConicalGearLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearLoadCase._Cast_ConicalGearLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2525.ConicalGear":
        """mastapy.system_model.part_model.gears.ConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_manufacture_errors(self: Self) -> "_6848.ConicalGearManufactureError":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearManufactureError

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearManufactureErrors

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.ConicalGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(self: Self) -> "ConicalGearLoadCase._Cast_ConicalGearLoadCase":
        return self._Cast_ConicalGearLoadCase(self)
