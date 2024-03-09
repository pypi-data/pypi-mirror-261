"""BevelDifferentialGearMeshMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.mbd_analyses import _5396
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses",
    "BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2303
    from mastapy.system_model.analyses_and_results.static_loads import _6826
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
__all__ = ("BevelDifferentialGearMeshMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="BevelDifferentialGearMeshMultibodyDynamicsAnalysis")


class BevelDifferentialGearMeshMultibodyDynamicsAnalysis(
    _5396.BevelGearMeshMultibodyDynamicsAnalysis
):
    """BevelDifferentialGearMeshMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_MESH_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis"
    )

    class _Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis:
        """Special nested class for casting BevelDifferentialGearMeshMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
            parent: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5396.BevelGearMeshMultibodyDynamicsAnalysis":
            return self._parent._cast(_5396.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5382.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382

            return self._parent._cast(
                _5382.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5413.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5439.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def connection_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_5416.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.ConnectionMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7544.ConnectionTimeSeriesLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7544

            return self._parent._cast(_7544.ConnectionTimeSeriesLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
        ) -> "BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "BevelDifferentialGearMeshMultibodyDynamicsAnalysis.TYPE",
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
    def connection_load_case(self: Self) -> "_6826.BevelDifferentialGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearMeshLoadCase

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
    ) -> "BevelDifferentialGearMeshMultibodyDynamicsAnalysis._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
        return self._Cast_BevelDifferentialGearMeshMultibodyDynamicsAnalysis(self)
