"""CouplingHalfModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.modal_analyses import _4660
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses",
    "CouplingHalfModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.system_deflections import _2732
    from mastapy.system_model.analyses_and_results.modal_analyses import (
        _4596,
        _4601,
        _4617,
        _4666,
        _4673,
        _4678,
        _4689,
        _4699,
        _4701,
        _4702,
        _4705,
        _4706,
        _4599,
        _4664,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfModalAnalysis",)


Self = TypeVar("Self", bound="CouplingHalfModalAnalysis")


class CouplingHalfModalAnalysis(_4660.MountableComponentModalAnalysis):
    """CouplingHalfModalAnalysis

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfModalAnalysis")

    class _Cast_CouplingHalfModalAnalysis:
        """Special nested class for casting CouplingHalfModalAnalysis to subclasses."""

        def __init__(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
            parent: "CouplingHalfModalAnalysis",
        ):
            self._parent = parent

        @property
        def mountable_component_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4660.MountableComponentModalAnalysis":
            return self._parent._cast(_4660.MountableComponentModalAnalysis)

        @property
        def component_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4599.ComponentModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4599

            return self._parent._cast(_4599.ComponentModalAnalysis)

        @property
        def part_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4664.PartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4664

            return self._parent._cast(_4664.PartModalAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4596.ClutchHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4596

            return self._parent._cast(_4596.ClutchHalfModalAnalysis)

        @property
        def concept_coupling_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4601.ConceptCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4601

            return self._parent._cast(_4601.ConceptCouplingHalfModalAnalysis)

        @property
        def cvt_pulley_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4617.CVTPulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4617

            return self._parent._cast(_4617.CVTPulleyModalAnalysis)

        @property
        def part_to_part_shear_coupling_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4666.PartToPartShearCouplingHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4666

            return self._parent._cast(_4666.PartToPartShearCouplingHalfModalAnalysis)

        @property
        def pulley_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4673.PulleyModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4673

            return self._parent._cast(_4673.PulleyModalAnalysis)

        @property
        def rolling_ring_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4678.RollingRingModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4678

            return self._parent._cast(_4678.RollingRingModalAnalysis)

        @property
        def spring_damper_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4689.SpringDamperHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4689

            return self._parent._cast(_4689.SpringDamperHalfModalAnalysis)

        @property
        def synchroniser_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4699.SynchroniserHalfModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4699

            return self._parent._cast(_4699.SynchroniserHalfModalAnalysis)

        @property
        def synchroniser_part_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4701.SynchroniserPartModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4701

            return self._parent._cast(_4701.SynchroniserPartModalAnalysis)

        @property
        def synchroniser_sleeve_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4702.SynchroniserSleeveModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4702

            return self._parent._cast(_4702.SynchroniserSleeveModalAnalysis)

        @property
        def torque_converter_pump_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4705.TorqueConverterPumpModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4705

            return self._parent._cast(_4705.TorqueConverterPumpModalAnalysis)

        @property
        def torque_converter_turbine_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "_4706.TorqueConverterTurbineModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses import _4706

            return self._parent._cast(_4706.TorqueConverterTurbineModalAnalysis)

        @property
        def coupling_half_modal_analysis(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis",
        ) -> "CouplingHalfModalAnalysis":
            return self._parent

        def __getattr__(
            self: "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2586.CouplingHalf":
        """mastapy.system_model.part_model.couplings.CouplingHalf

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def system_deflection_results(self: Self) -> "_2732.CouplingHalfSystemDeflection":
        """mastapy.system_model.analyses_and_results.system_deflections.CouplingHalfSystemDeflection

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
    ) -> "CouplingHalfModalAnalysis._Cast_CouplingHalfModalAnalysis":
        return self._Cast_CouplingHalfModalAnalysis(self)
