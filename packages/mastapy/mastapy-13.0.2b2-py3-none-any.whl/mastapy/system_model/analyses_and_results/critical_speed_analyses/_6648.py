"""SpiralBevelGearMeshCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6562
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "SpiralBevelGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.static_loads import _6957
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6550,
        _6578,
        _6607,
        _6613,
        _6580,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCriticalSpeedAnalysis")


class SpiralBevelGearMeshCriticalSpeedAnalysis(
    _6562.BevelGearMeshCriticalSpeedAnalysis
):
    """SpiralBevelGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCriticalSpeedAnalysis"
    )

    class _Cast_SpiralBevelGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting SpiralBevelGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
            parent: "SpiralBevelGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6562.BevelGearMeshCriticalSpeedAnalysis":
            return self._parent._cast(_6562.BevelGearMeshCriticalSpeedAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6550.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6550,
            )

            return self._parent._cast(
                _6550.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6578.ConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6607.GearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6607,
            )

            return self._parent._cast(_6607.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6613.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(
                _6613.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6580.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
        ) -> "SpiralBevelGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2325.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6957.SpiralBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SpiralBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SpiralBevelGearMeshCriticalSpeedAnalysis._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis":
        return self._Cast_SpiralBevelGearMeshCriticalSpeedAnalysis(self)
