"""PartHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "PartHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.system_model.analyses_and_results.modal_analyses import _4664
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5763,
        _5768,
        _5680,
        _5682,
        _5683,
        _5685,
        _5687,
        _5688,
        _5689,
        _5691,
        _5692,
        _5694,
        _5695,
        _5696,
        _5697,
        _5699,
        _5700,
        _5701,
        _5703,
        _5704,
        _5707,
        _5709,
        _5710,
        _5711,
        _5713,
        _5714,
        _5716,
        _5718,
        _5720,
        _5721,
        _5723,
        _5724,
        _5725,
        _5727,
        _5729,
        _5731,
        _5732,
        _5733,
        _5748,
        _5749,
        _5751,
        _5752,
        _5753,
        _5755,
        _5760,
        _5762,
        _5773,
        _5775,
        _5777,
        _5779,
        _5780,
        _5782,
        _5783,
        _5785,
        _5786,
        _5787,
        _5788,
        _5789,
        _5792,
        _5793,
        _5796,
        _5797,
        _5798,
        _5799,
        _5800,
        _5802,
        _5804,
        _5806,
        _5807,
        _5808,
        _5809,
        _5812,
        _5814,
        _5816,
        _5818,
        _5819,
        _5821,
        _5823,
        _5824,
        _5826,
        _5827,
        _5828,
        _5829,
        _5830,
        _5831,
        _5832,
        _5834,
        _5835,
        _5836,
        _5838,
        _5839,
        _5840,
        _5842,
        _5843,
        _5845,
    )
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6072,
    )
    from mastapy.system_model.analyses_and_results.system_deflections import _2787
    from mastapy.system_model.drawing import _2251
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartHarmonicAnalysis",)


Self = TypeVar("Self", bound="PartHarmonicAnalysis")


class PartHarmonicAnalysis(_7550.PartStaticLoadAnalysisCase):
    """PartHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_HARMONIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartHarmonicAnalysis")

    class _Cast_PartHarmonicAnalysis:
        """Special nested class for casting PartHarmonicAnalysis to subclasses."""

        def __init__(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
            parent: "PartHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5680.AbstractAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5680,
            )

            return self._parent._cast(_5680.AbstractAssemblyHarmonicAnalysis)

        @property
        def abstract_shaft_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5682.AbstractShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5682,
            )

            return self._parent._cast(_5682.AbstractShaftHarmonicAnalysis)

        @property
        def abstract_shaft_or_housing_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5683.AbstractShaftOrHousingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5683,
            )

            return self._parent._cast(_5683.AbstractShaftOrHousingHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5685.AGMAGleasonConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5685,
            )

            return self._parent._cast(_5685.AGMAGleasonConicalGearHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5687.AGMAGleasonConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5687,
            )

            return self._parent._cast(_5687.AGMAGleasonConicalGearSetHarmonicAnalysis)

        @property
        def assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5688.AssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5688,
            )

            return self._parent._cast(_5688.AssemblyHarmonicAnalysis)

        @property
        def bearing_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5689.BearingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5689,
            )

            return self._parent._cast(_5689.BearingHarmonicAnalysis)

        @property
        def belt_drive_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5691.BeltDriveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5691,
            )

            return self._parent._cast(_5691.BeltDriveHarmonicAnalysis)

        @property
        def bevel_differential_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5692.BevelDifferentialGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5692,
            )

            return self._parent._cast(_5692.BevelDifferentialGearHarmonicAnalysis)

        @property
        def bevel_differential_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5694.BevelDifferentialGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5694,
            )

            return self._parent._cast(_5694.BevelDifferentialGearSetHarmonicAnalysis)

        @property
        def bevel_differential_planet_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5695.BevelDifferentialPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5695,
            )

            return self._parent._cast(_5695.BevelDifferentialPlanetGearHarmonicAnalysis)

        @property
        def bevel_differential_sun_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5696.BevelDifferentialSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5696,
            )

            return self._parent._cast(_5696.BevelDifferentialSunGearHarmonicAnalysis)

        @property
        def bevel_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5697.BevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5697,
            )

            return self._parent._cast(_5697.BevelGearHarmonicAnalysis)

        @property
        def bevel_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5699.BevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5699,
            )

            return self._parent._cast(_5699.BevelGearSetHarmonicAnalysis)

        @property
        def bolted_joint_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5700.BoltedJointHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5700,
            )

            return self._parent._cast(_5700.BoltedJointHarmonicAnalysis)

        @property
        def bolt_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5701.BoltHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5701,
            )

            return self._parent._cast(_5701.BoltHarmonicAnalysis)

        @property
        def clutch_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5703.ClutchHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5703,
            )

            return self._parent._cast(_5703.ClutchHalfHarmonicAnalysis)

        @property
        def clutch_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5704.ClutchHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5704,
            )

            return self._parent._cast(_5704.ClutchHarmonicAnalysis)

        @property
        def component_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5707.ComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5707,
            )

            return self._parent._cast(_5707.ComponentHarmonicAnalysis)

        @property
        def concept_coupling_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5709.ConceptCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5709,
            )

            return self._parent._cast(_5709.ConceptCouplingHalfHarmonicAnalysis)

        @property
        def concept_coupling_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5710.ConceptCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5710,
            )

            return self._parent._cast(_5710.ConceptCouplingHarmonicAnalysis)

        @property
        def concept_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5711.ConceptGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5711,
            )

            return self._parent._cast(_5711.ConceptGearHarmonicAnalysis)

        @property
        def concept_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5713.ConceptGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5713,
            )

            return self._parent._cast(_5713.ConceptGearSetHarmonicAnalysis)

        @property
        def conical_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5714.ConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5714,
            )

            return self._parent._cast(_5714.ConicalGearHarmonicAnalysis)

        @property
        def conical_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5716.ConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5716,
            )

            return self._parent._cast(_5716.ConicalGearSetHarmonicAnalysis)

        @property
        def connector_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5718.ConnectorHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5718,
            )

            return self._parent._cast(_5718.ConnectorHarmonicAnalysis)

        @property
        def coupling_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5720.CouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5720,
            )

            return self._parent._cast(_5720.CouplingHalfHarmonicAnalysis)

        @property
        def coupling_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5721.CouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5721,
            )

            return self._parent._cast(_5721.CouplingHarmonicAnalysis)

        @property
        def cvt_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5723.CVTHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5723,
            )

            return self._parent._cast(_5723.CVTHarmonicAnalysis)

        @property
        def cvt_pulley_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5724.CVTPulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5724,
            )

            return self._parent._cast(_5724.CVTPulleyHarmonicAnalysis)

        @property
        def cycloidal_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5725.CycloidalAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5725,
            )

            return self._parent._cast(_5725.CycloidalAssemblyHarmonicAnalysis)

        @property
        def cycloidal_disc_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5727.CycloidalDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5727,
            )

            return self._parent._cast(_5727.CycloidalDiscHarmonicAnalysis)

        @property
        def cylindrical_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5729.CylindricalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5729,
            )

            return self._parent._cast(_5729.CylindricalGearHarmonicAnalysis)

        @property
        def cylindrical_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5731.CylindricalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5731,
            )

            return self._parent._cast(_5731.CylindricalGearSetHarmonicAnalysis)

        @property
        def cylindrical_planet_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5732.CylindricalPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5732,
            )

            return self._parent._cast(_5732.CylindricalPlanetGearHarmonicAnalysis)

        @property
        def datum_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5733.DatumHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5733,
            )

            return self._parent._cast(_5733.DatumHarmonicAnalysis)

        @property
        def external_cad_model_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5748.ExternalCADModelHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5748,
            )

            return self._parent._cast(_5748.ExternalCADModelHarmonicAnalysis)

        @property
        def face_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5749.FaceGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5749,
            )

            return self._parent._cast(_5749.FaceGearHarmonicAnalysis)

        @property
        def face_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5751.FaceGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5751,
            )

            return self._parent._cast(_5751.FaceGearSetHarmonicAnalysis)

        @property
        def fe_part_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5752.FEPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5752,
            )

            return self._parent._cast(_5752.FEPartHarmonicAnalysis)

        @property
        def flexible_pin_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5753.FlexiblePinAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5753,
            )

            return self._parent._cast(_5753.FlexiblePinAssemblyHarmonicAnalysis)

        @property
        def gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5755.GearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5755,
            )

            return self._parent._cast(_5755.GearHarmonicAnalysis)

        @property
        def gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5760.GearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5760,
            )

            return self._parent._cast(_5760.GearSetHarmonicAnalysis)

        @property
        def guide_dxf_model_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5762.GuideDxfModelHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5762,
            )

            return self._parent._cast(_5762.GuideDxfModelHarmonicAnalysis)

        @property
        def hypoid_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5773.HypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5773,
            )

            return self._parent._cast(_5773.HypoidGearHarmonicAnalysis)

        @property
        def hypoid_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5775.HypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5775,
            )

            return self._parent._cast(_5775.HypoidGearSetHarmonicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5777.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5777,
            )

            return self._parent._cast(
                _5777.KlingelnbergCycloPalloidConicalGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5779.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5779,
            )

            return self._parent._cast(
                _5779.KlingelnbergCycloPalloidConicalGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5780.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5780,
            )

            return self._parent._cast(
                _5780.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5782.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5782,
            )

            return self._parent._cast(
                _5782.KlingelnbergCycloPalloidHypoidGearSetHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5783.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5783,
            )

            return self._parent._cast(
                _5783.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5785.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5785,
            )

            return self._parent._cast(
                _5785.KlingelnbergCycloPalloidSpiralBevelGearSetHarmonicAnalysis
            )

        @property
        def mass_disc_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5786.MassDiscHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5786,
            )

            return self._parent._cast(_5786.MassDiscHarmonicAnalysis)

        @property
        def measurement_component_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5787.MeasurementComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5787,
            )

            return self._parent._cast(_5787.MeasurementComponentHarmonicAnalysis)

        @property
        def mountable_component_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5788.MountableComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5788,
            )

            return self._parent._cast(_5788.MountableComponentHarmonicAnalysis)

        @property
        def oil_seal_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5789.OilSealHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5789,
            )

            return self._parent._cast(_5789.OilSealHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5792.PartToPartShearCouplingHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5792,
            )

            return self._parent._cast(_5792.PartToPartShearCouplingHalfHarmonicAnalysis)

        @property
        def part_to_part_shear_coupling_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5793.PartToPartShearCouplingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5793,
            )

            return self._parent._cast(_5793.PartToPartShearCouplingHarmonicAnalysis)

        @property
        def planetary_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5796.PlanetaryGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5796,
            )

            return self._parent._cast(_5796.PlanetaryGearSetHarmonicAnalysis)

        @property
        def planet_carrier_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5797.PlanetCarrierHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5797,
            )

            return self._parent._cast(_5797.PlanetCarrierHarmonicAnalysis)

        @property
        def point_load_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5798.PointLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5798,
            )

            return self._parent._cast(_5798.PointLoadHarmonicAnalysis)

        @property
        def power_load_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5799.PowerLoadHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5799,
            )

            return self._parent._cast(_5799.PowerLoadHarmonicAnalysis)

        @property
        def pulley_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5800.PulleyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5800,
            )

            return self._parent._cast(_5800.PulleyHarmonicAnalysis)

        @property
        def ring_pins_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5802.RingPinsHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5802,
            )

            return self._parent._cast(_5802.RingPinsHarmonicAnalysis)

        @property
        def rolling_ring_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5804.RollingRingAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5804,
            )

            return self._parent._cast(_5804.RollingRingAssemblyHarmonicAnalysis)

        @property
        def rolling_ring_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5806.RollingRingHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5806,
            )

            return self._parent._cast(_5806.RollingRingHarmonicAnalysis)

        @property
        def root_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5807.RootAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5807,
            )

            return self._parent._cast(_5807.RootAssemblyHarmonicAnalysis)

        @property
        def shaft_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5808.ShaftHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5808,
            )

            return self._parent._cast(_5808.ShaftHarmonicAnalysis)

        @property
        def shaft_hub_connection_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5809.ShaftHubConnectionHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5809,
            )

            return self._parent._cast(_5809.ShaftHubConnectionHarmonicAnalysis)

        @property
        def specialised_assembly_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5812.SpecialisedAssemblyHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5812,
            )

            return self._parent._cast(_5812.SpecialisedAssemblyHarmonicAnalysis)

        @property
        def spiral_bevel_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5814.SpiralBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5814,
            )

            return self._parent._cast(_5814.SpiralBevelGearHarmonicAnalysis)

        @property
        def spiral_bevel_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5816.SpiralBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5816,
            )

            return self._parent._cast(_5816.SpiralBevelGearSetHarmonicAnalysis)

        @property
        def spring_damper_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5818.SpringDamperHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5818,
            )

            return self._parent._cast(_5818.SpringDamperHalfHarmonicAnalysis)

        @property
        def spring_damper_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5819.SpringDamperHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5819,
            )

            return self._parent._cast(_5819.SpringDamperHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5821.StraightBevelDiffGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5821,
            )

            return self._parent._cast(_5821.StraightBevelDiffGearHarmonicAnalysis)

        @property
        def straight_bevel_diff_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5823.StraightBevelDiffGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5823,
            )

            return self._parent._cast(_5823.StraightBevelDiffGearSetHarmonicAnalysis)

        @property
        def straight_bevel_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5824.StraightBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5824,
            )

            return self._parent._cast(_5824.StraightBevelGearHarmonicAnalysis)

        @property
        def straight_bevel_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5826.StraightBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5826,
            )

            return self._parent._cast(_5826.StraightBevelGearSetHarmonicAnalysis)

        @property
        def straight_bevel_planet_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5827.StraightBevelPlanetGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5827,
            )

            return self._parent._cast(_5827.StraightBevelPlanetGearHarmonicAnalysis)

        @property
        def straight_bevel_sun_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5828.StraightBevelSunGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5828,
            )

            return self._parent._cast(_5828.StraightBevelSunGearHarmonicAnalysis)

        @property
        def synchroniser_half_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5829.SynchroniserHalfHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5829,
            )

            return self._parent._cast(_5829.SynchroniserHalfHarmonicAnalysis)

        @property
        def synchroniser_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5830.SynchroniserHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5830,
            )

            return self._parent._cast(_5830.SynchroniserHarmonicAnalysis)

        @property
        def synchroniser_part_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5831.SynchroniserPartHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5831,
            )

            return self._parent._cast(_5831.SynchroniserPartHarmonicAnalysis)

        @property
        def synchroniser_sleeve_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5832.SynchroniserSleeveHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5832,
            )

            return self._parent._cast(_5832.SynchroniserSleeveHarmonicAnalysis)

        @property
        def torque_converter_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5834.TorqueConverterHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5834,
            )

            return self._parent._cast(_5834.TorqueConverterHarmonicAnalysis)

        @property
        def torque_converter_pump_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5835.TorqueConverterPumpHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5835,
            )

            return self._parent._cast(_5835.TorqueConverterPumpHarmonicAnalysis)

        @property
        def torque_converter_turbine_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5836.TorqueConverterTurbineHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5836,
            )

            return self._parent._cast(_5836.TorqueConverterTurbineHarmonicAnalysis)

        @property
        def unbalanced_mass_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5838.UnbalancedMassHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5838,
            )

            return self._parent._cast(_5838.UnbalancedMassHarmonicAnalysis)

        @property
        def virtual_component_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5839.VirtualComponentHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5839,
            )

            return self._parent._cast(_5839.VirtualComponentHarmonicAnalysis)

        @property
        def worm_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5840.WormGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5840,
            )

            return self._parent._cast(_5840.WormGearHarmonicAnalysis)

        @property
        def worm_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5842.WormGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5842,
            )

            return self._parent._cast(_5842.WormGearSetHarmonicAnalysis)

        @property
        def zerol_bevel_gear_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5843.ZerolBevelGearHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5843,
            )

            return self._parent._cast(_5843.ZerolBevelGearHarmonicAnalysis)

        @property
        def zerol_bevel_gear_set_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "_5845.ZerolBevelGearSetHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5845,
            )

            return self._parent._cast(_5845.ZerolBevelGearSetHarmonicAnalysis)

        @property
        def part_harmonic_analysis(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis",
        ) -> "PartHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartHarmonicAnalysis.TYPE"):
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
    def coupled_modal_analysis(self: Self) -> "_4664.PartModalAnalysis":
        """mastapy.system_model.analyses_and_results.modal_analyses.PartModalAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CoupledModalAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis(self: Self) -> "_5763.HarmonicAnalysis":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysis

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analysis_options(self: Self) -> "_5768.HarmonicAnalysisOptions":
        """mastapy.system_model.analyses_and_results.harmonic_analyses.HarmonicAnalysisOptions

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysisOptions

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def harmonic_analyses_of_single_excitations(
        self: Self,
    ) -> "List[_6072.HarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.HarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.HarmonicAnalysesOfSingleExcitations

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

    def create_viewable(self: Self) -> "_2251.HarmonicAnalysisViewable":
        """mastapy.system_model.drawing.HarmonicAnalysisViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartHarmonicAnalysis._Cast_PartHarmonicAnalysis":
        return self._Cast_PartHarmonicAnalysis(self)
