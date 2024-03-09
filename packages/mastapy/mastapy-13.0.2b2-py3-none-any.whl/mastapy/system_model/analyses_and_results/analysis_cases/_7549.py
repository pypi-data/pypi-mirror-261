"""PartFEAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_FE_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases", "PartFEAnalysis"
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2687,
        _2688,
        _2689,
        _2692,
        _2693,
        _2694,
        _2700,
        _2702,
        _2704,
        _2705,
        _2706,
        _2707,
        _2709,
        _2710,
        _2711,
        _2712,
        _2714,
        _2715,
        _2717,
        _2720,
        _2721,
        _2723,
        _2724,
        _2727,
        _2728,
        _2730,
        _2732,
        _2733,
        _2735,
        _2736,
        _2737,
        _2740,
        _2744,
        _2745,
        _2746,
        _2747,
        _2748,
        _2749,
        _2752,
        _2753,
        _2754,
        _2757,
        _2758,
        _2759,
        _2760,
        _2762,
        _2763,
        _2764,
        _2766,
        _2767,
        _2771,
        _2772,
        _2774,
        _2775,
        _2777,
        _2778,
        _2781,
        _2782,
        _2784,
        _2786,
        _2787,
        _2789,
        _2790,
        _2792,
        _2793,
        _2794,
        _2795,
        _2796,
        _2799,
        _2801,
        _2802,
        _2803,
        _2806,
        _2808,
        _2810,
        _2811,
        _2813,
        _2814,
        _2816,
        _2817,
        _2819,
        _2820,
        _2821,
        _2822,
        _2823,
        _2824,
        _2825,
        _2826,
        _2831,
        _2832,
        _2833,
        _2836,
        _2837,
        _2839,
        _2840,
        _2842,
        _2843,
    )
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6279,
        _6280,
        _6281,
        _6283,
        _6285,
        _6286,
        _6287,
        _6289,
        _6290,
        _6292,
        _6293,
        _6294,
        _6295,
        _6297,
        _6298,
        _6299,
        _6301,
        _6302,
        _6304,
        _6306,
        _6307,
        _6308,
        _6310,
        _6311,
        _6313,
        _6315,
        _6317,
        _6318,
        _6320,
        _6321,
        _6322,
        _6324,
        _6326,
        _6328,
        _6329,
        _6330,
        _6333,
        _6334,
        _6336,
        _6337,
        _6338,
        _6339,
        _6341,
        _6342,
        _6343,
        _6345,
        _6347,
        _6349,
        _6350,
        _6352,
        _6353,
        _6355,
        _6356,
        _6357,
        _6358,
        _6359,
        _6360,
        _6362,
        _6363,
        _6365,
        _6366,
        _6367,
        _6368,
        _6369,
        _6370,
        _6372,
        _6374,
        _6375,
        _6376,
        _6377,
        _6379,
        _6380,
        _6382,
        _6384,
        _6385,
        _6386,
        _6388,
        _6389,
        _6391,
        _6392,
        _6393,
        _6394,
        _6395,
        _6396,
        _6397,
        _6399,
        _6400,
        _6401,
        _6402,
        _6403,
        _6404,
        _6406,
        _6407,
        _6409,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartFEAnalysis",)


Self = TypeVar("Self", bound="PartFEAnalysis")


class PartFEAnalysis(_7550.PartStaticLoadAnalysisCase):
    """PartFEAnalysis

    This is a mastapy class.
    """

    TYPE = _PART_FE_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartFEAnalysis")

    class _Cast_PartFEAnalysis:
        """Special nested class for casting PartFEAnalysis to subclasses."""

        def __init__(
            self: "PartFEAnalysis._Cast_PartFEAnalysis", parent: "PartFEAnalysis"
        ):
            self._parent = parent

        @property
        def part_static_load_analysis_case(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2687.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2688.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2689.AbstractShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2692.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2692,
            )

            return self._parent._cast(_2692.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2693.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2693,
            )

            return self._parent._cast(_2693.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2694.AssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2694,
            )

            return self._parent._cast(_2694.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2700.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2702.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2704.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2705.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2706.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2707.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2709.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2710.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2711.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2712.BoltSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2714.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2715.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ClutchSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2717.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2720.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2721.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2723.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2724.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2727.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2728.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2730.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2732.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2733.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2735.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2736.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2737.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2737,
            )

            return self._parent._cast(_2737.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2740.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2744.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2745.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(_2745.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2746.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2746,
            )

            return self._parent._cast(
                _2746.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2747.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2748.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2749.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(
                _2749.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2752.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2753.DatumSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2754.ExternalCADModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2757.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2758.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2759.FEPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2760.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2762.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.GearSetSystemDeflection)

        @property
        def gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2763.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2764.GuideDxfModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2766.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2767.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(_2767.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2771.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(
                _2771.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2772.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2774.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(
                _2774.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2775.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2777.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(
                _2777.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2778.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(
                _2778.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2781.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2782.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2784.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2786.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.OilSealSystemDeflection)

        @property
        def part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2787.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2789.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2790.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2792.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2793.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2794.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(_2794.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2795.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2796.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2799.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2801.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2802.RootAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2803.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2806.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2808.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2810.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2811.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2813.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2814.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2816.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2817.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2819.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2820.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2821.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2822.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2823.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2824.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2825.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2826.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2831.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2832.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2833.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2836.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2837.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2839.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2840.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2842.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_2843.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.ZerolBevelGearSystemDeflection)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6279.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AbstractAssemblyDynamicAnalysis)

        @property
        def abstract_shaft_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6280.AbstractShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6280

            return self._parent._cast(_6280.AbstractShaftDynamicAnalysis)

        @property
        def abstract_shaft_or_housing_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6281.AbstractShaftOrHousingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6281

            return self._parent._cast(_6281.AbstractShaftOrHousingDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6283.AGMAGleasonConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6283

            return self._parent._cast(_6283.AGMAGleasonConicalGearDynamicAnalysis)

        @property
        def agma_gleason_conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6285.AGMAGleasonConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6285

            return self._parent._cast(_6285.AGMAGleasonConicalGearSetDynamicAnalysis)

        @property
        def assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6286.AssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6286

            return self._parent._cast(_6286.AssemblyDynamicAnalysis)

        @property
        def bearing_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6287.BearingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6287

            return self._parent._cast(_6287.BearingDynamicAnalysis)

        @property
        def belt_drive_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6289.BeltDriveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6289

            return self._parent._cast(_6289.BeltDriveDynamicAnalysis)

        @property
        def bevel_differential_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6290.BevelDifferentialGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6290

            return self._parent._cast(_6290.BevelDifferentialGearDynamicAnalysis)

        @property
        def bevel_differential_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6292.BevelDifferentialGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6292

            return self._parent._cast(_6292.BevelDifferentialGearSetDynamicAnalysis)

        @property
        def bevel_differential_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6293.BevelDifferentialPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6293

            return self._parent._cast(_6293.BevelDifferentialPlanetGearDynamicAnalysis)

        @property
        def bevel_differential_sun_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6294.BevelDifferentialSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6294

            return self._parent._cast(_6294.BevelDifferentialSunGearDynamicAnalysis)

        @property
        def bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6295.BevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6295

            return self._parent._cast(_6295.BevelGearDynamicAnalysis)

        @property
        def bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6297.BevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6297

            return self._parent._cast(_6297.BevelGearSetDynamicAnalysis)

        @property
        def bolt_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6298.BoltDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6298

            return self._parent._cast(_6298.BoltDynamicAnalysis)

        @property
        def bolted_joint_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6299.BoltedJointDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6299

            return self._parent._cast(_6299.BoltedJointDynamicAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6301.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ClutchDynamicAnalysis)

        @property
        def clutch_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6302.ClutchHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6302

            return self._parent._cast(_6302.ClutchHalfDynamicAnalysis)

        @property
        def component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6304.ComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6304

            return self._parent._cast(_6304.ComponentDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6306.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.ConceptCouplingDynamicAnalysis)

        @property
        def concept_coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6307.ConceptCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6307

            return self._parent._cast(_6307.ConceptCouplingHalfDynamicAnalysis)

        @property
        def concept_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6308.ConceptGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6308

            return self._parent._cast(_6308.ConceptGearDynamicAnalysis)

        @property
        def concept_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6310.ConceptGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6310

            return self._parent._cast(_6310.ConceptGearSetDynamicAnalysis)

        @property
        def conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6311.ConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6311

            return self._parent._cast(_6311.ConicalGearDynamicAnalysis)

        @property
        def conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6313.ConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6313

            return self._parent._cast(_6313.ConicalGearSetDynamicAnalysis)

        @property
        def connector_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6315.ConnectorDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6315

            return self._parent._cast(_6315.ConnectorDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6317.CouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6317

            return self._parent._cast(_6317.CouplingDynamicAnalysis)

        @property
        def coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6318.CouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6318

            return self._parent._cast(_6318.CouplingHalfDynamicAnalysis)

        @property
        def cvt_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6320.CVTDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6320

            return self._parent._cast(_6320.CVTDynamicAnalysis)

        @property
        def cvt_pulley_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6321.CVTPulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6321

            return self._parent._cast(_6321.CVTPulleyDynamicAnalysis)

        @property
        def cycloidal_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6322.CycloidalAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6322

            return self._parent._cast(_6322.CycloidalAssemblyDynamicAnalysis)

        @property
        def cycloidal_disc_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6324.CycloidalDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6324

            return self._parent._cast(_6324.CycloidalDiscDynamicAnalysis)

        @property
        def cylindrical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6326.CylindricalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6326

            return self._parent._cast(_6326.CylindricalGearDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6328.CylindricalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6328

            return self._parent._cast(_6328.CylindricalGearSetDynamicAnalysis)

        @property
        def cylindrical_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6329.CylindricalPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6329

            return self._parent._cast(_6329.CylindricalPlanetGearDynamicAnalysis)

        @property
        def datum_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6330.DatumDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6330

            return self._parent._cast(_6330.DatumDynamicAnalysis)

        @property
        def external_cad_model_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6333.ExternalCADModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6333

            return self._parent._cast(_6333.ExternalCADModelDynamicAnalysis)

        @property
        def face_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6334.FaceGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6334

            return self._parent._cast(_6334.FaceGearDynamicAnalysis)

        @property
        def face_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6336.FaceGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6336

            return self._parent._cast(_6336.FaceGearSetDynamicAnalysis)

        @property
        def fe_part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6337.FEPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6337

            return self._parent._cast(_6337.FEPartDynamicAnalysis)

        @property
        def flexible_pin_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6338.FlexiblePinAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6338

            return self._parent._cast(_6338.FlexiblePinAssemblyDynamicAnalysis)

        @property
        def gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6339.GearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6339

            return self._parent._cast(_6339.GearDynamicAnalysis)

        @property
        def gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6341.GearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341

            return self._parent._cast(_6341.GearSetDynamicAnalysis)

        @property
        def guide_dxf_model_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6342.GuideDxfModelDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6342

            return self._parent._cast(_6342.GuideDxfModelDynamicAnalysis)

        @property
        def hypoid_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6343.HypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6343

            return self._parent._cast(_6343.HypoidGearDynamicAnalysis)

        @property
        def hypoid_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6345.HypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6345

            return self._parent._cast(_6345.HypoidGearSetDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6347.KlingelnbergCycloPalloidConicalGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6347

            return self._parent._cast(
                _6347.KlingelnbergCycloPalloidConicalGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6349.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6349

            return self._parent._cast(
                _6349.KlingelnbergCycloPalloidConicalGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6350.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6350

            return self._parent._cast(
                _6350.KlingelnbergCycloPalloidHypoidGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6352.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6352

            return self._parent._cast(
                _6352.KlingelnbergCycloPalloidHypoidGearSetDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6353.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6353

            return self._parent._cast(
                _6353.KlingelnbergCycloPalloidSpiralBevelGearDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6355.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6355

            return self._parent._cast(
                _6355.KlingelnbergCycloPalloidSpiralBevelGearSetDynamicAnalysis
            )

        @property
        def mass_disc_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6356.MassDiscDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6356

            return self._parent._cast(_6356.MassDiscDynamicAnalysis)

        @property
        def measurement_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6357.MeasurementComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6357

            return self._parent._cast(_6357.MeasurementComponentDynamicAnalysis)

        @property
        def mountable_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6358.MountableComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6358

            return self._parent._cast(_6358.MountableComponentDynamicAnalysis)

        @property
        def oil_seal_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6359.OilSealDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6359

            return self._parent._cast(_6359.OilSealDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6360.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6362.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PartToPartShearCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6363.PartToPartShearCouplingHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6363

            return self._parent._cast(_6363.PartToPartShearCouplingHalfDynamicAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6365.PlanetaryGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.PlanetaryGearSetDynamicAnalysis)

        @property
        def planet_carrier_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6366.PlanetCarrierDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6366

            return self._parent._cast(_6366.PlanetCarrierDynamicAnalysis)

        @property
        def point_load_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6367.PointLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6367

            return self._parent._cast(_6367.PointLoadDynamicAnalysis)

        @property
        def power_load_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6368.PowerLoadDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6368

            return self._parent._cast(_6368.PowerLoadDynamicAnalysis)

        @property
        def pulley_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6369.PulleyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6369

            return self._parent._cast(_6369.PulleyDynamicAnalysis)

        @property
        def ring_pins_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6370.RingPinsDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6370

            return self._parent._cast(_6370.RingPinsDynamicAnalysis)

        @property
        def rolling_ring_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6372.RollingRingAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6372

            return self._parent._cast(_6372.RollingRingAssemblyDynamicAnalysis)

        @property
        def rolling_ring_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6374.RollingRingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6374

            return self._parent._cast(_6374.RollingRingDynamicAnalysis)

        @property
        def root_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6375.RootAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6375

            return self._parent._cast(_6375.RootAssemblyDynamicAnalysis)

        @property
        def shaft_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6376.ShaftDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6376

            return self._parent._cast(_6376.ShaftDynamicAnalysis)

        @property
        def shaft_hub_connection_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6377.ShaftHubConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6377

            return self._parent._cast(_6377.ShaftHubConnectionDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6379.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpecialisedAssemblyDynamicAnalysis)

        @property
        def spiral_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6380.SpiralBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6380

            return self._parent._cast(_6380.SpiralBevelGearDynamicAnalysis)

        @property
        def spiral_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6382.SpiralBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6382

            return self._parent._cast(_6382.SpiralBevelGearSetDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6384.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.SpringDamperDynamicAnalysis)

        @property
        def spring_damper_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6385.SpringDamperHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6385

            return self._parent._cast(_6385.SpringDamperHalfDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6386.StraightBevelDiffGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6386

            return self._parent._cast(_6386.StraightBevelDiffGearDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6388.StraightBevelDiffGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6388

            return self._parent._cast(_6388.StraightBevelDiffGearSetDynamicAnalysis)

        @property
        def straight_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6389.StraightBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6389

            return self._parent._cast(_6389.StraightBevelGearDynamicAnalysis)

        @property
        def straight_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6391.StraightBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6391

            return self._parent._cast(_6391.StraightBevelGearSetDynamicAnalysis)

        @property
        def straight_bevel_planet_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6392.StraightBevelPlanetGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6392

            return self._parent._cast(_6392.StraightBevelPlanetGearDynamicAnalysis)

        @property
        def straight_bevel_sun_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6393.StraightBevelSunGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6393

            return self._parent._cast(_6393.StraightBevelSunGearDynamicAnalysis)

        @property
        def synchroniser_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6394.SynchroniserDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6394

            return self._parent._cast(_6394.SynchroniserDynamicAnalysis)

        @property
        def synchroniser_half_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6395.SynchroniserHalfDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6395

            return self._parent._cast(_6395.SynchroniserHalfDynamicAnalysis)

        @property
        def synchroniser_part_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6396.SynchroniserPartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6396

            return self._parent._cast(_6396.SynchroniserPartDynamicAnalysis)

        @property
        def synchroniser_sleeve_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6397.SynchroniserSleeveDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6397

            return self._parent._cast(_6397.SynchroniserSleeveDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6399.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.TorqueConverterDynamicAnalysis)

        @property
        def torque_converter_pump_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6400.TorqueConverterPumpDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6400

            return self._parent._cast(_6400.TorqueConverterPumpDynamicAnalysis)

        @property
        def torque_converter_turbine_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6401.TorqueConverterTurbineDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6401

            return self._parent._cast(_6401.TorqueConverterTurbineDynamicAnalysis)

        @property
        def unbalanced_mass_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6402.UnbalancedMassDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6402

            return self._parent._cast(_6402.UnbalancedMassDynamicAnalysis)

        @property
        def virtual_component_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6403.VirtualComponentDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6403

            return self._parent._cast(_6403.VirtualComponentDynamicAnalysis)

        @property
        def worm_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6404.WormGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6404

            return self._parent._cast(_6404.WormGearDynamicAnalysis)

        @property
        def worm_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6406.WormGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6406

            return self._parent._cast(_6406.WormGearSetDynamicAnalysis)

        @property
        def zerol_bevel_gear_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6407.ZerolBevelGearDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6407

            return self._parent._cast(_6407.ZerolBevelGearDynamicAnalysis)

        @property
        def zerol_bevel_gear_set_dynamic_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "_6409.ZerolBevelGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6409

            return self._parent._cast(_6409.ZerolBevelGearSetDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "PartFEAnalysis._Cast_PartFEAnalysis",
        ) -> "PartFEAnalysis":
            return self._parent

        def __getattr__(self: "PartFEAnalysis._Cast_PartFEAnalysis", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartFEAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(self: Self) -> "PartFEAnalysis._Cast_PartFEAnalysis":
        return self._Cast_PartFEAnalysis(self)
