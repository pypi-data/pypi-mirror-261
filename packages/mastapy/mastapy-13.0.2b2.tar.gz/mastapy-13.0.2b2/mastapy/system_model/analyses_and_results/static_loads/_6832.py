"""BevelGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6818
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "BevelGearSetLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2522
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6827,
        _6958,
        _6964,
        _6967,
        _6990,
        _6851,
        _6898,
        _6955,
        _6809,
        _6931,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearSetLoadCase",)


Self = TypeVar("Self", bound="BevelGearSetLoadCase")


class BevelGearSetLoadCase(_6818.AGMAGleasonConicalGearSetLoadCase):
    """BevelGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearSetLoadCase")

    class _Cast_BevelGearSetLoadCase:
        """Special nested class for casting BevelGearSetLoadCase to subclasses."""

        def __init__(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
            parent: "BevelGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6818.AGMAGleasonConicalGearSetLoadCase":
            return self._parent._cast(_6818.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6851.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6898.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6898

            return self._parent._cast(_6898.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6955.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6809.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6809

            return self._parent._cast(_6809.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6931.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6827.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelDifferentialGearSetLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6958.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.SpiralBevelGearSetLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6964.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6967.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.StraightBevelGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "_6990.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6990

            return self._parent._cast(_6990.ZerolBevelGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase",
        ) -> "BevelGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2522.BevelGearSet":
        """mastapy.system_model.part_model.gears.BevelGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "BevelGearSetLoadCase._Cast_BevelGearSetLoadCase":
        return self._Cast_BevelGearSetLoadCase(self)
