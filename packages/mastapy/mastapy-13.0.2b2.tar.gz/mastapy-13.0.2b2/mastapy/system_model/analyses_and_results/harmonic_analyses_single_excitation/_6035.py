"""ComponentHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6091,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "ComponentHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6011,
        _6012,
        _6014,
        _6018,
        _6021,
        _6024,
        _6025,
        _6026,
        _6030,
        _6032,
        _6037,
        _6039,
        _6042,
        _6046,
        _6048,
        _6052,
        _6055,
        _6057,
        _6060,
        _6061,
        _6062,
        _6063,
        _6066,
        _6068,
        _6071,
        _6073,
        _6077,
        _6080,
        _6083,
        _6086,
        _6087,
        _6089,
        _6090,
        _6093,
        _6097,
        _6098,
        _6099,
        _6100,
        _6101,
        _6105,
        _6107,
        _6108,
        _6111,
        _6115,
        _6117,
        _6120,
        _6123,
        _6124,
        _6125,
        _6127,
        _6128,
        _6131,
        _6132,
        _6133,
        _6134,
        _6135,
        _6138,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ComponentHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="ComponentHarmonicAnalysisOfSingleExcitation")


class ComponentHarmonicAnalysisOfSingleExcitation(
    _6091.PartHarmonicAnalysisOfSingleExcitation
):
    """ComponentHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _COMPONENT_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ComponentHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_ComponentHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting ComponentHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
            parent: "ComponentHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def part_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6091.PartHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6091.PartHarmonicAnalysisOfSingleExcitation)

        @property
        def part_static_load_analysis_case(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6011.AbstractShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6011,
            )

            return self._parent._cast(
                _6011.AbstractShaftHarmonicAnalysisOfSingleExcitation
            )

        @property
        def abstract_shaft_or_housing_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6012.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6012,
            )

            return self._parent._cast(
                _6012.AbstractShaftOrHousingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def agma_gleason_conical_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6014.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6014,
            )

            return self._parent._cast(
                _6014.AGMAGleasonConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bearing_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6018.BearingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6018,
            )

            return self._parent._cast(_6018.BearingHarmonicAnalysisOfSingleExcitation)

        @property
        def bevel_differential_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6021.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6021,
            )

            return self._parent._cast(
                _6021.BevelDifferentialGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_planet_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6024.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6024,
            )

            return self._parent._cast(
                _6024.BevelDifferentialPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_differential_sun_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6025.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6025,
            )

            return self._parent._cast(
                _6025.BevelDifferentialSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6026.BevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6026,
            )

            return self._parent._cast(_6026.BevelGearHarmonicAnalysisOfSingleExcitation)

        @property
        def bolt_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6030.BoltHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6030,
            )

            return self._parent._cast(_6030.BoltHarmonicAnalysisOfSingleExcitation)

        @property
        def clutch_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6032.ClutchHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6032,
            )

            return self._parent._cast(
                _6032.ClutchHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_coupling_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6037.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6037,
            )

            return self._parent._cast(
                _6037.ConceptCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def concept_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6039.ConceptGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6039,
            )

            return self._parent._cast(
                _6039.ConceptGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6042.ConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6042,
            )

            return self._parent._cast(
                _6042.ConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connector_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6046.ConnectorHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6046,
            )

            return self._parent._cast(_6046.ConnectorHarmonicAnalysisOfSingleExcitation)

        @property
        def coupling_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6048.CouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6048,
            )

            return self._parent._cast(
                _6048.CouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cvt_pulley_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6052.CVTPulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6052,
            )

            return self._parent._cast(_6052.CVTPulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def cycloidal_disc_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6055.CycloidalDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6055,
            )

            return self._parent._cast(
                _6055.CycloidalDiscHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6057.CylindricalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6057,
            )

            return self._parent._cast(
                _6057.CylindricalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def cylindrical_planet_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6060.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6060,
            )

            return self._parent._cast(
                _6060.CylindricalPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def datum_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6061.DatumHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6061,
            )

            return self._parent._cast(_6061.DatumHarmonicAnalysisOfSingleExcitation)

        @property
        def external_cad_model_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6062.ExternalCADModelHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6062,
            )

            return self._parent._cast(
                _6062.ExternalCADModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def face_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6063.FaceGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6063,
            )

            return self._parent._cast(_6063.FaceGearHarmonicAnalysisOfSingleExcitation)

        @property
        def fe_part_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6066.FEPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6066,
            )

            return self._parent._cast(_6066.FEPartHarmonicAnalysisOfSingleExcitation)

        @property
        def gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6068.GearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6068,
            )

            return self._parent._cast(_6068.GearHarmonicAnalysisOfSingleExcitation)

        @property
        def guide_dxf_model_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6071.GuideDxfModelHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6071,
            )

            return self._parent._cast(
                _6071.GuideDxfModelHarmonicAnalysisOfSingleExcitation
            )

        @property
        def hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6073.HypoidGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6073,
            )

            return self._parent._cast(
                _6073.HypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6077.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6077,
            )

            return self._parent._cast(
                _6077.KlingelnbergCycloPalloidConicalGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6080.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6080,
            )

            return self._parent._cast(
                _6080.KlingelnbergCycloPalloidHypoidGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6083.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6083,
            )

            return self._parent._cast(
                _6083.KlingelnbergCycloPalloidSpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mass_disc_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6086.MassDiscHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6086,
            )

            return self._parent._cast(_6086.MassDiscHarmonicAnalysisOfSingleExcitation)

        @property
        def measurement_component_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6087.MeasurementComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6087,
            )

            return self._parent._cast(
                _6087.MeasurementComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def mountable_component_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6089.MountableComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6089,
            )

            return self._parent._cast(
                _6089.MountableComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def oil_seal_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6090.OilSealHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6090,
            )

            return self._parent._cast(_6090.OilSealHarmonicAnalysisOfSingleExcitation)

        @property
        def part_to_part_shear_coupling_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6093.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6093,
            )

            return self._parent._cast(
                _6093.PartToPartShearCouplingHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def planet_carrier_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6097.PlanetCarrierHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6097,
            )

            return self._parent._cast(
                _6097.PlanetCarrierHarmonicAnalysisOfSingleExcitation
            )

        @property
        def point_load_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6098.PointLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6098,
            )

            return self._parent._cast(_6098.PointLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def power_load_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6099.PowerLoadHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6099,
            )

            return self._parent._cast(_6099.PowerLoadHarmonicAnalysisOfSingleExcitation)

        @property
        def pulley_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6100.PulleyHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6100,
            )

            return self._parent._cast(_6100.PulleyHarmonicAnalysisOfSingleExcitation)

        @property
        def ring_pins_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6101.RingPinsHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6101,
            )

            return self._parent._cast(_6101.RingPinsHarmonicAnalysisOfSingleExcitation)

        @property
        def rolling_ring_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6105.RollingRingHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6105,
            )

            return self._parent._cast(
                _6105.RollingRingHarmonicAnalysisOfSingleExcitation
            )

        @property
        def shaft_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6107.ShaftHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6107,
            )

            return self._parent._cast(_6107.ShaftHarmonicAnalysisOfSingleExcitation)

        @property
        def shaft_hub_connection_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6108.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6108,
            )

            return self._parent._cast(
                _6108.ShaftHubConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spiral_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6111.SpiralBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6111,
            )

            return self._parent._cast(
                _6111.SpiralBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def spring_damper_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6115.SpringDamperHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6115,
            )

            return self._parent._cast(
                _6115.SpringDamperHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_diff_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6117.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6117,
            )

            return self._parent._cast(
                _6117.StraightBevelDiffGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6120.StraightBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6120,
            )

            return self._parent._cast(
                _6120.StraightBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_planet_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6123.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6123,
            )

            return self._parent._cast(
                _6123.StraightBevelPlanetGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def straight_bevel_sun_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6124.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6124,
            )

            return self._parent._cast(
                _6124.StraightBevelSunGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_half_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6125.SynchroniserHalfHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6125,
            )

            return self._parent._cast(
                _6125.SynchroniserHalfHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_part_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6127.SynchroniserPartHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6127,
            )

            return self._parent._cast(
                _6127.SynchroniserPartHarmonicAnalysisOfSingleExcitation
            )

        @property
        def synchroniser_sleeve_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6128.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6128,
            )

            return self._parent._cast(
                _6128.SynchroniserSleeveHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_pump_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6131.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6131,
            )

            return self._parent._cast(
                _6131.TorqueConverterPumpHarmonicAnalysisOfSingleExcitation
            )

        @property
        def torque_converter_turbine_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6132.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6132,
            )

            return self._parent._cast(
                _6132.TorqueConverterTurbineHarmonicAnalysisOfSingleExcitation
            )

        @property
        def unbalanced_mass_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6133.UnbalancedMassHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6133,
            )

            return self._parent._cast(
                _6133.UnbalancedMassHarmonicAnalysisOfSingleExcitation
            )

        @property
        def virtual_component_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6134.VirtualComponentHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6134,
            )

            return self._parent._cast(
                _6134.VirtualComponentHarmonicAnalysisOfSingleExcitation
            )

        @property
        def worm_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6135.WormGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6135,
            )

            return self._parent._cast(_6135.WormGearHarmonicAnalysisOfSingleExcitation)

        @property
        def zerol_bevel_gear_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "_6138.ZerolBevelGearHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6138,
            )

            return self._parent._cast(
                _6138.ZerolBevelGearHarmonicAnalysisOfSingleExcitation
            )

        @property
        def component_harmonic_analysis_of_single_excitation(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
        ) -> "ComponentHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation",
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
        self: Self, instance_to_wrap: "ComponentHarmonicAnalysisOfSingleExcitation.TYPE"
    ):
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
    ) -> "ComponentHarmonicAnalysisOfSingleExcitation._Cast_ComponentHarmonicAnalysisOfSingleExcitation":
        return self._Cast_ComponentHarmonicAnalysisOfSingleExcitation(self)
