"""CylindricalGearMeshHarmonicAnalysisOfSingleExcitation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
    _6069,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalysesSingleExcitation",
    "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2311
    from mastapy.system_model.analyses_and_results.static_loads import _6866
    from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
        _6076,
        _6045,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",)


Self = TypeVar("Self", bound="CylindricalGearMeshHarmonicAnalysisOfSingleExcitation")


class CylindricalGearMeshHarmonicAnalysisOfSingleExcitation(
    _6069.GearMeshHarmonicAnalysisOfSingleExcitation
):
    """CylindricalGearMeshHarmonicAnalysisOfSingleExcitation

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_HARMONIC_ANALYSIS_OF_SINGLE_EXCITATION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation"
    )

    class _Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation:
        """Special nested class for casting CylindricalGearMeshHarmonicAnalysisOfSingleExcitation to subclasses."""

        def __init__(
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
            parent: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
        ):
            self._parent = parent

        @property
        def gear_mesh_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6069.GearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent._cast(_6069.GearMeshHarmonicAnalysisOfSingleExcitation)

        @property
        def inter_mountable_component_connection_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
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
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_6045.ConnectionHarmonicAnalysisOfSingleExcitation":
            from mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation import (
                _6045,
            )

            return self._parent._cast(
                _6045.ConnectionHarmonicAnalysisOfSingleExcitation
            )

        @property
        def connection_static_load_analysis_case(
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_harmonic_analysis_of_single_excitation(
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
        ) -> "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation",
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
        instance_to_wrap: "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2311.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6866.CylindricalGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def planetaries(
        self: Self,
    ) -> "List[CylindricalGearMeshHarmonicAnalysisOfSingleExcitation]":
        """List[mastapy.system_model.analyses_and_results.harmonic_analyses_single_excitation.CylindricalGearMeshHarmonicAnalysisOfSingleExcitation]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Planetaries

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearMeshHarmonicAnalysisOfSingleExcitation._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation":
        return self._Cast_CylindricalGearMeshHarmonicAnalysisOfSingleExcitation(self)
