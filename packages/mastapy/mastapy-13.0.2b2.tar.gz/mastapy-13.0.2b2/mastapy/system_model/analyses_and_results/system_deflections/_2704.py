"""BevelDifferentialGearSetSystemDeflection"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.system_deflections import _2709
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BEVEL_DIFFERENTIAL_GEAR_SET_SYSTEM_DEFLECTION = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "BevelDifferentialGearSetSystemDeflection",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2518
    from mastapy.system_model.analyses_and_results.static_loads import _6827
    from mastapy.gears.rating.bevel import _556
    from mastapy.system_model.analyses_and_results.power_flows import _4047
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2705,
        _2703,
        _2692,
        _2727,
        _2762,
        _2808,
        _2687,
        _2787,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("BevelDifferentialGearSetSystemDeflection",)


Self = TypeVar("Self", bound="BevelDifferentialGearSetSystemDeflection")


class BevelDifferentialGearSetSystemDeflection(_2709.BevelGearSetSystemDeflection):
    """BevelDifferentialGearSetSystemDeflection

    This is a mastapy class.
    """

    TYPE = _BEVEL_DIFFERENTIAL_GEAR_SET_SYSTEM_DEFLECTION
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_BevelDifferentialGearSetSystemDeflection"
    )

    class _Cast_BevelDifferentialGearSetSystemDeflection:
        """Special nested class for casting BevelDifferentialGearSetSystemDeflection to subclasses."""

        def __init__(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
            parent: "BevelDifferentialGearSetSystemDeflection",
        ):
            self._parent = parent

        @property
        def bevel_gear_set_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_2709.BevelGearSetSystemDeflection":
            return self._parent._cast(_2709.BevelGearSetSystemDeflection)

        @property
        def agma_gleason_conical_gear_set_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_2692.AGMAGleasonConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2692,
            )

            return self._parent._cast(_2692.AGMAGleasonConicalGearSetSystemDeflection)

        @property
        def conical_gear_set_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_2727.ConicalGearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2727,
            )

            return self._parent._cast(_2727.ConicalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_2762.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_2808.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_2687.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_2787.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bevel_differential_gear_set_system_deflection(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
        ) -> "BevelDifferentialGearSetSystemDeflection":
            return self._parent

        def __getattr__(
            self: "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection",
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
        self: Self, instance_to_wrap: "BevelDifferentialGearSetSystemDeflection.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2518.BevelDifferentialGearSet":
        """mastapy.system_model.part_model.gears.BevelDifferentialGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6827.BevelDifferentialGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.BevelDifferentialGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def rating(self: Self) -> "_556.BevelGearSetRating":
        """mastapy.gears.rating.bevel.BevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Rating

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_detailed_analysis(self: Self) -> "_556.BevelGearSetRating":
        """mastapy.gears.rating.bevel.BevelGearSetRating

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDetailedAnalysis

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def power_flow_results(self: Self) -> "_4047.BevelDifferentialGearSetPowerFlow":
        """mastapy.system_model.analyses_and_results.power_flows.BevelDifferentialGearSetPowerFlow

        Note:
            This property is readonly.
        """
        temp = self.wrapped.PowerFlowResults

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def bevel_differential_gears_system_deflection(
        self: Self,
    ) -> "List[_2705.BevelDifferentialGearSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialGearsSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def bevel_differential_meshes_system_deflection(
        self: Self,
    ) -> "List[_2703.BevelDifferentialGearMeshSystemDeflection]":
        """List[mastapy.system_model.analyses_and_results.system_deflections.BevelDifferentialGearMeshSystemDeflection]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.BevelDifferentialMeshesSystemDeflection

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BevelDifferentialGearSetSystemDeflection._Cast_BevelDifferentialGearSetSystemDeflection":
        return self._Cast_BevelDifferentialGearSetSystemDeflection(self)
