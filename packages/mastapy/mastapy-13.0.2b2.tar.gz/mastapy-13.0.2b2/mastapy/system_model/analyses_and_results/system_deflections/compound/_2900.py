"""CylindricalGearCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2912
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CylindricalGearCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2527
    from mastapy.gears.rating.cylindrical import _455
    from mastapy.system_model.analyses_and_results.system_deflections import _2749
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2903,
        _2931,
        _2878,
        _2933,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalGearCompoundSystemDeflection")


class CylindricalGearCompoundSystemDeflection(_2912.GearCompoundSystemDeflection):
    """CylindricalGearCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearCompoundSystemDeflection"
    )

    class _Cast_CylindricalGearCompoundSystemDeflection:
        """Special nested class for casting CylindricalGearCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
            parent: "CylindricalGearCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_compound_system_deflection(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
        ) -> "_2912.GearCompoundSystemDeflection":
            return self._parent._cast(_2912.GearCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
        ) -> "_2931.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
        ) -> "_2878.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(_2878.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
        ) -> "_2933.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
        ) -> "_2903.CylindricalPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2903,
            )

            return self._parent._cast(
                _2903.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
        ) -> "CylindricalGearCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CylindricalGearCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def duty_cycle_rating(self: Self) -> "_455.CylindricalGearDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_duty_cycle_rating(
        self: Self,
    ) -> "_455.CylindricalGearDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalGearDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalDutyCycleRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2749.CylindricalGearSystemDeflectionWithLTCAResults]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflectionWithLTCAResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def planetaries(self: Self) -> "List[CylindricalGearCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.CylindricalGearCompoundSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2749.CylindricalGearSystemDeflectionWithLTCAResults]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearSystemDeflectionWithLTCAResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearCompoundSystemDeflection._Cast_CylindricalGearCompoundSystemDeflection":
        return self._Cast_CylindricalGearCompoundSystemDeflection(self)
