"""GearMeshDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6346
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "GearMeshDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2315
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6284,
        _6291,
        _6296,
        _6309,
        _6312,
        _6327,
        _6335,
        _6344,
        _6348,
        _6351,
        _6354,
        _6381,
        _6387,
        _6390,
        _6405,
        _6408,
        _6314,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7542,
        _7543,
        _7540,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshDynamicAnalysis",)


Self = TypeVar("Self", bound="GearMeshDynamicAnalysis")


class GearMeshDynamicAnalysis(_6346.InterMountableComponentConnectionDynamicAnalysis):
    """GearMeshDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshDynamicAnalysis")

    class _Cast_GearMeshDynamicAnalysis:
        """Special nested class for casting GearMeshDynamicAnalysis to subclasses."""

        def __init__(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
            parent: "GearMeshDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def inter_mountable_component_connection_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6346.InterMountableComponentConnectionDynamicAnalysis":
            return self._parent._cast(
                _6346.InterMountableComponentConnectionDynamicAnalysis
            )

        @property
        def connection_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6314.ConnectionDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6314

            return self._parent._cast(_6314.ConnectionDynamicAnalysis)

        @property
        def connection_fe_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_7542.ConnectionFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7542

            return self._parent._cast(_7542.ConnectionFEAnalysis)

        @property
        def connection_static_load_analysis_case(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6284.AGMAGleasonConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6284

            return self._parent._cast(_6284.AGMAGleasonConicalGearMeshDynamicAnalysis)

        @property
        def bevel_differential_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6291.BevelDifferentialGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6291

            return self._parent._cast(_6291.BevelDifferentialGearMeshDynamicAnalysis)

        @property
        def bevel_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6296.BevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6296

            return self._parent._cast(_6296.BevelGearMeshDynamicAnalysis)

        @property
        def concept_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6309.ConceptGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6309

            return self._parent._cast(_6309.ConceptGearMeshDynamicAnalysis)

        @property
        def conical_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6312.ConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6312

            return self._parent._cast(_6312.ConicalGearMeshDynamicAnalysis)

        @property
        def cylindrical_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6327.CylindricalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6327

            return self._parent._cast(_6327.CylindricalGearMeshDynamicAnalysis)

        @property
        def face_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6335.FaceGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6335

            return self._parent._cast(_6335.FaceGearMeshDynamicAnalysis)

        @property
        def hypoid_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6344.HypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6344

            return self._parent._cast(_6344.HypoidGearMeshDynamicAnalysis)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6348.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6348

            return self._parent._cast(
                _6348.KlingelnbergCycloPalloidConicalGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6351.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6351

            return self._parent._cast(
                _6351.KlingelnbergCycloPalloidHypoidGearMeshDynamicAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6354.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6354

            return self._parent._cast(
                _6354.KlingelnbergCycloPalloidSpiralBevelGearMeshDynamicAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6381.SpiralBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6381

            return self._parent._cast(_6381.SpiralBevelGearMeshDynamicAnalysis)

        @property
        def straight_bevel_diff_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6387.StraightBevelDiffGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6387

            return self._parent._cast(_6387.StraightBevelDiffGearMeshDynamicAnalysis)

        @property
        def straight_bevel_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6390.StraightBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6390

            return self._parent._cast(_6390.StraightBevelGearMeshDynamicAnalysis)

        @property
        def worm_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6405.WormGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6405

            return self._parent._cast(_6405.WormGearMeshDynamicAnalysis)

        @property
        def zerol_bevel_gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "_6408.ZerolBevelGearMeshDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6408

            return self._parent._cast(_6408.ZerolBevelGearMeshDynamicAnalysis)

        @property
        def gear_mesh_dynamic_analysis(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis",
        ) -> "GearMeshDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2315.GearMesh":
        """mastapy.system_model.connections_and_sockets.gears.GearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearMeshDynamicAnalysis._Cast_GearMeshDynamicAnalysis":
        return self._Cast_GearMeshDynamicAnalysis(self)
