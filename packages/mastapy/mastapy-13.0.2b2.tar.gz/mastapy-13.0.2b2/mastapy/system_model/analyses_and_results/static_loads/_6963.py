"""StraightBevelDiffGearMeshLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6831
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "StraightBevelDiffGearMeshLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6817,
        _6849,
        _6895,
        _6914,
        _6852,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshLoadCase",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshLoadCase")


class StraightBevelDiffGearMeshLoadCase(_6831.BevelGearMeshLoadCase):
    """StraightBevelDiffGearMeshLoadCase

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_StraightBevelDiffGearMeshLoadCase")

    class _Cast_StraightBevelDiffGearMeshLoadCase:
        """Special nested class for casting StraightBevelDiffGearMeshLoadCase to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
            parent: "StraightBevelDiffGearMeshLoadCase",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_load_case(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
        ) -> "_6831.BevelGearMeshLoadCase":
            return self._parent._cast(_6831.BevelGearMeshLoadCase)

        @property
        def agma_gleason_conical_gear_mesh_load_case(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
        ) -> "_6817.AGMAGleasonConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6817

            return self._parent._cast(_6817.AGMAGleasonConicalGearMeshLoadCase)

        @property
        def conical_gear_mesh_load_case(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
        ) -> "_6849.ConicalGearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6849

            return self._parent._cast(_6849.ConicalGearMeshLoadCase)

        @property
        def gear_mesh_load_case(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
        ) -> "_6895.GearMeshLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6895

            return self._parent._cast(_6895.GearMeshLoadCase)

        @property
        def inter_mountable_component_connection_load_case(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
        ) -> "_6914.InterMountableComponentConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6914

            return self._parent._cast(_6914.InterMountableComponentConnectionLoadCase)

        @property
        def connection_load_case(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
        ) -> "_6852.ConnectionLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6852

            return self._parent._cast(_6852.ConnectionLoadCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_load_case(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
        ) -> "StraightBevelDiffGearMeshLoadCase":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearMeshLoadCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2327.StraightBevelDiffGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelDiffGearMesh

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
    ) -> "StraightBevelDiffGearMeshLoadCase._Cast_StraightBevelDiffGearMeshLoadCase":
        return self._Cast_StraightBevelDiffGearMeshLoadCase(self)
