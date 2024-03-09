"""MountableComponentMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5406
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "MountableComponentMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5383,
        _5387,
        _5392,
        _5394,
        _5395,
        _5397,
        _5402,
        _5408,
        _5411,
        _5414,
        _5417,
        _5419,
        _5423,
        _5429,
        _5431,
        _5435,
        _5441,
        _5445,
        _5453,
        _5456,
        _5459,
        _5461,
        _5465,
        _5468,
        _5471,
        _5475,
        _5476,
        _5477,
        _5478,
        _5479,
        _5483,
        _5487,
        _5493,
        _5496,
        _5499,
        _5502,
        _5504,
        _5505,
        _5506,
        _5508,
        _5509,
        _5513,
        _5515,
        _5516,
        _5517,
        _5520,
        _5523,
        _5469,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7551, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="MountableComponentMultibodyDynamicsAnalysis")


class MountableComponentMultibodyDynamicsAnalysis(
    _5406.ComponentMultibodyDynamicsAnalysis
):
    """MountableComponentMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentMultibodyDynamicsAnalysis"
    )

    class _Cast_MountableComponentMultibodyDynamicsAnalysis:
        """Special nested class for casting MountableComponentMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
            parent: "MountableComponentMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def component_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5406.ComponentMultibodyDynamicsAnalysis":
            return self._parent._cast(_5406.ComponentMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5469.PartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5469

            return self._parent._cast(_5469.PartMultibodyDynamicsAnalysis)

        @property
        def part_time_series_load_analysis_case(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_7551.PartTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7551

            return self._parent._cast(_7551.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5383.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5383

            return self._parent._cast(
                _5383.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def bearing_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5387.BearingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(_5387.BearingMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5392.BevelDifferentialGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(
                _5392.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5394.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394

            return self._parent._cast(
                _5394.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5395.BevelDifferentialSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395

            return self._parent._cast(
                _5395.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5397.BevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.BevelGearMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5402.ClutchHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402

            return self._parent._cast(_5402.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5408.ConceptCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408

            return self._parent._cast(
                _5408.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5411.ConceptGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5414.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5417.ConnectorMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(_5417.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5419.CouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5423.CVTPulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423

            return self._parent._cast(_5423.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5429.CylindricalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429

            return self._parent._cast(_5429.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5431.CylindricalPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(
                _5431.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5435.FaceGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.FaceGearMultibodyDynamicsAnalysis)

        @property
        def gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5441.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.GearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5445.HypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(_5445.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5453.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5456.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5456

            return self._parent._cast(
                _5456.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5459.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459

            return self._parent._cast(
                _5459.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5461.MassDiscMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5465.MeasurementComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465

            return self._parent._cast(
                _5465.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5468.OilSealMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(_5468.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5471.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(
                _5471.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def planet_carrier_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5475.PlanetCarrierMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5476.PointLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(_5476.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5477.PowerLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477

            return self._parent._cast(_5477.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5478.PulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(_5478.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5479.RingPinsMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(_5479.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5483.RollingRingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483

            return self._parent._cast(_5483.RollingRingMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5487.ShaftHubConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(_5487.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5493.SpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(_5493.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5496.SpringDamperHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(_5496.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5499.StraightBevelDiffGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5502.StraightBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5502

            return self._parent._cast(_5502.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5504.StraightBevelPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(
                _5504.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5505.StraightBevelSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(
                _5505.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5506.SynchroniserHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(_5506.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5508.SynchroniserPartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(_5508.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5509.SynchroniserSleeveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5509

            return self._parent._cast(_5509.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5513.TorqueConverterPumpMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(
                _5513.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5515.TorqueConverterTurbineMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(
                _5515.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5516.UnbalancedMassMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5517.VirtualComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(_5517.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5520.WormGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5520

            return self._parent._cast(_5520.WormGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "_5523.ZerolBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5523

            return self._parent._cast(_5523.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
        ) -> "MountableComponentMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2466.MountableComponent":
        """mastapy.system_model.part_model.MountableComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentMultibodyDynamicsAnalysis._Cast_MountableComponentMultibodyDynamicsAnalysis":
        return self._Cast_MountableComponentMultibodyDynamicsAnalysis(self)
