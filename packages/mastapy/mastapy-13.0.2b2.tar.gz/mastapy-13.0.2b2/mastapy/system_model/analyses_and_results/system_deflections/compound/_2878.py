"""ComponentCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2933
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "ComponentCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2717
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2854,
        _2855,
        _2857,
        _2861,
        _2864,
        _2867,
        _2868,
        _2869,
        _2872,
        _2876,
        _2881,
        _2882,
        _2885,
        _2889,
        _2892,
        _2895,
        _2898,
        _2900,
        _2903,
        _2904,
        _2906,
        _2907,
        _2910,
        _2912,
        _2915,
        _2916,
        _2920,
        _2923,
        _2926,
        _2929,
        _2930,
        _2931,
        _2932,
        _2936,
        _2939,
        _2940,
        _2941,
        _2942,
        _2943,
        _2946,
        _2949,
        _2951,
        _2954,
        _2959,
        _2960,
        _2963,
        _2966,
        _2967,
        _2969,
        _2970,
        _2971,
        _2974,
        _2975,
        _2976,
        _2977,
        _2978,
        _2981,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("ComponentCompoundSystemDeflection",)


Self = TypeVar("Self", bound="ComponentCompoundSystemDeflection")


class ComponentCompoundSystemDeflection(_2933.PartCompoundSystemDeflection):
    """ComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentCompoundSystemDeflection")

    class _Cast_ComponentCompoundSystemDeflection:
        """Special nested class for casting ComponentCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
            parent: "ComponentCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2933.PartCompoundSystemDeflection":
            return self._parent._cast(_2933.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2854.AbstractShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2854,
            )

            return self._parent._cast(_2854.AbstractShaftCompoundSystemDeflection)

        @property
        def abstract_shaft_or_housing_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2855.AbstractShaftOrHousingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2855,
            )

            return self._parent._cast(
                _2855.AbstractShaftOrHousingCompoundSystemDeflection
            )

        @property
        def agma_gleason_conical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2857.AGMAGleasonConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2857,
            )

            return self._parent._cast(
                _2857.AGMAGleasonConicalGearCompoundSystemDeflection
            )

        @property
        def bearing_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2861.BearingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2861,
            )

            return self._parent._cast(_2861.BearingCompoundSystemDeflection)

        @property
        def bevel_differential_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2864.BevelDifferentialGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2864,
            )

            return self._parent._cast(
                _2864.BevelDifferentialGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_planet_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2867.BevelDifferentialPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2867,
            )

            return self._parent._cast(
                _2867.BevelDifferentialPlanetGearCompoundSystemDeflection
            )

        @property
        def bevel_differential_sun_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2868.BevelDifferentialSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2868,
            )

            return self._parent._cast(
                _2868.BevelDifferentialSunGearCompoundSystemDeflection
            )

        @property
        def bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2869.BevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2869,
            )

            return self._parent._cast(_2869.BevelGearCompoundSystemDeflection)

        @property
        def bolt_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2872.BoltCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2872,
            )

            return self._parent._cast(_2872.BoltCompoundSystemDeflection)

        @property
        def clutch_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2876.ClutchHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2876,
            )

            return self._parent._cast(_2876.ClutchHalfCompoundSystemDeflection)

        @property
        def concept_coupling_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2881.ConceptCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2881,
            )

            return self._parent._cast(_2881.ConceptCouplingHalfCompoundSystemDeflection)

        @property
        def concept_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2882.ConceptGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2882,
            )

            return self._parent._cast(_2882.ConceptGearCompoundSystemDeflection)

        @property
        def conical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2885.ConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2885,
            )

            return self._parent._cast(_2885.ConicalGearCompoundSystemDeflection)

        @property
        def connector_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2889.ConnectorCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2889,
            )

            return self._parent._cast(_2889.ConnectorCompoundSystemDeflection)

        @property
        def coupling_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2892.CouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2892,
            )

            return self._parent._cast(_2892.CouplingHalfCompoundSystemDeflection)

        @property
        def cvt_pulley_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2895.CVTPulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2895,
            )

            return self._parent._cast(_2895.CVTPulleyCompoundSystemDeflection)

        @property
        def cycloidal_disc_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2898.CycloidalDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2898,
            )

            return self._parent._cast(_2898.CycloidalDiscCompoundSystemDeflection)

        @property
        def cylindrical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2900.CylindricalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2900,
            )

            return self._parent._cast(_2900.CylindricalGearCompoundSystemDeflection)

        @property
        def cylindrical_planet_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2903.CylindricalPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2903,
            )

            return self._parent._cast(
                _2903.CylindricalPlanetGearCompoundSystemDeflection
            )

        @property
        def datum_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2904.DatumCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2904,
            )

            return self._parent._cast(_2904.DatumCompoundSystemDeflection)

        @property
        def external_cad_model_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2906.ExternalCADModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2906,
            )

            return self._parent._cast(_2906.ExternalCADModelCompoundSystemDeflection)

        @property
        def face_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2907.FaceGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2907,
            )

            return self._parent._cast(_2907.FaceGearCompoundSystemDeflection)

        @property
        def fe_part_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2910.FEPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2910,
            )

            return self._parent._cast(_2910.FEPartCompoundSystemDeflection)

        @property
        def gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2912.GearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2912,
            )

            return self._parent._cast(_2912.GearCompoundSystemDeflection)

        @property
        def guide_dxf_model_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2915.GuideDxfModelCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2915,
            )

            return self._parent._cast(_2915.GuideDxfModelCompoundSystemDeflection)

        @property
        def hypoid_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2916.HypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2916,
            )

            return self._parent._cast(_2916.HypoidGearCompoundSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2920.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2920,
            )

            return self._parent._cast(
                _2920.KlingelnbergCycloPalloidConicalGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2923.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2923,
            )

            return self._parent._cast(
                _2923.KlingelnbergCycloPalloidHypoidGearCompoundSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2926.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2926,
            )

            return self._parent._cast(
                _2926.KlingelnbergCycloPalloidSpiralBevelGearCompoundSystemDeflection
            )

        @property
        def mass_disc_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2929.MassDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2930.MeasurementComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(
                _2930.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def mountable_component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2931.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.MountableComponentCompoundSystemDeflection)

        @property
        def oil_seal_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2932.OilSealCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2932,
            )

            return self._parent._cast(_2932.OilSealCompoundSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2936.PartToPartShearCouplingHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2936,
            )

            return self._parent._cast(
                _2936.PartToPartShearCouplingHalfCompoundSystemDeflection
            )

        @property
        def planet_carrier_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2939.PlanetCarrierCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2939,
            )

            return self._parent._cast(_2939.PlanetCarrierCompoundSystemDeflection)

        @property
        def point_load_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2940.PointLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(_2940.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2941.PowerLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2941,
            )

            return self._parent._cast(_2941.PowerLoadCompoundSystemDeflection)

        @property
        def pulley_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2942.PulleyCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2942,
            )

            return self._parent._cast(_2942.PulleyCompoundSystemDeflection)

        @property
        def ring_pins_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2943.RingPinsCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2943,
            )

            return self._parent._cast(_2943.RingPinsCompoundSystemDeflection)

        @property
        def rolling_ring_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2946.RollingRingCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2946,
            )

            return self._parent._cast(_2946.RollingRingCompoundSystemDeflection)

        @property
        def shaft_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2949.ShaftCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2949,
            )

            return self._parent._cast(_2949.ShaftCompoundSystemDeflection)

        @property
        def shaft_hub_connection_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2951.ShaftHubConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2951,
            )

            return self._parent._cast(_2951.ShaftHubConnectionCompoundSystemDeflection)

        @property
        def spiral_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2954.SpiralBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2954,
            )

            return self._parent._cast(_2954.SpiralBevelGearCompoundSystemDeflection)

        @property
        def spring_damper_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2959.SpringDamperHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2959,
            )

            return self._parent._cast(_2959.SpringDamperHalfCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2960.StraightBevelDiffGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2960,
            )

            return self._parent._cast(
                _2960.StraightBevelDiffGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2963.StraightBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2963,
            )

            return self._parent._cast(_2963.StraightBevelGearCompoundSystemDeflection)

        @property
        def straight_bevel_planet_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2966.StraightBevelPlanetGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2966,
            )

            return self._parent._cast(
                _2966.StraightBevelPlanetGearCompoundSystemDeflection
            )

        @property
        def straight_bevel_sun_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2967.StraightBevelSunGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2967,
            )

            return self._parent._cast(
                _2967.StraightBevelSunGearCompoundSystemDeflection
            )

        @property
        def synchroniser_half_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2969.SynchroniserHalfCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2969,
            )

            return self._parent._cast(_2969.SynchroniserHalfCompoundSystemDeflection)

        @property
        def synchroniser_part_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2970.SynchroniserPartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2970,
            )

            return self._parent._cast(_2970.SynchroniserPartCompoundSystemDeflection)

        @property
        def synchroniser_sleeve_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2971.SynchroniserSleeveCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2971,
            )

            return self._parent._cast(_2971.SynchroniserSleeveCompoundSystemDeflection)

        @property
        def torque_converter_pump_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2974.TorqueConverterPumpCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2974,
            )

            return self._parent._cast(_2974.TorqueConverterPumpCompoundSystemDeflection)

        @property
        def torque_converter_turbine_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2975.TorqueConverterTurbineCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2975,
            )

            return self._parent._cast(
                _2975.TorqueConverterTurbineCompoundSystemDeflection
            )

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2976.UnbalancedMassCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2977.VirtualComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2977,
            )

            return self._parent._cast(_2977.VirtualComponentCompoundSystemDeflection)

        @property
        def worm_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2978.WormGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2978,
            )

            return self._parent._cast(_2978.WormGearCompoundSystemDeflection)

        @property
        def zerol_bevel_gear_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "_2981.ZerolBevelGearCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2981,
            )

            return self._parent._cast(_2981.ZerolBevelGearCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
        ) -> "ComponentCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "ComponentCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(self: Self) -> "List[_2717.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

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
    ) -> "List[_2717.ComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection]

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
    ) -> "ComponentCompoundSystemDeflection._Cast_ComponentCompoundSystemDeflection":
        return self._Cast_ComponentCompoundSystemDeflection(self)
