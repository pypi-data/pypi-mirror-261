"""VirtualComponentCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2931
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_VIRTUAL_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "VirtualComponentCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import _2837
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2929,
        _2930,
        _2940,
        _2941,
        _2976,
        _2878,
        _2933,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("VirtualComponentCompoundSystemDeflection",)


Self = TypeVar("Self", bound="VirtualComponentCompoundSystemDeflection")


class VirtualComponentCompoundSystemDeflection(
    _2931.MountableComponentCompoundSystemDeflection
):
    """VirtualComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _VIRTUAL_COMPONENT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_VirtualComponentCompoundSystemDeflection"
    )

    class _Cast_VirtualComponentCompoundSystemDeflection:
        """Special nested class for casting VirtualComponentCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
            parent: "VirtualComponentCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def mountable_component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2931.MountableComponentCompoundSystemDeflection":
            return self._parent._cast(_2931.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2878.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(_2878.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2933.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def mass_disc_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2929.MassDiscCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2929,
            )

            return self._parent._cast(_2929.MassDiscCompoundSystemDeflection)

        @property
        def measurement_component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2930.MeasurementComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2930,
            )

            return self._parent._cast(
                _2930.MeasurementComponentCompoundSystemDeflection
            )

        @property
        def point_load_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2940.PointLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2940,
            )

            return self._parent._cast(_2940.PointLoadCompoundSystemDeflection)

        @property
        def power_load_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2941.PowerLoadCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2941,
            )

            return self._parent._cast(_2941.PowerLoadCompoundSystemDeflection)

        @property
        def unbalanced_mass_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "_2976.UnbalancedMassCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2976,
            )

            return self._parent._cast(_2976.UnbalancedMassCompoundSystemDeflection)

        @property
        def virtual_component_compound_system_deflection(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
        ) -> "VirtualComponentCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection",
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
        self: Self, instance_to_wrap: "VirtualComponentCompoundSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2837.VirtualComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2837.VirtualComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.VirtualComponentSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "VirtualComponentCompoundSystemDeflection._Cast_VirtualComponentCompoundSystemDeflection":
        return self._Cast_VirtualComponentCompoundSystemDeflection(self)
