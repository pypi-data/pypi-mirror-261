"""CouplingDynamicAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.dynamic_analyses import _6379
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_DYNAMIC_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.DynamicAnalyses",
    "CouplingDynamicAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2585
    from mastapy.system_model.analyses_and_results.dynamic_analyses import (
        _6301,
        _6306,
        _6362,
        _6384,
        _6399,
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
__all__ = ("CouplingDynamicAnalysis",)


Self = TypeVar("Self", bound="CouplingDynamicAnalysis")


class CouplingDynamicAnalysis(_6379.SpecialisedAssemblyDynamicAnalysis):
    """CouplingDynamicAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_DYNAMIC_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingDynamicAnalysis")

    class _Cast_CouplingDynamicAnalysis:
        """Special nested class for casting CouplingDynamicAnalysis to subclasses."""

        def __init__(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
            parent: "CouplingDynamicAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6379.SpecialisedAssemblyDynamicAnalysis":
            return self._parent._cast(_6379.SpecialisedAssemblyDynamicAnalysis)

        @property
        def abstract_assembly_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6279.AbstractAssemblyDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6279

            return self._parent._cast(_6279.AbstractAssemblyDynamicAnalysis)

        @property
        def part_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6360.PartDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6360

            return self._parent._cast(_6360.PartDynamicAnalysis)

        @property
        def part_fe_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6301.ClutchDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6301

            return self._parent._cast(_6301.ClutchDynamicAnalysis)

        @property
        def concept_coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6306.ConceptCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6306

            return self._parent._cast(_6306.ConceptCouplingDynamicAnalysis)

        @property
        def part_to_part_shear_coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6362.PartToPartShearCouplingDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6362

            return self._parent._cast(_6362.PartToPartShearCouplingDynamicAnalysis)

        @property
        def spring_damper_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6384.SpringDamperDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6384

            return self._parent._cast(_6384.SpringDamperDynamicAnalysis)

        @property
        def torque_converter_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "_6399.TorqueConverterDynamicAnalysis":
            from mastapy.system_model.analyses_and_results.dynamic_analyses import _6399

            return self._parent._cast(_6399.TorqueConverterDynamicAnalysis)

        @property
        def coupling_dynamic_analysis(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis",
        ) -> "CouplingDynamicAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingDynamicAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2585.Coupling":
        """mastapy.system_model.part_model.couplings.Coupling

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "CouplingDynamicAnalysis._Cast_CouplingDynamicAnalysis":
        return self._Cast_CouplingDynamicAnalysis(self)
