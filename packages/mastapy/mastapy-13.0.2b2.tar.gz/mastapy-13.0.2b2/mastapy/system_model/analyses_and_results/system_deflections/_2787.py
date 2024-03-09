"""PartSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from PIL.Image import Image

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7549
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "PartSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2470
    from mastapy.math_utility import _1520
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2827,
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
    from mastapy.system_model.analyses_and_results.power_flows import _4116
    from mastapy.system_model.drawing import _2262
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartSystemDeflection",)


Self = TypeVar("Self", bound="PartSystemDeflection")


class PartSystemDeflection(_7549.PartFEAnalysis):
    """PartSystemDeflection

    This is a mastapy class.
    """

    TYPE = _PART_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartSystemDeflection")

    class _Cast_PartSystemDeflection:
        """Special nested class for casting PartSystemDeflection to subclasses."""

        def __init__(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
            parent: "PartSystemDeflection",
        ):
            self._parent = parent

        @property
        def part_fe_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_7549.PartFEAnalysis":
            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2687.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AbstractAssemblySystemDeflection)

        @property
        def abstract_shaft_or_housing_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2688.AbstractShaftOrHousingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2688,
            )

            return self._parent._cast(_2688.AbstractShaftOrHousingSystemDeflection)

        @property
        def abstract_shaft_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2689.AbstractShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2689,
            )

            return self._parent._cast(_2689.AbstractShaftSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2692.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2692,
            )

            return self._parent._cast(_2692.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2693.AGMAGleasonConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2693,
            )

            return self._parent._cast(_2693.AGMAGleasonConicalGearSystemDeflection)

        @property
        def assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2694.AssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2694,
            )

            return self._parent._cast(_2694.AssemblySystemDeflection)

        @property
        def bearing_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2700.BearingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2700,
            )

            return self._parent._cast(_2700.BearingSystemDeflection)

        @property
        def belt_drive_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2702.BeltDriveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2702,
            )

            return self._parent._cast(_2702.BeltDriveSystemDeflection)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2704.BevelDifferentialGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2704,
            )

            return self._parent._cast(_2704.BevelDifferentialGearSetSystemDeflection)

        @property
        def bevel_differential_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2705.BevelDifferentialGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2705,
            )

            return self._parent._cast(_2705.BevelDifferentialGearSystemDeflection)

        @property
        def bevel_differential_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2706.BevelDifferentialPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2706,
            )

            return self._parent._cast(_2706.BevelDifferentialPlanetGearSystemDeflection)

        @property
        def bevel_differential_sun_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2707.BevelDifferentialSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2707,
            )

            return self._parent._cast(_2707.BevelDifferentialSunGearSystemDeflection)

        @property
        def bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2709.BevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2709,
            )

            return self._parent._cast(_2709.BevelGearSetSystemDeflection)

        @property
        def bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2710.BevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2710,
            )

            return self._parent._cast(_2710.BevelGearSystemDeflection)

        @property
        def bolted_joint_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2711.BoltedJointSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2711,
            )

            return self._parent._cast(_2711.BoltedJointSystemDeflection)

        @property
        def bolt_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2712.BoltSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2712,
            )

            return self._parent._cast(_2712.BoltSystemDeflection)

        @property
        def clutch_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2714.ClutchHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2714,
            )

            return self._parent._cast(_2714.ClutchHalfSystemDeflection)

        @property
        def clutch_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2715.ClutchSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2715,
            )

            return self._parent._cast(_2715.ClutchSystemDeflection)

        @property
        def component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2717.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ComponentSystemDeflection)

        @property
        def concept_coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2720.ConceptCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2720,
            )

            return self._parent._cast(_2720.ConceptCouplingHalfSystemDeflection)

        @property
        def concept_coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2721.ConceptCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2721,
            )

            return self._parent._cast(_2721.ConceptCouplingSystemDeflection)

        @property
        def concept_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2723.ConceptGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2723,
            )

            return self._parent._cast(_2723.ConceptGearSetSystemDeflection)

        @property
        def concept_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2724.ConceptGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2724,
            )

            return self._parent._cast(_2724.ConceptGearSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2727.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConicalGearSetSystemDeflection)

        @property
        def conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2728.ConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2728,
            )

            return self._parent._cast(_2728.ConicalGearSystemDeflection)

        @property
        def connector_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2730.ConnectorSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2730,
            )

            return self._parent._cast(_2730.ConnectorSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2732.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CouplingHalfSystemDeflection)

        @property
        def coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2733.CouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2733,
            )

            return self._parent._cast(_2733.CouplingSystemDeflection)

        @property
        def cvt_pulley_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2735.CVTPulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2735,
            )

            return self._parent._cast(_2735.CVTPulleySystemDeflection)

        @property
        def cvt_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2736.CVTSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2736,
            )

            return self._parent._cast(_2736.CVTSystemDeflection)

        @property
        def cycloidal_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2737.CycloidalAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2737,
            )

            return self._parent._cast(_2737.CycloidalAssemblySystemDeflection)

        @property
        def cycloidal_disc_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2740.CycloidalDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2740,
            )

            return self._parent._cast(_2740.CycloidalDiscSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2744.CylindricalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2744,
            )

            return self._parent._cast(_2744.CylindricalGearSetSystemDeflection)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2745.CylindricalGearSetSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2745,
            )

            return self._parent._cast(_2745.CylindricalGearSetSystemDeflectionTimestep)

        @property
        def cylindrical_gear_set_system_deflection_with_ltca_results(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2746.CylindricalGearSetSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2746,
            )

            return self._parent._cast(
                _2746.CylindricalGearSetSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2747.CylindricalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2747,
            )

            return self._parent._cast(_2747.CylindricalGearSystemDeflection)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2748.CylindricalGearSystemDeflectionTimestep":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2748,
            )

            return self._parent._cast(_2748.CylindricalGearSystemDeflectionTimestep)

        @property
        def cylindrical_gear_system_deflection_with_ltca_results(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2749.CylindricalGearSystemDeflectionWithLTCAResults":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2749,
            )

            return self._parent._cast(
                _2749.CylindricalGearSystemDeflectionWithLTCAResults
            )

        @property
        def cylindrical_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2752.CylindricalPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2752,
            )

            return self._parent._cast(_2752.CylindricalPlanetGearSystemDeflection)

        @property
        def datum_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2753.DatumSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2753,
            )

            return self._parent._cast(_2753.DatumSystemDeflection)

        @property
        def external_cad_model_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2754.ExternalCADModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2754,
            )

            return self._parent._cast(_2754.ExternalCADModelSystemDeflection)

        @property
        def face_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2757.FaceGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2757,
            )

            return self._parent._cast(_2757.FaceGearSetSystemDeflection)

        @property
        def face_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2758.FaceGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2758,
            )

            return self._parent._cast(_2758.FaceGearSystemDeflection)

        @property
        def fe_part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2759.FEPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2759,
            )

            return self._parent._cast(_2759.FEPartSystemDeflection)

        @property
        def flexible_pin_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2760.FlexiblePinAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2760,
            )

            return self._parent._cast(_2760.FlexiblePinAssemblySystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2762.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.GearSetSystemDeflection)

        @property
        def gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2763.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.GearSystemDeflection)

        @property
        def guide_dxf_model_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2764.GuideDxfModelSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2764,
            )

            return self._parent._cast(_2764.GuideDxfModelSystemDeflection)

        @property
        def hypoid_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2766.HypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2766,
            )

            return self._parent._cast(_2766.HypoidGearSetSystemDeflection)

        @property
        def hypoid_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2767.HypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2767,
            )

            return self._parent._cast(_2767.HypoidGearSystemDeflection)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2771.KlingelnbergCycloPalloidConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2771,
            )

            return self._parent._cast(
                _2771.KlingelnbergCycloPalloidConicalGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2772.KlingelnbergCycloPalloidConicalGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2772,
            )

            return self._parent._cast(
                _2772.KlingelnbergCycloPalloidConicalGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2774.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2774,
            )

            return self._parent._cast(
                _2774.KlingelnbergCycloPalloidHypoidGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2775.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2777.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2777,
            )

            return self._parent._cast(
                _2777.KlingelnbergCycloPalloidSpiralBevelGearSetSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2778.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(
                _2778.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def mass_disc_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2781.MassDiscSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2781,
            )

            return self._parent._cast(_2781.MassDiscSystemDeflection)

        @property
        def measurement_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2782.MeasurementComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2782,
            )

            return self._parent._cast(_2782.MeasurementComponentSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2784.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.MountableComponentSystemDeflection)

        @property
        def oil_seal_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2786.OilSealSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2786,
            )

            return self._parent._cast(_2786.OilSealSystemDeflection)

        @property
        def part_to_part_shear_coupling_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2789.PartToPartShearCouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2789,
            )

            return self._parent._cast(_2789.PartToPartShearCouplingHalfSystemDeflection)

        @property
        def part_to_part_shear_coupling_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2790.PartToPartShearCouplingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2790,
            )

            return self._parent._cast(_2790.PartToPartShearCouplingSystemDeflection)

        @property
        def planet_carrier_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2792.PlanetCarrierSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2792,
            )

            return self._parent._cast(_2792.PlanetCarrierSystemDeflection)

        @property
        def point_load_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2793.PointLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2793,
            )

            return self._parent._cast(_2793.PointLoadSystemDeflection)

        @property
        def power_load_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2794.PowerLoadSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2794,
            )

            return self._parent._cast(_2794.PowerLoadSystemDeflection)

        @property
        def pulley_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2795.PulleySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2795,
            )

            return self._parent._cast(_2795.PulleySystemDeflection)

        @property
        def ring_pins_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2796.RingPinsSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2796,
            )

            return self._parent._cast(_2796.RingPinsSystemDeflection)

        @property
        def rolling_ring_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2799.RollingRingAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2799,
            )

            return self._parent._cast(_2799.RollingRingAssemblySystemDeflection)

        @property
        def rolling_ring_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2801.RollingRingSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2801,
            )

            return self._parent._cast(_2801.RollingRingSystemDeflection)

        @property
        def root_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2802.RootAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2802,
            )

            return self._parent._cast(_2802.RootAssemblySystemDeflection)

        @property
        def shaft_hub_connection_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2803.ShaftHubConnectionSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2803,
            )

            return self._parent._cast(_2803.ShaftHubConnectionSystemDeflection)

        @property
        def shaft_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2806.ShaftSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2806,
            )

            return self._parent._cast(_2806.ShaftSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2808.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpecialisedAssemblySystemDeflection)

        @property
        def spiral_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2810.SpiralBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2810,
            )

            return self._parent._cast(_2810.SpiralBevelGearSetSystemDeflection)

        @property
        def spiral_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2811.SpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2811,
            )

            return self._parent._cast(_2811.SpiralBevelGearSystemDeflection)

        @property
        def spring_damper_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2813.SpringDamperHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2813,
            )

            return self._parent._cast(_2813.SpringDamperHalfSystemDeflection)

        @property
        def spring_damper_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2814.SpringDamperSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2814,
            )

            return self._parent._cast(_2814.SpringDamperSystemDeflection)

        @property
        def straight_bevel_diff_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2816.StraightBevelDiffGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2816,
            )

            return self._parent._cast(_2816.StraightBevelDiffGearSetSystemDeflection)

        @property
        def straight_bevel_diff_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2817.StraightBevelDiffGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2817,
            )

            return self._parent._cast(_2817.StraightBevelDiffGearSystemDeflection)

        @property
        def straight_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2819.StraightBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2819,
            )

            return self._parent._cast(_2819.StraightBevelGearSetSystemDeflection)

        @property
        def straight_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2820.StraightBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2820,
            )

            return self._parent._cast(_2820.StraightBevelGearSystemDeflection)

        @property
        def straight_bevel_planet_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2821.StraightBevelPlanetGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2821,
            )

            return self._parent._cast(_2821.StraightBevelPlanetGearSystemDeflection)

        @property
        def straight_bevel_sun_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2822.StraightBevelSunGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2822,
            )

            return self._parent._cast(_2822.StraightBevelSunGearSystemDeflection)

        @property
        def synchroniser_half_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2823.SynchroniserHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2823,
            )

            return self._parent._cast(_2823.SynchroniserHalfSystemDeflection)

        @property
        def synchroniser_part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2824.SynchroniserPartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2824,
            )

            return self._parent._cast(_2824.SynchroniserPartSystemDeflection)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2825.SynchroniserSleeveSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2825,
            )

            return self._parent._cast(_2825.SynchroniserSleeveSystemDeflection)

        @property
        def synchroniser_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2826.SynchroniserSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2826,
            )

            return self._parent._cast(_2826.SynchroniserSystemDeflection)

        @property
        def torque_converter_pump_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2831.TorqueConverterPumpSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2831,
            )

            return self._parent._cast(_2831.TorqueConverterPumpSystemDeflection)

        @property
        def torque_converter_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2832.TorqueConverterSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2832,
            )

            return self._parent._cast(_2832.TorqueConverterSystemDeflection)

        @property
        def torque_converter_turbine_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2833.TorqueConverterTurbineSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2833,
            )

            return self._parent._cast(_2833.TorqueConverterTurbineSystemDeflection)

        @property
        def unbalanced_mass_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2836.UnbalancedMassSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2836,
            )

            return self._parent._cast(_2836.UnbalancedMassSystemDeflection)

        @property
        def virtual_component_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2837.VirtualComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2837,
            )

            return self._parent._cast(_2837.VirtualComponentSystemDeflection)

        @property
        def worm_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2839.WormGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2839,
            )

            return self._parent._cast(_2839.WormGearSetSystemDeflection)

        @property
        def worm_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2840.WormGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2840,
            )

            return self._parent._cast(_2840.WormGearSystemDeflection)

        @property
        def zerol_bevel_gear_set_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2842.ZerolBevelGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2842,
            )

            return self._parent._cast(_2842.ZerolBevelGearSetSystemDeflection)

        @property
        def zerol_bevel_gear_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "_2843.ZerolBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2843,
            )

            return self._parent._cast(_2843.ZerolBevelGearSystemDeflection)

        @property
        def part_system_deflection(
            self: "PartSystemDeflection._Cast_PartSystemDeflection",
        ) -> "PartSystemDeflection":
            return self._parent

        def __getattr__(
            self: "PartSystemDeflection._Cast_PartSystemDeflection", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartSystemDeflection.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def two_d_drawing_showing_axial_forces(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingAxialForces

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

    @property
    def two_d_drawing_showing_power_flow(self: Self) -> "Image":
        """Image

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TwoDDrawingShowingPowerFlow

        if temp is None:
            return None

        value = conversion.pn_to_mp_smt_bitmap(temp)

        if value is None:
            return None

        return value

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
    def mass_properties_from_node_model(self: Self) -> "_1520.MassProperties":
        """mastapy.math_utility.MassProperties

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MassPropertiesFromNodeModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection(self: Self) -> "_2827.SystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.SystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflection

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4116.PartPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.PartPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    def create_viewable(self: Self) -> "_2262.SystemDeflectionViewable":
        """mastapy.system_model.drawing.SystemDeflectionViewable"""
        method_result = self.wrapped.CreateViewable()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "PartSystemDeflection._Cast_PartSystemDeflection":
        return self._Cast_PartSystemDeflection(self)
