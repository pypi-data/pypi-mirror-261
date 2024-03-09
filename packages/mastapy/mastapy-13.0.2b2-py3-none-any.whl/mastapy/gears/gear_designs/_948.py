"""GearDesign"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy._internal import constructor
from mastapy.gears.gear_designs import _949
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_GEAR_DESIGN = python_net_import("SMT.MastaAPI.Gears.GearDesigns", "GearDesign")

if TYPE_CHECKING:
    from mastapy.gears.fe_model import _1198
    from mastapy.gears.gear_designs.zerol_bevel import _953
    from mastapy.gears.gear_designs.worm import _957, _958, _961
    from mastapy.gears.gear_designs.straight_bevel import _962
    from mastapy.gears.gear_designs.straight_bevel_diff import _966
    from mastapy.gears.gear_designs.spiral_bevel import _970
    from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _974
    from mastapy.gears.gear_designs.klingelnberg_hypoid import _978
    from mastapy.gears.gear_designs.klingelnberg_conical import _982
    from mastapy.gears.gear_designs.hypoid import _986
    from mastapy.gears.gear_designs.face import _990, _995, _998
    from mastapy.gears.gear_designs.cylindrical import _1013, _1043
    from mastapy.gears.gear_designs.conical import _1155
    from mastapy.gears.gear_designs.concept import _1177
    from mastapy.gears.gear_designs.bevel import _1181
    from mastapy.gears.gear_designs.agma_gleason_conical import _1194


__docformat__ = "restructuredtext en"
__all__ = ("GearDesign",)


Self = TypeVar("Self", bound="GearDesign")


class GearDesign(_949.GearDesignComponent):
    """GearDesign

    This is a mastapy class.
    """

    TYPE = _GEAR_DESIGN
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_GearDesign")

    class _Cast_GearDesign:
        """Special nested class for casting GearDesign to subclasses."""

        def __init__(self: "GearDesign._Cast_GearDesign", parent: "GearDesign"):
            self._parent = parent

        @property
        def gear_design_component(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_949.GearDesignComponent":
            return self._parent._cast(_949.GearDesignComponent)

        @property
        def zerol_bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_953.ZerolBevelGearDesign":
            from mastapy.gears.gear_designs.zerol_bevel import _953

            return self._parent._cast(_953.ZerolBevelGearDesign)

        @property
        def worm_design(self: "GearDesign._Cast_GearDesign") -> "_957.WormDesign":
            from mastapy.gears.gear_designs.worm import _957

            return self._parent._cast(_957.WormDesign)

        @property
        def worm_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_958.WormGearDesign":
            from mastapy.gears.gear_designs.worm import _958

            return self._parent._cast(_958.WormGearDesign)

        @property
        def worm_wheel_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_961.WormWheelDesign":
            from mastapy.gears.gear_designs.worm import _961

            return self._parent._cast(_961.WormWheelDesign)

        @property
        def straight_bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_962.StraightBevelGearDesign":
            from mastapy.gears.gear_designs.straight_bevel import _962

            return self._parent._cast(_962.StraightBevelGearDesign)

        @property
        def straight_bevel_diff_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_966.StraightBevelDiffGearDesign":
            from mastapy.gears.gear_designs.straight_bevel_diff import _966

            return self._parent._cast(_966.StraightBevelDiffGearDesign)

        @property
        def spiral_bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_970.SpiralBevelGearDesign":
            from mastapy.gears.gear_designs.spiral_bevel import _970

            return self._parent._cast(_970.SpiralBevelGearDesign)

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_974.KlingelnbergCycloPalloidSpiralBevelGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_spiral_bevel import _974

            return self._parent._cast(
                _974.KlingelnbergCycloPalloidSpiralBevelGearDesign
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_978.KlingelnbergCycloPalloidHypoidGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_hypoid import _978

            return self._parent._cast(_978.KlingelnbergCycloPalloidHypoidGearDesign)

        @property
        def klingelnberg_conical_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_982.KlingelnbergConicalGearDesign":
            from mastapy.gears.gear_designs.klingelnberg_conical import _982

            return self._parent._cast(_982.KlingelnbergConicalGearDesign)

        @property
        def hypoid_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_986.HypoidGearDesign":
            from mastapy.gears.gear_designs.hypoid import _986

            return self._parent._cast(_986.HypoidGearDesign)

        @property
        def face_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_990.FaceGearDesign":
            from mastapy.gears.gear_designs.face import _990

            return self._parent._cast(_990.FaceGearDesign)

        @property
        def face_gear_pinion_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_995.FaceGearPinionDesign":
            from mastapy.gears.gear_designs.face import _995

            return self._parent._cast(_995.FaceGearPinionDesign)

        @property
        def face_gear_wheel_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_998.FaceGearWheelDesign":
            from mastapy.gears.gear_designs.face import _998

            return self._parent._cast(_998.FaceGearWheelDesign)

        @property
        def cylindrical_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1013.CylindricalGearDesign":
            from mastapy.gears.gear_designs.cylindrical import _1013

            return self._parent._cast(_1013.CylindricalGearDesign)

        @property
        def cylindrical_planet_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1043.CylindricalPlanetGearDesign":
            from mastapy.gears.gear_designs.cylindrical import _1043

            return self._parent._cast(_1043.CylindricalPlanetGearDesign)

        @property
        def conical_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1155.ConicalGearDesign":
            from mastapy.gears.gear_designs.conical import _1155

            return self._parent._cast(_1155.ConicalGearDesign)

        @property
        def concept_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1177.ConceptGearDesign":
            from mastapy.gears.gear_designs.concept import _1177

            return self._parent._cast(_1177.ConceptGearDesign)

        @property
        def bevel_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1181.BevelGearDesign":
            from mastapy.gears.gear_designs.bevel import _1181

            return self._parent._cast(_1181.BevelGearDesign)

        @property
        def agma_gleason_conical_gear_design(
            self: "GearDesign._Cast_GearDesign",
        ) -> "_1194.AGMAGleasonConicalGearDesign":
            from mastapy.gears.gear_designs.agma_gleason_conical import _1194

            return self._parent._cast(_1194.AGMAGleasonConicalGearDesign)

        @property
        def gear_design(self: "GearDesign._Cast_GearDesign") -> "GearDesign":
            return self._parent

        def __getattr__(self: "GearDesign._Cast_GearDesign", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "GearDesign.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def absolute_shaft_inner_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AbsoluteShaftInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def face_width(self: Self) -> "float":
        """float"""
        temp = self.wrapped.FaceWidth

        if temp is None:
            return 0.0

        return temp

    @face_width.setter
    @enforce_parameter_types
    def face_width(self: Self, value: "float"):
        self.wrapped.FaceWidth = float(value) if value is not None else 0.0

    @property
    def mass(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Mass

        if temp is None:
            return 0.0

        return temp

    @property
    def name(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.Name

        if temp is None:
            return ""

        return temp

    @property
    def names_of_meshing_gears(self: Self) -> "str":
        """str

        Note:
            This property is readonly.
        """
        temp = self.wrapped.NamesOfMeshingGears

        if temp is None:
            return ""

        return temp

    @property
    def number_of_teeth(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeeth

        if temp is None:
            return 0

        return temp

    @number_of_teeth.setter
    @enforce_parameter_types
    def number_of_teeth(self: Self, value: "int"):
        self.wrapped.NumberOfTeeth = int(value) if value is not None else 0

    @property
    def number_of_teeth_maintaining_ratio(self: Self) -> "int":
        """int"""
        temp = self.wrapped.NumberOfTeethMaintainingRatio

        if temp is None:
            return 0

        return temp

    @number_of_teeth_maintaining_ratio.setter
    @enforce_parameter_types
    def number_of_teeth_maintaining_ratio(self: Self, value: "int"):
        self.wrapped.NumberOfTeethMaintainingRatio = (
            int(value) if value is not None else 0
        )

    @property
    def shaft_inner_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftInnerDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def shaft_outer_diameter(self: Self) -> "float":
        """float

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ShaftOuterDiameter

        if temp is None:
            return 0.0

        return temp

    @property
    def tifffe_model(self: Self) -> "_1198.GearFEModel":
        """mastapy.gears.fe_model.GearFEModel

        Note:
            This property is readonly.
        """
        temp = self.wrapped.TIFFFEModel

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(self: Self) -> "GearDesign._Cast_GearDesign":
        return self._Cast_GearDesign(self)
