"""PartMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7551
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "PartMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5467,
        _5378,
        _5379,
        _5380,
        _5383,
        _5384,
        _5386,
        _5387,
        _5390,
        _5392,
        _5393,
        _5394,
        _5395,
        _5397,
        _5398,
        _5399,
        _5400,
        _5402,
        _5403,
        _5406,
        _5408,
        _5409,
        _5411,
        _5412,
        _5414,
        _5415,
        _5417,
        _5419,
        _5420,
        _5422,
        _5423,
        _5424,
        _5426,
        _5429,
        _5430,
        _5431,
        _5432,
        _5433,
        _5435,
        _5436,
        _5437,
        _5438,
        _5441,
        _5442,
        _5443,
        _5445,
        _5446,
        _5453,
        _5454,
        _5456,
        _5457,
        _5459,
        _5460,
        _5461,
        _5465,
        _5466,
        _5468,
        _5471,
        _5472,
        _5474,
        _5475,
        _5476,
        _5477,
        _5478,
        _5479,
        _5481,
        _5483,
        _5484,
        _5487,
        _5488,
        _5491,
        _5493,
        _5494,
        _5496,
        _5497,
        _5499,
        _5500,
        _5502,
        _5503,
        _5504,
        _5505,
        _5506,
        _5507,
        _5508,
        _5509,
        _5512,
        _5513,
        _5515,
        _5516,
        _5517,
        _5520,
        _5521,
        _5523,
        _5524,
    )
    from mastapy.math_utility.convergence import _1577
    from mastapy.system_model.drawing import _2252
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="PartMultibodyDynamicsAnalysis")


class PartMultibodyDynamicsAnalysis(_7551.PartTimeSeriesLoadAnalysisCase):
    """PartMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartMultibodyDynamicsAnalysis")

    class _Cast_PartMultibodyDynamicsAnalysis:
        """Special nested class for casting PartMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
            parent: "PartMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def part_time_series_load_analysis_case(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_7551.PartTimeSeriesLoadAnalysisCase":
            return self._parent._cast(_7551.PartTimeSeriesLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5378.AbstractAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5378

            return self._parent._cast(_5378.AbstractAssemblyMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5379.AbstractShaftMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5379

            return self._parent._cast(_5379.AbstractShaftMultibodyDynamicsAnalysis)

        @property
        def abstract_shaft_or_housing_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5380.AbstractShaftOrHousingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5380

            return self._parent._cast(
                _5380.AbstractShaftOrHousingMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5383.AGMAGleasonConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5383

            return self._parent._cast(
                _5383.AGMAGleasonConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5384.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5384

            return self._parent._cast(
                _5384.AGMAGleasonConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5386.AssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5386

            return self._parent._cast(_5386.AssemblyMultibodyDynamicsAnalysis)

        @property
        def bearing_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5387.BearingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5387

            return self._parent._cast(_5387.BearingMultibodyDynamicsAnalysis)

        @property
        def belt_drive_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5390.BeltDriveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5390

            return self._parent._cast(_5390.BeltDriveMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5392.BevelDifferentialGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5392

            return self._parent._cast(
                _5392.BevelDifferentialGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5393.BevelDifferentialGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5393

            return self._parent._cast(
                _5393.BevelDifferentialGearSetMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_planet_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5394.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5394

            return self._parent._cast(
                _5394.BevelDifferentialPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_differential_sun_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5395.BevelDifferentialSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5395

            return self._parent._cast(
                _5395.BevelDifferentialSunGearMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5397.BevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5397

            return self._parent._cast(_5397.BevelGearMultibodyDynamicsAnalysis)

        @property
        def bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5398.BevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5398

            return self._parent._cast(_5398.BevelGearSetMultibodyDynamicsAnalysis)

        @property
        def bolted_joint_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5399.BoltedJointMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5399

            return self._parent._cast(_5399.BoltedJointMultibodyDynamicsAnalysis)

        @property
        def bolt_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5400.BoltMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5400

            return self._parent._cast(_5400.BoltMultibodyDynamicsAnalysis)

        @property
        def clutch_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5402.ClutchHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5402

            return self._parent._cast(_5402.ClutchHalfMultibodyDynamicsAnalysis)

        @property
        def clutch_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5403.ClutchMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5403

            return self._parent._cast(_5403.ClutchMultibodyDynamicsAnalysis)

        @property
        def component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5406.ComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5406

            return self._parent._cast(_5406.ComponentMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5408.ConceptCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5408

            return self._parent._cast(
                _5408.ConceptCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def concept_coupling_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5409.ConceptCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5409

            return self._parent._cast(_5409.ConceptCouplingMultibodyDynamicsAnalysis)

        @property
        def concept_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5411.ConceptGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5411

            return self._parent._cast(_5411.ConceptGearMultibodyDynamicsAnalysis)

        @property
        def concept_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5412.ConceptGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5412

            return self._parent._cast(_5412.ConceptGearSetMultibodyDynamicsAnalysis)

        @property
        def conical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5414.ConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5414

            return self._parent._cast(_5414.ConicalGearMultibodyDynamicsAnalysis)

        @property
        def conical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5415.ConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5415

            return self._parent._cast(_5415.ConicalGearSetMultibodyDynamicsAnalysis)

        @property
        def connector_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5417.ConnectorMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5417

            return self._parent._cast(_5417.ConnectorMultibodyDynamicsAnalysis)

        @property
        def coupling_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5419.CouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5419

            return self._parent._cast(_5419.CouplingHalfMultibodyDynamicsAnalysis)

        @property
        def coupling_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5420.CouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5420

            return self._parent._cast(_5420.CouplingMultibodyDynamicsAnalysis)

        @property
        def cvt_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5422.CVTMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5422

            return self._parent._cast(_5422.CVTMultibodyDynamicsAnalysis)

        @property
        def cvt_pulley_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5423.CVTPulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5423

            return self._parent._cast(_5423.CVTPulleyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5424.CycloidalAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5424

            return self._parent._cast(_5424.CycloidalAssemblyMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5426.CycloidalDiscMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5426

            return self._parent._cast(_5426.CycloidalDiscMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5429.CylindricalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5429

            return self._parent._cast(_5429.CylindricalGearMultibodyDynamicsAnalysis)

        @property
        def cylindrical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5430.CylindricalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5430

            return self._parent._cast(_5430.CylindricalGearSetMultibodyDynamicsAnalysis)

        @property
        def cylindrical_planet_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5431.CylindricalPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5431

            return self._parent._cast(
                _5431.CylindricalPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def datum_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5432.DatumMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5432

            return self._parent._cast(_5432.DatumMultibodyDynamicsAnalysis)

        @property
        def external_cad_model_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5433.ExternalCADModelMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5433

            return self._parent._cast(_5433.ExternalCADModelMultibodyDynamicsAnalysis)

        @property
        def face_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5435.FaceGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5435

            return self._parent._cast(_5435.FaceGearMultibodyDynamicsAnalysis)

        @property
        def face_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5436.FaceGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5436

            return self._parent._cast(_5436.FaceGearSetMultibodyDynamicsAnalysis)

        @property
        def fe_part_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5437.FEPartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5437

            return self._parent._cast(_5437.FEPartMultibodyDynamicsAnalysis)

        @property
        def flexible_pin_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5438.FlexiblePinAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5438

            return self._parent._cast(
                _5438.FlexiblePinAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5441.GearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5441

            return self._parent._cast(_5441.GearMultibodyDynamicsAnalysis)

        @property
        def gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5442.GearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5442

            return self._parent._cast(_5442.GearSetMultibodyDynamicsAnalysis)

        @property
        def guide_dxf_model_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5443.GuideDxfModelMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5443

            return self._parent._cast(_5443.GuideDxfModelMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5445.HypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5445

            return self._parent._cast(_5445.HypoidGearMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5446.HypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5446

            return self._parent._cast(_5446.HypoidGearSetMultibodyDynamicsAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5453.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5453

            return self._parent._cast(
                _5453.KlingelnbergCycloPalloidConicalGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5454.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5454

            return self._parent._cast(
                _5454.KlingelnbergCycloPalloidConicalGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5456.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5456

            return self._parent._cast(
                _5456.KlingelnbergCycloPalloidHypoidGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5457.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5457

            return self._parent._cast(
                _5457.KlingelnbergCycloPalloidHypoidGearSetMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5459.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5459

            return self._parent._cast(
                _5459.KlingelnbergCycloPalloidSpiralBevelGearMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> (
            "_5460.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5460

            return self._parent._cast(
                _5460.KlingelnbergCycloPalloidSpiralBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def mass_disc_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5461.MassDiscMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5461

            return self._parent._cast(_5461.MassDiscMultibodyDynamicsAnalysis)

        @property
        def measurement_component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5465.MeasurementComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5465

            return self._parent._cast(
                _5465.MeasurementComponentMultibodyDynamicsAnalysis
            )

        @property
        def mountable_component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5466.MountableComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5466

            return self._parent._cast(_5466.MountableComponentMultibodyDynamicsAnalysis)

        @property
        def oil_seal_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5468.OilSealMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5468

            return self._parent._cast(_5468.OilSealMultibodyDynamicsAnalysis)

        @property
        def part_to_part_shear_coupling_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5471.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5471

            return self._parent._cast(
                _5471.PartToPartShearCouplingHalfMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5472.PartToPartShearCouplingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5472

            return self._parent._cast(
                _5472.PartToPartShearCouplingMultibodyDynamicsAnalysis
            )

        @property
        def planetary_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5474.PlanetaryGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5474

            return self._parent._cast(_5474.PlanetaryGearSetMultibodyDynamicsAnalysis)

        @property
        def planet_carrier_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5475.PlanetCarrierMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5475

            return self._parent._cast(_5475.PlanetCarrierMultibodyDynamicsAnalysis)

        @property
        def point_load_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5476.PointLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5476

            return self._parent._cast(_5476.PointLoadMultibodyDynamicsAnalysis)

        @property
        def power_load_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5477.PowerLoadMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5477

            return self._parent._cast(_5477.PowerLoadMultibodyDynamicsAnalysis)

        @property
        def pulley_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5478.PulleyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5478

            return self._parent._cast(_5478.PulleyMultibodyDynamicsAnalysis)

        @property
        def ring_pins_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5479.RingPinsMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5479

            return self._parent._cast(_5479.RingPinsMultibodyDynamicsAnalysis)

        @property
        def rolling_ring_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5481.RollingRingAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5481

            return self._parent._cast(
                _5481.RollingRingAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5483.RollingRingMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5483

            return self._parent._cast(_5483.RollingRingMultibodyDynamicsAnalysis)

        @property
        def root_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5484.RootAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5484

            return self._parent._cast(_5484.RootAssemblyMultibodyDynamicsAnalysis)

        @property
        def shaft_hub_connection_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5487.ShaftHubConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5487

            return self._parent._cast(_5487.ShaftHubConnectionMultibodyDynamicsAnalysis)

        @property
        def shaft_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5488.ShaftMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5488

            return self._parent._cast(_5488.ShaftMultibodyDynamicsAnalysis)

        @property
        def specialised_assembly_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5491.SpecialisedAssemblyMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5491

            return self._parent._cast(
                _5491.SpecialisedAssemblyMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5493.SpiralBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5493

            return self._parent._cast(_5493.SpiralBevelGearMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5494.SpiralBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5494

            return self._parent._cast(_5494.SpiralBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def spring_damper_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5496.SpringDamperHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5496

            return self._parent._cast(_5496.SpringDamperHalfMultibodyDynamicsAnalysis)

        @property
        def spring_damper_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5497.SpringDamperMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5497

            return self._parent._cast(_5497.SpringDamperMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_diff_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5499.StraightBevelDiffGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5499

            return self._parent._cast(
                _5499.StraightBevelDiffGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5500.StraightBevelDiffGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5500

            return self._parent._cast(
                _5500.StraightBevelDiffGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5502.StraightBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5502

            return self._parent._cast(_5502.StraightBevelGearMultibodyDynamicsAnalysis)

        @property
        def straight_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5503.StraightBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5503

            return self._parent._cast(
                _5503.StraightBevelGearSetMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_planet_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5504.StraightBevelPlanetGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5504

            return self._parent._cast(
                _5504.StraightBevelPlanetGearMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_sun_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5505.StraightBevelSunGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5505

            return self._parent._cast(
                _5505.StraightBevelSunGearMultibodyDynamicsAnalysis
            )

        @property
        def synchroniser_half_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5506.SynchroniserHalfMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5506

            return self._parent._cast(_5506.SynchroniserHalfMultibodyDynamicsAnalysis)

        @property
        def synchroniser_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5507.SynchroniserMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5507

            return self._parent._cast(_5507.SynchroniserMultibodyDynamicsAnalysis)

        @property
        def synchroniser_part_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5508.SynchroniserPartMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5508

            return self._parent._cast(_5508.SynchroniserPartMultibodyDynamicsAnalysis)

        @property
        def synchroniser_sleeve_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5509.SynchroniserSleeveMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5509

            return self._parent._cast(_5509.SynchroniserSleeveMultibodyDynamicsAnalysis)

        @property
        def torque_converter_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5512.TorqueConverterMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5512

            return self._parent._cast(_5512.TorqueConverterMultibodyDynamicsAnalysis)

        @property
        def torque_converter_pump_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5513.TorqueConverterPumpMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5513

            return self._parent._cast(
                _5513.TorqueConverterPumpMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_turbine_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5515.TorqueConverterTurbineMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5515

            return self._parent._cast(
                _5515.TorqueConverterTurbineMultibodyDynamicsAnalysis
            )

        @property
        def unbalanced_mass_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5516.UnbalancedMassMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5516

            return self._parent._cast(_5516.UnbalancedMassMultibodyDynamicsAnalysis)

        @property
        def virtual_component_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5517.VirtualComponentMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5517

            return self._parent._cast(_5517.VirtualComponentMultibodyDynamicsAnalysis)

        @property
        def worm_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5520.WormGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5520

            return self._parent._cast(_5520.WormGearMultibodyDynamicsAnalysis)

        @property
        def worm_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5521.WormGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5521

            return self._parent._cast(_5521.WormGearSetMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5523.ZerolBevelGearMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5523

            return self._parent._cast(_5523.ZerolBevelGearMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_set_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "_5524.ZerolBevelGearSetMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5524

            return self._parent._cast(_5524.ZerolBevelGearSetMultibodyDynamicsAnalysis)

        @property
        def part_multibody_dynamics_analysis(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
        ) -> "PartMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartMultibodyDynamicsAnalysis.TYPE"):
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
    def multibody_dynamics_analysis(self: Self) -> "_5467.MultibodyDynamicsAnalysis":
        """mastapy.system_model.analyses_and_results.mbd_analyses.MultibodyDynamicsAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MultibodyDynamicsAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def data_logger(self: Self) -> "_1577.DataLogger":
        """mastapy.math_utility.convergence.DataLogger

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2252.MBDAnalysisViewable":
        """mastapy.system_model.drawing.MBDAnalysisViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(
        self: Self,
    ) -> "PartMultibodyDynamicsAnalysis._Cast_PartMultibodyDynamicsAnalysis":
        return self._Cast_PartMultibodyDynamicsAnalysis(self)
