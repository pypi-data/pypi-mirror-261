"""StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7030,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_STRAIGHT_BEVEL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2329
    from mastapy.system_model.analyses_and_results.static_loads import _6966
    from mastapy.system_model.analyses_and_results.system_deflections import _2818
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7017,
        _7046,
        _7072,
        _7079,
        _7048,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7543, _7540
    from mastapy.system_model.analyses_and_results import _2651, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation"
)


class StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation(
    _7030.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
):
    """StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = _STRAIGHT_BEVEL_GEAR_MESH_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
            parent: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7030.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7030.BevelGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def agma_gleason_conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> (
            "_7017.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation"
        ):
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7017,
            )

            return self._parent._cast(
                _7017.AGMAGleasonConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def conical_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7046.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7046,
            )

            return self._parent._cast(
                _7046.ConicalGearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7072.GearMeshAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7072,
            )

            return self._parent._cast(
                _7072.GearMeshAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def inter_mountable_component_connection_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7079.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7079,
            )

            return self._parent._cast(
                _7079.InterMountableComponentConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7048.ConnectionAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7048,
            )

            return self._parent._cast(
                _7048.ConnectionAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def connection_static_load_analysis_case(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7543.ConnectionStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7543

            return self._parent._cast(_7543.ConnectionStaticLoadAnalysisCase)

        @property
        def connection_analysis_case(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7540.ConnectionAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7540

            return self._parent._cast(_7540.ConnectionAnalysisCase)

        @property
        def connection_analysis(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2651.ConnectionAnalysis":
            from mastapy.system_model.analyses_and_results import _2651

            return self._parent._cast(_2651.ConnectionAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def straight_bevel_gear_mesh_advanced_time_stepping_analysis_for_modulation(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
        ) -> "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_design(self: Self) -> "_2329.StraightBevelGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.StraightBevelGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_load_case(self: Self) -> "_6966.StraightBevelGearMeshLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.StraightBevelGearMeshLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ConnectionLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2818.StraightBevelGearMeshSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.StraightBevelGearMeshSystemDeflection

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SystemDeflectionResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation":
        return (
            self._Cast_StraightBevelGearMeshAdvancedTimeSteppingAnalysisForModulation(
                self
            )
        )
