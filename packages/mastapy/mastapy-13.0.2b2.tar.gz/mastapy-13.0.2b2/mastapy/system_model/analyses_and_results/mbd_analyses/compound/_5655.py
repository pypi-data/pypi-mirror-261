"""WormGearMeshCompoundMultibodyDynamicsAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.mbd_analyses.compound import _5590
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.MBDAnalyses.Compound",
    "WormGearMeshCompoundMultibodyDynamicsAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.mbd_analyses import _5519
    from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
        _5596,
        _5566,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshCompoundMultibodyDynamicsAnalysis",)


Self = TypeVar("Self", bound="WormGearMeshCompoundMultibodyDynamicsAnalysis")


class WormGearMeshCompoundMultibodyDynamicsAnalysis(
    _5590.GearMeshCompoundMultibodyDynamicsAnalysis
):
    """WormGearMeshCompoundMultibodyDynamicsAnalysis

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_COMPOUND_MULTIBODY_DYNAMICS_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis"
    )

    class _Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis:
        """Special nested class for casting WormGearMeshCompoundMultibodyDynamicsAnalysis to subclasses."""

        def __init__(
            self: "WormGearMeshCompoundMultibodyDynamicsAnalysis._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis",
            parent: "WormGearMeshCompoundMultibodyDynamicsAnalysis",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_multibody_dynamics_analysis(
            self: "WormGearMeshCompoundMultibodyDynamicsAnalysis._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5590.GearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent._cast(_5590.GearMeshCompoundMultibodyDynamicsAnalysis)

        @property
        def inter_mountable_component_connection_compound_multibody_dynamics_analysis(
            self: "WormGearMeshCompoundMultibodyDynamicsAnalysis._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5596.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5596,
            )

            return self._parent._cast(
                _5596.InterMountableComponentConnectionCompoundMultibodyDynamicsAnalysis
            )

        @property
        def connection_compound_multibody_dynamics_analysis(
            self: "WormGearMeshCompoundMultibodyDynamicsAnalysis._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_5566.ConnectionCompoundMultibodyDynamicsAnalysis":
            from mastapy.system_model.analyses_and_results.mbd_analyses.compound import (
                _5566,
            )

            return self._parent._cast(_5566.ConnectionCompoundMultibodyDynamicsAnalysis)

        @property
        def connection_compound_analysis(
            self: "WormGearMeshCompoundMultibodyDynamicsAnalysis._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "WormGearMeshCompoundMultibodyDynamicsAnalysis._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshCompoundMultibodyDynamicsAnalysis._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_compound_multibody_dynamics_analysis(
            self: "WormGearMeshCompoundMultibodyDynamicsAnalysis._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis",
        ) -> "WormGearMeshCompoundMultibodyDynamicsAnalysis":
            return self._parent

        def __getattr__(
            self: "WormGearMeshCompoundMultibodyDynamicsAnalysis._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis",
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
        instance_to_wrap: "WormGearMeshCompoundMultibodyDynamicsAnalysis.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2331.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_design(self: Self) -> "_2331.WormGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.WormGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5519.WormGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.WormGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_5519.WormGearMeshMultibodyDynamicsAnalysis]":
        """List[mastapy.system_model.analyses_and_results.mbd_analyses.WormGearMeshMultibodyDynamicsAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "WormGearMeshCompoundMultibodyDynamicsAnalysis._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis":
        return self._Cast_WormGearMeshCompoundMultibodyDynamicsAnalysis(self)
