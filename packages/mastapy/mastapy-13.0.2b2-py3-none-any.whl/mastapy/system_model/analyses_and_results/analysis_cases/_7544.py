"""ConnectionTimeSeriesLoadAnalysisCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.analysis_cases import _7540
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONNECTION_TIME_SERIES_LOAD_ANALYSIS_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AnalysisCases",
    "ConnectionTimeSeriesLoadAnalysisCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.mbd_analyses import (
        _5381,
        _5382,
        _5389,
        _5391,
        _5396,
        _5401,
        _5405,
        _5407,
        _5410,
        _5413,
        _5416,
        _5418,
        _5421,
        _5425,
        _5427,
        _5428,
        _5434,
        _5439,
        _5444,
        _5451,
        _5452,
        _5455,
        _5458,
        _5470,
        _5473,
        _5480,
        _5482,
        _5489,
        _5492,
        _5495,
        _5498,
        _5501,
        _5510,
        _5519,
        _5522,
    )
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("ConnectionTimeSeriesLoadAnalysisCase",)


Self = TypeVar("Self", bound="ConnectionTimeSeriesLoadAnalysisCase")


class ConnectionTimeSeriesLoadAnalysisCase(_7540.ConnectionAnalysisCase):
    """ConnectionTimeSeriesLoadAnalysisCase

    This is a mastapy class.
    """

    TYPE = _CONNECTION_TIME_SERIES_LOAD_ANALYSIS_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConnectionTimeSeriesLoadAnalysisCase")

    class _Cast_ConnectionTimeSeriesLoadAnalysisCase:
        """Special nested class for casting ConnectionTimeSeriesLoadAnalysisCase to subclasses."""

        def __init__(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
            parent: "ConnectionTimeSeriesLoadAnalysisCase",
        ):
            self._parent = parent

        @property
        def connection_analysis_case(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_7540.ConnectionAnalysisCase":
            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> (
            "_5381.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5381

            return self._parent._cast(
                _5381.AbstractShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def agma_gleason_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5382.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5382

            return self._parent._cast(
                _5382.AGMAGleasonConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def belt_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5389.BeltConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5389

            return self._parent._cast(_5389.BeltConnectionMultibodyDynamicsAnalysis)

        @property
        def bevel_differential_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5391.BevelDifferentialGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5391

            return self._parent._cast(
                _5391.BevelDifferentialGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5396.BevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5396

            return self._parent._cast(_5396.BevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def clutch_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5401.ClutchConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5401

            return self._parent._cast(_5401.ClutchConnectionMultibodyDynamicsAnalysis)

        @property
        def coaxial_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5405.CoaxialConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5405

            return self._parent._cast(_5405.CoaxialConnectionMultibodyDynamicsAnalysis)

        @property
        def concept_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5407.ConceptCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5407

            return self._parent._cast(
                _5407.ConceptCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def concept_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5410.ConceptGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5410

            return self._parent._cast(_5410.ConceptGearMeshMultibodyDynamicsAnalysis)

        @property
        def conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5413.ConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5413

            return self._parent._cast(_5413.ConicalGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5416.ConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5416

            return self._parent._cast(_5416.ConnectionMultibodyDynamicsAnalysis)

        @property
        def coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5418.CouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5418

            return self._parent._cast(_5418.CouplingConnectionMultibodyDynamicsAnalysis)

        @property
        def cvt_belt_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5421.CVTBeltConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5421

            return self._parent._cast(_5421.CVTBeltConnectionMultibodyDynamicsAnalysis)

        @property
        def cycloidal_disc_central_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5425.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5425

            return self._parent._cast(
                _5425.CycloidalDiscCentralBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cycloidal_disc_planetary_bearing_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5427.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5427

            return self._parent._cast(
                _5427.CycloidalDiscPlanetaryBearingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def cylindrical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5428.CylindricalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5428

            return self._parent._cast(
                _5428.CylindricalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def face_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5434.FaceGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5434

            return self._parent._cast(_5434.FaceGearMeshMultibodyDynamicsAnalysis)

        @property
        def gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5439.GearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5439

            return self._parent._cast(_5439.GearMeshMultibodyDynamicsAnalysis)

        @property
        def hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5444.HypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5444

            return self._parent._cast(_5444.HypoidGearMeshMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5451

            return self._parent._cast(
                _5451.InterMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5452.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5452

            return self._parent._cast(
                _5452.KlingelnbergCycloPalloidConicalGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5455.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5455

            return self._parent._cast(
                _5455.KlingelnbergCycloPalloidHypoidGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> (
            "_5458.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis"
        ):
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5458

            return self._parent._cast(
                _5458.KlingelnbergCycloPalloidSpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def part_to_part_shear_coupling_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5470.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5470

            return self._parent._cast(
                _5470.PartToPartShearCouplingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def planetary_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5473.PlanetaryConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5473

            return self._parent._cast(
                _5473.PlanetaryConnectionMultibodyDynamicsAnalysis
            )

        @property
        def ring_pins_to_disc_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5480.RingPinsToDiscConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5480

            return self._parent._cast(
                _5480.RingPinsToDiscConnectionMultibodyDynamicsAnalysis
            )

        @property
        def rolling_ring_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5482.RollingRingConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5482

            return self._parent._cast(
                _5482.RollingRingConnectionMultibodyDynamicsAnalysis
            )

        @property
        def shaft_to_mountable_component_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5489.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5489

            return self._parent._cast(
                _5489.ShaftToMountableComponentConnectionMultibodyDynamicsAnalysis
            )

        @property
        def spiral_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5492.SpiralBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5492

            return self._parent._cast(
                _5492.SpiralBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def spring_damper_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5495.SpringDamperConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5495

            return self._parent._cast(
                _5495.SpringDamperConnectionMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_diff_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5498.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5498

            return self._parent._cast(
                _5498.StraightBevelDiffGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def straight_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5501.StraightBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5501

            return self._parent._cast(
                _5501.StraightBevelGearMeshMultibodyDynamicsAnalysis
            )

        @property
        def torque_converter_connection_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5510.TorqueConverterConnectionMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5510

            return self._parent._cast(
                _5510.TorqueConverterConnectionMultibodyDynamicsAnalysis
            )

        @property
        def worm_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5519.WormGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5519

            return self._parent._cast(_5519.WormGearMeshMultibodyDynamicsAnalysis)

        @property
        def zerol_bevel_gear_mesh_multibody_dynamics_analysis(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "_5522.ZerolBevelGearMeshMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses import _5522

            return self._parent._cast(_5522.ZerolBevelGearMeshMultibodyDynamicsAnalysis)

        @property
        def connection_time_series_load_analysis_case(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
        ) -> "ConnectionTimeSeriesLoadAnalysisCase":
            return self._parent

        def __getattr__(
            self: "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase",
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
        self: Self, instance_to_wrap: "ConnectionTimeSeriesLoadAnalysisCase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ConnectionTimeSeriesLoadAnalysisCase._Cast_ConnectionTimeSeriesLoadAnalysisCase":
        return self._Cast_ConnectionTimeSeriesLoadAnalysisCase(self)
