"""CylindricalGearSystemDeflectionTimestep"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.system_deflections import _2747
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CYLINDRICAL_GEAR_SYSTEM_DEFLECTION_TIMESTEP = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.SystemDeflections",
    "CylindricalGearSystemDeflectionTimestep",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.system_deflections import (
        _2763,
        _2784,
        _2717,
        _2787,
    )
    from mastapy.system_model.analyses_and_results.analysis_cases import (
        _7549,
        _7550,
        _7547,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("CylindricalGearSystemDeflectionTimestep",)


Self = TypeVar("Self", bound="CylindricalGearSystemDeflectionTimestep")


class CylindricalGearSystemDeflectionTimestep(_2747.CylindricalGearSystemDeflection):
    """CylindricalGearSystemDeflectionTimestep

    This is a mastapy class.
    """

    TYPE = _CYLINDRICAL_GEAR_SYSTEM_DEFLECTION_TIMESTEP
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_CylindricalGearSystemDeflectionTimestep"
    )

    class _Cast_CylindricalGearSystemDeflectionTimestep:
        """Special nested class for casting CylindricalGearSystemDeflectionTimestep to subclasses."""

        def __init__(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
            parent: "CylindricalGearSystemDeflectionTimestep",
        ):
            self._parent = parent

        @property
        def cylindrical_gear_system_deflection(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_2747.CylindricalGearSystemDeflection":
            return self._parent._cast(_2747.CylindricalGearSystemDeflection)

        @property
        def gear_system_deflection(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_2763.GearSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2763,
            )

            return self._parent._cast(_2763.GearSystemDeflection)

        @property
        def mountable_component_system_deflection(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_2784.MountableComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2784,
            )

            return self._parent._cast(_2784.MountableComponentSystemDeflection)

        @property
        def component_system_deflection(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_2717.ComponentSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2717,
            )

            return self._parent._cast(_2717.ComponentSystemDeflection)

        @property
        def part_system_deflection(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_2787.PartSystemDeflection":
            from mastapy.system_model.analyses_and_results.system_deflections import (
                _2787,
            )

            return self._parent._cast(_2787.PartSystemDeflection)

        @property
        def part_fe_analysis(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_7549.PartFEAnalysis":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7549

            return self._parent._cast(_7549.PartFEAnalysis)

        @property
        def part_static_load_analysis_case(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_7550.PartStaticLoadAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7550

            return self._parent._cast(_7550.PartStaticLoadAnalysisCase)

        @property
        def part_analysis_case(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_7547.PartAnalysisCase":
            from mastapy.system_model.analyses_and_results.analysis_cases import _7547

            return self._parent._cast(_7547.PartAnalysisCase)

        @property
        def part_analysis(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def cylindrical_gear_system_deflection_timestep(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
        ) -> "CylindricalGearSystemDeflectionTimestep":
            return self._parent

        def __getattr__(
            self: "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep",
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
        self: Self, instance_to_wrap: "CylindricalGearSystemDeflectionTimestep.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "CylindricalGearSystemDeflectionTimestep._Cast_CylindricalGearSystemDeflectionTimestep":
        return self._Cast_CylindricalGearSystemDeflectionTimestep(self)
