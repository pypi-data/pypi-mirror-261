"""CouplingHalfParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.parametric_study_tools import _4383
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_COUPLING_HALF_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "CouplingHalfParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.couplings import _2586
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4320,
        _4325,
        _4340,
        _4397,
        _4404,
        _4409,
        _4419,
        _4429,
        _4431,
        _4432,
        _4435,
        _4436,
        _4323,
        _4395,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CouplingHalfParametricStudyTool",)


Self = TypeVar("Self", bound="CouplingHalfParametricStudyTool")


class CouplingHalfParametricStudyTool(_4383.MountableComponentParametricStudyTool):
    """CouplingHalfParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _COUPLING_HALF_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_CouplingHalfParametricStudyTool")

    class _Cast_CouplingHalfParametricStudyTool:
        """Special nested class for casting CouplingHalfParametricStudyTool to subclasses."""

        def __init__(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
            parent: "CouplingHalfParametricStudyTool",
        ):
            self._parent = parent

        @property
        def mountable_component_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4383.MountableComponentParametricStudyTool":
            return self._parent._cast(_4383.MountableComponentParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4323.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ComponentParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4395.PartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4395,
            )

            return self._parent._cast(_4395.PartParametricStudyTool)

        @property
        def part_analysis_case(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def clutch_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4320.ClutchHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ClutchHalfParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4325.ConceptCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConceptCouplingHalfParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4340.CVTPulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.CVTPulleyParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4397.PartToPartShearCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(
                _4397.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def pulley_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4404.PulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.PulleyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4409.RollingRingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.RollingRingParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4419.SpringDamperHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.SpringDamperHalfParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4429.SynchroniserHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4431.SynchroniserPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4432.SynchroniserSleeveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4435.TorqueConverterPumpParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "_4436.TorqueConverterTurbineParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4436,
            )

            return self._parent._cast(_4436.TorqueConverterTurbineParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
        ) -> "CouplingHalfParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "CouplingHalfParametricStudyTool.TYPE"):
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
    def cast_to(
        self: Self,
    ) -> "CouplingHalfParametricStudyTool._Cast_CouplingHalfParametricStudyTool":
        return self._Cast_CouplingHalfParametricStudyTool(self)
