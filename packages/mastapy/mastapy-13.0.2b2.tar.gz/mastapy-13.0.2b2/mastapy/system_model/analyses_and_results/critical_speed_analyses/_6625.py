"""MountableComponentCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6570
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "MountableComponentCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6549,
        _6553,
        _6556,
        _6559,
        _6560,
        _6561,
        _6568,
        _6573,
        _6574,
        _6577,
        _6581,
        _6584,
        _6590,
        _6595,
        _6598,
        _6601,
        _6606,
        _6610,
        _6614,
        _6617,
        _6620,
        _6623,
        _6624,
        _6626,
        _6630,
        _6633,
        _6634,
        _6635,
        _6636,
        _6637,
        _6641,
        _6644,
        _6647,
        _6652,
        _6653,
        _6656,
        _6659,
        _6660,
        _6662,
        _6663,
        _6664,
        _6667,
        _6668,
        _6669,
        _6670,
        _6671,
        _6674,
        _6627,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="MountableComponentCriticalSpeedAnalysis")


class MountableComponentCriticalSpeedAnalysis(_6570.ComponentCriticalSpeedAnalysis):
    """MountableComponentCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCriticalSpeedAnalysis"
    )

    class _Cast_MountableComponentCriticalSpeedAnalysis:
        """Special nested class for casting MountableComponentCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
            parent: "MountableComponentCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def component_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6570.ComponentCriticalSpeedAnalysis":
            return self._parent._cast(_6570.ComponentCriticalSpeedAnalysis)

        @property
        def part_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6627.PartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6627,
            )

            return self._parent._cast(_6627.PartCriticalSpeedAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6549.AGMAGleasonConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6549,
            )

            return self._parent._cast(_6549.AGMAGleasonConicalGearCriticalSpeedAnalysis)

        @property
        def bearing_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6553.BearingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6553,
            )

            return self._parent._cast(_6553.BearingCriticalSpeedAnalysis)

        @property
        def bevel_differential_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6556.BevelDifferentialGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6556,
            )

            return self._parent._cast(_6556.BevelDifferentialGearCriticalSpeedAnalysis)

        @property
        def bevel_differential_planet_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6559.BevelDifferentialPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6559,
            )

            return self._parent._cast(
                _6559.BevelDifferentialPlanetGearCriticalSpeedAnalysis
            )

        @property
        def bevel_differential_sun_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6560.BevelDifferentialSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6560,
            )

            return self._parent._cast(
                _6560.BevelDifferentialSunGearCriticalSpeedAnalysis
            )

        @property
        def bevel_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6561.BevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6561,
            )

            return self._parent._cast(_6561.BevelGearCriticalSpeedAnalysis)

        @property
        def clutch_half_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6568.ClutchHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6568,
            )

            return self._parent._cast(_6568.ClutchHalfCriticalSpeedAnalysis)

        @property
        def concept_coupling_half_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6573.ConceptCouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6573,
            )

            return self._parent._cast(_6573.ConceptCouplingHalfCriticalSpeedAnalysis)

        @property
        def concept_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6574.ConceptGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6574,
            )

            return self._parent._cast(_6574.ConceptGearCriticalSpeedAnalysis)

        @property
        def conical_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6577.ConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6577,
            )

            return self._parent._cast(_6577.ConicalGearCriticalSpeedAnalysis)

        @property
        def connector_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6581.ConnectorCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6581,
            )

            return self._parent._cast(_6581.ConnectorCriticalSpeedAnalysis)

        @property
        def coupling_half_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6584.CouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6584,
            )

            return self._parent._cast(_6584.CouplingHalfCriticalSpeedAnalysis)

        @property
        def cvt_pulley_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6590.CVTPulleyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6590,
            )

            return self._parent._cast(_6590.CVTPulleyCriticalSpeedAnalysis)

        @property
        def cylindrical_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6595.CylindricalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6595,
            )

            return self._parent._cast(_6595.CylindricalGearCriticalSpeedAnalysis)

        @property
        def cylindrical_planet_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6598.CylindricalPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6598,
            )

            return self._parent._cast(_6598.CylindricalPlanetGearCriticalSpeedAnalysis)

        @property
        def face_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6601.FaceGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6601,
            )

            return self._parent._cast(_6601.FaceGearCriticalSpeedAnalysis)

        @property
        def gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6606.GearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6606,
            )

            return self._parent._cast(_6606.GearCriticalSpeedAnalysis)

        @property
        def hypoid_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6610.HypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6610,
            )

            return self._parent._cast(_6610.HypoidGearCriticalSpeedAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6614.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6614,
            )

            return self._parent._cast(
                _6614.KlingelnbergCycloPalloidConicalGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6617.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6617,
            )

            return self._parent._cast(
                _6617.KlingelnbergCycloPalloidHypoidGearCriticalSpeedAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6620.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6620,
            )

            return self._parent._cast(
                _6620.KlingelnbergCycloPalloidSpiralBevelGearCriticalSpeedAnalysis
            )

        @property
        def mass_disc_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6623.MassDiscCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6623,
            )

            return self._parent._cast(_6623.MassDiscCriticalSpeedAnalysis)

        @property
        def measurement_component_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6624.MeasurementComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6624,
            )

            return self._parent._cast(_6624.MeasurementComponentCriticalSpeedAnalysis)

        @property
        def oil_seal_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6626.OilSealCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6626,
            )

            return self._parent._cast(_6626.OilSealCriticalSpeedAnalysis)

        @property
        def part_to_part_shear_coupling_half_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6630.PartToPartShearCouplingHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6630,
            )

            return self._parent._cast(
                _6630.PartToPartShearCouplingHalfCriticalSpeedAnalysis
            )

        @property
        def planet_carrier_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6633.PlanetCarrierCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6633,
            )

            return self._parent._cast(_6633.PlanetCarrierCriticalSpeedAnalysis)

        @property
        def point_load_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6634.PointLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6634,
            )

            return self._parent._cast(_6634.PointLoadCriticalSpeedAnalysis)

        @property
        def power_load_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6635.PowerLoadCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6635,
            )

            return self._parent._cast(_6635.PowerLoadCriticalSpeedAnalysis)

        @property
        def pulley_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6636.PulleyCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6636,
            )

            return self._parent._cast(_6636.PulleyCriticalSpeedAnalysis)

        @property
        def ring_pins_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6637.RingPinsCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6637,
            )

            return self._parent._cast(_6637.RingPinsCriticalSpeedAnalysis)

        @property
        def rolling_ring_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6641.RollingRingCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6641,
            )

            return self._parent._cast(_6641.RollingRingCriticalSpeedAnalysis)

        @property
        def shaft_hub_connection_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6644.ShaftHubConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6644,
            )

            return self._parent._cast(_6644.ShaftHubConnectionCriticalSpeedAnalysis)

        @property
        def spiral_bevel_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6647.SpiralBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6647,
            )

            return self._parent._cast(_6647.SpiralBevelGearCriticalSpeedAnalysis)

        @property
        def spring_damper_half_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6652.SpringDamperHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6652,
            )

            return self._parent._cast(_6652.SpringDamperHalfCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6653.StraightBevelDiffGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6653,
            )

            return self._parent._cast(_6653.StraightBevelDiffGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6656.StraightBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6656,
            )

            return self._parent._cast(_6656.StraightBevelGearCriticalSpeedAnalysis)

        @property
        def straight_bevel_planet_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6659.StraightBevelPlanetGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6659,
            )

            return self._parent._cast(
                _6659.StraightBevelPlanetGearCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_sun_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6660.StraightBevelSunGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6660,
            )

            return self._parent._cast(_6660.StraightBevelSunGearCriticalSpeedAnalysis)

        @property
        def synchroniser_half_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6662.SynchroniserHalfCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6662,
            )

            return self._parent._cast(_6662.SynchroniserHalfCriticalSpeedAnalysis)

        @property
        def synchroniser_part_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6663.SynchroniserPartCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6663,
            )

            return self._parent._cast(_6663.SynchroniserPartCriticalSpeedAnalysis)

        @property
        def synchroniser_sleeve_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6664.SynchroniserSleeveCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6664,
            )

            return self._parent._cast(_6664.SynchroniserSleeveCriticalSpeedAnalysis)

        @property
        def torque_converter_pump_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6667.TorqueConverterPumpCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6667,
            )

            return self._parent._cast(_6667.TorqueConverterPumpCriticalSpeedAnalysis)

        @property
        def torque_converter_turbine_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6668.TorqueConverterTurbineCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6668,
            )

            return self._parent._cast(_6668.TorqueConverterTurbineCriticalSpeedAnalysis)

        @property
        def unbalanced_mass_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6669.UnbalancedMassCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6669,
            )

            return self._parent._cast(_6669.UnbalancedMassCriticalSpeedAnalysis)

        @property
        def virtual_component_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6670.VirtualComponentCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6670,
            )

            return self._parent._cast(_6670.VirtualComponentCriticalSpeedAnalysis)

        @property
        def worm_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6671.WormGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6671,
            )

            return self._parent._cast(_6671.WormGearCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "_6674.ZerolBevelGearCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6674,
            )

            return self._parent._cast(_6674.ZerolBevelGearCriticalSpeedAnalysis)

        @property
        def mountable_component_critical_speed_analysis(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
        ) -> "MountableComponentCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentCriticalSpeedAnalysis.TYPE"
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
    ) -> "MountableComponentCriticalSpeedAnalysis._Cast_MountableComponentCriticalSpeedAnalysis":
        return self._Cast_MountableComponentCriticalSpeedAnalysis(self)
