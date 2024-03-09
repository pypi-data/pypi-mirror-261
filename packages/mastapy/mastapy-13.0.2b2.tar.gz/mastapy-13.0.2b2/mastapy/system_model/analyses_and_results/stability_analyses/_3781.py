"""BevelGearMeshStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3769
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "BevelGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2305
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3776,
        _3866,
        _3875,
        _3878,
        _3896,
        _3797,
        _3825,
        _3832,
        _3800,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="BevelGearMeshStabilityAnalysis")


class BevelGearMeshStabilityAnalysis(_3769.AGMAGleasonConicalGearMeshStabilityAnalysis):
    """BevelGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BevelGearMeshStabilityAnalysis")

    class _Cast_BevelGearMeshStabilityAnalysis:
        """Special nested class for casting BevelGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
            parent: "BevelGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_3769.AGMAGleasonConicalGearMeshStabilityAnalysis":
            return self._parent._cast(_3769.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_3797.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_3825.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_3832.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_3800.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_3776.BevelDifferentialGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3776,
            )

            return self._parent._cast(_3776.BevelDifferentialGearMeshStabilityAnalysis)

        @property
        def spiral_bevel_gear_mesh_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_3866.SpiralBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3866,
            )

            return self._parent._cast(_3866.SpiralBevelGearMeshStabilityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_3875.StraightBevelDiffGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3875,
            )

            return self._parent._cast(_3875.StraightBevelDiffGearMeshStabilityAnalysis)

        @property
        def straight_bevel_gear_mesh_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_3878.StraightBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3878,
            )

            return self._parent._cast(_3878.StraightBevelGearMeshStabilityAnalysis)

        @property
        def zerol_bevel_gear_mesh_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "_3896.ZerolBevelGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3896,
            )

            return self._parent._cast(_3896.ZerolBevelGearMeshStabilityAnalysis)

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
        ) -> "BevelGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BevelGearMeshStabilityAnalysis.TYPE"):
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
    ) -> "BevelGearMeshStabilityAnalysis._Cast_BevelGearMeshStabilityAnalysis":
        return self._Cast_BevelGearMeshStabilityAnalysis(self)
