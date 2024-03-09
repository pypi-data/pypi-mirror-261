"""AbstractAssemblyLoadCase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal import constructor
from mastapy.system_model.analyses_and_results.static_loads import _6931
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_ABSTRACT_ASSEMBLY_LOAD_CASE = python_net_import(
    "SMT.MastaAPI.SystemModel.AnalysesAndResults.StaticLoads",
    "AbstractAssemblyLoadCase",
)

if TYPE_CHECKING:
    from mastapy.system_model.part_model import _2436
    from mastapy.system_model.analyses_and_results.static_loads import (
        _6818,
        _6821,
        _6824,
        _6827,
        _6832,
        _6833,
        _6837,
        _6843,
        _6846,
        _6851,
        _6856,
        _6858,
        _6860,
        _6868,
        _6889,
        _6891,
        _6898,
        _6910,
        _6917,
        _6920,
        _6923,
        _6934,
        _6936,
        _6948,
        _6951,
        _6955,
        _6958,
        _6961,
        _6964,
        _6967,
        _6971,
        _6976,
        _6987,
        _6990,
    )
    from mastapy.system_model.analyses_and_results import _2659, _2655, _2653


__docformat__ = "restructuredtext en"
__all__ = ("AbstractAssemblyLoadCase",)


Self = TypeVar("Self", bound="AbstractAssemblyLoadCase")


class AbstractAssemblyLoadCase(_6931.PartLoadCase):
    """AbstractAssemblyLoadCase

    This is a mastapy class.
    """

    TYPE = _ABSTRACT_ASSEMBLY_LOAD_CASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_AbstractAssemblyLoadCase")

    class _Cast_AbstractAssemblyLoadCase:
        """Special nested class for casting AbstractAssemblyLoadCase to subclasses."""

        def __init__(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
            parent: "AbstractAssemblyLoadCase",
        ):
            self._parent = parent

        @property
        def part_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6931.PartLoadCase":
            return self._parent._cast(_6931.PartLoadCase)

        @property
        def part_analysis(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_2659.PartAnalysis":
            from mastapy.system_model.analyses_and_results import _2659

            return self._parent._cast(_2659.PartAnalysis)

        @property
        def design_entity_single_context_analysis(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_2655.DesignEntitySingleContextAnalysis":
            from mastapy.system_model.analyses_and_results import _2655

            return self._parent._cast(_2655.DesignEntitySingleContextAnalysis)

        @property
        def design_entity_analysis(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_2653.DesignEntityAnalysis":
            from mastapy.system_model.analyses_and_results import _2653

            return self._parent._cast(_2653.DesignEntityAnalysis)

        @property
        def agma_gleason_conical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6818.AGMAGleasonConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6818

            return self._parent._cast(_6818.AGMAGleasonConicalGearSetLoadCase)

        @property
        def assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6821.AssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6821

            return self._parent._cast(_6821.AssemblyLoadCase)

        @property
        def belt_drive_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6824.BeltDriveLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6824

            return self._parent._cast(_6824.BeltDriveLoadCase)

        @property
        def bevel_differential_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6827.BevelDifferentialGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6827

            return self._parent._cast(_6827.BevelDifferentialGearSetLoadCase)

        @property
        def bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6832.BevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6832

            return self._parent._cast(_6832.BevelGearSetLoadCase)

        @property
        def bolted_joint_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6833.BoltedJointLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6833

            return self._parent._cast(_6833.BoltedJointLoadCase)

        @property
        def clutch_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6837.ClutchLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6837

            return self._parent._cast(_6837.ClutchLoadCase)

        @property
        def concept_coupling_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6843.ConceptCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6843

            return self._parent._cast(_6843.ConceptCouplingLoadCase)

        @property
        def concept_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6846.ConceptGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6846

            return self._parent._cast(_6846.ConceptGearSetLoadCase)

        @property
        def conical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6851.ConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6851

            return self._parent._cast(_6851.ConicalGearSetLoadCase)

        @property
        def coupling_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6856.CouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6856

            return self._parent._cast(_6856.CouplingLoadCase)

        @property
        def cvt_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6858.CVTLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6858

            return self._parent._cast(_6858.CVTLoadCase)

        @property
        def cycloidal_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6860.CycloidalAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6860

            return self._parent._cast(_6860.CycloidalAssemblyLoadCase)

        @property
        def cylindrical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6868.CylindricalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6868

            return self._parent._cast(_6868.CylindricalGearSetLoadCase)

        @property
        def face_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6889.FaceGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6889

            return self._parent._cast(_6889.FaceGearSetLoadCase)

        @property
        def flexible_pin_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6891.FlexiblePinAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6891

            return self._parent._cast(_6891.FlexiblePinAssemblyLoadCase)

        @property
        def gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6898.GearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6898

            return self._parent._cast(_6898.GearSetLoadCase)

        @property
        def hypoid_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6910.HypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6910

            return self._parent._cast(_6910.HypoidGearSetLoadCase)

        @property
        def klingelnberg_cyclo_palloid_conical_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6917.KlingelnbergCycloPalloidConicalGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6917

            return self._parent._cast(
                _6917.KlingelnbergCycloPalloidConicalGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_hypoid_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6920.KlingelnbergCycloPalloidHypoidGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6920

            return self._parent._cast(
                _6920.KlingelnbergCycloPalloidHypoidGearSetLoadCase
            )

        @property
        def klingelnberg_cyclo_palloid_spiral_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6923.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6923

            return self._parent._cast(
                _6923.KlingelnbergCycloPalloidSpiralBevelGearSetLoadCase
            )

        @property
        def part_to_part_shear_coupling_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6934.PartToPartShearCouplingLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6934

            return self._parent._cast(_6934.PartToPartShearCouplingLoadCase)

        @property
        def planetary_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6936.PlanetaryGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6936

            return self._parent._cast(_6936.PlanetaryGearSetLoadCase)

        @property
        def rolling_ring_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6948.RollingRingAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6948

            return self._parent._cast(_6948.RollingRingAssemblyLoadCase)

        @property
        def root_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6951.RootAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6951

            return self._parent._cast(_6951.RootAssemblyLoadCase)

        @property
        def specialised_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6955.SpecialisedAssemblyLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6955

            return self._parent._cast(_6955.SpecialisedAssemblyLoadCase)

        @property
        def spiral_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6958.SpiralBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6958

            return self._parent._cast(_6958.SpiralBevelGearSetLoadCase)

        @property
        def spring_damper_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6961.SpringDamperLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6961

            return self._parent._cast(_6961.SpringDamperLoadCase)

        @property
        def straight_bevel_diff_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6964.StraightBevelDiffGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6964

            return self._parent._cast(_6964.StraightBevelDiffGearSetLoadCase)

        @property
        def straight_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6967.StraightBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6967

            return self._parent._cast(_6967.StraightBevelGearSetLoadCase)

        @property
        def synchroniser_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6971.SynchroniserLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6971

            return self._parent._cast(_6971.SynchroniserLoadCase)

        @property
        def torque_converter_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6976.TorqueConverterLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6976

            return self._parent._cast(_6976.TorqueConverterLoadCase)

        @property
        def worm_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6987.WormGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6987

            return self._parent._cast(_6987.WormGearSetLoadCase)

        @property
        def zerol_bevel_gear_set_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "_6990.ZerolBevelGearSetLoadCase":
            from mastapy.system_model.analyses_and_results.static_loads import _6990

            return self._parent._cast(_6990.ZerolBevelGearSetLoadCase)

        @property
        def abstract_assembly_load_case(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase",
        ) -> "AbstractAssemblyLoadCase":
            return self._parent

        def __getattr__(
            self: "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase", name: str
        ):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "AbstractAssemblyLoadCase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def component_design(self: Self) -> "_2436.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.ComponentDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def assembly_design(self: Self) -> "_2436.AbstractAssembly":
        """mastapy.system_model.part_model.AbstractAssembly

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AssemblyDesign

        if temp is None:
            return None

        type_ = temp.GetType()
        return constructor.new(type_.Namespace, type_.Name)(temp)

    @property
    def cast_to(
        self: Self,
    ) -> "AbstractAssemblyLoadCase._Cast_AbstractAssemblyLoadCase":
        return self._Cast_AbstractAssemblyLoadCase(self)
