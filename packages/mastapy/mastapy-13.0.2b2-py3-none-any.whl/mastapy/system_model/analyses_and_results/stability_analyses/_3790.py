"""ComponentStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3846
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "ComponentStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3766,
        _3767,
        _3771,
        _3773,
        _3778,
        _3779,
        _3780,
        _3783,
        _3785,
        _3787,
        _3792,
        _3796,
        _3799,
        _3801,
        _3803,
        _3807,
        _3812,
        _3815,
        _3816,
        _3817,
        _3819,
        _3822,
        _3823,
        _3827,
        _3828,
        _3831,
        _3835,
        _3838,
        _3841,
        _3842,
        _3843,
        _3844,
        _3845,
        _3848,
        _3852,
        _3853,
        _3854,
        _3855,
        _3856,
        _3860,
        _3862,
        _3863,
        _3868,
        _3870,
        _3877,
        _3880,
        _3881,
        _3882,
        _3883,
        _3884,
        _3885,
        _3888,
        _3890,
        _3891,
        _3892,
        _3895,
        _3898,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ComponentStabilityAnalysis",)


Self = TypeVar("Self", bound="ComponentStabilityAnalysis")


class ComponentStabilityAnalysis(_3846.PartStabilityAnalysis):
    """ComponentStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentStabilityAnalysis")

    class _Cast_ComponentStabilityAnalysis:
        """Special nested class for casting ComponentStabilityAnalysis to subclasses."""

        def __init__(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
            parent: "ComponentStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def part_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3846.PartStabilityAnalysis":
            return self._parent._cast(_3846.PartStabilityAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_or_housing_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3766.AbstractShaftOrHousingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3766,
            )

            return self._parent._cast(_3766.AbstractShaftOrHousingStabilityAnalysis)

        @property
        def abstract_shaft_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3767.AbstractShaftStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3767,
            )

            return self._parent._cast(_3767.AbstractShaftStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3771.AGMAGleasonConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3771,
            )

            return self._parent._cast(_3771.AGMAGleasonConicalGearStabilityAnalysis)

        @property
        def bearing_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3773.BearingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3773,
            )

            return self._parent._cast(_3773.BearingStabilityAnalysis)

        @property
        def bevel_differential_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3778.BevelDifferentialGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3778,
            )

            return self._parent._cast(_3778.BevelDifferentialGearStabilityAnalysis)

        @property
        def bevel_differential_planet_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3779.BevelDifferentialPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3779,
            )

            return self._parent._cast(
                _3779.BevelDifferentialPlanetGearStabilityAnalysis
            )

        @property
        def bevel_differential_sun_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3780.BevelDifferentialSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3780,
            )

            return self._parent._cast(_3780.BevelDifferentialSunGearStabilityAnalysis)

        @property
        def bevel_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3783.BevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3783,
            )

            return self._parent._cast(_3783.BevelGearStabilityAnalysis)

        @property
        def bolt_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3785.BoltStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3785,
            )

            return self._parent._cast(_3785.BoltStabilityAnalysis)

        @property
        def clutch_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3787.ClutchHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3787,
            )

            return self._parent._cast(_3787.ClutchHalfStabilityAnalysis)

        @property
        def concept_coupling_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3792.ConceptCouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3792,
            )

            return self._parent._cast(_3792.ConceptCouplingHalfStabilityAnalysis)

        @property
        def concept_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3796.ConceptGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3796,
            )

            return self._parent._cast(_3796.ConceptGearStabilityAnalysis)

        @property
        def conical_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3799.ConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3799,
            )

            return self._parent._cast(_3799.ConicalGearStabilityAnalysis)

        @property
        def connector_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3801.ConnectorStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3801,
            )

            return self._parent._cast(_3801.ConnectorStabilityAnalysis)

        @property
        def coupling_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3803.CouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3803,
            )

            return self._parent._cast(_3803.CouplingHalfStabilityAnalysis)

        @property
        def cvt_pulley_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3807.CVTPulleyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3807,
            )

            return self._parent._cast(_3807.CVTPulleyStabilityAnalysis)

        @property
        def cycloidal_disc_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3812.CycloidalDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3812,
            )

            return self._parent._cast(_3812.CycloidalDiscStabilityAnalysis)

        @property
        def cylindrical_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3815.CylindricalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3815,
            )

            return self._parent._cast(_3815.CylindricalGearStabilityAnalysis)

        @property
        def cylindrical_planet_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3816.CylindricalPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3816,
            )

            return self._parent._cast(_3816.CylindricalPlanetGearStabilityAnalysis)

        @property
        def datum_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3817.DatumStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3817,
            )

            return self._parent._cast(_3817.DatumStabilityAnalysis)

        @property
        def external_cad_model_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3819.ExternalCADModelStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3819,
            )

            return self._parent._cast(_3819.ExternalCADModelStabilityAnalysis)

        @property
        def face_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3822.FaceGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3822,
            )

            return self._parent._cast(_3822.FaceGearStabilityAnalysis)

        @property
        def fe_part_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3823.FEPartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3823,
            )

            return self._parent._cast(_3823.FEPartStabilityAnalysis)

        @property
        def gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3827.GearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3827,
            )

            return self._parent._cast(_3827.GearStabilityAnalysis)

        @property
        def guide_dxf_model_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3828.GuideDxfModelStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3828,
            )

            return self._parent._cast(_3828.GuideDxfModelStabilityAnalysis)

        @property
        def hypoid_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3831.HypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3831,
            )

            return self._parent._cast(_3831.HypoidGearStabilityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3835.KlingelnbergCycloPalloidConicalGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3835,
            )

            return self._parent._cast(
                _3835.KlingelnbergCycloPalloidConicalGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3838.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3838,
            )

            return self._parent._cast(
                _3838.KlingelnbergCycloPalloidHypoidGearStabilityAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3841.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3841,
            )

            return self._parent._cast(
                _3841.KlingelnbergCycloPalloidSpiralBevelGearStabilityAnalysis
            )

        @property
        def mass_disc_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3842.MassDiscStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3842,
            )

            return self._parent._cast(_3842.MassDiscStabilityAnalysis)

        @property
        def measurement_component_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3843.MeasurementComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3843,
            )

            return self._parent._cast(_3843.MeasurementComponentStabilityAnalysis)

        @property
        def mountable_component_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3844.MountableComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3844,
            )

            return self._parent._cast(_3844.MountableComponentStabilityAnalysis)

        @property
        def oil_seal_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3845.OilSealStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3845,
            )

            return self._parent._cast(_3845.OilSealStabilityAnalysis)

        @property
        def part_to_part_shear_coupling_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3848.PartToPartShearCouplingHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3848,
            )

            return self._parent._cast(
                _3848.PartToPartShearCouplingHalfStabilityAnalysis
            )

        @property
        def planet_carrier_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3852.PlanetCarrierStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3852,
            )

            return self._parent._cast(_3852.PlanetCarrierStabilityAnalysis)

        @property
        def point_load_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3853.PointLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3853,
            )

            return self._parent._cast(_3853.PointLoadStabilityAnalysis)

        @property
        def power_load_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3854.PowerLoadStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3854,
            )

            return self._parent._cast(_3854.PowerLoadStabilityAnalysis)

        @property
        def pulley_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3855.PulleyStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3855,
            )

            return self._parent._cast(_3855.PulleyStabilityAnalysis)

        @property
        def ring_pins_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3856.RingPinsStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3856,
            )

            return self._parent._cast(_3856.RingPinsStabilityAnalysis)

        @property
        def rolling_ring_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3860.RollingRingStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3860,
            )

            return self._parent._cast(_3860.RollingRingStabilityAnalysis)

        @property
        def shaft_hub_connection_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3862.ShaftHubConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3862,
            )

            return self._parent._cast(_3862.ShaftHubConnectionStabilityAnalysis)

        @property
        def shaft_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3863.ShaftStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3863,
            )

            return self._parent._cast(_3863.ShaftStabilityAnalysis)

        @property
        def spiral_bevel_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3868.SpiralBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3868,
            )

            return self._parent._cast(_3868.SpiralBevelGearStabilityAnalysis)

        @property
        def spring_damper_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3870.SpringDamperHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3870,
            )

            return self._parent._cast(_3870.SpringDamperHalfStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3877.StraightBevelDiffGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3877,
            )

            return self._parent._cast(_3877.StraightBevelDiffGearStabilityAnalysis)

        @property
        def straight_bevel_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3880.StraightBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3880,
            )

            return self._parent._cast(_3880.StraightBevelGearStabilityAnalysis)

        @property
        def straight_bevel_planet_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3881.StraightBevelPlanetGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3881,
            )

            return self._parent._cast(_3881.StraightBevelPlanetGearStabilityAnalysis)

        @property
        def straight_bevel_sun_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3882.StraightBevelSunGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3882,
            )

            return self._parent._cast(_3882.StraightBevelSunGearStabilityAnalysis)

        @property
        def synchroniser_half_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3883.SynchroniserHalfStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3883,
            )

            return self._parent._cast(_3883.SynchroniserHalfStabilityAnalysis)

        @property
        def synchroniser_part_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3884.SynchroniserPartStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3884,
            )

            return self._parent._cast(_3884.SynchroniserPartStabilityAnalysis)

        @property
        def synchroniser_sleeve_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3885.SynchroniserSleeveStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3885,
            )

            return self._parent._cast(_3885.SynchroniserSleeveStabilityAnalysis)

        @property
        def torque_converter_pump_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3888.TorqueConverterPumpStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3888,
            )

            return self._parent._cast(_3888.TorqueConverterPumpStabilityAnalysis)

        @property
        def torque_converter_turbine_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3890.TorqueConverterTurbineStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3890,
            )

            return self._parent._cast(_3890.TorqueConverterTurbineStabilityAnalysis)

        @property
        def unbalanced_mass_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3891.UnbalancedMassStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3891,
            )

            return self._parent._cast(_3891.UnbalancedMassStabilityAnalysis)

        @property
        def virtual_component_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3892.VirtualComponentStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3892,
            )

            return self._parent._cast(_3892.VirtualComponentStabilityAnalysis)

        @property
        def worm_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3895.WormGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3895,
            )

            return self._parent._cast(_3895.WormGearStabilityAnalysis)

        @property
        def zerol_bevel_gear_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "_3898.ZerolBevelGearStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3898,
            )

            return self._parent._cast(_3898.ZerolBevelGearStabilityAnalysis)

        @property
        def component_stability_analysis(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
        ) -> "ComponentStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentStabilityAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def cast_to(
        self: Self,
    ) -> "ComponentStabilityAnalysis._Cast_ComponentStabilityAnalysis":
        return self._Cast_ComponentStabilityAnalysis(self)
