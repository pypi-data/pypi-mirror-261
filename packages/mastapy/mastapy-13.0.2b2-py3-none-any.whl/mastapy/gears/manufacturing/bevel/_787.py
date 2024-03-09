"""ConicalMeshMicroGeometryConfigBase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.gears.analysis import _1226
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE = python_net_import(
    "SMT.MastaAPI.Gears.Manufacturing.Bevel", "ConicalMeshMicroGeometryConfigBase"
)

if TYPE_CHECKING:
    from mastapy.gears.gear_designs.conical import _1156
    from mastapy.gears.manufacturing.bevel import _778, _785, _786
    from mastapy.gears.analysis import _1223, _1217


__docformat__ = "restructuredtext en"
__all__ = ("ConicalMeshMicroGeometryConfigBase",)


Self = TypeVar("Self", bound="ConicalMeshMicroGeometryConfigBase")


class ConicalMeshMicroGeometryConfigBase(_1226.GearMeshImplementationDetail):
    """ConicalMeshMicroGeometryConfigBase

    This is a mastapy class.
    """

    TYPE = _CONICAL_MESH_MICRO_GEOMETRY_CONFIG_BASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_ConicalMeshMicroGeometryConfigBase")

    class _Cast_ConicalMeshMicroGeometryConfigBase:
        """Special nested class for casting ConicalMeshMicroGeometryConfigBase to subclasses."""

        def __init__(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
            parent: "ConicalMeshMicroGeometryConfigBase",
        ):
            self._parent = parent

        @property
        def gear_mesh_implementation_detail(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "_1226.GearMeshImplementationDetail":
            return self._parent._cast(_1226.GearMeshImplementationDetail)

        @property
        def gear_mesh_design_analysis(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "_1223.GearMeshDesignAnalysis":
            from mastapy.gears.analysis import _1223

            return self._parent._cast(_1223.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "_1217.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearMeshAnalysis)

        @property
        def conical_mesh_manufacturing_config(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "_785.ConicalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "_786.ConicalMeshMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _786

            return self._parent._cast(_786.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
        ) -> "ConicalMeshMicroGeometryConfigBase":
            return self._parent

        def __getattr__(
            self: "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase",
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
        self: Self, instance_to_wrap: "ConicalMeshMicroGeometryConfigBase.TYPE"
    ):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def mesh(self: Self) -> "_1156.ConicalGearMeshDesign":
        """mastapy.gears.gear_designs.conical.ConicalGearMeshDesign

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mesh

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def wheel_config(self: Self) -> "_778.ConicalGearMicroGeometryConfigBase":
        """mastapy.gears.manufacturing.bevel.ConicalGearMicroGeometryConfigBase

        Note:
            This property is readonly.
        """
        temp = self.wrapped.WheelConfig

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "ConicalMeshMicroGeometryConfigBase._Cast_ConicalMeshMicroGeometryConfigBase":
        return self._Cast_ConicalMeshMicroGeometryConfigBase(self)
