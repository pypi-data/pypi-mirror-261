"""KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2921
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
        "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.connections_and_sockets.gears import _2321
    from mastapy.system_model.analyses_and_results.system_deflections import _2773
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2886,
        _2913,
        _2919,
        _2888,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection"
)


class KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection(
    _2921.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
):
    """KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_HYPOID_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
            parent: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def klingelnberg_cyclo_palloid_conical_gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2921.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection":
            return self._parent._cast(
                _2921.KlingelnbergCycloPalloidConicalGearMeshCompoundSystemDeflection
            )

        @property
        def conical_gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2886.ConicalGearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2886,
            )

            return self._parent._cast(_2886.ConicalGearMeshCompoundSystemDeflection)

        @property
        def gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2913.GearMeshCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2913,
            )

            return self._parent._cast(_2913.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2919.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(
                _2919.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2888.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_mesh_compound_system_deflection(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
        ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2321.KlingelnbergCycloPalloidHypoidGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.KlingelnbergCycloPalloidHypoidGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2773.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]

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
    ) -> "List[_2773.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.KlingelnbergCycloPalloidHypoidGearMeshSystemDeflection]

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
    ) -> "KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection":
        return (
            self._Cast_KlingelnbergCycloPalloidHypoidGearMeshCompoundSystemDeflection(
                self
            )
        )
