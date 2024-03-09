"""WormGearMeshHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6069,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_WORM_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "WormGearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2331
    from mastapy.system_model.analyses_and_results.static_loads import _6986
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6076,
        _6045,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("WormGearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="WormGearMeshHarmonicAnalysisOfSingleExcitation")


class WormGearMeshHarmonicAnalysisOfSingleExcitation(
    _6069.GearMeshHarmonicAnalysisOfSingleExcitation
):
    """WormGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _WORM_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting WormGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.GearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6069.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> (
            "_6076.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation"
        ):
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6076,
            )

            return self._parent._cast(
                _6076.InterMountableComponentConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_harmonic_analysis_of_single_excitation(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6045.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(
                _6045.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def worm_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "WormGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "WormGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

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
    def connection_load_case(self: Self) -> "_6986.WormGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.WormGearMeshLoadCase

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
    ) -> "WormGearMeshHarmonicAnalysisOfSingleExcitation._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_WormGearMeshHarmonicAnalysisOfSingleExcitation(self)
