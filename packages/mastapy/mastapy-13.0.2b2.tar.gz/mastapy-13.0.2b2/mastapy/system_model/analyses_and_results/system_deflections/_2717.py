"""ComponentSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2787
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "ComponentSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446
    from mastapy.math_utility import _1520
    from mastapy.materials.efficiency import _302, _303
    from mastapy.system_model.analyses_and_results.system_deflections.reporting import (
        _2850,
    )
    from mastapy.math_utility.measured_vectors import _1563, _1564
    from mastapy.system_model.analyses_and_results.power_flows import _4059
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2688,
        _2689,
        _2693,
        _2700,
        _2705,
        _2706,
        _2707,
        _2710,
        _2712,
        _2714,
        _2720,
        _2724,
        _2728,
        _2730,
        _2732,
        _2735,
        _2740,
        _2747,
        _2748,
        _2749,
        _2752,
        _2753,
        _2754,
        _2758,
        _2759,
        _2763,
        _2764,
        _2767,
        _2772,
        _2775,
        _2778,
        _2781,
        _2782,
        _2784,
        _2786,
        _2789,
        _2792,
        _2793,
        _2794,
        _2795,
        _2796,
        _2801,
        _2803,
        _2806,
        _2811,
        _2813,
        _2817,
        _2820,
        _2821,
        _2822,
        _2823,
        _2824,
        _2825,
        _2831,
        _2833,
        _2836,
        _2837,
        _2840,
        _2843,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ComponentSystemDeflection",)


Self = TypeVar("Self", bound="ComponentSystemDeflection")


class ComponentSystemDeflection(_2787.PartSystemDeflection):
    """ComponentSystemDeflection

    This is a mastapy class.
    """

    TYPE = _COMPONENT_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentSystemDeflection")

    class _Cast_ComponentSystemDeflection:
        """Special nested class for casting ComponentSystemDeflection to subclasses."""

        def __init__(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
            parent: "ComponentSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2787.PartSystemDeflection":
            return self._parent._cast(_2787.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2688.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2689.AbstractShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2693.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2693,
            )

            return self._parent._cast(_2693.AGMAGleasonConicalGearSystemDeflection)

        @property
        def bearing_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2700.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BearingSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2705.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2706.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2707.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2710.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.BevelGearSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2712.BoltSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2714.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.ClutchHalfSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2720.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2724.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConceptGearSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2728.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2730.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2732.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CouplingHalfSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2735.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.CVTPulleySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2740.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2747.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2748.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2749.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(
                _2749.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2752.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2753.DatumSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2754.ExternalCADModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.ExternalCADModelSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2758.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2759.FEPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.FEPartSystemDeflection)

        @property
        def gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2763.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2764.GuideDxfModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2767.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(_2767.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2772.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2775.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2778.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(
                _2778.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2781.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2782.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2784.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2786.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2789.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2792.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2793.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2794.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(_2794.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2795.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2796.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.RingPinsSystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2801.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.RollingRingSystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2803.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2806.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.ShaftSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2811.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2813.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.SpringDamperHalfSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2817.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2820.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2821.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2822.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2823.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2824.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2825.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.SynchroniserSleeveSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2831.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2833.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2836.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2837.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.VirtualComponentSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2840.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "_2843.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.ZerolBevelGearSystemDeflection)

        @property
        def component_system_deflection(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection",
        ) -> "ComponentSystemDeflection":
            return self._parent

        def __getattr__(
            self: "ComponentSystemDeflection._Cast_ComponentSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def energy_loss_during_load_case(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.EnergyLossDuringLoadCase

        if temp is None:
            return 0.0

        return temp

    @property
    def has_converged(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HasConverged

        if temp is None:
            return False

        return temp

    @property
    def percentage_of_iterations_converged(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PercentageOfIterationsConverged

        if temp is None:
            return 0.0

        return temp

    @property
    def reason_for_non_convergence(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonForNonConvergence

        if temp is None:
            return ""

        return temp

    @property
    def reason_mass_properties_are_unknown(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonMassPropertiesAreUnknown

        if temp is None:
            return ""

        return temp

    @property
    def reason_mass_properties_are_zero(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ReasonMassPropertiesAreZero

        if temp is None:
            return ""

        return temp

    @property
    def relaxation(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Relaxation

        if temp is None:
            return 0.0

        return temp

    @property
    def speed(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Speed

        if temp is None:
            return 0.0

        return temp

    @property
    def component_design(self: Self) -> "_2446.Component":
        """mastapy.system_model.part_model.Component

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def mass_properties_in_local_coordinate_system_from_node_model(
        self: Self,
    ) -> "_1520.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesInLocalCoordinateSystemFromNodeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_loss(self: Self) -> "_302.PowerLoss":
        """mastapy.materials.efficiency.PowerLoss

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerLoss

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def resistive_torque(self: Self) -> "_303.ResistiveTorque":
        """mastapy.materials.efficiency.ResistiveTorque

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResistiveTorque

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rigidly_connected_components(
        self: Self,
    ) -> "_2850.RigidlyConnectedComponentGroupSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.reporting.RigidlyConnectedComponentGroupSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.RigidlyConnectedComponents

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connected_components_forces_in_lcs(self: Self) -> "List[_1563.ForceResults]":
        """List[mastapy.math_utility.measured_vectors.ForceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponentsForcesInLCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connected_components_forces_in_wcs(self: Self) -> "List[_1563.ForceResults]":
        """List[mastapy.math_utility.measured_vectors.ForceResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectedComponentsForcesInWCS

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def node_results(self: Self) -> "List[_1564.NodeResults]":
        """List[mastapy.math_utility.measured_vectors.NodeResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NodeResults

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def power_flow_results(self: Self) -> "_4059.ComponentPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.ComponentPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ComponentSystemDeflection._Cast_ComponentSystemDeflection":
        return self._Cast_ComponentSystemDeflection(self)
