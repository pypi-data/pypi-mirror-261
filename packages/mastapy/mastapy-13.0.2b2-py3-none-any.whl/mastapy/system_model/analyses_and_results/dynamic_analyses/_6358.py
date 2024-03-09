"""MountableComponentDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "MountableComponentDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6283,
        _6287,
        _6290,
        _6293,
        _6294,
        _6295,
        _6302,
        _6307,
        _6308,
        _6311,
        _6315,
        _6318,
        _6321,
        _6326,
        _6329,
        _6334,
        _6339,
        _6343,
        _6347,
        _6350,
        _6353,
        _6356,
        _6357,
        _6359,
        _6363,
        _6366,
        _6367,
        _6368,
        _6369,
        _6370,
        _6374,
        _6377,
        _6380,
        _6385,
        _6386,
        _6389,
        _6392,
        _6393,
        _6395,
        _6396,
        _6397,
        _6400,
        _6401,
        _6402,
        _6403,
        _6404,
        _6407,
        _6360,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentDynamicAnalysis",)


Self = TypeVar("Self", bound="MountableComponentDynamicAnalysis")


class MountableComponentDynamicAnalysis(_6304.ComponentDynamicAnalysis):
    """MountableComponentDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentDynamicAnalysis")

    class _Cast_MountableComponentDynamicAnalysis:
        """Special nested class for casting MountableComponentDynamicAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
            parent: "MountableComponentDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def component_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6304.ComponentDynamicAnalysis":
            return self._parent._cast(_6304.ComponentDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6360.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6283.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6287.BearingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.BearingDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6290.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6293.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6294.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6295.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.BevelGearDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6302.ClutchHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ClutchHalfDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6307.ConceptCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6308.ConceptGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConceptGearDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6311.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConicalGearDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6315.ConnectorDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.ConnectorDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6318.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.CouplingHalfDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6321.CVTPulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.CVTPulleyDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6326.CylindricalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6329.CylindricalPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329

            return self._parent._cast(_6329.CylindricalPlanetGearDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6334.FaceGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.FaceGearDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6339.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.GearDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6343.HypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(_6343.HypoidGearDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6347.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6350.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(
                _6350.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6353.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(
                _6353.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6356.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6357.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.MeasurementComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6359.OilSealDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(_6359.OilSealDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6363.PartToPartShearCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6366.PlanetCarrierDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6367.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6368.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6369.PulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6370.RingPinsDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6374.RollingRingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.RollingRingDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6377.ShaftHubConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.ShaftHubConnectionDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6380.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.SpiralBevelGearDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6385.SpringDamperHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6386.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6389.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6392.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6393.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6395.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6396.SynchroniserPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6397.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6400.TorqueConverterPumpDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6401.TorqueConverterTurbineDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6402.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6403.VirtualComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6404.WormGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.WormGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "_6407.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6407

            return self._parent._cast(_6407.ZerolBevelGearDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
        ) -> "MountableComponentDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentDynamicAnalysis.TYPE"
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
    ) -> "MountableComponentDynamicAnalysis._Cast_MountableComponentDynamicAnalysis":
        return self._Cast_MountableComponentDynamicAnalysis(self)
