"""SpecialisedAssemblyCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
    _7408,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7376,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7414,
        _7418,
        _7421,
        _7426,
        _7428,
        _7429,
        _7434,
        _7439,
        _7442,
        _7445,
        _7449,
        _7451,
        _7457,
        _7463,
        _7465,
        _7468,
        _7472,
        _7476,
        _7479,
        _7482,
        _7488,
        _7492,
        _7499,
        _7509,
        _7510,
        _7515,
        _7518,
        _7521,
        _7525,
        _7533,
        _7536,
        _7487,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpecialisedAssemblyCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="SpecialisedAssemblyCompoundAdvancedSystemDeflection")


class SpecialisedAssemblyCompoundAdvancedSystemDeflection(
    _7408.AbstractAssemblyCompoundAdvancedSystemDeflection
):
    """SpecialisedAssemblyCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SPECIALISED_ASSEMBLY_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection"
    )

    class _Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection:
        """Special nested class for casting SpecialisedAssemblyCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
            parent: "SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7408.AbstractAssemblyCompoundAdvancedSystemDeflection":
            return self._parent._cast(
                _7408.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7487.PartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7487,
            )

            return self._parent._cast(_7487.PartCompoundAdvancedSystemDeflection)

        @property
        def part_compound_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7414.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7414,
            )

            return self._parent._cast(
                _7414.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7418.BeltDriveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(_7418.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7421.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7421,
            )

            return self._parent._cast(
                _7421.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7426.BevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7426,
            )

            return self._parent._cast(
                _7426.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bolted_joint_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7428.BoltedJointCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(_7428.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7429.ClutchCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(_7429.ClutchCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7434.ConceptCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(
                _7434.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7439.ConceptGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(
                _7439.ConceptGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7442.ConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7445.CouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(_7445.CouplingCompoundAdvancedSystemDeflection)

        @property
        def cvt_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7449.CVTCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.CVTCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7451.CycloidalAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(
                _7451.CycloidalAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7457.CylindricalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(
                _7457.CylindricalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7463.FaceGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7463,
            )

            return self._parent._cast(_7463.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7465.FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(
                _7465.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7468.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(_7468.GearSetCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7472.HypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7472,
            )

            return self._parent._cast(
                _7472.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7476.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7479.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7482.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7488.PartToPartShearCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(
                _7488.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7492.PlanetaryGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(
                _7492.PlanetaryGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7499.RollingRingAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.RollingRingAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7509.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7510.SpringDamperCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7515.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7518.StraightBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7521.SynchroniserCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.SynchroniserCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7525.TorqueConverterCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7533.WormGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(_7533.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "_7536.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7536,
            )

            return self._parent._cast(
                _7536.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
        ) -> "SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection",
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
        instance_to_wrap: "SpecialisedAssemblyCompoundAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_7376.SpecialisedAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpecialisedAssemblyAdvancedSystemDeflection]

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
    ) -> "List[_7376.SpecialisedAssemblyAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.SpecialisedAssemblyAdvancedSystemDeflection]

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
    ) -> "SpecialisedAssemblyCompoundAdvancedSystemDeflection._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection":
        return self._Cast_SpecialisedAssemblyCompoundAdvancedSystemDeflection(self)
