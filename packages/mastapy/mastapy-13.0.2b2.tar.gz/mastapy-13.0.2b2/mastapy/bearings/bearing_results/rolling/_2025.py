"""LoadedNonBarrelRollerBearingDutyCycle"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.bearings.bearing_results import _1961
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_LOADED_NON_BARREL_ROLLER_BEARING_DUTY_CYCLE = python_net_import(
    "SMT.MastaAPI.Bearings.BearingResults.Rolling",
    "LoadedNonBarrelRollerBearingDutyCycle",
)

if TYPE_CHECKING:
    from mastapy.bearings.bearing_results.rolling import _1994, _2009, _2048
    from mastapy.bearings.bearing_results import _1958, _1950


__docformat__ = "restructuredtext en"
__all__ = ("LoadedNonBarrelRollerBearingDutyCycle",)


Self = TypeVar("Self", bound="LoadedNonBarrelRollerBearingDutyCycle")


class LoadedNonBarrelRollerBearingDutyCycle(_1961.LoadedRollingBearingDutyCycle):
    """LoadedNonBarrelRollerBearingDutyCycle

    This is a mastapy class.
    """

    TYPE = _LOADED_NON_BARREL_ROLLER_BEARING_DUTY_CYCLE
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_LoadedNonBarrelRollerBearingDutyCycle"
    )

    class _Cast_LoadedNonBarrelRollerBearingDutyCycle:
        """Special nested class for casting LoadedNonBarrelRollerBearingDutyCycle to subclasses."""

        def __init__(
            self: "LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle",
            parent: "LoadedNonBarrelRollerBearingDutyCycle",
        ):
            self._parent = parent

        @property
        def loaded_rolling_bearing_duty_cycle(
            self: "LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle",
        ) -> "_1961.LoadedRollingBearingDutyCycle":
            return self._parent._cast(_1961.LoadedRollingBearingDutyCycle)

        @property
        def loaded_non_linear_bearing_duty_cycle_results(
            self: "LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle",
        ) -> "_1958.LoadedNonLinearBearingDutyCycleResults":
            from mastapy.bearings.bearing_results import _1958

            return self._parent._cast(_1958.LoadedNonLinearBearingDutyCycleResults)

        @property
        def loaded_bearing_duty_cycle(
            self: "LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle",
        ) -> "_1950.LoadedBearingDutyCycle":
            from mastapy.bearings.bearing_results import _1950

            return self._parent._cast(_1950.LoadedBearingDutyCycle)

        @property
        def loaded_axial_thrust_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle",
        ) -> "_1994.LoadedAxialThrustCylindricalRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _1994

            return self._parent._cast(
                _1994.LoadedAxialThrustCylindricalRollerBearingDutyCycle
            )

        @property
        def loaded_cylindrical_roller_bearing_duty_cycle(
            self: "LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle",
        ) -> "_2009.LoadedCylindricalRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2009

            return self._parent._cast(_2009.LoadedCylindricalRollerBearingDutyCycle)

        @property
        def loaded_taper_roller_bearing_duty_cycle(
            self: "LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle",
        ) -> "_2048.LoadedTaperRollerBearingDutyCycle":
            from mastapy.bearings.bearing_results.rolling import _2048

            return self._parent._cast(_2048.LoadedTaperRollerBearingDutyCycle)

        @property
        def loaded_non_barrel_roller_bearing_duty_cycle(
            self: "LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle",
        ) -> "LoadedNonBarrelRollerBearingDutyCycle":
            return self._parent

        def __getattr__(
            self: "LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle",
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
        self: Self, instance_to_wrap: "LoadedNonBarrelRollerBearingDutyCycle.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def smt_rib_stress_safety_factor(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.SMTRibStressSafetyFactor

        if temp is None:
            return 0.0

        return temp

    @property
    def cast_to(
        self: Self,
    ) -> "LoadedNonBarrelRollerBearingDutyCycle._Cast_LoadedNonBarrelRollerBearingDutyCycle":
        return self._Cast_LoadedNonBarrelRollerBearingDutyCycle(self)
