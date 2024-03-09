"""MountableComponentCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4755
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "MountableComponentCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses import _4660
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4734,
        _4738,
        _4741,
        _4744,
        _4745,
        _4746,
        _4753,
        _4758,
        _4759,
        _4762,
        _4766,
        _4769,
        _4772,
        _4777,
        _4780,
        _4783,
        _4788,
        _4792,
        _4796,
        _4799,
        _4802,
        _4805,
        _4806,
        _4808,
        _4812,
        _4815,
        _4816,
        _4817,
        _4818,
        _4819,
        _4822,
        _4826,
        _4829,
        _4834,
        _4835,
        _4838,
        _4841,
        _4842,
        _4844,
        _4845,
        _4846,
        _4849,
        _4850,
        _4851,
        _4852,
        _4853,
        _4856,
        _4809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundModalAnalysis",)


Self = TypeVar("Self", bound="MountableComponentCompoundModalAnalysis")


class MountableComponentCompoundModalAnalysis(_4755.ComponentCompoundModalAnalysis):
    """MountableComponentCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MountableComponentCompoundModalAnalysis"
    )

    class _Cast_MountableComponentCompoundModalAnalysis:
        """Special nested class for casting MountableComponentCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
            parent: "MountableComponentCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def component_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4755.ComponentCompoundModalAnalysis":
            return self._parent._cast(_4755.ComponentCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4809.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4734.AGMAGleasonConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4734,
            )

            return self._parent._cast(_4734.AGMAGleasonConicalGearCompoundModalAnalysis)

        @property
        def bearing_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4738.BearingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4738,
            )

            return self._parent._cast(_4738.BearingCompoundModalAnalysis)

        @property
        def bevel_differential_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4741.BevelDifferentialGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4741,
            )

            return self._parent._cast(_4741.BevelDifferentialGearCompoundModalAnalysis)

        @property
        def bevel_differential_planet_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4744.BevelDifferentialPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4744,
            )

            return self._parent._cast(
                _4744.BevelDifferentialPlanetGearCompoundModalAnalysis
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4745.BevelDifferentialSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4745,
            )

            return self._parent._cast(
                _4745.BevelDifferentialSunGearCompoundModalAnalysis
            )

        @property
        def bevel_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4746.BevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4746,
            )

            return self._parent._cast(_4746.BevelGearCompoundModalAnalysis)

        @property
        def clutch_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4753.ClutchHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4753,
            )

            return self._parent._cast(_4753.ClutchHalfCompoundModalAnalysis)

        @property
        def concept_coupling_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4758.ConceptCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4758,
            )

            return self._parent._cast(_4758.ConceptCouplingHalfCompoundModalAnalysis)

        @property
        def concept_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4759.ConceptGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4759,
            )

            return self._parent._cast(_4759.ConceptGearCompoundModalAnalysis)

        @property
        def conical_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4762.ConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4762,
            )

            return self._parent._cast(_4762.ConicalGearCompoundModalAnalysis)

        @property
        def connector_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4766.ConnectorCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4766,
            )

            return self._parent._cast(_4766.ConnectorCompoundModalAnalysis)

        @property
        def coupling_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4769.CouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4769,
            )

            return self._parent._cast(_4769.CouplingHalfCompoundModalAnalysis)

        @property
        def cvt_pulley_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4772.CVTPulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4772,
            )

            return self._parent._cast(_4772.CVTPulleyCompoundModalAnalysis)

        @property
        def cylindrical_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4777.CylindricalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4777,
            )

            return self._parent._cast(_4777.CylindricalGearCompoundModalAnalysis)

        @property
        def cylindrical_planet_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4780.CylindricalPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4780,
            )

            return self._parent._cast(_4780.CylindricalPlanetGearCompoundModalAnalysis)

        @property
        def face_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4783.FaceGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4783,
            )

            return self._parent._cast(_4783.FaceGearCompoundModalAnalysis)

        @property
        def gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4788.GearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4788,
            )

            return self._parent._cast(_4788.GearCompoundModalAnalysis)

        @property
        def hypoid_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4792.HypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4792,
            )

            return self._parent._cast(_4792.HypoidGearCompoundModalAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4796.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4796,
            )

            return self._parent._cast(
                _4796.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4799.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4799,
            )

            return self._parent._cast(
                _4799.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4802.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4802,
            )

            return self._parent._cast(
                _4802.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysis
            )

        @property
        def mass_disc_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4805.MassDiscCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4805,
            )

            return self._parent._cast(_4805.MassDiscCompoundModalAnalysis)

        @property
        def measurement_component_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4806.MeasurementComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4806,
            )

            return self._parent._cast(_4806.MeasurementComponentCompoundModalAnalysis)

        @property
        def oil_seal_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4808.OilSealCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4808,
            )

            return self._parent._cast(_4808.OilSealCompoundModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4812.PartToPartShearCouplingHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4812,
            )

            return self._parent._cast(
                _4812.PartToPartShearCouplingHalfCompoundModalAnalysis
            )

        @property
        def planet_carrier_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4815.PlanetCarrierCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4815,
            )

            return self._parent._cast(_4815.PlanetCarrierCompoundModalAnalysis)

        @property
        def point_load_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4816.PointLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4816,
            )

            return self._parent._cast(_4816.PointLoadCompoundModalAnalysis)

        @property
        def power_load_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4817.PowerLoadCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4817,
            )

            return self._parent._cast(_4817.PowerLoadCompoundModalAnalysis)

        @property
        def pulley_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4818.PulleyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4818,
            )

            return self._parent._cast(_4818.PulleyCompoundModalAnalysis)

        @property
        def ring_pins_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4819.RingPinsCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4819,
            )

            return self._parent._cast(_4819.RingPinsCompoundModalAnalysis)

        @property
        def rolling_ring_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4822.RollingRingCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4822,
            )

            return self._parent._cast(_4822.RollingRingCompoundModalAnalysis)

        @property
        def shaft_hub_connection_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4826.ShaftHubConnectionCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4826,
            )

            return self._parent._cast(_4826.ShaftHubConnectionCompoundModalAnalysis)

        @property
        def spiral_bevel_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4829.SpiralBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4829,
            )

            return self._parent._cast(_4829.SpiralBevelGearCompoundModalAnalysis)

        @property
        def spring_damper_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4834.SpringDamperHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4834,
            )

            return self._parent._cast(_4834.SpringDamperHalfCompoundModalAnalysis)

        @property
        def straight_bevel_diff_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4835.StraightBevelDiffGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4835,
            )

            return self._parent._cast(_4835.StraightBevelDiffGearCompoundModalAnalysis)

        @property
        def straight_bevel_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4838.StraightBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4838,
            )

            return self._parent._cast(_4838.StraightBevelGearCompoundModalAnalysis)

        @property
        def straight_bevel_planet_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4841.StraightBevelPlanetGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4841,
            )

            return self._parent._cast(
                _4841.StraightBevelPlanetGearCompoundModalAnalysis
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4842.StraightBevelSunGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4842,
            )

            return self._parent._cast(_4842.StraightBevelSunGearCompoundModalAnalysis)

        @property
        def synchroniser_half_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4844.SynchroniserHalfCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4844,
            )

            return self._parent._cast(_4844.SynchroniserHalfCompoundModalAnalysis)

        @property
        def synchroniser_part_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4845.SynchroniserPartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4845,
            )

            return self._parent._cast(_4845.SynchroniserPartCompoundModalAnalysis)

        @property
        def synchroniser_sleeve_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4846.SynchroniserSleeveCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4846,
            )

            return self._parent._cast(_4846.SynchroniserSleeveCompoundModalAnalysis)

        @property
        def torque_converter_pump_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4849.TorqueConverterPumpCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4849,
            )

            return self._parent._cast(_4849.TorqueConverterPumpCompoundModalAnalysis)

        @property
        def torque_converter_turbine_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4850.TorqueConverterTurbineCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4850,
            )

            return self._parent._cast(_4850.TorqueConverterTurbineCompoundModalAnalysis)

        @property
        def unbalanced_mass_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4851.UnbalancedMassCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4851,
            )

            return self._parent._cast(_4851.UnbalancedMassCompoundModalAnalysis)

        @property
        def virtual_component_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4852.VirtualComponentCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4852,
            )

            return self._parent._cast(_4852.VirtualComponentCompoundModalAnalysis)

        @property
        def worm_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4853.WormGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4853,
            )

            return self._parent._cast(_4853.WormGearCompoundModalAnalysis)

        @property
        def zerol_bevel_gear_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "_4856.ZerolBevelGearCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4856,
            )

            return self._parent._cast(_4856.ZerolBevelGearCompoundModalAnalysis)

        @property
        def mountable_component_compound_modal_analysis(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
        ) -> "MountableComponentCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis",
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
        self: Self, instance_to_wrap: "MountableComponentCompoundModalAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4660.MountableComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis]

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
    ) -> "List[_4660.MountableComponentModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.MountableComponentModalAnalysis]

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
    ) -> "MountableComponentCompoundModalAnalysis._Cast_MountableComponentCompoundModalAnalysis":
        return self._Cast_MountableComponentCompoundModalAnalysis(self)
