"""NonCADElectricMachineDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.electric_machines import _1263
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_NON_CAD_ELECTRIC_MACHINE_DETAIL = python_net_import(
    "SMT.MastaAPI.ElectricMachines", "NonCADElectricMachineDetail"
)

if TYPE_CHECKING:
    from mastapy.electric_machines import _1301, _1277, _1291, _1305, _1307, _1322


__docformat__ = "restructuredtext en"
__all__ = ("NonCADElectricMachineDetail",)


Self = TypeVar("Self", bound="NonCADElectricMachineDetail")


class NonCADElectricMachineDetail(_1263.ElectricMachineDetail):
    """NonCADElectricMachineDetail

    This is a mastapy class.
    """

    TYPE = _NON_CAD_ELECTRIC_MACHINE_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_NonCADElectricMachineDetail")

    class _Cast_NonCADElectricMachineDetail:
        """Special nested class for casting NonCADElectricMachineDetail to subclasses."""

        def __init__(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
            parent: "NonCADElectricMachineDetail",
        ):
            self._parent = parent

        @property
        def electric_machine_detail(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1263.ElectricMachineDetail":
            return self._parent._cast(_1263.ElectricMachineDetail)

        @property
        def interior_permanent_magnet_machine(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1277.InteriorPermanentMagnetMachine":
            from mastapy.electric_machines import _1277

            return self._parent._cast(_1277.InteriorPermanentMagnetMachine)

        @property
        def permanent_magnet_assisted_synchronous_reluctance_machine(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1291.PermanentMagnetAssistedSynchronousReluctanceMachine":
            from mastapy.electric_machines import _1291

            return self._parent._cast(
                _1291.PermanentMagnetAssistedSynchronousReluctanceMachine
            )

        @property
        def surface_permanent_magnet_machine(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1305.SurfacePermanentMagnetMachine":
            from mastapy.electric_machines import _1305

            return self._parent._cast(_1305.SurfacePermanentMagnetMachine)

        @property
        def synchronous_reluctance_machine(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1307.SynchronousReluctanceMachine":
            from mastapy.electric_machines import _1307

            return self._parent._cast(_1307.SynchronousReluctanceMachine)

        @property
        def wound_field_synchronous_machine(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "_1322.WoundFieldSynchronousMachine":
            from mastapy.electric_machines import _1322

            return self._parent._cast(_1322.WoundFieldSynchronousMachine)

        @property
        def non_cad_electric_machine_detail(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
        ) -> "NonCADElectricMachineDetail":
            return self._parent

        def __getattr__(
            self: "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "NonCADElectricMachineDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def stator(self: Self) -> "_1301.Stator":
        """mastapy.electric_machines.Stator

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Stator

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "NonCADElectricMachineDetail._Cast_NonCADElectricMachineDetail":
        return self._Cast_NonCADElectricMachineDetail(self)
