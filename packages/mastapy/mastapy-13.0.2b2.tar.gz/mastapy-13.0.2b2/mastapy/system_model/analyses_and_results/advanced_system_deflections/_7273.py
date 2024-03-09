"""AbstractShaftAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7274
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_SHAFT_ADVANCED_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
    "AbstractShaftAdvancedSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2437
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7320,
        _7373,
        _7300,
        _7357,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractShaftAdvancedSystemDeflection",)


Self = TypeVar("Self", bound="AbstractShaftAdvancedSystemDeflection")


class AbstractShaftAdvancedSystemDeflection(
    _7274.AbstractShaftOrHousingAdvancedSystemDeflection
):
    """AbstractShaftAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_SHAFT_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractShaftAdvancedSystemDeflection"
    )

    class _Cast_AbstractShaftAdvancedSystemDeflection:
        """Special nested class for casting AbstractShaftAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
            parent: "AbstractShaftAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def abstract_shaft_or_housing_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7274.AbstractShaftOrHousingAdvancedSystemDeflection":
            return self._parent._cast(
                _7274.AbstractShaftOrHousingAdvancedSystemDeflection
            )

        @property
        def component_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7300.ComponentAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7300,
            )

            return self._parent._cast(_7300.ComponentAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7357.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cycloidal_disc_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7320.CycloidalDiscAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7320,
            )

            return self._parent._cast(_7320.CycloidalDiscAdvancedSystemDeflection)

        @property
        def shaft_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "_7373.ShaftAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7373,
            )

            return self._parent._cast(_7373.ShaftAdvancedSystemDeflection)

        @property
        def abstract_shaft_advanced_system_deflection(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
        ) -> "AbstractShaftAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection",
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
        self: Self, instance_to_wrap: "AbstractShaftAdvancedSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2437.AbstractShaft":
        """mastapy.system_model.part_model.AbstractShaft

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractShaftAdvancedSystemDeflection._Cast_AbstractShaftAdvancedSystemDeflection":
        return self._Cast_AbstractShaftAdvancedSystemDeflection(self)
