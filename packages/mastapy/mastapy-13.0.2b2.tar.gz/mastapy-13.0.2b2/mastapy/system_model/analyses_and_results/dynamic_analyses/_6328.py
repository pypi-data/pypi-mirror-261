"""CylindricalGearSetDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6341
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CylindricalGearSetDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2528
    from mastapy.system_model.analyses_and_results.static_loads import _6868
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6326,
        _6327,
        _6365,
        _6379,
        _6279,
        _6360,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSetDynamicAnalysis",)


Self = TypeVar("Self", bound="CylindricalGearSetDynamicAnalysis")


class CylindricalGearSetDynamicAnalysis(_6341.GearSetDynamicAnalysis):
    """CylindricalGearSetDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CylindricalGearSetDynamicAnalysis")

    class _Cast_CylindricalGearSetDynamicAnalysis:
        """Special nested class for casting CylindricalGearSetDynamicAnalysis to subclasses."""

        def __init__(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
            parent: "CylindricalGearSetDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def gear_set_dynamic_analysis(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_6341.GearSetDynamicAnalysis":
            return self._parent._cast(_6341.GearSetDynamicAnalysis)

        @property
        def specialised_assembly_dynamic_analysis(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_6379.SpecialisedAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379

            return self._parent._cast(_6379.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_6279.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_6360.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def planetary_gear_set_dynamic_analysis(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "_6365.PlanetaryGearSetDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6365

            return self._parent._cast(_6365.PlanetaryGearSetDynamicAnalysis)

        @property
        def cylindrical_gear_set_dynamic_analysis(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
        ) -> "CylindricalGearSetDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis",
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
        self: Self, instance_to_wrap: "CylindricalGearSetDynamicAnalysis.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2528.CylindricalGearSet":
        """mastapy.system_model.part_model.gears.CylindricalGearSet

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_load_case(self: Self) -> "_6868.CylindricalGearSetLoadCase":
        """mastapy.system_model.analyses_and_results.static_loads.CylindricalGearSetLoadCase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyLoadCase

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cylindrical_gears_dynamic_analysis(
        self: Self,
    ) -> "List[_6326.CylindricalGearDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalGearsDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cylindrical_meshes_dynamic_analysis(
        self: Self,
    ) -> "List[_6327.CylindricalGearMeshDynamicAnalysis]":
        """List[mastapy.system_model.analyses_and_results.dynamic_analyses.CylindricalGearMeshDynamicAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.CylindricalMeshesDynamicAnalysis

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetDynamicAnalysis._Cast_CylindricalGearSetDynamicAnalysis":
        return self._Cast_CylindricalGearSetDynamicAnalysis(self)
