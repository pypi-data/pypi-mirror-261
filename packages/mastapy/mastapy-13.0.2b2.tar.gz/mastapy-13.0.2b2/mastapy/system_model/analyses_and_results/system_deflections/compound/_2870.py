"""BevelGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2858
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "BevelGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2708
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2865,
        _2955,
        _2961,
        _2964,
        _2982,
        _2886,
        _2913,
        _2919,
        _2888,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="BevelGearMeshCompoundSystemDeflection")


class BevelGearMeshCompoundSystemDeflection(
    _2858.AGMAGleasonConicalGearMeshCompoundSystemDeflection
):
    """BevelGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelGearMeshCompoundSystemDeflection"
    )

    class _Cast_BevelGearMeshCompoundSystemDeflection:
        """Special nested class for casting BevelGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
            parent: "BevelGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def agma_gleason_conical_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2858.AGMAGleasonConicalGearMeshCompoundSystemDeflection":
            return self._parent._cast(
                _2858.AGMAGleasonConicalGearMeshCompoundSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2886.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(_2886.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2913.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2919.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(
                _2919.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2888.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2865.BevelDifferentialGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2865,
            )

            return self._parent._cast(
                _2865.BevelDifferentialGearMeshCompoundSystemDeflection
            )

        @property
        def spiral_bevel_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2955.SpiralBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2955,
            )

            return self._parent._cast(_2955.SpiralBevelGearMeshCompoundSystemDeflection)

        @property
        def straight_bevel_diff_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2961.StraightBevelDiffGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2961,
            )

            return self._parent._cast(
                _2961.StraightBevelDiffGearMeshCompoundSystemDeflection
            )

        @property
        def straight_bevel_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2964.StraightBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2964,
            )

            return self._parent._cast(
                _2964.StraightBevelGearMeshCompoundSystemDeflection
            )

        @property
        def zerol_bevel_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "_2982.ZerolBevelGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2982,
            )

            return self._parent._cast(_2982.ZerolBevelGearMeshCompoundSystemDeflection)

        @property
        def bevel_gear_mesh_compound_system_deflection(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
        ) -> "BevelGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelGearMeshCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2708.BevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection]

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2708.BevelGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelGearMeshSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "BevelGearMeshCompoundSystemDeflection._Cast_BevelGearMeshCompoundSystemDeflection":
        return self._Cast_BevelGearMeshCompoundSystemDeflection(self)
