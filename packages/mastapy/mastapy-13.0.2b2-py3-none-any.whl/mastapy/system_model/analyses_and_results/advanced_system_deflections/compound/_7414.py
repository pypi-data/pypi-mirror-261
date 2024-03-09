"""AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7442,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7281,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7421,
        _7426,
        _7472,
        _7509,
        _7515,
        _7518,
        _7536,
        _7468,
        _7506,
        _7408,
        _7487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection"
)


class AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection(
    _7442.ConicalGearSetCompoundAdvancedSystemDeflection
):
    """AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_SET_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
    )

    class _Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection:
        """Special nested class for casting AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
            parent: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7442.ConicalGearSetCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7442.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7468.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(_7468.GearSetCompoundAdvancedSystemDeflection)

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7506.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7408.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7487.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7421.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7421,
            )

            return self._parent._cast(
                _7421.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7426.BevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7426,
            )

            return self._parent._cast(
                _7426.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7472.HypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7472,
            )

            return self._parent._cast(
                _7472.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7509.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7515.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7518.StraightBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "_7536.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7536,
            )

            return self._parent._cast(
                _7536.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
        ) -> "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7281.AGMAGleasonConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearSetAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_7281.AGMAGleasonConicalGearSetAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.AGMAGleasonConicalGearSetAdvancedSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
        return self._Cast_AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection(
            self
        )
