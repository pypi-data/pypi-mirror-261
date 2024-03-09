"""AbstractAssemblyCompoundParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
    _4524,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools.Compound",
    "AbstractAssemblyCompoundParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.parametric_study_tools import _4298
    from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
        _4451,
        _4452,
        _4455,
        _4458,
        _4463,
        _4465,
        _4466,
        _4471,
        _4476,
        _4479,
        _4482,
        _4486,
        _4488,
        _4494,
        _4500,
        _4502,
        _4505,
        _4509,
        _4513,
        _4516,
        _4519,
        _4525,
        _4529,
        _4536,
        _4539,
        _4543,
        _4546,
        _4547,
        _4552,
        _4555,
        _4558,
        _4562,
        _4570,
        _4573,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7548, _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyCompoundParametricStudyTool",)


Self = TypeVar("Self", bound="AbstractAssemblyCompoundParametricStudyTool")


class AbstractAssemblyCompoundParametricStudyTool(
    _4524.PartCompoundParametricStudyTool
):
    """AbstractAssemblyCompoundParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_COMPOUND_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_AbstractAssemblyCompoundParametricStudyTool"
    )

    class _Cast_AbstractAssemblyCompoundParametricStudyTool:
        """Special nested class for casting AbstractAssemblyCompoundParametricStudyTool to subclasses."""

        def __init__(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
            parent: "AbstractAssemblyCompoundParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4524.PartCompoundParametricStudyTool":
            return self._parent._cast(_4524.PartCompoundParametricStudyTool)

        @property
        def part_compound_analysis(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_7548.PartCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7548

            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4451.AGMAGleasonConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4451,
            )

            return self._parent._cast(
                _4451.AGMAGleasonConicalGearSetCompoundParametricStudyTool
            )

        @property
        def assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4452.AssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4452,
            )

            return self._parent._cast(_4452.AssemblyCompoundParametricStudyTool)

        @property
        def belt_drive_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4455.BeltDriveCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4455,
            )

            return self._parent._cast(_4455.BeltDriveCompoundParametricStudyTool)

        @property
        def bevel_differential_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4458.BevelDifferentialGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4458,
            )

            return self._parent._cast(
                _4458.BevelDifferentialGearSetCompoundParametricStudyTool
            )

        @property
        def bevel_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4463.BevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4463,
            )

            return self._parent._cast(_4463.BevelGearSetCompoundParametricStudyTool)

        @property
        def bolted_joint_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4465.BoltedJointCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4465,
            )

            return self._parent._cast(_4465.BoltedJointCompoundParametricStudyTool)

        @property
        def clutch_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4466.ClutchCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4466,
            )

            return self._parent._cast(_4466.ClutchCompoundParametricStudyTool)

        @property
        def concept_coupling_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4471.ConceptCouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4471,
            )

            return self._parent._cast(_4471.ConceptCouplingCompoundParametricStudyTool)

        @property
        def concept_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4476.ConceptGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4476,
            )

            return self._parent._cast(_4476.ConceptGearSetCompoundParametricStudyTool)

        @property
        def conical_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4479.ConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4479,
            )

            return self._parent._cast(_4479.ConicalGearSetCompoundParametricStudyTool)

        @property
        def coupling_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4482.CouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4482,
            )

            return self._parent._cast(_4482.CouplingCompoundParametricStudyTool)

        @property
        def cvt_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4486.CVTCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4486,
            )

            return self._parent._cast(_4486.CVTCompoundParametricStudyTool)

        @property
        def cycloidal_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4488.CycloidalAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4488,
            )

            return self._parent._cast(
                _4488.CycloidalAssemblyCompoundParametricStudyTool
            )

        @property
        def cylindrical_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4494.CylindricalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4494,
            )

            return self._parent._cast(
                _4494.CylindricalGearSetCompoundParametricStudyTool
            )

        @property
        def face_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4500.FaceGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4500,
            )

            return self._parent._cast(_4500.FaceGearSetCompoundParametricStudyTool)

        @property
        def flexible_pin_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4502.FlexiblePinAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4502,
            )

            return self._parent._cast(
                _4502.FlexiblePinAssemblyCompoundParametricStudyTool
            )

        @property
        def gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4505.GearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4505,
            )

            return self._parent._cast(_4505.GearSetCompoundParametricStudyTool)

        @property
        def hypoid_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4509.HypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4509,
            )

            return self._parent._cast(_4509.HypoidGearSetCompoundParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4513.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4513,
            )

            return self._parent._cast(
                _4513.KlingelnbergCycloPalloidConicalGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4516.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4516,
            )

            return self._parent._cast(
                _4516.KlingelnbergCycloPalloidHypoidGearSetCompoundParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4519.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4519,
            )

            return self._parent._cast(
                _4519.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4525.PartToPartShearCouplingCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4525,
            )

            return self._parent._cast(
                _4525.PartToPartShearCouplingCompoundParametricStudyTool
            )

        @property
        def planetary_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4529.PlanetaryGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4529,
            )

            return self._parent._cast(_4529.PlanetaryGearSetCompoundParametricStudyTool)

        @property
        def rolling_ring_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4536.RollingRingAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4536,
            )

            return self._parent._cast(
                _4536.RollingRingAssemblyCompoundParametricStudyTool
            )

        @property
        def root_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4539.RootAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4539,
            )

            return self._parent._cast(_4539.RootAssemblyCompoundParametricStudyTool)

        @property
        def specialised_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4543.SpecialisedAssemblyCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4543,
            )

            return self._parent._cast(
                _4543.SpecialisedAssemblyCompoundParametricStudyTool
            )

        @property
        def spiral_bevel_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4546.SpiralBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4546,
            )

            return self._parent._cast(
                _4546.SpiralBevelGearSetCompoundParametricStudyTool
            )

        @property
        def spring_damper_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4547.SpringDamperCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4547,
            )

            return self._parent._cast(_4547.SpringDamperCompoundParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4552.StraightBevelDiffGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4552,
            )

            return self._parent._cast(
                _4552.StraightBevelDiffGearSetCompoundParametricStudyTool
            )

        @property
        def straight_bevel_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4555.StraightBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4555,
            )

            return self._parent._cast(
                _4555.StraightBevelGearSetCompoundParametricStudyTool
            )

        @property
        def synchroniser_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4558.SynchroniserCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4558,
            )

            return self._parent._cast(_4558.SynchroniserCompoundParametricStudyTool)

        @property
        def torque_converter_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4562.TorqueConverterCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4562,
            )

            return self._parent._cast(_4562.TorqueConverterCompoundParametricStudyTool)

        @property
        def worm_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4570.WormGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4570,
            )

            return self._parent._cast(_4570.WormGearSetCompoundParametricStudyTool)

        @property
        def zerol_bevel_gear_set_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "_4573.ZerolBevelGearSetCompoundParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools.compound import (
                _4573,
            )

            return self._parent._cast(
                _4573.ZerolBevelGearSetCompoundParametricStudyTool
            )

        @property
        def abstract_assembly_compound_parametric_study_tool(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
        ) -> "AbstractAssemblyCompoundParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool",
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
        self: Self, instance_to_wrap: "AbstractAssemblyCompoundParametricStudyTool.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_analysis_cases(
        self: Self,
    ) -> "List[_4298.AbstractAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractAssemblyParametricStudyTool]

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
    def assembly_analysis_cases_ready(
        self: Self,
    ) -> "List[_4298.AbstractAssemblyParametricStudyTool]":
        """List[mastapy.system_model.analyses_and_results.parametric_study_tools.AbstractAssemblyParametricStudyTool]

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
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyCompoundParametricStudyTool._Cast_AbstractAssemblyCompoundParametricStudyTool":
        return self._Cast_AbstractAssemblyCompoundParametricStudyTool(self)
