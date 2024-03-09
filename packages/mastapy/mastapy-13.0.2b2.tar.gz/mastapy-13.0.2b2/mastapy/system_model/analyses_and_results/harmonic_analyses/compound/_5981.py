"""SpiralBevelGearMeshCompoundHarmonicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import _5898
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SPIRAL_BEVEL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses.Compound",
    "SpiralBevelGearMeshCompoundHarmonicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2325
    from mastapy.system_model.analyses_and_results.harmonic_analyses import _5815
    from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
        _5886,
        _5914,
        _5940,
        _5946,
        _5916,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("SpiralBevelGearMeshCompoundHarmonicAnalysis",)


Self = TypeVar("Self", bound="SpiralBevelGearMeshCompoundHarmonicAnalysis")


class SpiralBevelGearMeshCompoundHarmonicAnalysis(
    _5898.BevelGearMeshCompoundHarmonicAnalysis
):
    """SpiralBevelGearMeshCompoundHarmonicAnalysis

    This is a mastapy class.
    """

    TYPE = _SPIRAL_BEVEL_GEAR_MESH_COMPOUND_HARMONIC_ANALYSIS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis"
    )

    class _Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis:
        """Special nested class for casting SpiralBevelGearMeshCompoundHarmonicAnalysis to subclasses."""

        def __init__(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
            parent: "SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_compound_harmonic_analysis(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ) -> "_5898.BevelGearMeshCompoundHarmonicAnalysis":
            return self._parent._cast(_5898.BevelGearMeshCompoundHarmonicAnalysis)

        @property
        def agma_gleason_conical_gear_mesh_compound_harmonic_analysis(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ) -> "_5886.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5886,
            )

            return self._parent._cast(
                _5886.AGMAGleasonConicalGearMeshCompoundHarmonicAnalysis
            )

        @property
        def conical_gear_mesh_compound_harmonic_analysis(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ) -> "_5914.ConicalGearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5914,
            )

            return self._parent._cast(_5914.ConicalGearMeshCompoundHarmonicAnalysis)

        @property
        def gear_mesh_compound_harmonic_analysis(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ) -> "_5940.GearMeshCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5940,
            )

            return self._parent._cast(_5940.GearMeshCompoundHarmonicAnalysis)

        @property
        def inter_mountable_component_connection_compound_harmonic_analysis(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ) -> "_5946.InterMountableComponentConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5946,
            )

            return self._parent._cast(
                _5946.InterMountableComponentConnectionCompoundHarmonicAnalysis
            )

        @property
        def connection_compound_harmonic_analysis(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ) -> "_5916.ConnectionCompoundHarmonicAnalysis":
            from mastapy.system_model.analyses_and_results.harmonic_analyses.compound import (
                _5916,
            )

            return self._parent._cast(_5916.ConnectionCompoundHarmonicAnalysis)

        @property
        def connection_compound_analysis(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def spiral_bevel_gear_mesh_compound_harmonic_analysis(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
        ) -> "SpiralBevelGearMeshCompoundHarmonicAnalysis":
            return self._parent

        def __getattr__(
            self: "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis",
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
        self: Self, instance_to_wrap: "SpiralBevelGearMeshCompoundHarmonicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2325.SpiralBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.SpiralBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_5815.SpiralBevelGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearMeshHarmonicAnalysis]

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
    ) -> "List[_5815.SpiralBevelGearMeshHarmonicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses.SpiralBevelGearMeshHarmonicAnalysis]

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
    ) -> "SpiralBevelGearMeshCompoundHarmonicAnalysis._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis":
        return self._Cast_SpiralBevelGearMeshCompoundHarmonicAnalysis(self)
