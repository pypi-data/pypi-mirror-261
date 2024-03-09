"""SynchroniserSleeveSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2824
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SYNCHRONISER_SLEEVE_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "SynchroniserSleeveSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2608
    from mastapy.system_model.analyses_and_results.static_loads import _6973
    from mastapy.system_model.analyses_and_results.power_flows import _4155
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2732,
        _2784,
        _2717,
        _2787,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("SynchroniserSleeveSystemDeflection",)


Self = TypeVar("Self", bound="SynchroniserSleeveSystemDeflection")


class SynchroniserSleeveSystemDeflection(_2824.SynchroniserPartSystemDeflection):
    """SynchroniserSleeveSystemDeflection

    This is a mastapy class.
    """

    TYPE = _SYNCHRONISER_SLEEVE_SYSTEM_DEFLECTION
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SynchroniserSleeveSystemDeflection")

    class _Cast_SynchroniserSleeveSystemDeflection:
        """Special nested class for casting SynchroniserSleeveSystemDeflection to subclasses."""

        def __init__(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
            parent: "SynchroniserSleeveSystemDeflection",
        ):
            self._parent = parent

        @property
        def synchroniser_part_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_2824.SynchroniserPartSystemDeflection":
            return self._parent._cast(_2824.SynchroniserPartSystemDeflection)

        @property
        def coupling_half_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_2732.CouplingHalfSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2732,
            )

            return self._parent._cast(_2732.CouplingHalfSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_2784.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_2717.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_2787.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def synchroniser_sleeve_system_deflection(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
        ) -> "SynchroniserSleeveSystemDeflection":
            return self._parent

        def __getattr__(
            self: "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection",
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
        self: Self, instance_to_wrap: "SynchroniserSleeveSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2608.SynchroniserSleeve":
        """mastapy.system_model.part_model.couplings.SynchroniserSleeve

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_load_case(self: Self) -> "_6973.SynchroniserSleeveLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.SynchroniserSleeveLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4155.SynchroniserSleevePowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.SynchroniserSleevePowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "SynchroniserSleeveSystemDeflection._Cast_SynchroniserSleeveSystemDeflection":
        return self._Cast_SynchroniserSleeveSystemDeflection(self)
