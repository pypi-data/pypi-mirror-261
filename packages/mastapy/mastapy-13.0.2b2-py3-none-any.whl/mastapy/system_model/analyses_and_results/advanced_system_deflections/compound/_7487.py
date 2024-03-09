"""PartCompoundAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7548
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections.Compound",
    "PartCompoundAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7357,
    )
    from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
        _7408,
        _7409,
        _7410,
        _7412,
        _7414,
        _7415,
        _7416,
        _7418,
        _7419,
        _7421,
        _7422,
        _7423,
        _7424,
        _7426,
        _7427,
        _7428,
        _7429,
        _7431,
        _7433,
        _7434,
        _7436,
        _7437,
        _7439,
        _7440,
        _7442,
        _7444,
        _7445,
        _7447,
        _7449,
        _7450,
        _7451,
        _7453,
        _7455,
        _7457,
        _7458,
        _7459,
        _7460,
        _7461,
        _7463,
        _7464,
        _7465,
        _7466,
        _7468,
        _7469,
        _7470,
        _7472,
        _7474,
        _7476,
        _7477,
        _7479,
        _7480,
        _7482,
        _7483,
        _7484,
        _7485,
        _7486,
        _7488,
        _7490,
        _7492,
        _7493,
        _7494,
        _7495,
        _7496,
        _7497,
        _7499,
        _7500,
        _7502,
        _7503,
        _7504,
        _7506,
        _7507,
        _7509,
        _7510,
        _7512,
        _7513,
        _7515,
        _7516,
        _7518,
        _7519,
        _7520,
        _7521,
        _7522,
        _7523,
        _7524,
        _7525,
        _7527,
        _7528,
        _7529,
        _7530,
        _7531,
        _7533,
        _7534,
        _7536,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="PartCompoundAdvancedSystemDeflection")


class PartCompoundAdvancedSystemDeflection(_7548.PartCompoundAnalysis):
    """PartCompoundAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartCompoundAdvancedSystemDeflection")

    class _Cast_PartCompoundAdvancedSystemDeflection:
        """Special nested class for casting PartCompoundAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
            parent: "PartCompoundAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7408.AbstractAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7408,
            )

            return self._parent._cast(
                _7408.AbstractAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7409.AbstractShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7409,
            )

            return self._parent._cast(
                _7409.AbstractShaftCompoundAdvancedSystemDeflection
            )

        @property
        def abstract_shaft_or_housing_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7410.AbstractShaftOrHousingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7410,
            )

            return self._parent._cast(
                _7410.AbstractShaftOrHousingCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7412.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7412,
            )

            return self._parent._cast(
                _7412.AGMAGleasonConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7414.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7414,
            )

            return self._parent._cast(
                _7414.AGMAGleasonConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def assembly_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7415.AssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7415,
            )

            return self._parent._cast(_7415.AssemblyCompoundAdvancedSystemDeflection)

        @property
        def bearing_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7416.BearingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7416,
            )

            return self._parent._cast(_7416.BearingCompoundAdvancedSystemDeflection)

        @property
        def belt_drive_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7418.BeltDriveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7418,
            )

            return self._parent._cast(_7418.BeltDriveCompoundAdvancedSystemDeflection)

        @property
        def bevel_differential_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7419.BevelDifferentialGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7419,
            )

            return self._parent._cast(
                _7419.BevelDifferentialGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7421.BevelDifferentialGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7421,
            )

            return self._parent._cast(
                _7421.BevelDifferentialGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7422.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7422,
            )

            return self._parent._cast(
                _7422.BevelDifferentialPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7423.BevelDifferentialSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7423,
            )

            return self._parent._cast(
                _7423.BevelDifferentialSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7424.BevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7424,
            )

            return self._parent._cast(_7424.BevelGearCompoundAdvancedSystemDeflection)

        @property
        def bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7426.BevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7426,
            )

            return self._parent._cast(
                _7426.BevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def bolt_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7427.BoltCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7427,
            )

            return self._parent._cast(_7427.BoltCompoundAdvancedSystemDeflection)

        @property
        def bolted_joint_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7428.BoltedJointCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7428,
            )

            return self._parent._cast(_7428.BoltedJointCompoundAdvancedSystemDeflection)

        @property
        def clutch_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7429.ClutchCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7429,
            )

            return self._parent._cast(_7429.ClutchCompoundAdvancedSystemDeflection)

        @property
        def clutch_half_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7431.ClutchHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7431,
            )

            return self._parent._cast(_7431.ClutchHalfCompoundAdvancedSystemDeflection)

        @property
        def component_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7433.ComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7433,
            )

            return self._parent._cast(_7433.ComponentCompoundAdvancedSystemDeflection)

        @property
        def concept_coupling_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7434.ConceptCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7434,
            )

            return self._parent._cast(
                _7434.ConceptCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def concept_coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7436.ConceptCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7436,
            )

            return self._parent._cast(
                _7436.ConceptCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def concept_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7437.ConceptGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7437,
            )

            return self._parent._cast(_7437.ConceptGearCompoundAdvancedSystemDeflection)

        @property
        def concept_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7439.ConceptGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7439,
            )

            return self._parent._cast(
                _7439.ConceptGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7440.ConicalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7440,
            )

            return self._parent._cast(_7440.ConicalGearCompoundAdvancedSystemDeflection)

        @property
        def conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7442.ConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7442,
            )

            return self._parent._cast(
                _7442.ConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def connector_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7444.ConnectorCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7444,
            )

            return self._parent._cast(_7444.ConnectorCompoundAdvancedSystemDeflection)

        @property
        def coupling_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7445.CouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7445,
            )

            return self._parent._cast(_7445.CouplingCompoundAdvancedSystemDeflection)

        @property
        def coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7447.CouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7447,
            )

            return self._parent._cast(
                _7447.CouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def cvt_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7449.CVTCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7449,
            )

            return self._parent._cast(_7449.CVTCompoundAdvancedSystemDeflection)

        @property
        def cvt_pulley_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7450.CVTPulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7450,
            )

            return self._parent._cast(_7450.CVTPulleyCompoundAdvancedSystemDeflection)

        @property
        def cycloidal_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7451.CycloidalAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7451,
            )

            return self._parent._cast(
                _7451.CycloidalAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def cycloidal_disc_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7453.CycloidalDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7453,
            )

            return self._parent._cast(
                _7453.CycloidalDiscCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7455.CylindricalGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7455,
            )

            return self._parent._cast(
                _7455.CylindricalGearCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7457.CylindricalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7457,
            )

            return self._parent._cast(
                _7457.CylindricalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def cylindrical_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7458.CylindricalPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7458,
            )

            return self._parent._cast(
                _7458.CylindricalPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def datum_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7459.DatumCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7459,
            )

            return self._parent._cast(_7459.DatumCompoundAdvancedSystemDeflection)

        @property
        def external_cad_model_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7460.ExternalCADModelCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7460,
            )

            return self._parent._cast(
                _7460.ExternalCADModelCompoundAdvancedSystemDeflection
            )

        @property
        def face_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7461.FaceGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7461,
            )

            return self._parent._cast(_7461.FaceGearCompoundAdvancedSystemDeflection)

        @property
        def face_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7463.FaceGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7463,
            )

            return self._parent._cast(_7463.FaceGearSetCompoundAdvancedSystemDeflection)

        @property
        def fe_part_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7464.FEPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7464,
            )

            return self._parent._cast(_7464.FEPartCompoundAdvancedSystemDeflection)

        @property
        def flexible_pin_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7465.FlexiblePinAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7465,
            )

            return self._parent._cast(
                _7465.FlexiblePinAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7466.GearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7466,
            )

            return self._parent._cast(_7466.GearCompoundAdvancedSystemDeflection)

        @property
        def gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7468.GearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7468,
            )

            return self._parent._cast(_7468.GearSetCompoundAdvancedSystemDeflection)

        @property
        def guide_dxf_model_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7469.GuideDxfModelCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7469,
            )

            return self._parent._cast(
                _7469.GuideDxfModelCompoundAdvancedSystemDeflection
            )

        @property
        def hypoid_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7470.HypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7470,
            )

            return self._parent._cast(_7470.HypoidGearCompoundAdvancedSystemDeflection)

        @property
        def hypoid_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7472.HypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7472,
            )

            return self._parent._cast(
                _7472.HypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> (
            "_7474.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection"
        ):
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7474,
            )

            return self._parent._cast(
                _7474.KlingelnbergCycloPalloidConicalGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7476.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7476,
            )

            return self._parent._cast(
                _7476.KlingelnbergCycloPalloidConicalGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7477.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7477,
            )

            return self._parent._cast(
                _7477.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7479.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7479,
            )

            return self._parent._cast(
                _7479.KlingelnbergCycloPalloidHypoidGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7480.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7480,
            )

            return self._parent._cast(
                _7480.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7482.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7482,
            )

            return self._parent._cast(
                _7482.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def mass_disc_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7483.MassDiscCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7483,
            )

            return self._parent._cast(_7483.MassDiscCompoundAdvancedSystemDeflection)

        @property
        def measurement_component_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7484.MeasurementComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7484,
            )

            return self._parent._cast(
                _7484.MeasurementComponentCompoundAdvancedSystemDeflection
            )

        @property
        def mountable_component_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7485.MountableComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7485,
            )

            return self._parent._cast(
                _7485.MountableComponentCompoundAdvancedSystemDeflection
            )

        @property
        def oil_seal_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7486.OilSealCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7486,
            )

            return self._parent._cast(_7486.OilSealCompoundAdvancedSystemDeflection)

        @property
        def part_to_part_shear_coupling_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7488.PartToPartShearCouplingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7488,
            )

            return self._parent._cast(
                _7488.PartToPartShearCouplingCompoundAdvancedSystemDeflection
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7490.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7490,
            )

            return self._parent._cast(
                _7490.PartToPartShearCouplingHalfCompoundAdvancedSystemDeflection
            )

        @property
        def planetary_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7492.PlanetaryGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7492,
            )

            return self._parent._cast(
                _7492.PlanetaryGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def planet_carrier_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7493.PlanetCarrierCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7493,
            )

            return self._parent._cast(
                _7493.PlanetCarrierCompoundAdvancedSystemDeflection
            )

        @property
        def point_load_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7494.PointLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7494,
            )

            return self._parent._cast(_7494.PointLoadCompoundAdvancedSystemDeflection)

        @property
        def power_load_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7495.PowerLoadCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7495,
            )

            return self._parent._cast(_7495.PowerLoadCompoundAdvancedSystemDeflection)

        @property
        def pulley_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7496.PulleyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7496,
            )

            return self._parent._cast(_7496.PulleyCompoundAdvancedSystemDeflection)

        @property
        def ring_pins_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7497.RingPinsCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7497,
            )

            return self._parent._cast(_7497.RingPinsCompoundAdvancedSystemDeflection)

        @property
        def rolling_ring_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7499.RollingRingAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7499,
            )

            return self._parent._cast(
                _7499.RollingRingAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def rolling_ring_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7500.RollingRingCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7500,
            )

            return self._parent._cast(_7500.RollingRingCompoundAdvancedSystemDeflection)

        @property
        def root_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7502.RootAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7502,
            )

            return self._parent._cast(
                _7502.RootAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def shaft_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7503.ShaftCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7503,
            )

            return self._parent._cast(_7503.ShaftCompoundAdvancedSystemDeflection)

        @property
        def shaft_hub_connection_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7504.ShaftHubConnectionCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7504,
            )

            return self._parent._cast(
                _7504.ShaftHubConnectionCompoundAdvancedSystemDeflection
            )

        @property
        def specialised_assembly_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7506.SpecialisedAssemblyCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7506,
            )

            return self._parent._cast(
                _7506.SpecialisedAssemblyCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7507.SpiralBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7507,
            )

            return self._parent._cast(
                _7507.SpiralBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def spiral_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7509.SpiralBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7509,
            )

            return self._parent._cast(
                _7509.SpiralBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7510.SpringDamperCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7510,
            )

            return self._parent._cast(
                _7510.SpringDamperCompoundAdvancedSystemDeflection
            )

        @property
        def spring_damper_half_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7512.SpringDamperHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7512,
            )

            return self._parent._cast(
                _7512.SpringDamperHalfCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7513.StraightBevelDiffGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7513,
            )

            return self._parent._cast(
                _7513.StraightBevelDiffGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_diff_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7515.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7515,
            )

            return self._parent._cast(
                _7515.StraightBevelDiffGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7516.StraightBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7516,
            )

            return self._parent._cast(
                _7516.StraightBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7518.StraightBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7518,
            )

            return self._parent._cast(
                _7518.StraightBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7519.StraightBevelPlanetGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7519,
            )

            return self._parent._cast(
                _7519.StraightBevelPlanetGearCompoundAdvancedSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7520.StraightBevelSunGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7520,
            )

            return self._parent._cast(
                _7520.StraightBevelSunGearCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7521.SynchroniserCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7521,
            )

            return self._parent._cast(
                _7521.SynchroniserCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_half_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7522.SynchroniserHalfCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7522,
            )

            return self._parent._cast(
                _7522.SynchroniserHalfCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_part_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7523.SynchroniserPartCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7523,
            )

            return self._parent._cast(
                _7523.SynchroniserPartCompoundAdvancedSystemDeflection
            )

        @property
        def synchroniser_sleeve_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7524.SynchroniserSleeveCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7524,
            )

            return self._parent._cast(
                _7524.SynchroniserSleeveCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7525.TorqueConverterCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7525,
            )

            return self._parent._cast(
                _7525.TorqueConverterCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_pump_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7527.TorqueConverterPumpCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7527,
            )

            return self._parent._cast(
                _7527.TorqueConverterPumpCompoundAdvancedSystemDeflection
            )

        @property
        def torque_converter_turbine_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7528.TorqueConverterTurbineCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7528,
            )

            return self._parent._cast(
                _7528.TorqueConverterTurbineCompoundAdvancedSystemDeflection
            )

        @property
        def unbalanced_mass_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7529.UnbalancedMassCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7529,
            )

            return self._parent._cast(
                _7529.UnbalancedMassCompoundAdvancedSystemDeflection
            )

        @property
        def virtual_component_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7530.VirtualComponentCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7530,
            )

            return self._parent._cast(
                _7530.VirtualComponentCompoundAdvancedSystemDeflection
            )

        @property
        def worm_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7531.WormGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7531,
            )

            return self._parent._cast(_7531.WormGearCompoundAdvancedSystemDeflection)

        @property
        def worm_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7533.WormGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7533,
            )

            return self._parent._cast(_7533.WormGearSetCompoundAdvancedSystemDeflection)

        @property
        def zerol_bevel_gear_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7534.ZerolBevelGearCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7534,
            )

            return self._parent._cast(
                _7534.ZerolBevelGearCompoundAdvancedSystemDeflection
            )

        @property
        def zerol_bevel_gear_set_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "_7536.ZerolBevelGearSetCompoundAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections.compound import (
                _7536,
            )

            return self._parent._cast(
                _7536.ZerolBevelGearSetCompoundAdvancedSystemDeflection
            )

        @property
        def part_compound_advanced_system_deflection(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
        ) -> "PartCompoundAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "PartCompoundAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7357.PartAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PartAdvancedSystemDeflection]

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
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7357.PartAdvancedSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.advanced_system_deflections.PartAdvancedSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "PartCompoundAdvancedSystemDeflection._Cast_PartCompoundAdvancedSystemDeflection":
        return self._Cast_PartCompoundAdvancedSystemDeflection(self)
