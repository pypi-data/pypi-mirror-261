"""ElectricMachinePeriodicExcitationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.harmonic_analyses import _5794
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_PERIODIC_EXCITATION_DETAIL = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.HarmonicAnalyses",
    "ElectricMachinePeriodicExcitationDetail",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.harmonic_analyses import (
        _5736,
        _5737,
        _5738,
        _5739,
        _5740,
        _5741,
        _5742,
        _5743,
        _5744,
        _5745,
        _5746,
        _5681,
    )


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachinePeriodicExcitationDetail",)


Self = TypeVar("Self", bound="ElectricMachinePeriodicExcitationDetail")


class ElectricMachinePeriodicExcitationDetail(
    _5794.PeriodicExcitationWithReferenceShaft
):
    """ElectricMachinePeriodicExcitationDetail

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_PERIODIC_EXCITATION_DETAIL
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachinePeriodicExcitationDetail"
    )

    class _Cast_ElectricMachinePeriodicExcitationDetail:
        """Special nested class for casting ElectricMachinePeriodicExcitationDetail to subclasses."""

        def __init__(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
            parent: "ElectricMachinePeriodicExcitationDetail",
        ):
            self._parent = parent

        @property
        def periodic_excitation_with_reference_shaft(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5794.PeriodicExcitationWithReferenceShaft":
            return self._parent._cast(_5794.PeriodicExcitationWithReferenceShaft)

        @property
        def abstract_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5681.AbstractPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5681,
            )

            return self._parent._cast(_5681.AbstractPeriodicExcitationDetail)

        @property
        def electric_machine_rotor_x_force_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5736.ElectricMachineRotorXForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5736,
            )

            return self._parent._cast(
                _5736.ElectricMachineRotorXForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_x_moment_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5737.ElectricMachineRotorXMomentPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5737,
            )

            return self._parent._cast(
                _5737.ElectricMachineRotorXMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_force_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5738.ElectricMachineRotorYForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5738,
            )

            return self._parent._cast(
                _5738.ElectricMachineRotorYForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_y_moment_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5739.ElectricMachineRotorYMomentPeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5739,
            )

            return self._parent._cast(
                _5739.ElectricMachineRotorYMomentPeriodicExcitationDetail
            )

        @property
        def electric_machine_rotor_z_force_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5740.ElectricMachineRotorZForcePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5740,
            )

            return self._parent._cast(
                _5740.ElectricMachineRotorZForcePeriodicExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_axial_loads_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5741.ElectricMachineStatorToothAxialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5741,
            )

            return self._parent._cast(
                _5741.ElectricMachineStatorToothAxialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_loads_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5742.ElectricMachineStatorToothLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5742,
            )

            return self._parent._cast(
                _5742.ElectricMachineStatorToothLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_moments_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5743.ElectricMachineStatorToothMomentsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5743,
            )

            return self._parent._cast(
                _5743.ElectricMachineStatorToothMomentsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_radial_loads_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5744.ElectricMachineStatorToothRadialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5744,
            )

            return self._parent._cast(
                _5744.ElectricMachineStatorToothRadialLoadsExcitationDetail
            )

        @property
        def electric_machine_stator_tooth_tangential_loads_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5745.ElectricMachineStatorToothTangentialLoadsExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5745,
            )

            return self._parent._cast(
                _5745.ElectricMachineStatorToothTangentialLoadsExcitationDetail
            )

        @property
        def electric_machine_torque_ripple_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "_5746.ElectricMachineTorqueRipplePeriodicExcitationDetail":
            from mastapy.system_model.analyses_and_results.harmonic_analyses import (
                _5746,
            )

            return self._parent._cast(
                _5746.ElectricMachineTorqueRipplePeriodicExcitationDetail
            )

        @property
        def electric_machine_periodic_excitation_detail(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
        ) -> "ElectricMachinePeriodicExcitationDetail":
            return self._parent

        def __getattr__(
            self: "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail",
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
        self: Self, instance_to_wrap: "ElectricMachinePeriodicExcitationDetail.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachinePeriodicExcitationDetail._Cast_ElectricMachinePeriodicExcitationDetail":
        return self._Cast_ElectricMachinePeriodicExcitationDetail(self)
