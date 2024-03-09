"""PartParametricStudyTool"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.analysis_cases import _7547
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_PARAMETRIC_STUDY_TOOL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ParametricStudyTools",
    "PartParametricStudyTool",
)

if TYPE_CHECKING:
    from mastapy.utility_gui.charts import _1861, _1869, _1867
    from mastapy.system_model.part_model import _2470
    from mastapy.utility_gui import _1852
    from mastapy.system_model.analyses_and_results.parametric_study_tools import (
        _4390,
        _4298,
        _4299,
        _4300,
        _4303,
        _4304,
        _4305,
        _4306,
        _4308,
        _4310,
        _4311,
        _4312,
        _4313,
        _4315,
        _4316,
        _4317,
        _4318,
        _4320,
        _4321,
        _4323,
        _4325,
        _4326,
        _4328,
        _4329,
        _4331,
        _4332,
        _4334,
        _4336,
        _4337,
        _4339,
        _4340,
        _4341,
        _4343,
        _4346,
        _4347,
        _4348,
        _4349,
        _4357,
        _4359,
        _4360,
        _4361,
        _4362,
        _4364,
        _4365,
        _4366,
        _4368,
        _4369,
        _4372,
        _4373,
        _4375,
        _4376,
        _4378,
        _4379,
        _4380,
        _4381,
        _4383,
        _4384,
        _4397,
        _4398,
        _4400,
        _4401,
        _4402,
        _4403,
        _4404,
        _4405,
        _4407,
        _4409,
        _4410,
        _4411,
        _4412,
        _4414,
        _4416,
        _4417,
        _4419,
        _4420,
        _4422,
        _4423,
        _4425,
        _4426,
        _4427,
        _4428,
        _4429,
        _4430,
        _4431,
        _4432,
        _4434,
        _4435,
        _4436,
        _4437,
        _4438,
        _4440,
        _4441,
        _4443,
        _4444,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartParametricStudyTool",)


Self = TypeVar("Self", bound="PartParametricStudyTool")


class PartParametricStudyTool(_7547.PartAnalysisCase):
    """PartParametricStudyTool

    This is a mastapy class.
    """

    TYPE = _PART_PARAMETRIC_STUDY_TOOL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PartParametricStudyTool")

    class _Cast_PartParametricStudyTool:
        """Special nested class for casting PartParametricStudyTool to subclasses."""

        def __init__(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
            parent: "PartParametricStudyTool",
        ):
            self._parent = parent

        @property
        def part_analysis_case(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_7547.PartAnalysisCase":
            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4298.AbstractAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4298,
            )

            return self._parent._cast(_4298.AbstractAssemblyParametricStudyTool)

        @property
        def abstract_shaft_or_housing_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4299.AbstractShaftOrHousingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4299,
            )

            return self._parent._cast(_4299.AbstractShaftOrHousingParametricStudyTool)

        @property
        def abstract_shaft_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4300.AbstractShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4300,
            )

            return self._parent._cast(_4300.AbstractShaftParametricStudyTool)

        @property
        def agma_gleason_conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4303.AGMAGleasonConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4303,
            )

            return self._parent._cast(_4303.AGMAGleasonConicalGearParametricStudyTool)

        @property
        def agma_gleason_conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4304.AGMAGleasonConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4304,
            )

            return self._parent._cast(
                _4304.AGMAGleasonConicalGearSetParametricStudyTool
            )

        @property
        def assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4305.AssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4305,
            )

            return self._parent._cast(_4305.AssemblyParametricStudyTool)

        @property
        def bearing_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4306.BearingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4306,
            )

            return self._parent._cast(_4306.BearingParametricStudyTool)

        @property
        def belt_drive_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4308.BeltDriveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4308,
            )

            return self._parent._cast(_4308.BeltDriveParametricStudyTool)

        @property
        def bevel_differential_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4310.BevelDifferentialGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4310,
            )

            return self._parent._cast(_4310.BevelDifferentialGearParametricStudyTool)

        @property
        def bevel_differential_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4311.BevelDifferentialGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4311,
            )

            return self._parent._cast(_4311.BevelDifferentialGearSetParametricStudyTool)

        @property
        def bevel_differential_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4312.BevelDifferentialPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4312,
            )

            return self._parent._cast(
                _4312.BevelDifferentialPlanetGearParametricStudyTool
            )

        @property
        def bevel_differential_sun_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4313.BevelDifferentialSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4313,
            )

            return self._parent._cast(_4313.BevelDifferentialSunGearParametricStudyTool)

        @property
        def bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4315.BevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4315,
            )

            return self._parent._cast(_4315.BevelGearParametricStudyTool)

        @property
        def bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4316.BevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4316,
            )

            return self._parent._cast(_4316.BevelGearSetParametricStudyTool)

        @property
        def bolted_joint_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4317.BoltedJointParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4317,
            )

            return self._parent._cast(_4317.BoltedJointParametricStudyTool)

        @property
        def bolt_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4318.BoltParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4318,
            )

            return self._parent._cast(_4318.BoltParametricStudyTool)

        @property
        def clutch_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4320.ClutchHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4320,
            )

            return self._parent._cast(_4320.ClutchHalfParametricStudyTool)

        @property
        def clutch_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4321.ClutchParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4321,
            )

            return self._parent._cast(_4321.ClutchParametricStudyTool)

        @property
        def component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4323.ComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4323,
            )

            return self._parent._cast(_4323.ComponentParametricStudyTool)

        @property
        def concept_coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4325.ConceptCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4325,
            )

            return self._parent._cast(_4325.ConceptCouplingHalfParametricStudyTool)

        @property
        def concept_coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4326.ConceptCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4326,
            )

            return self._parent._cast(_4326.ConceptCouplingParametricStudyTool)

        @property
        def concept_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4328.ConceptGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4328,
            )

            return self._parent._cast(_4328.ConceptGearParametricStudyTool)

        @property
        def concept_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4329.ConceptGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4329,
            )

            return self._parent._cast(_4329.ConceptGearSetParametricStudyTool)

        @property
        def conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4331.ConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4331,
            )

            return self._parent._cast(_4331.ConicalGearParametricStudyTool)

        @property
        def conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4332.ConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4332,
            )

            return self._parent._cast(_4332.ConicalGearSetParametricStudyTool)

        @property
        def connector_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4334.ConnectorParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4334,
            )

            return self._parent._cast(_4334.ConnectorParametricStudyTool)

        @property
        def coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4336.CouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4336,
            )

            return self._parent._cast(_4336.CouplingHalfParametricStudyTool)

        @property
        def coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4337.CouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4337,
            )

            return self._parent._cast(_4337.CouplingParametricStudyTool)

        @property
        def cvt_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4339.CVTParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4339,
            )

            return self._parent._cast(_4339.CVTParametricStudyTool)

        @property
        def cvt_pulley_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4340.CVTPulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4340,
            )

            return self._parent._cast(_4340.CVTPulleyParametricStudyTool)

        @property
        def cycloidal_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4341.CycloidalAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4341,
            )

            return self._parent._cast(_4341.CycloidalAssemblyParametricStudyTool)

        @property
        def cycloidal_disc_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4343.CycloidalDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4343,
            )

            return self._parent._cast(_4343.CycloidalDiscParametricStudyTool)

        @property
        def cylindrical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4346.CylindricalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4346,
            )

            return self._parent._cast(_4346.CylindricalGearParametricStudyTool)

        @property
        def cylindrical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4347.CylindricalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4347,
            )

            return self._parent._cast(_4347.CylindricalGearSetParametricStudyTool)

        @property
        def cylindrical_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4348.CylindricalPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4348,
            )

            return self._parent._cast(_4348.CylindricalPlanetGearParametricStudyTool)

        @property
        def datum_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4349.DatumParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4349,
            )

            return self._parent._cast(_4349.DatumParametricStudyTool)

        @property
        def external_cad_model_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4357.ExternalCADModelParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4357,
            )

            return self._parent._cast(_4357.ExternalCADModelParametricStudyTool)

        @property
        def face_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4359.FaceGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4359,
            )

            return self._parent._cast(_4359.FaceGearParametricStudyTool)

        @property
        def face_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4360.FaceGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4360,
            )

            return self._parent._cast(_4360.FaceGearSetParametricStudyTool)

        @property
        def fe_part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4361.FEPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4361,
            )

            return self._parent._cast(_4361.FEPartParametricStudyTool)

        @property
        def flexible_pin_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4362.FlexiblePinAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4362,
            )

            return self._parent._cast(_4362.FlexiblePinAssemblyParametricStudyTool)

        @property
        def gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4364.GearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4364,
            )

            return self._parent._cast(_4364.GearParametricStudyTool)

        @property
        def gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4365.GearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4365,
            )

            return self._parent._cast(_4365.GearSetParametricStudyTool)

        @property
        def guide_dxf_model_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4366.GuideDxfModelParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4366,
            )

            return self._parent._cast(_4366.GuideDxfModelParametricStudyTool)

        @property
        def hypoid_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4368.HypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4368,
            )

            return self._parent._cast(_4368.HypoidGearParametricStudyTool)

        @property
        def hypoid_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4369.HypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4369,
            )

            return self._parent._cast(_4369.HypoidGearSetParametricStudyTool)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4372.KlingelnbergCycloPalloidConicalGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4372,
            )

            return self._parent._cast(
                _4372.KlingelnbergCycloPalloidConicalGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4373.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4373,
            )

            return self._parent._cast(
                _4373.KlingelnbergCycloPalloidConicalGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4375.KlingelnbergCycloPalloidHypoidGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4375,
            )

            return self._parent._cast(
                _4375.KlingelnbergCycloPalloidHypoidGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4376.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4376,
            )

            return self._parent._cast(
                _4376.KlingelnbergCycloPalloidHypoidGearSetParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4378.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4378,
            )

            return self._parent._cast(
                _4378.KlingelnbergCycloPalloidSpiralBevelGearParametricStudyTool
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4379.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4379,
            )

            return self._parent._cast(
                _4379.KlingelnbergCycloPalloidSpiralBevelGearSetParametricStudyTool
            )

        @property
        def mass_disc_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4380.MassDiscParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4380,
            )

            return self._parent._cast(_4380.MassDiscParametricStudyTool)

        @property
        def measurement_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4381.MeasurementComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4381,
            )

            return self._parent._cast(_4381.MeasurementComponentParametricStudyTool)

        @property
        def mountable_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4383.MountableComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4383,
            )

            return self._parent._cast(_4383.MountableComponentParametricStudyTool)

        @property
        def oil_seal_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4384.OilSealParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4384,
            )

            return self._parent._cast(_4384.OilSealParametricStudyTool)

        @property
        def part_to_part_shear_coupling_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4397.PartToPartShearCouplingHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4397,
            )

            return self._parent._cast(
                _4397.PartToPartShearCouplingHalfParametricStudyTool
            )

        @property
        def part_to_part_shear_coupling_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4398.PartToPartShearCouplingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4398,
            )

            return self._parent._cast(_4398.PartToPartShearCouplingParametricStudyTool)

        @property
        def planetary_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4400.PlanetaryGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4400,
            )

            return self._parent._cast(_4400.PlanetaryGearSetParametricStudyTool)

        @property
        def planet_carrier_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4401.PlanetCarrierParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4401,
            )

            return self._parent._cast(_4401.PlanetCarrierParametricStudyTool)

        @property
        def point_load_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4402.PointLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4402,
            )

            return self._parent._cast(_4402.PointLoadParametricStudyTool)

        @property
        def power_load_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4403.PowerLoadParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4403,
            )

            return self._parent._cast(_4403.PowerLoadParametricStudyTool)

        @property
        def pulley_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4404.PulleyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4404,
            )

            return self._parent._cast(_4404.PulleyParametricStudyTool)

        @property
        def ring_pins_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4405.RingPinsParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4405,
            )

            return self._parent._cast(_4405.RingPinsParametricStudyTool)

        @property
        def rolling_ring_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4407.RollingRingAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4407,
            )

            return self._parent._cast(_4407.RollingRingAssemblyParametricStudyTool)

        @property
        def rolling_ring_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4409.RollingRingParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4409,
            )

            return self._parent._cast(_4409.RollingRingParametricStudyTool)

        @property
        def root_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4410.RootAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4410,
            )

            return self._parent._cast(_4410.RootAssemblyParametricStudyTool)

        @property
        def shaft_hub_connection_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4411.ShaftHubConnectionParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4411,
            )

            return self._parent._cast(_4411.ShaftHubConnectionParametricStudyTool)

        @property
        def shaft_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4412.ShaftParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4412,
            )

            return self._parent._cast(_4412.ShaftParametricStudyTool)

        @property
        def specialised_assembly_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4414.SpecialisedAssemblyParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4414,
            )

            return self._parent._cast(_4414.SpecialisedAssemblyParametricStudyTool)

        @property
        def spiral_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4416.SpiralBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4416,
            )

            return self._parent._cast(_4416.SpiralBevelGearParametricStudyTool)

        @property
        def spiral_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4417.SpiralBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4417,
            )

            return self._parent._cast(_4417.SpiralBevelGearSetParametricStudyTool)

        @property
        def spring_damper_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4419.SpringDamperHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4419,
            )

            return self._parent._cast(_4419.SpringDamperHalfParametricStudyTool)

        @property
        def spring_damper_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4420.SpringDamperParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4420,
            )

            return self._parent._cast(_4420.SpringDamperParametricStudyTool)

        @property
        def straight_bevel_diff_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4422.StraightBevelDiffGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4422,
            )

            return self._parent._cast(_4422.StraightBevelDiffGearParametricStudyTool)

        @property
        def straight_bevel_diff_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4423.StraightBevelDiffGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4423,
            )

            return self._parent._cast(_4423.StraightBevelDiffGearSetParametricStudyTool)

        @property
        def straight_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4425.StraightBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4425,
            )

            return self._parent._cast(_4425.StraightBevelGearParametricStudyTool)

        @property
        def straight_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4426.StraightBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4426,
            )

            return self._parent._cast(_4426.StraightBevelGearSetParametricStudyTool)

        @property
        def straight_bevel_planet_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4427.StraightBevelPlanetGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4427,
            )

            return self._parent._cast(_4427.StraightBevelPlanetGearParametricStudyTool)

        @property
        def straight_bevel_sun_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4428.StraightBevelSunGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4428,
            )

            return self._parent._cast(_4428.StraightBevelSunGearParametricStudyTool)

        @property
        def synchroniser_half_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4429.SynchroniserHalfParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4429,
            )

            return self._parent._cast(_4429.SynchroniserHalfParametricStudyTool)

        @property
        def synchroniser_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4430.SynchroniserParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4430,
            )

            return self._parent._cast(_4430.SynchroniserParametricStudyTool)

        @property
        def synchroniser_part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4431.SynchroniserPartParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4431,
            )

            return self._parent._cast(_4431.SynchroniserPartParametricStudyTool)

        @property
        def synchroniser_sleeve_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4432.SynchroniserSleeveParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4432,
            )

            return self._parent._cast(_4432.SynchroniserSleeveParametricStudyTool)

        @property
        def torque_converter_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4434.TorqueConverterParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4434,
            )

            return self._parent._cast(_4434.TorqueConverterParametricStudyTool)

        @property
        def torque_converter_pump_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4435.TorqueConverterPumpParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4435,
            )

            return self._parent._cast(_4435.TorqueConverterPumpParametricStudyTool)

        @property
        def torque_converter_turbine_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4436.TorqueConverterTurbineParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4436,
            )

            return self._parent._cast(_4436.TorqueConverterTurbineParametricStudyTool)

        @property
        def unbalanced_mass_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4437.UnbalancedMassParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4437,
            )

            return self._parent._cast(_4437.UnbalancedMassParametricStudyTool)

        @property
        def virtual_component_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4438.VirtualComponentParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4438,
            )

            return self._parent._cast(_4438.VirtualComponentParametricStudyTool)

        @property
        def worm_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4440.WormGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4440,
            )

            return self._parent._cast(_4440.WormGearParametricStudyTool)

        @property
        def worm_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4441.WormGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4441,
            )

            return self._parent._cast(_4441.WormGearSetParametricStudyTool)

        @property
        def zerol_bevel_gear_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4443.ZerolBevelGearParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4443,
            )

            return self._parent._cast(_4443.ZerolBevelGearParametricStudyTool)

        @property
        def zerol_bevel_gear_set_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "_4444.ZerolBevelGearSetParametricStudyTool":
            from mastapy.system_model.analyses_and_results.parametric_study_tools import (
                _4444,
            )

            return self._parent._cast(_4444.ZerolBevelGearSetParametricStudyTool)

        @property
        def part_parametric_study_tool(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool",
        ) -> "PartParametricStudyTool":
            return self._parent

        def __getattr__(
            self: "PartParametricStudyTool._Cast_PartParametricStudyTool", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PartParametricStudyTool.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def design_of_experiments_chart(self: Self) -> "_1861.NDChartDefinition":
        """mastapy.utility_gui.charts.NDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DesignOfExperimentsChart

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_sweep_chart_2d(self: Self) -> "_1869.TwoDChartDefinition":
        """mastapy.utility_gui.charts.TwoDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearSweepChart2D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def linear_sweep_chart_3d(self: Self) -> "_1867.ThreeDChartDefinition":
        """mastapy.utility_gui.charts.ThreeDChartDefinition

        Note:
            This property is readonly.
        """
        temp = self.wrapped.LinearSweepChart3D

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def component_design(self: Self) -> "_2470.Part":
        """mastapy.system_model.part_model.Part

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def data_logger(self: Self) -> "_1852.DataLoggerWithCharts":
        """mastapy.utility_gui.DataLoggerWithCharts

        Note:
            This property is readonly.
        """
        temp = self.wrapped.DataLogger

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def parametric_study_tool(self: Self) -> "_4390.ParametricStudyTool":
        """mastapy.system_model.analyses_and_results.parametric_study_tools.ParametricStudyTool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ParametricStudyTool

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "PartParametricStudyTool._Cast_PartParametricStudyTool":
        return self._Cast_PartParametricStudyTool(self)
