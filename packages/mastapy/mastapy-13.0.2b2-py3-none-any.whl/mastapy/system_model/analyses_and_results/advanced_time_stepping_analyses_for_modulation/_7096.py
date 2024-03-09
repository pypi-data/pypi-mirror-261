"""PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
    _7052,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_TO_PART_SHEAR_COUPLING_HALF_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedTimeSteppingAnalysesForModulation",
    "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2591
    from mastapy.system_model.analyses_and_results.static_loads import _6933
    from mastapy.system_model.analyses_and_results.system_deflections import _2789
    from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
        _7091,
        _7038,
        _7093,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",)


Self = TypeVar(
    "Self", bound="PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation"
)


class PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation(
    _7052.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
):
    """PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation

    This is a mastapy class.
    """

    TYPE = (
        _PART_TO_PART_SHEAR_COUPLING_HALF_ADVANCED_TIME_STEPPING_ANALYSIS_FOR_MODULATION
    )
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
    )

    class _Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation:
        """Special nested class for casting PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation to subclasses."""

        def __init__(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
            parent: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ):
            self._parent = parent

        @property
        def coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7052.CouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            return self._parent._cast(
                _7052.CouplingHalfAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def mountable_component_advanced_time_stepping_analysis_for_modulation(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7091.MountableComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7091,
            )

            return self._parent._cast(
                _7091.MountableComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def component_advanced_time_stepping_analysis_for_modulation(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7038.ComponentAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7038,
            )

            return self._parent._cast(
                _7038.ComponentAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_advanced_time_stepping_analysis_for_modulation(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7093.PartAdvancedTimeSteppingAnalysisForModulation":
            from mastapy.system_model.analyses_and_results.advanced_time_stepping_analyses_for_modulation import (
                _7093,
            )

            return self._parent._cast(
                _7093.PartAdvancedTimeSteppingAnalysisForModulation
            )

        @property
        def part_static_load_analysis_case(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def part_to_part_shear_coupling_half_advanced_time_stepping_analysis_for_modulation(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
        ) -> "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation":
            return self._parent

        def __getattr__(
            self: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation",
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
        instance_to_wrap: "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2591.PartToPartShearCouplingHalf":
        """mastapy.system_model.part_model.couplings.PartToPartShearCouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6933.PartToPartShearCouplingHalfLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.PartToPartShearCouplingHalfLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(
        self: Self,
    ) -> "_2789.PartToPartShearCouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.PartToPartShearCouplingHalfSystemDeflection

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
    ) -> "PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation":
        return self._Cast_PartToPartShearCouplingHalfAdvancedTimeSteppingAnalysisForModulation(
            self
        )
