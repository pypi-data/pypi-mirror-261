"""ComponentLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6931
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COMPONENT_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ComponentLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2446
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6810,
        _6811,
        _6816,
        _6822,
        _6825,
        _6828,
        _6829,
        _6830,
        _6834,
        _6836,
        _6842,
        _6844,
        _6847,
        _6853,
        _6855,
        _6859,
        _6862,
        _6864,
        _6869,
        _6872,
        _6886,
        _6887,
        _6890,
        _6893,
        _6899,
        _6908,
        _6915,
        _6918,
        _6921,
        _6924,
        _6925,
        _6927,
        _6929,
        _6933,
        _6938,
        _6941,
        _6942,
        _6943,
        _6946,
        _6950,
        _6952,
        _6953,
        _6956,
        _6960,
        _6962,
        _6965,
        _6968,
        _6969,
        _6970,
        _6972,
        _6973,
        _6977,
        _6978,
        _6983,
        _6984,
        _6985,
        _6988,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ComponentLoadCase",)


Self = TypeVar("Self", bound="ComponentLoadCase")


class ComponentLoadCase(_6931.PartLoadCase):
    """ComponentLoadCase

    This is a mastapy class.
    """

    TYPE = _COMPONENT_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ComponentLoadCase")

    class _Cast_ComponentLoadCase:
        """Special nested class for casting ComponentLoadCase to subclasses."""

        def __init__(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
            parent: "ComponentLoadCase",
        ):
            self._parent = parent

        @property
        def part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6931.PartLoadCase":
            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6810.AbstractShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6810

            return self._parent._cast(_6810.AbstractShaftLoadCase)

        @property
        def abstract_shaft_or_housing_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6811.AbstractShaftOrHousingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6811

            return self._parent._cast(_6811.AbstractShaftOrHousingLoadCase)

        @property
        def agma_gleason_conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6816.AGMAGleasonConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6816

            return self._parent._cast(_6816.AGMAGleasonConicalGearLoadCase)

        @property
        def bearing_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6822.BearingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6822

            return self._parent._cast(_6822.BearingLoadCase)

        @property
        def bevel_differential_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6825.BevelDifferentialGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6825

            return self._parent._cast(_6825.BevelDifferentialGearLoadCase)

        @property
        def bevel_differential_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6828.BevelDifferentialPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6828

            return self._parent._cast(_6828.BevelDifferentialPlanetGearLoadCase)

        @property
        def bevel_differential_sun_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6829.BevelDifferentialSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6829

            return self._parent._cast(_6829.BevelDifferentialSunGearLoadCase)

        @property
        def bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6830.BevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6830

            return self._parent._cast(_6830.BevelGearLoadCase)

        @property
        def bolt_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6834.BoltLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6834

            return self._parent._cast(_6834.BoltLoadCase)

        @property
        def clutch_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6836.ClutchHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6836

            return self._parent._cast(_6836.ClutchHalfLoadCase)

        @property
        def concept_coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6842.ConceptCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6842

            return self._parent._cast(_6842.ConceptCouplingHalfLoadCase)

        @property
        def concept_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6844.ConceptGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6844

            return self._parent._cast(_6844.ConceptGearLoadCase)

        @property
        def conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6847.ConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6847

            return self._parent._cast(_6847.ConicalGearLoadCase)

        @property
        def connector_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6853.ConnectorLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6853

            return self._parent._cast(_6853.ConnectorLoadCase)

        @property
        def coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6855.CouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6855

            return self._parent._cast(_6855.CouplingHalfLoadCase)

        @property
        def cvt_pulley_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6859.CVTPulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6859

            return self._parent._cast(_6859.CVTPulleyLoadCase)

        @property
        def cycloidal_disc_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6862.CycloidalDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6862

            return self._parent._cast(_6862.CycloidalDiscLoadCase)

        @property
        def cylindrical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6864.CylindricalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6864

            return self._parent._cast(_6864.CylindricalGearLoadCase)

        @property
        def cylindrical_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6869.CylindricalPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6869

            return self._parent._cast(_6869.CylindricalPlanetGearLoadCase)

        @property
        def datum_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6872.DatumLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6872

            return self._parent._cast(_6872.DatumLoadCase)

        @property
        def external_cad_model_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6886.ExternalCADModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6886

            return self._parent._cast(_6886.ExternalCADModelLoadCase)

        @property
        def face_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6887.FaceGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6887

            return self._parent._cast(_6887.FaceGearLoadCase)

        @property
        def fe_part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6890.FEPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6890

            return self._parent._cast(_6890.FEPartLoadCase)

        @property
        def gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6893.GearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6893

            return self._parent._cast(_6893.GearLoadCase)

        @property
        def guide_dxf_model_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6899.GuideDxfModelLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6899

            return self._parent._cast(_6899.GuideDxfModelLoadCase)

        @property
        def hypoid_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6908.HypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6908

            return self._parent._cast(_6908.HypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6915.KlingelnbergCycloPalloidConicalGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6915

            return self._parent._cast(_6915.KlingelnbergCycloPalloidConicalGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6918.KlingelnbergCycloPalloidHypoidGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6918

            return self._parent._cast(_6918.KlingelnbergCycloPalloidHypoidGearLoadCase)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6921.KlingelnbergCycloPalloidSpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6921

            return self._parent._cast(
                _6921.KlingelnbergCycloPalloidSpiralBevelGearLoadCase
            )

        @property
        def mass_disc_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6924.MassDiscLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6924

            return self._parent._cast(_6924.MassDiscLoadCase)

        @property
        def measurement_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6925.MeasurementComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6925

            return self._parent._cast(_6925.MeasurementComponentLoadCase)

        @property
        def mountable_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6927.MountableComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6927

            return self._parent._cast(_6927.MountableComponentLoadCase)

        @property
        def oil_seal_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6929.OilSealLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6929

            return self._parent._cast(_6929.OilSealLoadCase)

        @property
        def part_to_part_shear_coupling_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6933.PartToPartShearCouplingHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6933

            return self._parent._cast(_6933.PartToPartShearCouplingHalfLoadCase)

        @property
        def planet_carrier_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6938.PlanetCarrierLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6938

            return self._parent._cast(_6938.PlanetCarrierLoadCase)

        @property
        def point_load_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6941.PointLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6941

            return self._parent._cast(_6941.PointLoadLoadCase)

        @property
        def power_load_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6942.PowerLoadLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6942

            return self._parent._cast(_6942.PowerLoadLoadCase)

        @property
        def pulley_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6943.PulleyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6943

            return self._parent._cast(_6943.PulleyLoadCase)

        @property
        def ring_pins_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6946.RingPinsLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6946

            return self._parent._cast(_6946.RingPinsLoadCase)

        @property
        def rolling_ring_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6950.RollingRingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6950

            return self._parent._cast(_6950.RollingRingLoadCase)

        @property
        def shaft_hub_connection_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6952.ShaftHubConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6952

            return self._parent._cast(_6952.ShaftHubConnectionLoadCase)

        @property
        def shaft_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6953.ShaftLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6953

            return self._parent._cast(_6953.ShaftLoadCase)

        @property
        def spiral_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6956.SpiralBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6956

            return self._parent._cast(_6956.SpiralBevelGearLoadCase)

        @property
        def spring_damper_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6960.SpringDamperHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6960

            return self._parent._cast(_6960.SpringDamperHalfLoadCase)

        @property
        def straight_bevel_diff_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6962.StraightBevelDiffGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6962

            return self._parent._cast(_6962.StraightBevelDiffGearLoadCase)

        @property
        def straight_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6965.StraightBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6965

            return self._parent._cast(_6965.StraightBevelGearLoadCase)

        @property
        def straight_bevel_planet_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6968.StraightBevelPlanetGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6968

            return self._parent._cast(_6968.StraightBevelPlanetGearLoadCase)

        @property
        def straight_bevel_sun_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6969.StraightBevelSunGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6969

            return self._parent._cast(_6969.StraightBevelSunGearLoadCase)

        @property
        def synchroniser_half_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6970.SynchroniserHalfLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6970

            return self._parent._cast(_6970.SynchroniserHalfLoadCase)

        @property
        def synchroniser_part_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6972.SynchroniserPartLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6972

            return self._parent._cast(_6972.SynchroniserPartLoadCase)

        @property
        def synchroniser_sleeve_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6973.SynchroniserSleeveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6973

            return self._parent._cast(_6973.SynchroniserSleeveLoadCase)

        @property
        def torque_converter_pump_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6977.TorqueConverterPumpLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6977

            return self._parent._cast(_6977.TorqueConverterPumpLoadCase)

        @property
        def torque_converter_turbine_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6978.TorqueConverterTurbineLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6978

            return self._parent._cast(_6978.TorqueConverterTurbineLoadCase)

        @property
        def unbalanced_mass_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6983.UnbalancedMassLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6983

            return self._parent._cast(_6983.UnbalancedMassLoadCase)

        @property
        def virtual_component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6984.VirtualComponentLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6984

            return self._parent._cast(_6984.VirtualComponentLoadCase)

        @property
        def worm_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6985.WormGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6985

            return self._parent._cast(_6985.WormGearLoadCase)

        @property
        def zerol_bevel_gear_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "_6988.ZerolBevelGearLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6988

            return self._parent._cast(_6988.ZerolBevelGearLoadCase)

        @property
        def component_load_case(
            self: "ComponentLoadCase._Cast_ComponentLoadCase",
        ) -> "ComponentLoadCase":
            return self._parent

        def __getattr__(self: "ComponentLoadCase._Cast_ComponentLoadCase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ComponentLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def additional_modal_damping_ratio(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.AdditionalModalDampingRatio

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @additional_modal_damping_ratio.setter
    @enforce_parameter_types
    def additional_modal_damping_ratio(
        self: Self, value: "Union[float, Tuple[float, bool]]"
    ):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.AdditionalModalDampingRatio = value

    @property
    def is_connected_to_ground(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsConnectedToGround

        if temp is None:
            return False

        return temp

    @property
    def is_torsionally_free(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.IsTorsionallyFree

        if temp is None:
            return False

        return temp

    @property
    def magnitude_of_rotation(self: Self) -> "float":
        """float"""
        temp = self.wrapped.MagnitudeOfRotation

        if temp is None:
            return 0.0

        return temp

    @magnitude_of_rotation.setter
    @enforce_parameter_types
    def magnitude_of_rotation(self: Self, value: "float"):
        self.wrapped.MagnitudeOfRotation = float(value) if value is not None else 0.0

    @property
    def rayleigh_damping_beta(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.RayleighDampingBeta

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @rayleigh_damping_beta.setter
    @enforce_parameter_types
    def rayleigh_damping_beta(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.RayleighDampingBeta = value

    @property
    def rotation_angle(self: Self) -> "float":
        """float"""
        temp = self.wrapped.RotationAngle

        if temp is None:
            return 0.0

        return temp

    @rotation_angle.setter
    @enforce_parameter_types
    def rotation_angle(self: Self, value: "float"):
        self.wrapped.RotationAngle = float(value) if value is not None else 0.0

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
    def cast_to(self: Self) -> "ComponentLoadCase._Cast_ComponentLoadCase":
        return self._Cast_ComponentLoadCase(self)
