"""InterMountableComponentConnectionLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6852
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "InterMountableComponentConnectionLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets import _2283
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6817,
        _6823,
        _6826,
        _6831,
        _6835,
        _6841,
        _6845,
        _6849,
        _6854,
        _6857,
        _6866,
        _6888,
        _6895,
        _6909,
        _6916,
        _6919,
        _6922,
        _6932,
        _6947,
        _6949,
        _6957,
        _6959,
        _6963,
        _6966,
        _6975,
        _6986,
        _6989,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("InterMountableComponentConnectionLoadCase",)


Self = TypeVar("Self", bound="InterMountableComponentConnectionLoadCase")


class InterMountableComponentConnectionLoadCase(_6852.ConnectionLoadCase):
    """InterMountableComponentConnectionLoadCase

    This is a mastapy class.
    """

    TYPE = _INTER_MOUNTABLE_COMPONENT_CONNECTION_LOAD_CASE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_InterMountableComponentConnectionLoadCase"
    )

    class _Cast_InterMountableComponentConnectionLoadCase:
        """Special nested class for casting InterMountableComponentConnectionLoadCase to subclasses."""

        def __init__(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
            parent: "InterMountableComponentConnectionLoadCase",
        ):
            self._parent = parent

        @property
        def connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6852.ConnectionLoadCase":
            return self._parent._cast(_6852.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6817.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def belt_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6823.BeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6823

            return self._parent._cast(_6823.BeltConnectionLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6826.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6831.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.BevelGearMeshLoadCase)

        @property
        def clutch_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6835.ClutchConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6835

            return self._parent._cast(_6835.ClutchConnectionLoadCase)

        @property
        def concept_coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6841.ConceptCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6841

            return self._parent._cast(_6841.ConceptCouplingConnectionLoadCase)

        @property
        def concept_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6845.ConceptGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6845

            return self._parent._cast(_6845.ConceptGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6849.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConicalGearMeshLoadCase)

        @property
        def coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6854.CouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6854

            return self._parent._cast(_6854.CouplingConnectionLoadCase)

        @property
        def cvt_belt_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6857.CVTBeltConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6857

            return self._parent._cast(_6857.CVTBeltConnectionLoadCase)

        @property
        def cylindrical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6866.CylindricalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6866

            return self._parent._cast(_6866.CylindricalGearMeshLoadCase)

        @property
        def face_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6888.FaceGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6888

            return self._parent._cast(_6888.FaceGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6895.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.GearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6909.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6916.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(
                _6916.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6919.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6919

            return self._parent._cast(
                _6919.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6922.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(
                _6922.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def part_to_part_shear_coupling_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6932.PartToPartShearCouplingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6932

            return self._parent._cast(_6932.PartToPartShearCouplingConnectionLoadCase)

        @property
        def ring_pins_to_disc_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6947.RingPinsToDiscConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6947

            return self._parent._cast(_6947.RingPinsToDiscConnectionLoadCase)

        @property
        def rolling_ring_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6949.RollingRingConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6949

            return self._parent._cast(_6949.RollingRingConnectionLoadCase)

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6957.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.SpiralBevelGearMeshLoadCase)

        @property
        def spring_damper_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6959.SpringDamperConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6959

            return self._parent._cast(_6959.SpringDamperConnectionLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6963.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6966.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.StraightBevelGearMeshLoadCase)

        @property
        def torque_converter_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6975.TorqueConverterConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6975

            return self._parent._cast(_6975.TorqueConverterConnectionLoadCase)

        @property
        def worm_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6986.WormGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6986

            return self._parent._cast(_6986.WormGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "_6989.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.ZerolBevelGearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
        ) -> "InterMountableComponentConnectionLoadCase":
            return self._parent

        def __getattr__(
            self: "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase",
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
        self: Self, instance_to_wrap: "InterMountableComponentConnectionLoadCase.TYPE"
    ):
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
    def connection_design(self: Self) -> "_2283.InterMountableComponentConnection":
        """mastapy.system_model.connections_and_sockets.InterMountableComponentConnection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "InterMountableComponentConnectionLoadCase._Cast_InterMountableComponentConnectionLoadCase":
        return self._Cast_InterMountableComponentConnectionLoadCase(self)
