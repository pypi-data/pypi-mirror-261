"""ElectricMachineHarmonicLoadDataFromMotorCAD"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.system_model.analyses_and_results.static_loads import _6880
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_CAD = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "ElectricMachineHarmonicLoadDataFromMotorCAD",
)

if TYPE_CHECKING:
    from mastapy.system_model.analyses_and_results.static_loads import _6874
    from mastapy.electric_machines.harmonic_load_data import _1380, _1385, _1382


__docformat__ = "restructuredtext en"
__all__ = ("ElectricMachineHarmonicLoadDataFromMotorCAD",)


Self = TypeVar("Self", bound="ElectricMachineHarmonicLoadDataFromMotorCAD")


class ElectricMachineHarmonicLoadDataFromMotorCAD(
    _6880.ElectricMachineHarmonicLoadDataFromMotorPackages[
        "_6885.ElectricMachineHarmonicLoadMotorCADImportOptions"
    ]
):
    """ElectricMachineHarmonicLoadDataFromMotorCAD

    This is a mastapy class.
    """

    TYPE = _ELECTRIC_MACHINE_HARMONIC_LOAD_DATA_FROM_MOTOR_CAD
    _CastSelf = TypeVar(
        "_CastSelf", bound="_Cast_ElectricMachineHarmonicLoadDataFromMotorCAD"
    )

    class _Cast_ElectricMachineHarmonicLoadDataFromMotorCAD:
        """Special nested class for casting ElectricMachineHarmonicLoadDataFromMotorCAD to subclasses."""

        def __init__(
            self: "ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD",
            parent: "ElectricMachineHarmonicLoadDataFromMotorCAD",
        ):
            self._parent = parent

        @property
        def electric_machine_harmonic_load_data_from_motor_packages(
            self: "ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD",
        ) -> "_6880.ElectricMachineHarmonicLoadDataFromMotorPackages":
            return self._parent._cast(
                _6880.ElectricMachineHarmonicLoadDataFromMotorPackages
            )

        @property
        def electric_machine_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD",
        ) -> "_6874.ElectricMachineHarmonicLoadData":
            from mastapy.system_model.analyses_and_results.static_loads import _6874

            return self._parent._cast(_6874.ElectricMachineHarmonicLoadData)

        @property
        def electric_machine_harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD",
        ) -> "_1380.ElectricMachineHarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1380

            return self._parent._cast(_1380.ElectricMachineHarmonicLoadDataBase)

        @property
        def speed_dependent_harmonic_load_data(
            self: "ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD",
        ) -> "_1385.SpeedDependentHarmonicLoadData":
            from mastapy.electric_machines.harmonic_load_data import _1385

            return self._parent._cast(_1385.SpeedDependentHarmonicLoadData)

        @property
        def harmonic_load_data_base(
            self: "ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD",
        ) -> "_1382.HarmonicLoadDataBase":
            from mastapy.electric_machines.harmonic_load_data import _1382

            return self._parent._cast(_1382.HarmonicLoadDataBase)

        @property
        def electric_machine_harmonic_load_data_from_motor_cad(
            self: "ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD",
        ) -> "ElectricMachineHarmonicLoadDataFromMotorCAD":
            return self._parent

        def __getattr__(
            self: "ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD",
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
        self: Self, instance_to_wrap: "ElectricMachineHarmonicLoadDataFromMotorCAD.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "ElectricMachineHarmonicLoadDataFromMotorCAD._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD":
        return self._Cast_ElectricMachineHarmonicLoadDataFromMotorCAD(self)
