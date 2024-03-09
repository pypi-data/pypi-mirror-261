"""CylindricalGearMeshCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2913
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "CylindricalGearMeshCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1100
    from mastapy.system_model.connections_and_sockets.gears import _2311
    from mastapy.gears.rating.cylindrical import _466
    from mastapy.system_model.analyses_and_results.system_deflections import _2743
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2919,
        _2888,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7541, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearMeshCompoundSystemDeflection",)


Self = TypeVar("Self", bound="CylindricalGearMeshCompoundSystemDeflection")


class CylindricalGearMeshCompoundSystemDeflection(
    _2913.GearMeshCompoundSystemDeflection
):
    """CylindricalGearMeshCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_MESH_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearMeshCompoundSystemDeflection"
    )

    class _Cast_CylindricalGearMeshCompoundSystemDeflection:
        """Special nested class for casting CylindricalGearMeshCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "CylindricalGearMeshCompoundSystemDeflection._Cast_CylindricalGearMeshCompoundSystemDeflection",
            parent: "CylindricalGearMeshCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def gear_mesh_compound_system_deflection(
            self: "CylindricalGearMeshCompoundSystemDeflection._Cast_CylindricalGearMeshCompoundSystemDeflection",
        ) -> "_2913.GearMeshCompoundSystemDeflection":
            return self._parent._cast(_2913.GearMeshCompoundSystemDeflection)

        @property
        def inter_mountable_component_connection_compound_system_deflection(
            self: "CylindricalGearMeshCompoundSystemDeflection._Cast_CylindricalGearMeshCompoundSystemDeflection",
        ) -> "_2919.InterMountableComponentConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2919,
            )

            return self._parent._cast(
                _2919.InterMountableComponentConnectionCompoundSystemDeflection
            )

        @property
        def connection_compound_system_deflection(
            self: "CylindricalGearMeshCompoundSystemDeflection._Cast_CylindricalGearMeshCompoundSystemDeflection",
        ) -> "_2888.ConnectionCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2888,
            )

            return self._parent._cast(_2888.ConnectionCompoundSystemDeflection)

        @property
        def connection_compound_analysis(
            self: "CylindricalGearMeshCompoundSystemDeflection._Cast_CylindricalGearMeshCompoundSystemDeflection",
        ) -> "_7541.ConnectionCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7541

            return self._parent._cast(_7541.ConnectionCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "CylindricalGearMeshCompoundSystemDeflection._Cast_CylindricalGearMeshCompoundSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearMeshCompoundSystemDeflection._Cast_CylindricalGearMeshCompoundSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_gear_mesh_compound_system_deflection(
            self: "CylindricalGearMeshCompoundSystemDeflection._Cast_CylindricalGearMeshCompoundSystemDeflection",
        ) -> "CylindricalGearMeshCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "CylindricalGearMeshCompoundSystemDeflection._Cast_CylindricalGearMeshCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "CylindricalGearMeshCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def maximum_operating_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MaximumOperatingBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_operating_backlash(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingBacklash

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_operating_tip_root_clearance(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingTipRootClearance

        if temp is None:
            return 0.0

        return temp

    @property
    def minimum_operating_transverse_contact_ratio(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.MinimumOperatingTransverseContactRatio

        if temp is None:
            return 0.0

        return temp

    @property
    def basic_ltca_results(
        self: Self,
    ) -> "_1100.CylindricalGearMeshMicroGeometryDutyCycle":
        """mastapy.gears.gear_designs.cylindrical.micro_geometry.CylindricalGearMeshMicroGeometryDutyCycle

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BasicLTCAResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: Self) -> "_2311.CylindricalGearMesh":
        """mastapy.system_model.connections_and_sockets.gears.CylindricalGearMesh

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

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
    def cylindrical_mesh_rating(self: Self) -> "_466.CylindricalMeshDutyCycleRating":
        """mastapy.gears.rating.cylindrical.CylindricalMeshDutyCycleRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshRating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def connection_analysis_cases_ready(
        self: Self,
    ) -> "List[_2743.CylindricalGearMeshSystemDeflectionWithLTCAResults]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflectionWithLTCAResults]

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
    def planetaries(self: Self) -> "List[CylindricalGearMeshCompoundSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.compound.CylindricalGearMeshCompoundSystemDeflection]

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
    def connection_analysis_cases(
        self: Self,
    ) -> "List[_2743.CylindricalGearMeshSystemDeflectionWithLTCAResults]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.CylindricalGearMeshSystemDeflectionWithLTCAResults]

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
    ) -> "CylindricalGearMeshCompoundSystemDeflection._Cast_CylindricalGearMeshCompoundSystemDeflection":
        return self._Cast_CylindricalGearMeshCompoundSystemDeflection(self)
