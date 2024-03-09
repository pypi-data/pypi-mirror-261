"""KlingelnbergCycloPalloidConicalGearSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.system_deflections import _2728
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "KlingelnbergCycloPalloidConicalGearSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2538
    from mastapy.system_model.analyses_and_results.power_flows import _4104
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2775,
        _2778,
        _2763,
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
__all__ = ("KlingelnbergCycloPalloidConicalGearSystemDeflection",)


Self = TypeVar("Self", bound="KlingelnbergCycloPalloidConicalGearSystemDeflection")


class KlingelnbergCycloPalloidConicalGearSystemDeflection(
    _2728.ConicalGearSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection"
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_2728.ConicalGearSystemDeflection":
            return self._parent._cast(_2728.ConicalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_2763.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_2784.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_2717.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_2787.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_2775.KlingelnbergCycloPalloidHypoidGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2775,
            )

            return self._parent._cast(
                _2775.KlingelnbergCycloPalloidHypoidGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "_2778.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2778,
            )

            return self._parent._cast(
                _2778.KlingelnbergCycloPalloidSpiralBevelGearSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2538.KlingelnbergCycloPalloidConicalGear":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGear

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(
        self: Self,
    ) -> "_4104.KlingelnbergCycloPalloidConicalGearPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.KlingelnbergCycloPalloidConicalGearPowerFlow

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
    ) -> "KlingelnbergCycloPalloidConicalGearSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection":
        return self._Cast_KlingelnbergCycloPalloidConicalGearSystemDeflection(self)
