"""MountableComponentAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7038,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2466
    from mastapy.system_model.analyses_and_results.system_deflections import _2784
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7016,
        _7021,
        _7024,
        _7027,
        _7028,
        _7029,
        _7036,
        _7041,
        _7042,
        _7045,
        _7049,
        _7052,
        _7055,
        _7060,
        _7063,
        _7066,
        _7071,
        _7076,
        _7080,
        _7083,
        _7086,
        _7089,
        _7090,
        _7092,
        _7096,
        _7099,
        _7100,
        _7101,
        _7102,
        _7103,
        _7105,
        _7110,
        _7113,
        _7118,
        _7119,
        _7122,
        _7125,
        _7126,
        _7128,
        _7129,
        _7130,
        _7133,
        _7134,
        _7135,
        _7136,
        _7137,
        _7140,
        _7093,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="MountableComponentAdvancedTimeSteppingAnalysisForModulation"
)


class MountableComponentAdvancedTimeSteppingAnalysisForModulation(
    _7038.ComponentAdvancedTimeSteppingAnalysisForModulation
):
    """MountableComponentAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting MountableComponentAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
            parent: "MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7038.ComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7038.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7093.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7016.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7016,
            )

            return self._parent._cast(
                _7016.AGMAGleasonConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bearing_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7021.BearingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7021,
            )

            return self._parent._cast(
                _7021.BearingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7024.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7024,
            )

            return self._parent._cast(
                _7024.BevelDifferentialGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7027.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7027,
            )

            return self._parent._cast(
                _7027.BevelDifferentialPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_differential_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7028.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7028,
            )

            return self._parent._cast(
                _7028.BevelDifferentialSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7029.BevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7029,
            )

            return self._parent._cast(
                _7029.BevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def clutch_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7036.ClutchHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7036,
            )

            return self._parent._cast(
                _7036.ClutchHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7041.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7041,
            )

            return self._parent._cast(
                _7041.ConceptCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def concept_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7042.ConceptGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7042,
            )

            return self._parent._cast(
                _7042.ConceptGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7045.ConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7045,
            )

            return self._parent._cast(
                _7045.ConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connector_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7049.ConnectorAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7049,
            )

            return self._parent._cast(
                _7049.ConnectorAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7052.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7052,
            )

            return self._parent._cast(
                _7052.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cvt_pulley_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7055.CVTPulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7055,
            )

            return self._parent._cast(
                _7055.CVTPulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7060.CylindricalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7060,
            )

            return self._parent._cast(
                _7060.CylindricalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def cylindrical_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7063.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7063,
            )

            return self._parent._cast(
                _7063.CylindricalPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def face_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7066.FaceGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7066,
            )

            return self._parent._cast(
                _7066.FaceGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7071.GearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7071,
            )

            return self._parent._cast(
                _7071.GearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7076.HypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7076,
            )

            return self._parent._cast(
                _7076.HypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7080.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7080,
            )

            return self._parent._cast(
                _7080.KlingelnbergCycloPalloidConicalGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7083.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7083,
            )

            return self._parent._cast(
                _7083.KlingelnbergCycloPalloidHypoidGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7086.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7086,
            )

            return self._parent._cast(
                _7086.KlingelnbergCycloPalloidSpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mass_disc_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7089.MassDiscAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7089,
            )

            return self._parent._cast(
                _7089.MassDiscAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def measurement_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7090.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7090,
            )

            return self._parent._cast(
                _7090.MeasurementComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def oil_seal_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7092.OilSealAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7092,
            )

            return self._parent._cast(
                _7092.OilSealAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7096.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7096,
            )

            return self._parent._cast(
                _7096.PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def planet_carrier_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7099.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7099,
            )

            return self._parent._cast(
                _7099.PlanetCarrierAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def point_load_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7100.PointLoadAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7100,
            )

            return self._parent._cast(
                _7100.PointLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def power_load_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7101.PowerLoadAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7101,
            )

            return self._parent._cast(
                _7101.PowerLoadAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def pulley_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7102.PulleyAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7102,
            )

            return self._parent._cast(
                _7102.PulleyAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def ring_pins_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7103.RingPinsAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7103,
            )

            return self._parent._cast(
                _7103.RingPinsAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def rolling_ring_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7105.RollingRingAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7105,
            )

            return self._parent._cast(
                _7105.RollingRingAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def shaft_hub_connection_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7110.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7110,
            )

            return self._parent._cast(
                _7110.ShaftHubConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spiral_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7113.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7113,
            )

            return self._parent._cast(
                _7113.SpiralBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def spring_damper_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7118.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7118,
            )

            return self._parent._cast(
                _7118.SpringDamperHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_diff_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7119.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7119,
            )

            return self._parent._cast(
                _7119.StraightBevelDiffGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7122.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7122,
            )

            return self._parent._cast(
                _7122.StraightBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_planet_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7125.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7125,
            )

            return self._parent._cast(
                _7125.StraightBevelPlanetGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def straight_bevel_sun_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7126.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7126,
            )

            return self._parent._cast(
                _7126.StraightBevelSunGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_half_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7128.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7128,
            )

            return self._parent._cast(
                _7128.SynchroniserHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_part_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7129.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7129,
            )

            return self._parent._cast(
                _7129.SynchroniserPartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def synchroniser_sleeve_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7130.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7130,
            )

            return self._parent._cast(
                _7130.SynchroniserSleeveAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_pump_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7133.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7133,
            )

            return self._parent._cast(
                _7133.TorqueConverterPumpAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def torque_converter_turbine_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7134.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7134,
            )

            return self._parent._cast(
                _7134.TorqueConverterTurbineAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def unbalanced_mass_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7135.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7135,
            )

            return self._parent._cast(
                _7135.UnbalancedMassAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def virtual_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7136.VirtualComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7136,
            )

            return self._parent._cast(
                _7136.VirtualComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def worm_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7137.WormGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7137,
            )

            return self._parent._cast(
                _7137.WormGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def zerol_bevel_gear_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7140.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7140,
            )

            return self._parent._cast(
                _7140.ZerolBevelGearAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
        ) -> "MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "MountableComponentAdvancedTimeSteppingAnalysisForModulation.TYPE",
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
    def system_deflection_results(
        self: Self,
    ) -> "_2784.MountableComponentSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.MountableComponentSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "MountableComponentAdvancedTimeSteppingAnalysisForModulation._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_MountableComponentAdvancedTimeSteppingAnalysisForModulation(
            self
        )
