"""PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
    _3295,
)
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PLANETARY_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SteadyStateSynchronousResponsesOnAShaft",
    "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model.gears import _2544
    from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
        _3306,
        _3345,
        _3247,
        _3326,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import _7550, _7547
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",)


Self = TypeVar("Self", bound="PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft")


class PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft(
    _3295.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
):
    """PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft

    This is a mastapy class.
    """

    TYPE = _PLANETARY_GEAR_SET_STEADY_STATE_SYNCHRONOUS_RESPONSE_ON_A_SHAFT
    _CastSelf = TypeVar(
        "_CastSelf",
        bound="_Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
    )

    class _Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft:
        """Special nested class for casting PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft to subclasses."""

        def __init__(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
            parent: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3295.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent._cast(
                _3295.CylindricalGearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3306.GearSetSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3306,
            )

            return self._parent._cast(
                _3306.GearSetSteadyStateSynchronousResponseOnAShaft
            )

        @property
        def specialised_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3345.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3345,
            )

            return self._parent._cast(
                _3345.SpecialisedAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def abstract_assembly_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3247.AbstractAssemblySteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3247,
            )

            return self._parent._cast(
                _3247.AbstractAssemblySteadyStateSynchronousResponseOnAShaft
            )

        @property
        def part_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_3326.PartSteadyStateSynchronousResponseOnAShaft":
            from mastapy.system_model.analyses_and_results.steady_state_synchronous_responses_on_a_shaft import (
                _3326,
            )

            return self._parent._cast(_3326.PartSteadyStateSynchronousResponseOnAShaft)

        @property
        def part_static_load_analysis_case(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def planetary_gear_set_steady_state_synchronous_response_on_a_shaft(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
        ) -> "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
            return self._parent

        def __getattr__(
            self: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft",
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
        instance_to_wrap: "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft.TYPE",
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def assembly_design(self: Self) -> "_2544.PlanetaryGearSet":
        """mastapy.system_model.part_model.gears.PlanetaryGearSet

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
    ) -> "PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft":
        return self._Cast_PlanetaryGearSetSteadyStateSynchronousResponseOnAShaft(self)
