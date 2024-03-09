"""AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5413
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_AGMA_GLEASON_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2301
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5391,
        _5396,
        _5444,
        _5492,
        _5498,
        _5501,
        _5522,
        _5439,
        _5451,
        _5416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7544, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis")


class AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis(
    _5413.ConicalGearMeshMultibodyDynamicsAnalysis
):
    """AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _AGMA_GLEASON_CONICAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
            parent: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5413.ConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(_5413.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5439.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5416.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7544.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5391.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(
                _5391.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5396.BevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5444.HypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(_5444.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5492.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(
                _5492.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5498.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5501.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(
                _5501.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5522.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(_5522.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
        ) -> "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis",
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
        self: Self,
        instance_to_wrap: "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2301.AGMAGleasonConicalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.AGMAGleasonConicalGearMesh

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
    ) -> "AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis(self)
