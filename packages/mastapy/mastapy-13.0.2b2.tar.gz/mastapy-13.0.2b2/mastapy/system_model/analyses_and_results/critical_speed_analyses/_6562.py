"""BevelGearMeshCriticalSpeedAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.critical_speed_analyses import _6550
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.CriticalSpeedAnalyses",
    "BevelGearMeshCriticalSpeedAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2305
    from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
        _6557,
        _6648,
        _6654,
        _6657,
        _6675,
        _6578,
        _6607,
        _6613,
        _6580,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCriticalSpeedAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshCriticalSpeedAnalysis")


class BevelGearMeshCriticalSpeedAnalysis(
    _6550.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
):
    """BevelGearMeshCriticalSpeedAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_CRITICAL_SPEED_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshCriticalSpeedAnalysis")

    class _Cast_BevelGearMeshCriticalSpeedAnalysis:
        """Special nested class for casting BevelGearMeshCriticalSpeedAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
            parent: "BevelGearMeshCriticalSpeedAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6550.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis":
            return self._parent._cast(
                _6550.AGMAGleasonConicalGearMeshCriticalSpeedAnalysis
            )

        @property
        def conical_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6578.ConicalGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6578,
            )

            return self._parent._cast(_6578.ConicalGearMeshCriticalSpeedAnalysis)

        @property
        def gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6607.GearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6607,
            )

            return self._parent._cast(_6607.GearMeshCriticalSpeedAnalysis)

        @property
        def inter_mountable_component_connection_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6613.InterMountableComponentConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6613,
            )

            return self._parent._cast(
                _6613.InterMountableComponentConnectionCriticalSpeedAnalysis
            )

        @property
        def connection_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6580.ConnectionCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6580,
            )

            return self._parent._cast(_6580.ConnectionCriticalSpeedAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6557.BevelDifferentialGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6557,
            )

            return self._parent._cast(
                _6557.BevelDifferentialGearMeshCriticalSpeedAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6648.SpiralBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6648,
            )

            return self._parent._cast(_6648.SpiralBevelGearMeshCriticalSpeedAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6654.StraightBevelDiffGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6654,
            )

            return self._parent._cast(
                _6654.StraightBevelDiffGearMeshCriticalSpeedAnalysis
            )

        @property
        def straight_bevel_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6657.StraightBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6657,
            )

            return self._parent._cast(_6657.StraightBevelGearMeshCriticalSpeedAnalysis)

        @property
        def zerol_bevel_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "_6675.ZerolBevelGearMeshCriticalSpeedAnalysis":
            from mastapy.system_model.analyses_and_results.critical_speed_analyses import (
                _6675,
            )

            return self._parent._cast(_6675.ZerolBevelGearMeshCriticalSpeedAnalysis)

        @property
        def bevel_gear_mesh_critical_speed_analysis(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
        ) -> "BevelGearMeshCriticalSpeedAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis",
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
        self: Self, instance_to_wrap: "BevelGearMeshCriticalSpeedAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2305.BevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.BevelGearMesh

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
    ) -> "BevelGearMeshCriticalSpeedAnalysis._Cast_BevelGearMeshCriticalSpeedAnalysis":
        return self._Cast_BevelGearMeshCriticalSpeedAnalysis(self)
