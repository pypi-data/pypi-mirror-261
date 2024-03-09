"""MountableComponentCompoundPowerFlow"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.power_flows.compound import _4194
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MOUNTABLE_COMPONENT_COMPOUND_POWER_FLOW = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.PowerFlows.Compound",
    "MountableComponentCompoundPowerFlow",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.power_flows import _4114
    from mastapy.system_model.analyses_and_results.power_flows.compound import (
        _4173,
        _4177,
        _4180,
        _4183,
        _4184,
        _4185,
        _4192,
        _4197,
        _4198,
        _4201,
        _4205,
        _4208,
        _4211,
        _4216,
        _4219,
        _4222,
        _4227,
        _4231,
        _4235,
        _4238,
        _4241,
        _4244,
        _4245,
        _4247,
        _4251,
        _4254,
        _4255,
        _4256,
        _4257,
        _4258,
        _4261,
        _4265,
        _4268,
        _4273,
        _4274,
        _4277,
        _4280,
        _4281,
        _4283,
        _4284,
        _4285,
        _4288,
        _4289,
        _4290,
        _4291,
        _4292,
        _4295,
        _4248,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("MountableComponentCompoundPowerFlow",)


Self = TypeVar("Self", bound="MountableComponentCompoundPowerFlow")


class MountableComponentCompoundPowerFlow(_4194.ComponentCompoundPowerFlow):
    """MountableComponentCompoundPowerFlow

    This is a mastapy class.
    """

    TYPE = _MOUNTABLE_COMPONENT_COMPOUND_POWER_FLOW
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_MountableComponentCompoundPowerFlow")

    class _Cast_MountableComponentCompoundPowerFlow:
        """Special nested class for casting MountableComponentCompoundPowerFlow to subclasses."""

        def __init__(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
            parent: "MountableComponentCompoundPowerFlow",
        ):
            self._parent = parent

        @property
        def component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4194.ComponentCompoundPowerFlow":
            return self._parent._cast(_4194.ComponentCompoundPowerFlow)

        @property
        def part_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4248.PartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4248,
            )

            return self._parent._cast(_4248.PartCompoundPowerFlow)

        @property
        def part_compound_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4173.AGMAGleasonConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4173,
            )

            return self._parent._cast(_4173.AGMAGleasonConicalGearCompoundPowerFlow)

        @property
        def bearing_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4177.BearingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4177,
            )

            return self._parent._cast(_4177.BearingCompoundPowerFlow)

        @property
        def bevel_differential_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4180.BevelDifferentialGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4180,
            )

            return self._parent._cast(_4180.BevelDifferentialGearCompoundPowerFlow)

        @property
        def bevel_differential_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4183.BevelDifferentialPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4183,
            )

            return self._parent._cast(
                _4183.BevelDifferentialPlanetGearCompoundPowerFlow
            )

        @property
        def bevel_differential_sun_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4184.BevelDifferentialSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4184,
            )

            return self._parent._cast(_4184.BevelDifferentialSunGearCompoundPowerFlow)

        @property
        def bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4185.BevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4185,
            )

            return self._parent._cast(_4185.BevelGearCompoundPowerFlow)

        @property
        def clutch_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4192.ClutchHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4192,
            )

            return self._parent._cast(_4192.ClutchHalfCompoundPowerFlow)

        @property
        def concept_coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4197.ConceptCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4197,
            )

            return self._parent._cast(_4197.ConceptCouplingHalfCompoundPowerFlow)

        @property
        def concept_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4198.ConceptGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4198,
            )

            return self._parent._cast(_4198.ConceptGearCompoundPowerFlow)

        @property
        def conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4201.ConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4201,
            )

            return self._parent._cast(_4201.ConicalGearCompoundPowerFlow)

        @property
        def connector_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4205.ConnectorCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4205,
            )

            return self._parent._cast(_4205.ConnectorCompoundPowerFlow)

        @property
        def coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4208.CouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4208,
            )

            return self._parent._cast(_4208.CouplingHalfCompoundPowerFlow)

        @property
        def cvt_pulley_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4211.CVTPulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4211,
            )

            return self._parent._cast(_4211.CVTPulleyCompoundPowerFlow)

        @property
        def cylindrical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4216.CylindricalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4216,
            )

            return self._parent._cast(_4216.CylindricalGearCompoundPowerFlow)

        @property
        def cylindrical_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4219.CylindricalPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4219,
            )

            return self._parent._cast(_4219.CylindricalPlanetGearCompoundPowerFlow)

        @property
        def face_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4222.FaceGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4222,
            )

            return self._parent._cast(_4222.FaceGearCompoundPowerFlow)

        @property
        def gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4227.GearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4227,
            )

            return self._parent._cast(_4227.GearCompoundPowerFlow)

        @property
        def hypoid_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4231.HypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4231,
            )

            return self._parent._cast(_4231.HypoidGearCompoundPowerFlow)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4235.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4235,
            )

            return self._parent._cast(
                _4235.KlingelnbergCycloPalloidConicalGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4238.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4238,
            )

            return self._parent._cast(
                _4238.KlingelnbergCycloPalloidHypoidGearCompoundPowerFlow
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4241.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4241,
            )

            return self._parent._cast(
                _4241.KlingelnbergCycloPalloidSpiralBevelGearCompoundPowerFlow
            )

        @property
        def mass_disc_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4244.MassDiscCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4244,
            )

            return self._parent._cast(_4244.MassDiscCompoundPowerFlow)

        @property
        def measurement_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4245.MeasurementComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4245,
            )

            return self._parent._cast(_4245.MeasurementComponentCompoundPowerFlow)

        @property
        def oil_seal_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4247.OilSealCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4247,
            )

            return self._parent._cast(_4247.OilSealCompoundPowerFlow)

        @property
        def part_to_part_shear_coupling_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4251.PartToPartShearCouplingHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4251,
            )

            return self._parent._cast(
                _4251.PartToPartShearCouplingHalfCompoundPowerFlow
            )

        @property
        def planet_carrier_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4254.PlanetCarrierCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4254,
            )

            return self._parent._cast(_4254.PlanetCarrierCompoundPowerFlow)

        @property
        def point_load_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4255.PointLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4255,
            )

            return self._parent._cast(_4255.PointLoadCompoundPowerFlow)

        @property
        def power_load_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4256.PowerLoadCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4256,
            )

            return self._parent._cast(_4256.PowerLoadCompoundPowerFlow)

        @property
        def pulley_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4257.PulleyCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4257,
            )

            return self._parent._cast(_4257.PulleyCompoundPowerFlow)

        @property
        def ring_pins_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4258.RingPinsCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4258,
            )

            return self._parent._cast(_4258.RingPinsCompoundPowerFlow)

        @property
        def rolling_ring_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4261.RollingRingCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4261,
            )

            return self._parent._cast(_4261.RollingRingCompoundPowerFlow)

        @property
        def shaft_hub_connection_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4265.ShaftHubConnectionCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4265,
            )

            return self._parent._cast(_4265.ShaftHubConnectionCompoundPowerFlow)

        @property
        def spiral_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4268.SpiralBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4268,
            )

            return self._parent._cast(_4268.SpiralBevelGearCompoundPowerFlow)

        @property
        def spring_damper_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4273.SpringDamperHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4273,
            )

            return self._parent._cast(_4273.SpringDamperHalfCompoundPowerFlow)

        @property
        def straight_bevel_diff_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4274.StraightBevelDiffGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4274,
            )

            return self._parent._cast(_4274.StraightBevelDiffGearCompoundPowerFlow)

        @property
        def straight_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4277.StraightBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4277,
            )

            return self._parent._cast(_4277.StraightBevelGearCompoundPowerFlow)

        @property
        def straight_bevel_planet_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4280.StraightBevelPlanetGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4280,
            )

            return self._parent._cast(_4280.StraightBevelPlanetGearCompoundPowerFlow)

        @property
        def straight_bevel_sun_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4281.StraightBevelSunGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4281,
            )

            return self._parent._cast(_4281.StraightBevelSunGearCompoundPowerFlow)

        @property
        def synchroniser_half_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4283.SynchroniserHalfCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4283,
            )

            return self._parent._cast(_4283.SynchroniserHalfCompoundPowerFlow)

        @property
        def synchroniser_part_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4284.SynchroniserPartCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4284,
            )

            return self._parent._cast(_4284.SynchroniserPartCompoundPowerFlow)

        @property
        def synchroniser_sleeve_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4285.SynchroniserSleeveCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4285,
            )

            return self._parent._cast(_4285.SynchroniserSleeveCompoundPowerFlow)

        @property
        def torque_converter_pump_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4288.TorqueConverterPumpCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4288,
            )

            return self._parent._cast(_4288.TorqueConverterPumpCompoundPowerFlow)

        @property
        def torque_converter_turbine_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4289.TorqueConverterTurbineCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4289,
            )

            return self._parent._cast(_4289.TorqueConverterTurbineCompoundPowerFlow)

        @property
        def unbalanced_mass_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4290.UnbalancedMassCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4290,
            )

            return self._parent._cast(_4290.UnbalancedMassCompoundPowerFlow)

        @property
        def virtual_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4291.VirtualComponentCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4291,
            )

            return self._parent._cast(_4291.VirtualComponentCompoundPowerFlow)

        @property
        def worm_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4292.WormGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4292,
            )

            return self._parent._cast(_4292.WormGearCompoundPowerFlow)

        @property
        def zerol_bevel_gear_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "_4295.ZerolBevelGearCompoundPowerFlow":
            from mastapy.system_model.analyses_and_results.power_flows.compound import (
                _4295,
            )

            return self._parent._cast(_4295.ZerolBevelGearCompoundPowerFlow)

        @property
        def mountable_component_compound_power_flow(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
        ) -> "MountableComponentCompoundPowerFlow":
            return self._parent

        def __getattr__(
            self: "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow",
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
        self: Self, instance_to_wrap: "MountableComponentCompoundPowerFlow.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4114.MountableComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow]

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
    ) -> "List[_4114.MountableComponentPowerFlow]":
        """List[mastapy.system_model.analyses_and_results.power_flows.MountableComponentPowerFlow]

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
    ) -> (
        "MountableComponentCompoundPowerFlow._Cast_MountableComponentCompoundPowerFlow"
    ):
        return self._Cast_MountableComponentCompoundPowerFlow(self)
