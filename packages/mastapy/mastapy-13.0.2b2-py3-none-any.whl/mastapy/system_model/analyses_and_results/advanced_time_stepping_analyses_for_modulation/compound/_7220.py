"""MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
    _7168,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation.Compound",
    "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7091,
    )
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
        _7147,
        _7151,
        _7154,
        _7157,
        _7158,
        _7159,
        _7166,
        _7171,
        _7172,
        _7175,
        _7179,
        _7182,
        _7185,
        _7190,
        _7193,
        _7196,
        _7201,
        _7205,
        _7209,
        _7212,
        _7215,
        _7218,
        _7219,
        _7221,
        _7225,
        _7228,
        _7229,
        _7230,
        _7231,
        _7232,
        _7235,
        _7239,
        _7242,
        _7247,
        _7248,
        _7251,
        _7254,
        _7255,
        _7257,
        _7258,
        _7259,
        _7262,
        _7263,
        _7264,
        _7265,
        _7266,
        _7269,
        _7222,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation"
)


class MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation(
    _7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
):
    """MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
            parent: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7168.ComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7222,
            )

            return self._parent._cast(
                _7222.PartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7147.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7147,
            )

            return self._parent._cast(
                _7147.AGMAGleasonConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7151.BearingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7151,
            )

            return self._parent._cast(
                _7151.BearingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7154.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7154,
            )

            return self._parent._cast(
                _7154.BevelDifferentialGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7157.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7157,
            )

            return self._parent._cast(
                _7157.BevelDifferentialPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7158.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7158,
            )

            return self._parent._cast(
                _7158.BevelDifferentialSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7159.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7159,
            )

            return self._parent._cast(
                _7159.BevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7166.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7166,
            )

            return self._parent._cast(
                _7166.ClutchHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7171.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7171,
            )

            return self._parent._cast(
                _7171.ConceptCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7172.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7172,
            )

            return self._parent._cast(
                _7172.ConceptGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7175.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7175,
            )

            return self._parent._cast(
                _7175.ConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7179.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7179,
            )

            return self._parent._cast(
                _7179.ConnectorCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7182.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7182,
            )

            return self._parent._cast(
                _7182.CouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7185.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7185,
            )

            return self._parent._cast(
                _7185.CVTPulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7190.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7190,
            )

            return self._parent._cast(
                _7190.CylindricalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7193.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7193,
            )

            return self._parent._cast(
                _7193.CylindricalPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7196.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7196,
            )

            return self._parent._cast(
                _7196.FaceGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7201.GearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7201,
            )

            return self._parent._cast(
                _7201.GearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7205.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7205,
            )

            return self._parent._cast(
                _7205.HypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7209.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7209,
            )

            return self._parent._cast(
                _7209.KlingelnbergCycloPalloidConicalGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7212.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7212,
            )

            return self._parent._cast(
                _7212.KlingelnbergCycloPalloidHypoidGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7215.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7215,
            )

            return self._parent._cast(
                _7215.KlingelnbergCycloPalloidSpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7218.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7218,
            )

            return self._parent._cast(
                _7218.MassDiscCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7219.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7219,
            )

            return self._parent._cast(
                _7219.MeasurementComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7221.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7221,
            )

            return self._parent._cast(
                _7221.OilSealCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7225.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7225,
            )

            return self._parent._cast(
                _7225.PartToPartShearCouplingHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7228.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7228,
            )

            return self._parent._cast(
                _7228.PlanetCarrierCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7229.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7229,
            )

            return self._parent._cast(
                _7229.PointLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7230.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7230,
            )

            return self._parent._cast(
                _7230.PowerLoadCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7231.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7231,
            )

            return self._parent._cast(
                _7231.PulleyCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7232.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7232,
            )

            return self._parent._cast(
                _7232.RingPinsCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7235.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7235,
            )

            return self._parent._cast(
                _7235.RollingRingCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7239.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7239,
            )

            return self._parent._cast(
                _7239.ShaftHubConnectionCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7242.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7242,
            )

            return self._parent._cast(
                _7242.SpiralBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7247.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7247,
            )

            return self._parent._cast(
                _7247.SpringDamperHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7248.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7248,
            )

            return self._parent._cast(
                _7248.StraightBevelDiffGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7251.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7251,
            )

            return self._parent._cast(
                _7251.StraightBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7254.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7254,
            )

            return self._parent._cast(
                _7254.StraightBevelPlanetGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7255.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7255,
            )

            return self._parent._cast(
                _7255.StraightBevelSunGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7257.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7257,
            )

            return self._parent._cast(
                _7257.SynchroniserHalfCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7258.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7258,
            )

            return self._parent._cast(
                _7258.SynchroniserPartCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7259.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7259,
            )

            return self._parent._cast(
                _7259.SynchroniserSleeveCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7262.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7262,
            )

            return self._parent._cast(
                _7262.TorqueConverterPumpCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7263.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7263,
            )

            return self._parent._cast(
                _7263.TorqueConverterTurbineCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7264.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7264,
            )

            return self._parent._cast(
                _7264.UnbalancedMassCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7265.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7265,
            )

            return self._parent._cast(
                _7265.VirtualComponentCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7266.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7266,
            )

            return self._parent._cast(
                _7266.WormGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7269.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.compound import (
                _7269,
            )

            return self._parent._cast(
                _7269.ZerolBevelGearCompoundAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_compound_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
        ) -> "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation",
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
        self: Self,
        instance_to_wrap: "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_7091.MountableComponentAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.MountableComponentAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_7091.MountableComponentAdvancedTimeSteppingAnalysisForModulation]":
        """List[mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation.MountableComponentAdvancedTimeSteppingAnalysisForModulation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_MountableComponentCompoundAdvancedTimeSteppingAnalysisForModulation(
            self
        )
