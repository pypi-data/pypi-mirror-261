"""CylindricalGearAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7335
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "CylindricalGearAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.gears.rating.cylindrical import _460
    from mastapy.system_model.analyses_and_results.static_loads import _6864
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7324,
        _7326,
        _7327,
        _7355,
        _7300,
        _7357,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalGearAdvancedSystemDeflection")


class CylindricalGearAdvancedSystemDeflection(_7335.GearAdvancedSystemDeflection):
    """CylindricalGearAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearAdvancedSystemDeflection"
    )

    class _Cast_CylindricalGearAdvancedSystemDeflection:
        """Special nested class for casting CylindricalGearAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
            parent: "CylindricalGearAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "_7335.GearAdvancedSystemDeflection":
            return self._parent._cast(_7335.GearAdvancedSystemDeflection)

        @property
        def mountable_component_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "_7355.MountableComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7355,
            )

            return self._parent._cast(_7355.MountableComponentAdvancedSystemDeflection)

        @property
        def component_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "_7300.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "_7357.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "_7327.CylindricalPlanetGearAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7327,
            )

            return self._parent._cast(
                _7327.CylindricalPlanetGearAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_advanced_system_deflection(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
        ) -> "CylindricalGearAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "CylindricalGearAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_principal_root_stress_compression(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPrincipalRootStressCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_principal_root_stress_tension(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumPrincipalRootStressTension

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_von_mises_root_stress_compression(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumVonMisesRootStressCompression

        if temp is None:
            return 0.0

        return temp

    @property
    def maximum_von_mises_root_stress_tension(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumVonMisesRootStressTension

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2527.CylindricalGear":
        """mastapy.system_model.part_model.gears.CylindricalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_460.CylindricalGearRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6864.CylindricalGearLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gear_advanced_system_deflection_meshes(
        self: Self,
    ) -> "List[_7324.CylindricalGearMeshAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearMeshAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearAdvancedSystemDeflectionMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_gear_advanced_system_deflections_in_meshes(
        self: Self,
    ) -> "List[_7326.CylindricalMeshedGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalMeshedGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearAdvancedSystemDeflectionsInMeshes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshed_gear_advanced_system_deflections(
        self: Self,
    ) -> "List[_7326.CylindricalMeshedGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalMeshedGearAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshedGearAdvancedSystemDeflections

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[CylindricalGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.CylindricalGearAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "CylindricalGearAdvancedSystemDeflection._Cast_CylindricalGearAdvancedSystemDeflection":
        return self._Cast_CylindricalGearAdvancedSystemDeflection(self)
