"""CylindricalGearSetSystemDeflectionTimestep"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.system_deflections import _2744
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION_TIMESTEP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearSetSystemDeflectionTimestep",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
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
__all__ = ("CylindricalGearSetSystemDeflectionTimestep",)


Self = TypeVar("Self", bound="CylindricalGearSetSystemDeflectionTimestep")


class CylindricalGearSetSystemDeflectionTimestep(
    _2744.CylindricalGearSetSystemDeflection
):
    """CylindricalGearSetSystemDeflectionTimestep

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SET_SYSTEM_DEFLECTION_TIMESTEP
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSetSystemDeflectionTimestep"
    )

    class _Cast_CylindricalGearSetSystemDeflectionTimestep:
        """Special nested class for casting CylindricalGearSetSystemDeflectionTimestep to subclasses."""

        def __init__(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
            parent: "CylindricalGearSetSystemDeflectionTimestep",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_set_system_deflection(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2744.CylindricalGearSetSystemDeflection":
            return self._parent._cast(_2744.CylindricalGearSetSystemDeflection)

        @property
        def gear_set_system_deflection(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2762.GearSetSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2762,
            )

            return self._parent._cast(_2762.GearSetSystemDeflection)

        @property
        def specialised_assembly_system_deflection(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2808.SpecialisedAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2808,
            )

            return self._parent._cast(_2808.SpecialisedAssemblySystemDeflection)

        @property
        def abstract_assembly_system_deflection(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2687.AbstractAssemblySystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2687,
            )

            return self._parent._cast(_2687.AbstractAssemblySystemDeflection)

        @property
        def part_system_deflection(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2787.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_gear_set_system_deflection_timestep(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
        ) -> "CylindricalGearSetSystemDeflectionTimestep":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep",
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
        self: Self, instance_to_wrap: "CylindricalGearSetSystemDeflectionTimestep.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSetSystemDeflectionTimestep._Cast_CylindricalGearSetSystemDeflectionTimestep":
        return self._Cast_CylindricalGearSetSystemDeflectionTimestep(self)
