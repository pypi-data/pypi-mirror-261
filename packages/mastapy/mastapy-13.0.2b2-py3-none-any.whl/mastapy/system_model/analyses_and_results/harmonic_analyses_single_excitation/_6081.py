"""KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6078,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
        "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.static_loads import _6919
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6043,
        _6069,
        _6076,
        _6045,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar(
    "Self",
    bound="KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
)


class KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation(
    _6078.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
):
    """KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6078.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(
                _6078.KlingelnbergCycloPalloidConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def conical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6043.ConicalGearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6043,
            )

            return self._parent._cast(
                _6043.ConicalGearMeshHarmonicAnalysisOfSingleExcitation
            )

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.GearMeshHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6069,
            )

            return self._parent._cast(_6069.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
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
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6045.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(
                _6045.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2321.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(
        self: Self,
    ) -> "_6919.KlingelnbergCycloPalloidHypoidGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.KlingelnbergCycloPalloidHypoidGearMeshLoadCase

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_KlingelnbergCycloPalloidHypoidGearMeshHarmonicAnalysisOfSingleExcitation(
            self
        )
