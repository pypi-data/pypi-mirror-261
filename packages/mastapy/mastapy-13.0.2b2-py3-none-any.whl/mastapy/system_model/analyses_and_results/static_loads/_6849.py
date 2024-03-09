"""ConicalGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Union, Tuple, List

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal.implicit import overridable
from mastapy._internal.overridable_constructor import _unpack_overridable
from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.static_loads import _6895
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads", "ConicalGearMeshLoadCase"
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2309
    from mastapy.gears.gear_designs.conical import _1167, _1161
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6850,
        _6817,
        _6826,
        _6831,
        _6909,
        _6916,
        _6919,
        _6922,
        _6957,
        _6963,
        _6966,
        _6989,
        _6914,
        _6852,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConicalGearMeshLoadCase",)


Self = TypeVar("Self", bound="ConicalGearMeshLoadCase")


class ConicalGearMeshLoadCase(_6895.GearMeshLoadCase):
    """ConicalGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _CONICAL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalGearMeshLoadCase")

    class _Cast_ConicalGearMeshLoadCase:
        """Special nested class for casting ConicalGearMeshLoadCase to subclasses."""

        def __init__(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
            parent: "ConicalGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6895.GearMeshLoadCase":
            return self._parent._cast(_6895.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6914.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6852.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6817.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6826.BevelDifferentialGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6826

            return self._parent._cast(_6826.BevelDifferentialGearMeshLoadCase)

        @property
        def bevel_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6831.BevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6831

            return self._parent._cast(_6831.BevelGearMeshLoadCase)

        @property
        def hypoid_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6909.HypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6909

            return self._parent._cast(_6909.HypoidGearMeshLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6916.KlingelnbergCycloPalloidConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6916

            return self._parent._cast(
                _6916.KlingelnbergCycloPalloidConicalGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6919.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6919

            return self._parent._cast(
                _6919.KlingelnbergCycloPalloidHypoidGearMeshLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6922.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6922

            return self._parent._cast(
                _6922.KlingelnbergCycloPalloidSpiralBevelGearMeshLoadCase
            )

        @property
        def spiral_bevel_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6957.SpiralBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6957

            return self._parent._cast(_6957.SpiralBevelGearMeshLoadCase)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6963.StraightBevelDiffGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6963

            return self._parent._cast(_6963.StraightBevelDiffGearMeshLoadCase)

        @property
        def straight_bevel_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6966.StraightBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6966

            return self._parent._cast(_6966.StraightBevelGearMeshLoadCase)

        @property
        def zerol_bevel_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "_6989.ZerolBevelGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6989

            return self._parent._cast(_6989.ZerolBevelGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase",
        ) -> "ConicalGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "ConicalGearMeshLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def crowning(self: Self) -> "overridable.Overridable_float":
        """Overridable[float]"""
        temp = self.wrapped.Crowning

        if temp is None:
            return 0.0

        return constructor.new_from_mastapy(
            "mastapy._internal.implicit.overridable", "Overridable_float"
        )(temp)

    @crowning.setter
    @enforce_parameter_types
    def crowning(self: Self, value: "Union[float, Tuple[float, bool]]"):
        wrapper_type = overridable.Overridable_float.wrapper_type()
        enclosed_type = overridable.Overridable_float.implicit_type()
        value, is_overridden = _unpack_overridable(value)
        value = wrapper_type[enclosed_type](
            enclosed_type(value) if value is not None else 0.0, is_overridden
        )
        self.wrapped.Crowning = value

    @property
    def use_gleason_gems_data_for_efficiency(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseGleasonGEMSDataForEfficiency

        if temp is None:
            return False

        return temp

    @use_gleason_gems_data_for_efficiency.setter
    @enforce_parameter_types
    def use_gleason_gems_data_for_efficiency(self: Self, value: "bool"):
        self.wrapped.UseGleasonGEMSDataForEfficiency = (
            bool(value) if value is not None else False
        )

    @property
    def use_ki_mo_s_data_for_efficiency(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseKIMoSDataForEfficiency

        if temp is None:
            return False

        return temp

    @use_ki_mo_s_data_for_efficiency.setter
    @enforce_parameter_types
    def use_ki_mo_s_data_for_efficiency(self: Self, value: "bool"):
        self.wrapped.UseKIMoSDataForEfficiency = (
            bool(value) if value is not None else False
        )

    @property
    def use_user_specified_misalignments_in_tca(self: Self) -> "bool":
        """bool"""
        temp = self.wrapped.UseUserSpecifiedMisalignmentsInTCA

        if temp is None:
            return False

        return temp

    @use_user_specified_misalignments_in_tca.setter
    @enforce_parameter_types
    def use_user_specified_misalignments_in_tca(self: Self, value: "bool"):
        self.wrapped.UseUserSpecifiedMisalignmentsInTCA = (
            bool(value) if value is not None else False
        )

    @property
    def connection_design(self: Self) -> "_2309.ConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ConicalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def results_from_imported_xml(
        self: Self,
    ) -> "_1167.KIMoSBevelHypoidSingleLoadCaseResultsData":
        """mastapy.gears.gear_designs.conical.KIMoSBevelHypoidSingleLoadCaseResultsData

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ResultsFromImportedXML

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def user_specified_misalignments(self: Self) -> "_1161.ConicalMeshMisalignments":
        """mastapy.gears.gear_designs.conical.ConicalMeshMisalignments

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UserSpecifiedMisalignments

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(self: Self) -> "List[ConicalGearMeshLoadCase]":
        """List[mastapy.system_model.analyses_and_results.static_loads.ConicalGearMeshLoadCase]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    def get_harmonic_load_data_for_import(
        self: Self,
    ) -> "_6850.ConicalGearSetHarmonicLoadData":
        """mastapy.system_model.analyses_and_results.static_loads.ConicalGearSetHarmonicLoadData"""
        method_result = self.wrapped.GetHarmonicLoadDataForImport()
        type_ = method_result.GetType()
        return (
            constructor.new(type_.Namespace, type_.Name)(method_result)
            if method_result is not None
            else None
        )

    @property
    def cast_to(self: Self) -> "ConicalGearMeshLoadCase._Cast_ConicalGearMeshLoadCase":
        return self._Cast_ConicalGearMeshLoadCase(self)
