"""BevelDifferentialGearSetLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6832
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearSetLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2518
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6825,
        _6826,
        _6818,
        _6851,
        _6898,
        _6955,
        _6809,
        _6931,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetLoadCase",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetLoadCase")


class BevelDifferentialGearSetLoadCase(_6832.BevelGearSetLoadCase):
    """BevelDifferentialGearSetLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearSetLoadCase")

    class _Cast_BevelDifferentialGearSetLoadCase:
        """Special nested class for casting BevelDifferentialGearSetLoadCase to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
            parent: "BevelDifferentialGearSetLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6832.BevelGearSetLoadCase":
            return self._parent._cast(_6832.BevelGearSetLoadCase)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6818.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6818

            return self._parent._cast(_6818.AGMAGleasonConicalGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6851.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.ConicalGearSetLoadCase)

        @property
        def gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6898.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6898

            return self._parent._cast(_6898.GearSetLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6955.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpecialisedAssemblyLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6809.AbstractAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6809

            return self._parent._cast(_6809.AbstractAssemblyLoadCase)

        @property
        def part_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_6931.PartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6931

            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_load_case(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
        ) -> "BevelDifferentialGearSetLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelDifferentialGearSetLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def sun_speeds_are_equal(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.SunSpeedsAreEqual

        if temp is None:
            return False

        return temp

    @sun_speeds_are_equal.setter
    @enforce_parameter_types
    def sun_speeds_are_equal(self: Self, value: "bool"):
        self.wrapped.SunSpeedsAreEqual = bool(value) if value is not None else False

    @property
    def assembly_design(self: Self) -> "_2518.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gears(self: Self) -> "List[_6825.BevelDifferentialGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Gears

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_gears_load_case(
        self: Self,
    ) -> "List[_6825.BevelDifferentialGearLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_load_case(
        self: Self,
    ) -> "List[_6826.BevelDifferentialGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesLoadCase

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetLoadCase._Cast_BevelDifferentialGearSetLoadCase":
        return self._Cast_BevelDifferentialGearSetLoadCase(self)
