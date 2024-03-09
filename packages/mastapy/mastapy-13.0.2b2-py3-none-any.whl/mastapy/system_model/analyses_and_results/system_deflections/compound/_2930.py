"""MeasurementComponentCompoundSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections.compound import _2977
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_MEASUREMENT_COMPONENT_COMPOUND_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections.Compound",
    "MeasurementComponentCompoundSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2465
    from mastapy.system_model.analyses_and_results.system_deflections import _2782
    from mastapy.system_model.analyses_and_results.system_deflections.compound import (
        _2931,
        _2878,
        _2933,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("MeasurementComponentCompoundSystemDeflection",)


Self = TypeVar("Self", bound="MeasurementComponentCompoundSystemDeflection")


class MeasurementComponentCompoundSystemDeflection(
    _2977.VirtualComponentCompoundSystemDeflection
):
    """MeasurementComponentCompoundSystemDeflection

    This is a mastapy class.
    """

    TYPE = _MEASUREMENT_COMPONENT_COMPOUND_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_MeasurementComponentCompoundSystemDeflection"
    )

    class _Cast_MeasurementComponentCompoundSystemDeflection:
        """Special nested class for casting MeasurementComponentCompoundSystemDeflection to subclasses."""

        def __init__(
            self: "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection",
            parent: "MeasurementComponentCompoundSystemDeflection",
        ):
            self._parent = parent

        @property
        def virtual_component_compound_system_deflection(
            self: "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection",
        ) -> "_2977.VirtualComponentCompoundSystemDeflection":
            return self._parent._cast(_2977.VirtualComponentCompoundSystemDeflection)

        @property
        def mountable_component_compound_system_deflection(
            self: "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection",
        ) -> "_2931.MountableComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2931,
            )

            return self._parent._cast(_2931.MountableComponentCompoundSystemDeflection)

        @property
        def component_compound_system_deflection(
            self: "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection",
        ) -> "_2878.ComponentCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2878,
            )

            return self._parent._cast(_2878.ComponentCompoundSystemDeflection)

        @property
        def part_compound_system_deflection(
            self: "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection",
        ) -> "_2933.PartCompoundSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections.compound import (
                _2933,
            )

            return self._parent._cast(_2933.PartCompoundSystemDeflection)

        @property
        def part_compound_analysis(
            self: "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def measurement_component_compound_system_deflection(
            self: "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection",
        ) -> "MeasurementComponentCompoundSystemDeflection":
            return self._parent

        def __getattr__(
            self: "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection",
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
        instance_to_wrap: "MeasurementComponentCompoundSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2465.MeasurementComponent":
        """mastapy.system_model.part_model.MeasurementComponent

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_2782.MeasurementComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection]

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
    def component_analysis_cases(
        self: Self,
    ) -> "List[_2782.MeasurementComponentSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.MeasurementComponentSystemDeflection]

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
    def cast_to(
        self: Self,
    ) -> "MeasurementComponentCompoundSystemDeflection._Cast_MeasurementComponentCompoundSystemDeflection":
        return self._Cast_MeasurementComponentCompoundSystemDeflection(self)
