"""KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.advanced_system_deflections import _7309
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION = (
    python_net_import(
        "SMT.MastaAPI.SystemModel.AnalysesAndResults.AdvancedSystemDeflections",
        "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
    )
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2539
    from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
        _7348,
        _7351,
        _7337,
        _7376,
        _7272,
        _7357,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",)


Self = TypeVar(
    "Self", bound="KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection"
)


class KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection(
    _7309.ConicalGearSetAdvancedSystemDeflection
):
    """KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection

    This is a mastapy class.
    """

    TYPE = _KLINGELNBERG_CYCLO_PALLOID_CONICAL_GEAR_SET_ADVANCED_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
    )

    class _Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection:
        """Special nested class for casting KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection to subclasses."""

        def __init__(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
            parent: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ):
            self._parent = parent

        @property
        def conical_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_7309.ConicalGearSetAdvancedSystemDeflection":
            return self._parent._cast(_7309.ConicalGearSetAdvancedSystemDeflection)

        @property
        def gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_7337.GearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7337,
            )

            return self._parent._cast(_7337.GearSetAdvancedSystemDeflection)

        @property
        def specialised_assembly_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_7376.SpecialisedAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7376,
            )

            return self._parent._cast(_7376.SpecialisedAssemblyAdvancedSystemDeflection)

        @property
        def abstract_assembly_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_7272.AbstractAssemblyAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7272,
            )

            return self._parent._cast(_7272.AbstractAssemblyAdvancedSystemDeflection)

        @property
        def part_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_7357.PartAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7357,
            )

            return self._parent._cast(_7357.PartAdvancedSystemDeflection)

        @property
        def part_static_load_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_7348.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7348,
            )

            return self._parent._cast(
                _7348.KlingelnbergCycloPalloidHypoidGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "_7351.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection":
            from mastapy.system_model.analyses_and_results.advanced_system_deflections import (
                _7351,
            )

            return self._parent._cast(
                _7351.KlingelnbergCycloPalloidSpiralBevelGearSetAdvancedSystemDeflection
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_advanced_system_deflection(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
        ) -> "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
            return self._parent

        def __getattr__(
            self: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection",
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
        instance_to_wrap: "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2539.KlingelnbergCycloPalloidConicalGearSet":
        """mastapy.system_model.part_model.gears.KlingelnbergCycloPalloidConicalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection":
        return (
            self._Cast_KlingelnbergCycloPalloidConicalGearSetAdvancedSystemDeflection(
                self
            )
        )
