"""PartModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses", "PartModalAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4656,
        _4574,
        _4575,
        _4576,
        _4579,
        _4580,
        _4581,
        _4582,
        _4584,
        _4586,
        _4587,
        _4588,
        _4589,
        _4591,
        _4592,
        _4593,
        _4594,
        _4596,
        _4597,
        _4599,
        _4601,
        _4602,
        _4604,
        _4605,
        _4607,
        _4608,
        _4610,
        _4613,
        _4614,
        _4616,
        _4617,
        _4618,
        _4620,
        _4623,
        _4624,
        _4625,
        _4626,
        _4630,
        _4632,
        _4633,
        _4634,
        _4635,
        _4638,
        _4639,
        _4640,
        _4642,
        _4643,
        _4646,
        _4647,
        _4649,
        _4650,
        _4652,
        _4653,
        _4654,
        _4655,
        _4660,
        _4662,
        _4666,
        _4667,
        _4669,
        _4670,
        _4671,
        _4672,
        _4673,
        _4674,
        _4676,
        _4678,
        _4679,
        _4680,
        _4681,
        _4684,
        _4686,
        _4687,
        _4689,
        _4690,
        _4692,
        _4693,
        _4695,
        _4696,
        _4697,
        _4698,
        _4699,
        _4700,
        _4701,
        _4702,
        _4704,
        _4705,
        _4706,
        _4707,
        _4708,
        _4713,
        _4714,
        _4716,
        _4717,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses.reporting import (
        _4728,
        _4726,
        _4729,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2787
    from mastapy.system_model.drawing import _2253
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartModalAnalysis",)


Self = TypeVar("Self", bound="PartModalAnalysis")


class PartModalAnalysis(_7550.PartStaticLoadAnalysisCase):
    """PartModalAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartModalAnalysis")

    class _Cast_PartModalAnalysis:
        """Special nested class for casting PartModalAnalysis to subclasses."""

        def __init__(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
            parent: "PartModalAnalysis",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4574.AbstractAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4574

            return self._parent._cast(_4574.AbstractAssemblyModalAnalysis)

        @property
        def abstract_shaft_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4575.AbstractShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4575

            return self._parent._cast(_4575.AbstractShaftModalAnalysis)

        @property
        def abstract_shaft_or_housing_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4576.AbstractShaftOrHousingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4576

            return self._parent._cast(_4576.AbstractShaftOrHousingModalAnalysis)

        @property
        def agma_gleason_conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4579.AGMAGleasonConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4579

            return self._parent._cast(_4579.AGMAGleasonConicalGearModalAnalysis)

        @property
        def agma_gleason_conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4580.AGMAGleasonConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4580

            return self._parent._cast(_4580.AGMAGleasonConicalGearSetModalAnalysis)

        @property
        def assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4581.AssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4581

            return self._parent._cast(_4581.AssemblyModalAnalysis)

        @property
        def bearing_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4582.BearingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4582

            return self._parent._cast(_4582.BearingModalAnalysis)

        @property
        def belt_drive_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4584.BeltDriveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4584

            return self._parent._cast(_4584.BeltDriveModalAnalysis)

        @property
        def bevel_differential_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4586.BevelDifferentialGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4586

            return self._parent._cast(_4586.BevelDifferentialGearModalAnalysis)

        @property
        def bevel_differential_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4587.BevelDifferentialGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4587

            return self._parent._cast(_4587.BevelDifferentialGearSetModalAnalysis)

        @property
        def bevel_differential_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4588.BevelDifferentialPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4588

            return self._parent._cast(_4588.BevelDifferentialPlanetGearModalAnalysis)

        @property
        def bevel_differential_sun_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4589.BevelDifferentialSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4589

            return self._parent._cast(_4589.BevelDifferentialSunGearModalAnalysis)

        @property
        def bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4591.BevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4591

            return self._parent._cast(_4591.BevelGearModalAnalysis)

        @property
        def bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4592.BevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4592

            return self._parent._cast(_4592.BevelGearSetModalAnalysis)

        @property
        def bolted_joint_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4593.BoltedJointModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4593

            return self._parent._cast(_4593.BoltedJointModalAnalysis)

        @property
        def bolt_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4594.BoltModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4594

            return self._parent._cast(_4594.BoltModalAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4596.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ClutchHalfModalAnalysis)

        @property
        def clutch_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4597.ClutchModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4597

            return self._parent._cast(_4597.ClutchModalAnalysis)

        @property
        def component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4599.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ComponentModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4601.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConceptCouplingHalfModalAnalysis)

        @property
        def concept_coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4602.ConceptCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4602

            return self._parent._cast(_4602.ConceptCouplingModalAnalysis)

        @property
        def concept_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4604.ConceptGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4604

            return self._parent._cast(_4604.ConceptGearModalAnalysis)

        @property
        def concept_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4605.ConceptGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4605

            return self._parent._cast(_4605.ConceptGearSetModalAnalysis)

        @property
        def conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4607.ConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4607

            return self._parent._cast(_4607.ConicalGearModalAnalysis)

        @property
        def conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4608.ConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4608

            return self._parent._cast(_4608.ConicalGearSetModalAnalysis)

        @property
        def connector_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4610.ConnectorModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4610

            return self._parent._cast(_4610.ConnectorModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4613.CouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4613

            return self._parent._cast(_4613.CouplingHalfModalAnalysis)

        @property
        def coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4614.CouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4614

            return self._parent._cast(_4614.CouplingModalAnalysis)

        @property
        def cvt_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4616.CVTModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4616

            return self._parent._cast(_4616.CVTModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4617.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.CVTPulleyModalAnalysis)

        @property
        def cycloidal_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4618.CycloidalAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4618

            return self._parent._cast(_4618.CycloidalAssemblyModalAnalysis)

        @property
        def cycloidal_disc_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4620.CycloidalDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4620

            return self._parent._cast(_4620.CycloidalDiscModalAnalysis)

        @property
        def cylindrical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4623.CylindricalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4623

            return self._parent._cast(_4623.CylindricalGearModalAnalysis)

        @property
        def cylindrical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4624.CylindricalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4624

            return self._parent._cast(_4624.CylindricalGearSetModalAnalysis)

        @property
        def cylindrical_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4625.CylindricalPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4625

            return self._parent._cast(_4625.CylindricalPlanetGearModalAnalysis)

        @property
        def datum_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4626.DatumModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4626

            return self._parent._cast(_4626.DatumModalAnalysis)

        @property
        def external_cad_model_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4630.ExternalCADModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4630

            return self._parent._cast(_4630.ExternalCADModelModalAnalysis)

        @property
        def face_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4632.FaceGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4632

            return self._parent._cast(_4632.FaceGearModalAnalysis)

        @property
        def face_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4633.FaceGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4633

            return self._parent._cast(_4633.FaceGearSetModalAnalysis)

        @property
        def fe_part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4634.FEPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4634

            return self._parent._cast(_4634.FEPartModalAnalysis)

        @property
        def flexible_pin_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4635.FlexiblePinAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4635

            return self._parent._cast(_4635.FlexiblePinAssemblyModalAnalysis)

        @property
        def gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4638.GearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4638

            return self._parent._cast(_4638.GearModalAnalysis)

        @property
        def gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4639.GearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4639

            return self._parent._cast(_4639.GearSetModalAnalysis)

        @property
        def guide_dxf_model_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4640.GuideDxfModelModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4640

            return self._parent._cast(_4640.GuideDxfModelModalAnalysis)

        @property
        def hypoid_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4642.HypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4642

            return self._parent._cast(_4642.HypoidGearModalAnalysis)

        @property
        def hypoid_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4643.HypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4643

            return self._parent._cast(_4643.HypoidGearSetModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4646.KlingelnbergCycloPalloidConicalGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4646

            return self._parent._cast(
                _4646.KlingelnbergCycloPalloidConicalGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4647.KlingelnbergCycloPalloidConicalGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4647

            return self._parent._cast(
                _4647.KlingelnbergCycloPalloidConicalGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4649.KlingelnbergCycloPalloidHypoidGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4649

            return self._parent._cast(
                _4649.KlingelnbergCycloPalloidHypoidGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4650.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4650

            return self._parent._cast(
                _4650.KlingelnbergCycloPalloidHypoidGearSetModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4652.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4652

            return self._parent._cast(
                _4652.KlingelnbergCycloPalloidSpiralBevelGearModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4653.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4653

            return self._parent._cast(
                _4653.KlingelnbergCycloPalloidSpiralBevelGearSetModalAnalysis
            )

        @property
        def mass_disc_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4654.MassDiscModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4654

            return self._parent._cast(_4654.MassDiscModalAnalysis)

        @property
        def measurement_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4655.MeasurementComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4655

            return self._parent._cast(_4655.MeasurementComponentModalAnalysis)

        @property
        def mountable_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4660.MountableComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4660

            return self._parent._cast(_4660.MountableComponentModalAnalysis)

        @property
        def oil_seal_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4662.OilSealModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4662

            return self._parent._cast(_4662.OilSealModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4666.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def part_to_part_shear_coupling_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4667.PartToPartShearCouplingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4667

            return self._parent._cast(_4667.PartToPartShearCouplingModalAnalysis)

        @property
        def planetary_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4669.PlanetaryGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4669

            return self._parent._cast(_4669.PlanetaryGearSetModalAnalysis)

        @property
        def planet_carrier_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4670.PlanetCarrierModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4670

            return self._parent._cast(_4670.PlanetCarrierModalAnalysis)

        @property
        def point_load_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4671.PointLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4671

            return self._parent._cast(_4671.PointLoadModalAnalysis)

        @property
        def power_load_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4672.PowerLoadModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4672

            return self._parent._cast(_4672.PowerLoadModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4673.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.PulleyModalAnalysis)

        @property
        def ring_pins_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4674.RingPinsModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4674

            return self._parent._cast(_4674.RingPinsModalAnalysis)

        @property
        def rolling_ring_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4676.RollingRingAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4676

            return self._parent._cast(_4676.RollingRingAssemblyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4678.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.RollingRingModalAnalysis)

        @property
        def root_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4679.RootAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4679

            return self._parent._cast(_4679.RootAssemblyModalAnalysis)

        @property
        def shaft_hub_connection_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4680.ShaftHubConnectionModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4680

            return self._parent._cast(_4680.ShaftHubConnectionModalAnalysis)

        @property
        def shaft_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4681.ShaftModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4681

            return self._parent._cast(_4681.ShaftModalAnalysis)

        @property
        def specialised_assembly_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4684.SpecialisedAssemblyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4684

            return self._parent._cast(_4684.SpecialisedAssemblyModalAnalysis)

        @property
        def spiral_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4686.SpiralBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4686

            return self._parent._cast(_4686.SpiralBevelGearModalAnalysis)

        @property
        def spiral_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4687.SpiralBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4687

            return self._parent._cast(_4687.SpiralBevelGearSetModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4689.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.SpringDamperHalfModalAnalysis)

        @property
        def spring_damper_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4690.SpringDamperModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4690

            return self._parent._cast(_4690.SpringDamperModalAnalysis)

        @property
        def straight_bevel_diff_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4692.StraightBevelDiffGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4692

            return self._parent._cast(_4692.StraightBevelDiffGearModalAnalysis)

        @property
        def straight_bevel_diff_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4693.StraightBevelDiffGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4693

            return self._parent._cast(_4693.StraightBevelDiffGearSetModalAnalysis)

        @property
        def straight_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4695.StraightBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4695

            return self._parent._cast(_4695.StraightBevelGearModalAnalysis)

        @property
        def straight_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4696.StraightBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4696

            return self._parent._cast(_4696.StraightBevelGearSetModalAnalysis)

        @property
        def straight_bevel_planet_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4697.StraightBevelPlanetGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4697

            return self._parent._cast(_4697.StraightBevelPlanetGearModalAnalysis)

        @property
        def straight_bevel_sun_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4698.StraightBevelSunGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4698

            return self._parent._cast(_4698.StraightBevelSunGearModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4699.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4700.SynchroniserModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4700

            return self._parent._cast(_4700.SynchroniserModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4701.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4702.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4704.TorqueConverterModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4704

            return self._parent._cast(_4704.TorqueConverterModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4705.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4706.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.TorqueConverterTurbineModalAnalysis)

        @property
        def unbalanced_mass_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4707.UnbalancedMassModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4707

            return self._parent._cast(_4707.UnbalancedMassModalAnalysis)

        @property
        def virtual_component_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4708.VirtualComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4708

            return self._parent._cast(_4708.VirtualComponentModalAnalysis)

        @property
        def worm_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4713.WormGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4713

            return self._parent._cast(_4713.WormGearModalAnalysis)

        @property
        def worm_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4714.WormGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4714

            return self._parent._cast(_4714.WormGearSetModalAnalysis)

        @property
        def zerol_bevel_gear_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4716.ZerolBevelGearModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4716

            return self._parent._cast(_4716.ZerolBevelGearModalAnalysis)

        @property
        def zerol_bevel_gear_set_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "_4717.ZerolBevelGearSetModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4717

            return self._parent._cast(_4717.ZerolBevelGearSetModalAnalysis)

        @property
        def part_modal_analysis(
            self: "PartModalAnalysis._Cast_PartModalAnalysis",
        ) -> "PartModalAnalysis":
            return self._parent

        def __getattr__(self: "PartModalAnalysis._Cast_PartModalAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2470.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def modal_analysis(self: Self) -> "_4656.ModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.ModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def excited_modes_summary(
        self: Self,
    ) -> "List[_4728.SingleExcitationResultsModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.SingleExcitationResultsModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ExcitedModesSummary

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def gear_mesh_excitation_details(
        self: Self,
    ) -> "List[_4726.RigidlyConnectedDesignEntityGroupModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.GearMeshExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def results_for_modes(self: Self) -> "List[_4729.SingleModeResults]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.SingleModeResults]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsForModes

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def shaft_excitation_details(
        self: Self,
    ) -> "List[_4726.RigidlyConnectedDesignEntityGroupModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.reporting.RigidlyConnectedDesignEntityGroupModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftExcitationDetails

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def system_deflection_results(self: Self) -> "_2787.PartSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2253.ModalAnalysisViewable":
        """mastapy.system_model.drawing.ModalAnalysisViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartModalAnalysis._Cast_PartModalAnalysis":
        return self._Cast_PartModalAnalysis(self)
