"""GearMeshImplementationDetail"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy.gears.analysis import _1223
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_MESH_IMPLEMENTATION_DETAIL = python_net_import(
    "SMT.MastaAPI.Gears.Analysis", "GearMeshImplementationDetail"
)

if TYPE_CHECKING:
    from mastapy.gears.manufacturing.cylindrical import _622
    from mastapy.gears.manufacturing.bevel import _785, _786, _787
    from mastapy.gears.gear_designs.face import _993
    from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1099
    from mastapy.gears.fe_model import _1199
    from mastapy.gears.fe_model.cylindrical import _1203
    from mastapy.gears.fe_model.conical import _1206
    from mastapy.gears.analysis import _1217


__docformat__ = "restructuredtext en"
__all__ = ("GearMeshImplementationDetail",)


Self = TypeVar("Self", bound="GearMeshImplementationDetail")


class GearMeshImplementationDetail(_1223.GearMeshDesignAnalysis):
    """GearMeshImplementationDetail

    This is a mastapy class.
    """

    TYPE = _GEAR_MESH_IMPLEMENTATION_DETAIL
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearMeshImplementationDetail")

    class _Cast_GearMeshImplementationDetail:
        """Special nested class for casting GearMeshImplementationDetail to subclasses."""

        def __init__(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
            parent: "GearMeshImplementationDetail",
        ):
            self._parent = parent

        @property
        def gear_mesh_design_analysis(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1223.GearMeshDesignAnalysis":
            return self._parent._cast(_1223.GearMeshDesignAnalysis)

        @property
        def abstract_gear_mesh_analysis(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1217.AbstractGearMeshAnalysis":
            from mastapy.gears.analysis import _1217

            return self._parent._cast(_1217.AbstractGearMeshAnalysis)

        @property
        def cylindrical_mesh_manufacturing_config(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_622.CylindricalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.cylindrical import _622

            return self._parent._cast(_622.CylindricalMeshManufacturingConfig)

        @property
        def conical_mesh_manufacturing_config(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_785.ConicalMeshManufacturingConfig":
            from mastapy.gears.manufacturing.bevel import _785

            return self._parent._cast(_785.ConicalMeshManufacturingConfig)

        @property
        def conical_mesh_micro_geometry_config(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_786.ConicalMeshMicroGeometryConfig":
            from mastapy.gears.manufacturing.bevel import _786

            return self._parent._cast(_786.ConicalMeshMicroGeometryConfig)

        @property
        def conical_mesh_micro_geometry_config_base(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_787.ConicalMeshMicroGeometryConfigBase":
            from mastapy.gears.manufacturing.bevel import _787

            return self._parent._cast(_787.ConicalMeshMicroGeometryConfigBase)

        @property
        def face_gear_mesh_micro_geometry(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_993.FaceGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.face import _993

            return self._parent._cast(_993.FaceGearMeshMicroGeometry)

        @property
        def cylindrical_gear_mesh_micro_geometry(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1099.CylindricalGearMeshMicroGeometry":
            from mastapy.gears.gear_designs.cylindrical.micro_geometry import _1099

            return self._parent._cast(_1099.CylindricalGearMeshMicroGeometry)

        @property
        def gear_mesh_fe_model(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1199.GearMeshFEModel":
            from mastapy.gears.fe_model import _1199

            return self._parent._cast(_1199.GearMeshFEModel)

        @property
        def cylindrical_gear_mesh_fe_model(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1203.CylindricalGearMeshFEModel":
            from mastapy.gears.fe_model.cylindrical import _1203

            return self._parent._cast(_1203.CylindricalGearMeshFEModel)

        @property
        def conical_mesh_fe_model(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "_1206.ConicalMeshFEModel":
            from mastapy.gears.fe_model.conical import _1206

            return self._parent._cast(_1206.ConicalMeshFEModel)

        @property
        def gear_mesh_implementation_detail(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
        ) -> "GearMeshImplementationDetail":
            return self._parent

        def __getattr__(
            self: "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail",
            name: str,
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearMeshImplementationDetail.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def cast_to(
        self: Self,
    ) -> "GearMeshImplementationDetail._Cast_GearMeshImplementationDetail":
        return self._Cast_GearMeshImplementationDetail(self)
