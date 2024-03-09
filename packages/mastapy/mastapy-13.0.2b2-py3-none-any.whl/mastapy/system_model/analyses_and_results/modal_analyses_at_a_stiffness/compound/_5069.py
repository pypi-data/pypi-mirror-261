"""PartCompoundModalAnalysisAtAStiffness"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, List

from mastapy._internal import conversion
from mastapy.system_model.analyses_and_results.analysis_cases import _7548
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PART_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.ModalAnalysesAtAStiffness.Compound",
    "PartCompoundModalAnalysisAtAStiffness",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness import (
        _4940,
    )
    from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
        _4990,
        _4991,
        _4992,
        _4994,
        _4996,
        _4997,
        _4998,
        _5000,
        _5001,
        _5003,
        _5004,
        _5005,
        _5006,
        _5008,
        _5009,
        _5010,
        _5011,
        _5013,
        _5015,
        _5016,
        _5018,
        _5019,
        _5021,
        _5022,
        _5024,
        _5026,
        _5027,
        _5029,
        _5031,
        _5032,
        _5033,
        _5035,
        _5037,
        _5039,
        _5040,
        _5041,
        _5042,
        _5043,
        _5045,
        _5046,
        _5047,
        _5048,
        _5050,
        _5051,
        _5052,
        _5054,
        _5056,
        _5058,
        _5059,
        _5061,
        _5062,
        _5064,
        _5065,
        _5066,
        _5067,
        _5068,
        _5070,
        _5072,
        _5074,
        _5075,
        _5076,
        _5077,
        _5078,
        _5079,
        _5081,
        _5082,
        _5084,
        _5085,
        _5086,
        _5088,
        _5089,
        _5091,
        _5092,
        _5094,
        _5095,
        _5097,
        _5098,
        _5100,
        _5101,
        _5102,
        _5103,
        _5104,
        _5105,
        _5106,
        _5107,
        _5109,
        _5110,
        _5111,
        _5112,
        _5113,
        _5115,
        _5116,
        _5118,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7545
    from mastapy.system_model.analyses_and_results import _2653


__docformat__ = "restructuredtext en"
__all__ = ("PartCompoundModalAnalysisAtAStiffness",)


Self = TypeVar("Self", bound="PartCompoundModalAnalysisAtAStiffness")


class PartCompoundModalAnalysisAtAStiffness(_7548.PartCompoundAnalysis):
    """PartCompoundModalAnalysisAtAStiffness

    This is a mastapy class.
    """

    TYPE = _PART_COMPOUND_MODAL_ANALYSIS_AT_A_STIFFNESS
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_PartCompoundModalAnalysisAtAStiffness"
    )

    class _Cast_PartCompoundModalAnalysisAtAStiffness:
        """Special nested class for casting PartCompoundModalAnalysisAtAStiffness to subclasses."""

        def __init__(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
            parent: "PartCompoundModalAnalysisAtAStiffness",
        ):
            self._parent = parent

        @property
        def part_compound_analysis(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_7548.PartCompoundAnalysis":
            return self._parent._cast(_7548.PartCompoundAnalysis)

        @property
        def design_entity_compound_analysis(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_7545.DesignEntityCompoundAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7545

            return self._parent._cast(_7545.DesignEntityCompoundAnalysis)

        @property
        def design_entity_analysis(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def abstract_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_4990.AbstractAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4990,
            )

            return self._parent._cast(
                _4990.AbstractAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_4991.AbstractShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4991,
            )

            return self._parent._cast(
                _4991.AbstractShaftCompoundModalAnalysisAtAStiffness
            )

        @property
        def abstract_shaft_or_housing_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_4992.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4992,
            )

            return self._parent._cast(
                _4992.AbstractShaftOrHousingCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_4994.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4994,
            )

            return self._parent._cast(
                _4994.AGMAGleasonConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def agma_gleason_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_4996.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4996,
            )

            return self._parent._cast(
                _4996.AGMAGleasonConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_4997.AssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4997,
            )

            return self._parent._cast(_4997.AssemblyCompoundModalAnalysisAtAStiffness)

        @property
        def bearing_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_4998.BearingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _4998,
            )

            return self._parent._cast(_4998.BearingCompoundModalAnalysisAtAStiffness)

        @property
        def belt_drive_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5000.BeltDriveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5000,
            )

            return self._parent._cast(_5000.BeltDriveCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_differential_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5001.BevelDifferentialGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5001,
            )

            return self._parent._cast(
                _5001.BevelDifferentialGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5003.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5003,
            )

            return self._parent._cast(
                _5003.BevelDifferentialGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5004.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5004,
            )

            return self._parent._cast(
                _5004.BevelDifferentialPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_differential_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5005.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5005,
            )

            return self._parent._cast(
                _5005.BevelDifferentialSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5006.BevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5006,
            )

            return self._parent._cast(_5006.BevelGearCompoundModalAnalysisAtAStiffness)

        @property
        def bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5008.BevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5008,
            )

            return self._parent._cast(
                _5008.BevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def bolt_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5009.BoltCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5009,
            )

            return self._parent._cast(_5009.BoltCompoundModalAnalysisAtAStiffness)

        @property
        def bolted_joint_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5010.BoltedJointCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5010,
            )

            return self._parent._cast(
                _5010.BoltedJointCompoundModalAnalysisAtAStiffness
            )

        @property
        def clutch_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5011.ClutchCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5011,
            )

            return self._parent._cast(_5011.ClutchCompoundModalAnalysisAtAStiffness)

        @property
        def clutch_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5013.ClutchHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5013,
            )

            return self._parent._cast(_5013.ClutchHalfCompoundModalAnalysisAtAStiffness)

        @property
        def component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5015.ComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5015,
            )

            return self._parent._cast(_5015.ComponentCompoundModalAnalysisAtAStiffness)

        @property
        def concept_coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5016.ConceptCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5016,
            )

            return self._parent._cast(
                _5016.ConceptCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5018.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5018,
            )

            return self._parent._cast(
                _5018.ConceptCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5019.ConceptGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5019,
            )

            return self._parent._cast(
                _5019.ConceptGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def concept_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5021.ConceptGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5021,
            )

            return self._parent._cast(
                _5021.ConceptGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5022.ConicalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5022,
            )

            return self._parent._cast(
                _5022.ConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5024.ConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5024,
            )

            return self._parent._cast(
                _5024.ConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def connector_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5026.ConnectorCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5026,
            )

            return self._parent._cast(_5026.ConnectorCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5027.CouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5027,
            )

            return self._parent._cast(_5027.CouplingCompoundModalAnalysisAtAStiffness)

        @property
        def coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5029.CouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5029,
            )

            return self._parent._cast(
                _5029.CouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def cvt_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5031.CVTCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5031,
            )

            return self._parent._cast(_5031.CVTCompoundModalAnalysisAtAStiffness)

        @property
        def cvt_pulley_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5032.CVTPulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5032,
            )

            return self._parent._cast(_5032.CVTPulleyCompoundModalAnalysisAtAStiffness)

        @property
        def cycloidal_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5033.CycloidalAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5033,
            )

            return self._parent._cast(
                _5033.CycloidalAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def cycloidal_disc_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5035.CycloidalDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5035,
            )

            return self._parent._cast(
                _5035.CycloidalDiscCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5037.CylindricalGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5037,
            )

            return self._parent._cast(
                _5037.CylindricalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5039.CylindricalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5039,
            )

            return self._parent._cast(
                _5039.CylindricalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def cylindrical_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5040.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5040,
            )

            return self._parent._cast(
                _5040.CylindricalPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def datum_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5041.DatumCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5041,
            )

            return self._parent._cast(_5041.DatumCompoundModalAnalysisAtAStiffness)

        @property
        def external_cad_model_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5042.ExternalCADModelCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5042,
            )

            return self._parent._cast(
                _5042.ExternalCADModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def face_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5043.FaceGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5043,
            )

            return self._parent._cast(_5043.FaceGearCompoundModalAnalysisAtAStiffness)

        @property
        def face_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5045.FaceGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5045,
            )

            return self._parent._cast(
                _5045.FaceGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def fe_part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5046.FEPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5046,
            )

            return self._parent._cast(_5046.FEPartCompoundModalAnalysisAtAStiffness)

        @property
        def flexible_pin_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5047.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5047,
            )

            return self._parent._cast(
                _5047.FlexiblePinAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5048.GearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5048,
            )

            return self._parent._cast(_5048.GearCompoundModalAnalysisAtAStiffness)

        @property
        def gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5050.GearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5050,
            )

            return self._parent._cast(_5050.GearSetCompoundModalAnalysisAtAStiffness)

        @property
        def guide_dxf_model_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5051.GuideDxfModelCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5051,
            )

            return self._parent._cast(
                _5051.GuideDxfModelCompoundModalAnalysisAtAStiffness
            )

        @property
        def hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5052.HypoidGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5052,
            )

            return self._parent._cast(_5052.HypoidGearCompoundModalAnalysisAtAStiffness)

        @property
        def hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5054.HypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5054,
            )

            return self._parent._cast(
                _5054.HypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5056.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5056,
            )

            return self._parent._cast(
                _5056.KlingelnbergCycloPalloidConicalGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5058.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5058,
            )

            return self._parent._cast(
                _5058.KlingelnbergCycloPalloidConicalGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> (
            "_5059.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness"
        ):
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5059,
            )

            return self._parent._cast(
                _5059.KlingelnbergCycloPalloidHypoidGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5061.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5061,
            )

            return self._parent._cast(
                _5061.KlingelnbergCycloPalloidHypoidGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5062.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5062,
            )

            return self._parent._cast(
                _5062.KlingelnbergCycloPalloidSpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5064.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5064,
            )

            return self._parent._cast(
                _5064.KlingelnbergCycloPalloidSpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def mass_disc_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5065.MassDiscCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5065,
            )

            return self._parent._cast(_5065.MassDiscCompoundModalAnalysisAtAStiffness)

        @property
        def measurement_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5066.MeasurementComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5066,
            )

            return self._parent._cast(
                _5066.MeasurementComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def mountable_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5067.MountableComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5067,
            )

            return self._parent._cast(
                _5067.MountableComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def oil_seal_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5068.OilSealCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5068,
            )

            return self._parent._cast(_5068.OilSealCompoundModalAnalysisAtAStiffness)

        @property
        def part_to_part_shear_coupling_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5070.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5070,
            )

            return self._parent._cast(
                _5070.PartToPartShearCouplingCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_to_part_shear_coupling_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5072.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5072,
            )

            return self._parent._cast(
                _5072.PartToPartShearCouplingHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def planetary_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5074.PlanetaryGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5074,
            )

            return self._parent._cast(
                _5074.PlanetaryGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def planet_carrier_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5075.PlanetCarrierCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5075,
            )

            return self._parent._cast(
                _5075.PlanetCarrierCompoundModalAnalysisAtAStiffness
            )

        @property
        def point_load_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5076.PointLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5076,
            )

            return self._parent._cast(_5076.PointLoadCompoundModalAnalysisAtAStiffness)

        @property
        def power_load_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5077.PowerLoadCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5077,
            )

            return self._parent._cast(_5077.PowerLoadCompoundModalAnalysisAtAStiffness)

        @property
        def pulley_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5078.PulleyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5078,
            )

            return self._parent._cast(_5078.PulleyCompoundModalAnalysisAtAStiffness)

        @property
        def ring_pins_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5079.RingPinsCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5079,
            )

            return self._parent._cast(_5079.RingPinsCompoundModalAnalysisAtAStiffness)

        @property
        def rolling_ring_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5081.RollingRingAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5081,
            )

            return self._parent._cast(
                _5081.RollingRingAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def rolling_ring_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5082.RollingRingCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5082,
            )

            return self._parent._cast(
                _5082.RollingRingCompoundModalAnalysisAtAStiffness
            )

        @property
        def root_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5084.RootAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5084,
            )

            return self._parent._cast(
                _5084.RootAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def shaft_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5085.ShaftCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5085,
            )

            return self._parent._cast(_5085.ShaftCompoundModalAnalysisAtAStiffness)

        @property
        def shaft_hub_connection_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5086.ShaftHubConnectionCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5086,
            )

            return self._parent._cast(
                _5086.ShaftHubConnectionCompoundModalAnalysisAtAStiffness
            )

        @property
        def specialised_assembly_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5088.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5088,
            )

            return self._parent._cast(
                _5088.SpecialisedAssemblyCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5089.SpiralBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5089,
            )

            return self._parent._cast(
                _5089.SpiralBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def spiral_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5091.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5091,
            )

            return self._parent._cast(
                _5091.SpiralBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5092.SpringDamperCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5092,
            )

            return self._parent._cast(
                _5092.SpringDamperCompoundModalAnalysisAtAStiffness
            )

        @property
        def spring_damper_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5094.SpringDamperHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5094,
            )

            return self._parent._cast(
                _5094.SpringDamperHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5095.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5095,
            )

            return self._parent._cast(
                _5095.StraightBevelDiffGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_diff_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5097.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5097,
            )

            return self._parent._cast(
                _5097.StraightBevelDiffGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5098.StraightBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5098,
            )

            return self._parent._cast(
                _5098.StraightBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5100.StraightBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5100,
            )

            return self._parent._cast(
                _5100.StraightBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_planet_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5101.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5101,
            )

            return self._parent._cast(
                _5101.StraightBevelPlanetGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def straight_bevel_sun_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5102.StraightBevelSunGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5102,
            )

            return self._parent._cast(
                _5102.StraightBevelSunGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5103.SynchroniserCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5103,
            )

            return self._parent._cast(
                _5103.SynchroniserCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_half_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5104.SynchroniserHalfCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5104,
            )

            return self._parent._cast(
                _5104.SynchroniserHalfCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5105.SynchroniserPartCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5105,
            )

            return self._parent._cast(
                _5105.SynchroniserPartCompoundModalAnalysisAtAStiffness
            )

        @property
        def synchroniser_sleeve_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5106.SynchroniserSleeveCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5106,
            )

            return self._parent._cast(
                _5106.SynchroniserSleeveCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5107.TorqueConverterCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5107,
            )

            return self._parent._cast(
                _5107.TorqueConverterCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_pump_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5109.TorqueConverterPumpCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5109,
            )

            return self._parent._cast(
                _5109.TorqueConverterPumpCompoundModalAnalysisAtAStiffness
            )

        @property
        def torque_converter_turbine_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5110.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5110,
            )

            return self._parent._cast(
                _5110.TorqueConverterTurbineCompoundModalAnalysisAtAStiffness
            )

        @property
        def unbalanced_mass_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5111.UnbalancedMassCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5111,
            )

            return self._parent._cast(
                _5111.UnbalancedMassCompoundModalAnalysisAtAStiffness
            )

        @property
        def virtual_component_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5112.VirtualComponentCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5112,
            )

            return self._parent._cast(
                _5112.VirtualComponentCompoundModalAnalysisAtAStiffness
            )

        @property
        def worm_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5113.WormGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5113,
            )

            return self._parent._cast(_5113.WormGearCompoundModalAnalysisAtAStiffness)

        @property
        def worm_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5115.WormGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5115,
            )

            return self._parent._cast(
                _5115.WormGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5116.ZerolBevelGearCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5116,
            )

            return self._parent._cast(
                _5116.ZerolBevelGearCompoundModalAnalysisAtAStiffness
            )

        @property
        def zerol_bevel_gear_set_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "_5118.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness":
            from mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.compound import (
                _5118,
            )

            return self._parent._cast(
                _5118.ZerolBevelGearSetCompoundModalAnalysisAtAStiffness
            )

        @property
        def part_compound_modal_analysis_at_a_stiffness(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
        ) -> "PartCompoundModalAnalysisAtAStiffness":
            return self._parent

        def __getattr__(
            self: "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness",
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
        self: Self, instance_to_wrap: "PartCompoundModalAnalysisAtAStiffness.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_analysis_cases(
        self: Self,
    ) -> "List[_4940.PartModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PartModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCases

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def component_analysis_cases_ready(
        self: Self,
    ) -> "List[_4940.PartModalAnalysisAtAStiffness]":
        """List[mastapy.system_model.analyses_and_results.modal_analyses_at_a_stiffness.PartModalAnalysisAtAStiffness]

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentAnalysisCasesReady

        if temp is None:
            return None

        value = conversion.pn_to_mp_objects_in_list(temp)

        if value is None:
            return None

        return value

    @property
    def cast_to(
        self: Self,
    ) -> "PartCompoundModalAnalysisAtAStiffness._Cast_PartCompoundModalAnalysisAtAStiffness":
        return self._Cast_PartCompoundModalAnalysisAtAStiffness(self)
