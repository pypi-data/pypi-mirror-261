"""BevelDifferentialGearCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7424,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "BevelDifferentialGearCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2517
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7286,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7422,
        _7423,
        _7412,
        _7440,
        _7466,
        _7485,
        _7433,
        _7487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialGearCompoundAdvancedSystemDeflection")


class BevelDifferentialGearCompoundAdvancedSystemDeflection(
    _7424.BevelGearCompoundAdvancedSystemDeflection
):
    """BevelDifferentialGearCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection"
    )

    class _Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection:
        """Special nested class for casting BevelDifferentialGearCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
            parent: "BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7424.BevelGearCompoundAdvancedSystemDeflection":
            return self._parent._cast(_7424.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7412.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7412,
            )

            return self._parent._cast(
                _7412.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7440.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(_7440.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7466.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(_7466.GearCompoundAdvancedSystemDeflection)

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7485.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(
                _7485.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def component_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7433.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(_7433.ComponentCompoundAdvancedSystemDeflection)

        @property
        def part_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7487.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7422.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(
                _7422.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "_7423.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7423,
            )

            return self._parent._cast(
                _7423.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
        ) -> "BevelDifferentialGearCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "BevelDifferentialGearCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2517.BevelDifferentialGear":
        """mastapy.system_model.part_model.gears.BevelDifferentialGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7286.BevelDifferentialGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelDifferentialGearAdvancedSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7286.BevelDifferentialGearAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.BevelDifferentialGearAdvancedSystemDeflection]

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
    ) -> "BevelDifferentialGearCompoundAdvancedSystemDeflection._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection":
        return self._Cast_BevelDifferentialGearCompoundAdvancedSystemDeflection(self)
