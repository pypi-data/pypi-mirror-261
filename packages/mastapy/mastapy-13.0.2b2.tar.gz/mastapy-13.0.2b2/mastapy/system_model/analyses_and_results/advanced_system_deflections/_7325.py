"""CylindricalGearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7337
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CylindricalGearSetAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.static_loads import _6868
    from mastapy.gears.rating.cylindrical import _464
    from mastapy.gears.gear_designs.cylindrical import _1029
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1108
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7323,
        _7324,
        _7362,
        _7376,
        _7272,
        _7357,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalGearSetAdvancedSystemDeflection")


class CylindricalGearSetAdvancedSystemDeflection(_7337.GearSetAdvancedSystemDeflection):
    """CylindricalGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetAdvancedSystemDeflection"
    )

    class _Cast_CylindricalGearSetAdvancedSystemDeflection:
        """Special nested class for casting CylindricalGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
            parent: "CylindricalGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_set_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "_7337.GearSetAdvancedSystemDeflection":
            return self._parent._cast(_7337.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "_7376.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "_7272.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7272,
            )

            return self._parent._cast(_7272.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "_7357.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def planetary_gear_set_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "_7362.PlanetaryGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7362,
            )

            return self._parent._cast(_7362.PlanetaryGearSetAdvancedSystemDeflection)

        @property
        def cylindrical_gear_set_advanced_system_deflection(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
        ) -> "CylindricalGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CylindricalGearSetAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2528.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6868.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_464.CylindricalGearSetRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_464.CylindricalGearSetRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def gear_set_design(self: Self) -> "_1029.CylindricalGearSetDesign":
        """mastapy.gears.gear_designs.cylindrical.CylindricalGearSetDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearSetDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def micro_geometry(self: Self) -> "_1108.CylindricalGearSetMicroGeometry":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearSetMicroGeometry

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MicroGeometry

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears_advanced_system_deflection(
        self: Self,
    ) -> "List[_7323.CylindricalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_advanced_system_deflection(
        self: Self,
    ) -> "List[_7324.CylindricalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesAdvancedSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetAdvancedSystemDeflection._Cast_CylindricalGearSetAdvancedSystemDeflection":
        return self._Cast_CylindricalGearSetAdvancedSystemDeflection(self)
