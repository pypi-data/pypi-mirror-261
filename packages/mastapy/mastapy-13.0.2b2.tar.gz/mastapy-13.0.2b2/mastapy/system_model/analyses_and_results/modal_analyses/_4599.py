"""ComponentModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4664
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "ComponentModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446
    from mastapy.system_model.analyses_and_results.system_deflections import _2717
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4575,
        _4576,
        _4579,
        _4582,
        _4586,
        _4588,
        _4589,
        _4591,
        _4594,
        _4596,
        _4601,
        _4604,
        _4607,
        _4610,
        _4613,
        _4617,
        _4620,
        _4623,
        _4625,
        _4626,
        _4630,
        _4632,
        _4634,
        _4638,
        _4640,
        _4642,
        _4646,
        _4649,
        _4652,
        _4654,
        _4655,
        _4660,
        _4662,
        _4666,
        _4670,
        _4671,
        _4672,
        _4673,
        _4674,
        _4678,
        _4680,
        _4681,
        _4686,
        _4689,
        _4692,
        _4695,
        _4697,
        _4698,
        _4699,
        _4701,
        _4702,
        _4705,
        _4706,
        _4707,
        _4708,
        _4713,
        _4716,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ComponentModalAnalysis",)


Self = TypeVar("Self", bound="ComponentModalAnalysis")


class ComponentModalAnalysis(_4664.PartModalAnalysis):
    """ComponentModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COMPONENT_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentModalAnalysis")

    class _Cast_ComponentModalAnalysis:
        """Special nested class for casting ComponentModalAnalysis to subclasses."""

        def __init__(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
            parent: "ComponentModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4664.PartModalAnalysis":
            return self._parent._cast(_4664.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4575.AbstractShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575

            return self._parent._cast(_4575.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4576.AbstractShaftOrHousingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576

            return self._parent._cast(_4576.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4579.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579

            return self._parent._cast(_4579.AGMAGleasonConicalGearModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4582.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.BearingModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4586.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4588.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4589.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589

            return self._parent._cast(_4589.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4591.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4591

            return self._parent._cast(_4591.BevelGearModalAnalysis)

        @property
        def bolt_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4594.BoltModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4596.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4601.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4604.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConceptGearModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4607.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.ConicalGearModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4610.ConnectorModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4613.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.CouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4617.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.CVTPulleyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4620.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4623.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.CylindricalGearModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4625.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4626.DatumModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4630.ExternalCADModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4632.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.FaceGearModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4634.FEPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.FEPartModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4638.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.GearModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4640.GuideDxfModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(_4640.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4642.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(_4642.HypoidGearModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4646.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(
                _4646.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4649.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(
                _4649.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4652.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652

            return self._parent._cast(
                _4652.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4654.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4655.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4660.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4662.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.OilSealModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4666.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4670.PlanetCarrierModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4671.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(_4671.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4672.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4673.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4674.RingPinsModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(_4674.RingPinsModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4678.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.RollingRingModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4680.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4681.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.ShaftModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4686.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.SpiralBevelGearModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4689.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.SpringDamperHalfModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4692.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4695.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4697.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4698.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4699.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4701.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4702.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4705.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4706.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4707.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4708.VirtualComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4713.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.WormGearModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "_4716.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4716

            return self._parent._cast(_4716.ZerolBevelGearModalAnalysis)

        @property
        def component_modal_analysis(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis",
        ) -> "ComponentModalAnalysis":
            return self._parent

        def __getattr__(
            self: "ComponentModalAnalysis._Cast_ComponentModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentModalAnalysis.TYPE"):
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
    def system_deflection_results(self: Self) -> "_2717.ComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.ComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "ComponentModalAnalysis._Cast_ComponentModalAnalysis":
        return self._Cast_ComponentModalAnalysis(self)
