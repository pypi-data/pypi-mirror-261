"""BoltedJointCompoundModalAnalysis"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import constructor, conversion
from mastapy.system_model.analyses_and_results.modal_analyses.compound import _4828
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_BOLTED_JOINT_COMPOUND_MODAL_ANALYSIS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalyses.Compound",
    "BoltedJointCompoundModalAnalysis",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2445
    from mastapy.system_model.analyses_and_results.modal_analyses import _4593
    from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
        _4730,
        _4809,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("BoltedJointCompoundModalAnalysis",)


Self = TypeVar("Self", bound="BoltedJointCompoundModalAnalysis")


class BoltedJointCompoundModalAnalysis(_4828.SpecialisedAssemblyCompoundModalAnalysis):
    """BoltedJointCompoundModalAnalysis

    This is a mastapy class.
    """

    TYPE = _BOLTED_JOINT_COMPOUND_MODAL_ANALYSIS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_BoltedJointCompoundModalAnalysis")

    class _Cast_BoltedJointCompoundModalAnalysis:
        """Special nested class for casting BoltedJointCompoundModalAnalysis to subclasses."""

        def __init__(
            self: "BoltedJointCompoundModalAnalysis._Cast_BoltedJointCompoundModalAnalysis",
            parent: "BoltedJointCompoundModalAnalysis",
        ):
            self._parent = parent

        @property
        def specialised_assembly_compound_modal_analysis(
            self: "BoltedJointCompoundModalAnalysis._Cast_BoltedJointCompoundModalAnalysis",
        ) -> "_4828.SpecialisedAssemblyCompoundModalAnalysis":
            return self._parent._cast(_4828.SpecialisedAssemblyCompoundModalAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis(
            self: "BoltedJointCompoundModalAnalysis._Cast_BoltedJointCompoundModalAnalysis",
        ) -> "_4730.AbstractAssemblyCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4730,
            )

            return self._parent._cast(_4730.AbstractAssemblyCompoundModalAnalysis)

        @property
        def part_compound_modal_analysis(
            self: "BoltedJointCompoundModalAnalysis._Cast_BoltedJointCompoundModalAnalysis",
        ) -> "_4809.PartCompoundModalAnalysis":
            from mastapy.system_model.analyses_and_results.modal_analyses.compound import (
                _4809,
            )

            return self._parent._cast(_4809.PartCompoundModalAnalysis)

        @property
        def part_compound_analysis(
            self: "BoltedJointCompoundModalAnalysis._Cast_BoltedJointCompoundModalAnalysis",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "BoltedJointCompoundModalAnalysis._Cast_BoltedJointCompoundModalAnalysis",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "BoltedJointCompoundModalAnalysis._Cast_BoltedJointCompoundModalAnalysis",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def bolted_joint_compound_modal_analysis(
            self: "BoltedJointCompoundModalAnalysis._Cast_BoltedJointCompoundModalAnalysis",
        ) -> "BoltedJointCompoundModalAnalysis":
            return self._parent

        def __getattr__(
            self: "BoltedJointCompoundModalAnalysis._Cast_BoltedJointCompoundModalAnalysis",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "BoltedJointCompoundModalAnalysis.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2445.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2445.BoltedJoint":
        """mastapy.system_model.part_model.BoltedJoint

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4593.BoltedJointModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BoltedJointModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def assembly_analysis_cases(self: Self) -> "List[_4593.BoltedJointModalAnalysis]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses.BoltedJointModalAnalysis]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "BoltedJointCompoundModalAnalysis._Cast_BoltedJointCompoundModalAnalysis":
        return self._Cast_BoltedJointCompoundModalAnalysis(self)
