"""StraightBevelDiffGearMeshStabilityAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.stability_analyses import _3781
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_DIFF_GEAR_MESH_STABILITY_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StabilityAnalyses",
    "StraightBevelDiffGearMeshStabilityAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2327
    from mastapy.system_model.analyses_and_results.static_loads import _6963
    from mastapy.system_model.analyses_and_results.stability_analyses import (
        _3769,
        _3797,
        _3825,
        _3832,
        _3800,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelDiffGearMeshStabilityAnalysis",)


Self = TypeVar("Self", bound="StraightBevelDiffGearMeshStabilityAnalysis")


class StraightBevelDiffGearMeshStabilityAnalysis(_3781.BevelGearMeshStabilityAnalysis):
    """StraightBevelDiffGearMeshStabilityAnalysis

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_DIFF_GEAR_MESH_STABILITY_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_StraightBevelDiffGearMeshStabilityAnalysis"
    )

    class _Cast_StraightBevelDiffGearMeshStabilityAnalysis:
        """Special nested class for casting StraightBevelDiffGearMeshStabilityAnalysis to subclasses."""

        def __init__(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
            parent: "StraightBevelDiffGearMeshStabilityAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_3781.BevelGearMeshStabilityAnalysis":
            return self._parent._cast(_3781.BevelGearMeshStabilityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_3769.AGMAGleasonConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3769,
            )

            return self._parent._cast(_3769.AGMAGleasonConicalGearMeshStabilityAnalysis)

        @property
        def conical_gear_mesh_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_3797.ConicalGearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3797,
            )

            return self._parent._cast(_3797.ConicalGearMeshStabilityAnalysis)

        @property
        def gear_mesh_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_3825.GearMeshStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3825,
            )

            return self._parent._cast(_3825.GearMeshStabilityAnalysis)

        @property
        def inter_mountable_component_connection_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_3832.InterMountableComponentConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3832,
            )

            return self._parent._cast(
                _3832.InterMountableComponentConnectionStabilityAnalysis
            )

        @property
        def connection_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_3800.ConnectionStabilityAnalysis":
            from mastapy.system_model.analyses_and_results.stability_analyses import (
                _3800,
            )

            return self._parent._cast(_3800.ConnectionStabilityAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_stability_analysis(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
        ) -> "StraightBevelDiffGearMeshStabilityAnalysis":
            return self._parent

        def __getattr__(
            self: "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis",
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
        self: Self, instance_to_wrap: "StraightBevelDiffGearMeshStabilityAnalysis.TYPE"
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
    def connection_load_case(self: Self) -> "_6963.StraightBevelDiffGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelDiffGearMeshLoadCase

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
    ) -> "StraightBevelDiffGearMeshStabilityAnalysis._Cast_StraightBevelDiffGearMeshStabilityAnalysis":
        return self._Cast_StraightBevelDiffGearMeshStabilityAnalysis(self)
