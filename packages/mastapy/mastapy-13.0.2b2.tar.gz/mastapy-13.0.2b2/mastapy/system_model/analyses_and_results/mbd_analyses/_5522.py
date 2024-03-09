"""ZerolBevelGearMeshMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5396
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ZEROL_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "ZerolBevelGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2333
    from mastapy.system_model.analyses_and_results.static_loads import _6989
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5382,
        _5413,
        _5439,
        _5451,
        _5416,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7544, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ZerolBevelGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="ZerolBevelGearMeshMultibodyDynamicsAnalysis")


class ZerolBevelGearMeshMultibodyDynamicsAnalysis(
    _5396.BevelGearMeshMultibodyDynamicsAnalysis
):
    """ZerolBevelGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _ZEROL_BEVEL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting ZerolBevelGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
            parent: "ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5396.BevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(_5396.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5382.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382

            return self._parent._cast(
                _5382.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5413.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5439.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5416.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7544.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
        ) -> "ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis",
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
        self: Self, instance_to_wrap: "ZerolBevelGearMeshMultibodyDynamicsAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2333.ZerolBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.ZerolBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6989.ZerolBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.ZerolBevelGearMeshLoadCase

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
    ) -> "ZerolBevelGearMeshMultibodyDynamicsAnalysis._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_ZerolBevelGearMeshMultibodyDynamicsAnalysis(self)
