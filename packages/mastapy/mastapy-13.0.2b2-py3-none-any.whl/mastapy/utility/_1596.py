"""PerMachineSettings"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.utility import _1597
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_PER_MACHINE_SETTINGS = python_net_import("SMT.MastaAPI.Utility", "PerMachineSettings")

if TYPE_CHECKING:
    from mastapy.nodal_analysis import _68
    from mastapy.nodal_analysis.geometry_modeller_link import _160
    from mastapy.gears.materials import _596
    from mastapy.gears.ltca.cylindrical import _855
    from mastapy.gears.gear_designs.cylindrical import _1012
    from mastapy.utility import _1598, _1599
    from mastapy.utility.units_and_measurements import _1608
    from mastapy.utility.scripting import _1741
    from mastapy.utility.databases import _1829
    from mastapy.utility.cad_export import _1834
    from mastapy.bearings import _1901
    from mastapy.system_model.part_model import _2472


__docformat__ = "restructuredtext en"
__all__ = ("PerMachineSettings",)


Self = TypeVar("Self", bound="PerMachineSettings")


class PerMachineSettings(_1597.PersistentSingleton):
    """PerMachineSettings

    This is a mastapy class.
    """

    TYPE = _PER_MACHINE_SETTINGS
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_PerMachineSettings")

    class _Cast_PerMachineSettings:
        """Special nested class for casting PerMachineSettings to subclasses."""

        def __init__(
            self: "PerMachineSettings._Cast_PerMachineSettings",
            parent: "PerMachineSettings",
        ):
            self._parent = parent

        @property
        def persistent_singleton(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1597.PersistentSingleton":
            return self._parent._cast(_1597.PersistentSingleton)

        @property
        def fe_user_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_68.FEUserSettings":
            from mastapy.nodal_analysis import _68

            return self._parent._cast(_68.FEUserSettings)

        @property
        def geometry_modeller_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_160.GeometryModellerSettings":
            from mastapy.nodal_analysis.geometry_modeller_link import _160

            return self._parent._cast(_160.GeometryModellerSettings)

        @property
        def gear_material_expert_system_factor_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_596.GearMaterialExpertSystemFactorSettings":
            from mastapy.gears.materials import _596

            return self._parent._cast(_596.GearMaterialExpertSystemFactorSettings)

        @property
        def cylindrical_gear_fe_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_855.CylindricalGearFESettings":
            from mastapy.gears.ltca.cylindrical import _855

            return self._parent._cast(_855.CylindricalGearFESettings)

        @property
        def cylindrical_gear_defaults(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1012.CylindricalGearDefaults":
            from mastapy.gears.gear_designs.cylindrical import _1012

            return self._parent._cast(_1012.CylindricalGearDefaults)

        @property
        def program_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1598.ProgramSettings":
            from mastapy.utility import _1598

            return self._parent._cast(_1598.ProgramSettings)

        @property
        def pushbullet_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1599.PushbulletSettings":
            from mastapy.utility import _1599

            return self._parent._cast(_1599.PushbulletSettings)

        @property
        def measurement_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1608.MeasurementSettings":
            from mastapy.utility.units_and_measurements import _1608

            return self._parent._cast(_1608.MeasurementSettings)

        @property
        def scripting_setup(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1741.ScriptingSetup":
            from mastapy.utility.scripting import _1741

            return self._parent._cast(_1741.ScriptingSetup)

        @property
        def database_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1829.DatabaseSettings":
            from mastapy.utility.databases import _1829

            return self._parent._cast(_1829.DatabaseSettings)

        @property
        def cad_export_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1834.CADExportSettings":
            from mastapy.utility.cad_export import _1834

            return self._parent._cast(_1834.CADExportSettings)

        @property
        def skf_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_1901.SKFSettings":
            from mastapy.bearings import _1901

            return self._parent._cast(_1901.SKFSettings)

        @property
        def planet_carrier_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "_2472.PlanetCarrierSettings":
            from mastapy.system_model.part_model import _2472

            return self._parent._cast(_2472.PlanetCarrierSettings)

        @property
        def per_machine_settings(
            self: "PerMachineSettings._Cast_PerMachineSettings",
        ) -> "PerMachineSettings":
            return self._parent

        def __getattr__(self: "PerMachineSettings._Cast_PerMachineSettings", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "PerMachineSettings.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    def reset_to_defaults(self: Self):
        """Method does not return."""
        self.wrapped.ResetToDefaults()

    @property
    def cast_to(self: Self) -> "PerMachineSettings._Cast_PerMachineSettings":
        return self._Cast_PerMachineSettings(self)
