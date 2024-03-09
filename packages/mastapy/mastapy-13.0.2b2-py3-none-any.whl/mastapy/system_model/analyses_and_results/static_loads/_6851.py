"""ConicalGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6898
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2526
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6850,
        _6818,
        _6827,
        _6832,
        _6910,
        _6917,
        _6920,
        _6923,
        _6958,
        _6964,
        _6967,
        _6990,
        _6955,
        _6809,
        _6931,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearSetLoadCase",)


Self = TypeVar("Self", bound="ConicalGearSetLoadCase")


class ConicalGearSetLoadCase(_6898.GearSetLoadCase):
    """ConicalGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearSetLoadCase")

    class _Cast_ConicalGearSetLoadCase:
        """Special nested class for casting ConicalGearSetLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
            parent: "ConicalGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6898.GearSetLoadCase":
            return self._parent._cast(_6898.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6955.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6809.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6809

            return self._parent._cast(_6809.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6931.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6818.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6818

            return self._parent._cast(_6818.AGMAGleasonConicalGearSetLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6827.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6832.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6832

            return self._parent._cast(_6832.BevelGearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6910.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(_6910.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6917.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(
                _6917.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6920.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(
                _6920.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6923.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6923

            return self._parent._cast(
                _6923.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def spiral_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6958.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6964.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6967.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.StraightBevelGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "_6990.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6990

            return self._parent._cast(_6990.ZerolBevelGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase",
        ) -> "ConicalGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2526.ConicalGearSet":
        """mastapy.system_model.part_model.gears.ConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6850.ConicalGearSetHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "ConicalGearSetLoadCase._Cast_ConicalGearSetLoadCase":
        return self._Cast_ConicalGearSetLoadCase(self)
