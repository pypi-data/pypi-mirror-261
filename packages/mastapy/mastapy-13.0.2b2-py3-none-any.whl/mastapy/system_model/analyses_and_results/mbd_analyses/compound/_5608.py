"""MountableComponentCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5556
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "MountableComponentCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5466
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5535,
        _5539,
        _5542,
        _5545,
        _5546,
        _5547,
        _5554,
        _5559,
        _5560,
        _5563,
        _5567,
        _5570,
        _5573,
        _5578,
        _5581,
        _5584,
        _5589,
        _5593,
        _5597,
        _5600,
        _5603,
        _5606,
        _5607,
        _5609,
        _5613,
        _5616,
        _5617,
        _5618,
        _5619,
        _5620,
        _5623,
        _5627,
        _5630,
        _5635,
        _5636,
        _5639,
        _5642,
        _5643,
        _5645,
        _5646,
        _5647,
        _5650,
        _5651,
        _5652,
        _5653,
        _5654,
        _5657,
        _5610,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="MountableComponentCompoundMultibodyDynamicsAnalysis")


class MountableComponentCompoundMultibodyDynamicsAnalysis(
    _5556.ComponentCompoundMultibodyDynamicsAnalysis
):
    """MountableComponentCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_MountableComponentCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting MountableComponentCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
            parent: "MountableComponentCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5556.ComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5556.ComponentCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5610.PartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5610,
            )

            return self._parent._cast(_5610.PartCompoundMultibodyDynamicsAnalysis)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5535.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5535,
            )

            return self._parent._cast(
                _5535.AGMAGleasonConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bearing_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5539.BearingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5539,
            )

            return self._parent._cast(_5539.BearingCompoundMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5542.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5542,
            )

            return self._parent._cast(
                _5542.BevelDifferentialGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5545.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5545,
            )

            return self._parent._cast(
                _5545.BevelDifferentialPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5546.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5546,
            )

            return self._parent._cast(
                _5546.BevelDifferentialSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5547.BevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5547,
            )

            return self._parent._cast(_5547.BevelGearCompoundMultibodyDynamicsAnalysis)

        @property
        def clutch_half_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5554.ClutchHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5554,
            )

            return self._parent._cast(_5554.ClutchHalfCompoundMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5559.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5559,
            )

            return self._parent._cast(
                _5559.ConceptCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5560.ConceptGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5560,
            )

            return self._parent._cast(
                _5560.ConceptGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5563.ConicalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5563,
            )

            return self._parent._cast(
                _5563.ConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connector_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5567.ConnectorCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5567,
            )

            return self._parent._cast(_5567.ConnectorCompoundMultibodyDynamicsAnalysis)

        @property
        def coupling_half_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5570.CouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5570,
            )

            return self._parent._cast(
                _5570.CouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cvt_pulley_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5573.CVTPulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5573,
            )

            return self._parent._cast(_5573.CVTPulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5578.CylindricalGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5578,
            )

            return self._parent._cast(
                _5578.CylindricalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_planet_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5581.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5581,
            )

            return self._parent._cast(
                _5581.CylindricalPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5584.FaceGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5584,
            )

            return self._parent._cast(_5584.FaceGearCompoundMultibodyDynamicsAnalysis)

        @property
        def gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5589.GearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5589,
            )

            return self._parent._cast(_5589.GearCompoundMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5593.HypoidGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5593,
            )

            return self._parent._cast(_5593.HypoidGearCompoundMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5597.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5597,
            )

            return self._parent._cast(
                _5597.KlingelnbergCycloPalloidConicalGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> (
            "_5600.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5600,
            )

            return self._parent._cast(
                _5600.KlingelnbergCycloPalloidHypoidGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5603.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5603,
            )

            return self._parent._cast(
                _5603.KlingelnbergCycloPalloidSpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5606.MassDiscCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5606,
            )

            return self._parent._cast(_5606.MassDiscCompoundMultibodyDynamicsAnalysis)

        @property
        def measurement_component_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5607.MeasurementComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5607,
            )

            return self._parent._cast(
                _5607.MeasurementComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5609.OilSealCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5609,
            )

            return self._parent._cast(_5609.OilSealCompoundMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5613.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5613,
            )

            return self._parent._cast(
                _5613.PartToPartShearCouplingHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5616.PlanetCarrierCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5616,
            )

            return self._parent._cast(
                _5616.PlanetCarrierCompoundMultibodyDynamicsAnalysis
            )

        @property
        def point_load_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5617.PointLoadCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5617,
            )

            return self._parent._cast(_5617.PointLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def power_load_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5618.PowerLoadCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5618,
            )

            return self._parent._cast(_5618.PowerLoadCompoundMultibodyDynamicsAnalysis)

        @property
        def pulley_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5619.PulleyCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5619,
            )

            return self._parent._cast(_5619.PulleyCompoundMultibodyDynamicsAnalysis)

        @property
        def ring_pins_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5620.RingPinsCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5620,
            )

            return self._parent._cast(_5620.RingPinsCompoundMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5623.RollingRingCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5623,
            )

            return self._parent._cast(
                _5623.RollingRingCompoundMultibodyDynamicsAnalysis
            )

        @property
        def shaft_hub_connection_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5627.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5627,
            )

            return self._parent._cast(
                _5627.ShaftHubConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5630.SpiralBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5630,
            )

            return self._parent._cast(
                _5630.SpiralBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_half_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5635.SpringDamperHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5635,
            )

            return self._parent._cast(
                _5635.SpringDamperHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5636.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5636,
            )

            return self._parent._cast(
                _5636.StraightBevelDiffGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5639.StraightBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5639,
            )

            return self._parent._cast(
                _5639.StraightBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5642.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5642,
            )

            return self._parent._cast(
                _5642.StraightBevelPlanetGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5643.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5643,
            )

            return self._parent._cast(
                _5643.StraightBevelSunGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5645.SynchroniserHalfCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5645,
            )

            return self._parent._cast(
                _5645.SynchroniserHalfCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_part_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5646.SynchroniserPartCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5646,
            )

            return self._parent._cast(
                _5646.SynchroniserPartCompoundMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_sleeve_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5647.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5647,
            )

            return self._parent._cast(
                _5647.SynchroniserSleeveCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_pump_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5650.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5650,
            )

            return self._parent._cast(
                _5650.TorqueConverterPumpCompoundMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5651.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5651,
            )

            return self._parent._cast(
                _5651.TorqueConverterTurbineCompoundMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5652.UnbalancedMassCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5652,
            )

            return self._parent._cast(
                _5652.UnbalancedMassCompoundMultibodyDynamicsAnalysis
            )

        @property
        def virtual_component_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5653.VirtualComponentCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5653,
            )

            return self._parent._cast(
                _5653.VirtualComponentCompoundMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5654.WormGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5654,
            )

            return self._parent._cast(_5654.WormGearCompoundMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "_5657.ZerolBevelGearCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5657,
            )

            return self._parent._cast(
                _5657.ZerolBevelGearCompoundMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_compound_multibody_dynamics_analysis(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
        ) -> "MountableComponentCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "MountableComponentCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_5466.MountableComponentMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.MountableComponentMultibodyDynamicsAnalysis]

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
    ) -> "List[_5466.MountableComponentMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.MountableComponentMultibodyDynamicsAnalysis]

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
    ) -> "MountableComponentCompoundMultibodyDynamicsAnalysis._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis":
        return self._Cast_MountableComponentCompoundMultibodyDynamicsAnalysis(self)
