"""BevelDifferentialGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6831
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "BevelDifferentialGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2303
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6817,
        _6849,
        _6895,
        _6914,
        _6852,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearMeshLoadCase",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshLoadCase")


class BevelDifferentialGearMeshLoadCase(_6831.BevelGearMeshLoadCase):
    """BevelDifferentialGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelDifferentialGearMeshLoadCase")

    class _Cast_BevelDifferentialGearMeshLoadCase:
        """Special nested class for casting BevelDifferentialGearMeshLoadCase to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
            parent: "BevelDifferentialGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "_6831.BevelGearMeshLoadCase":
            return self._parent._cast(_6831.BevelGearMeshLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "_6817.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "_6849.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "_6895.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "_6914.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "_6852.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_load_case(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
        ) -> "BevelDifferentialGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearMeshLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2303.BevelDifferentialGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelDifferentialGearMesh

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
    ) -> "BevelDifferentialGearMeshLoadCase._Cast_BevelDifferentialGearMeshLoadCase":
        return self._Cast_BevelDifferentialGearMeshLoadCase(self)
