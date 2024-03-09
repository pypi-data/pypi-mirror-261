"""SQLDatabase"""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar

from mastapy._internal.type_enforcement import enforce_parameter_types
from mastapy.utility.databases import _1826
from mastapy import _0
from mastapy._internal.cast_exception import CastException
from mastapy._internal.python_net import python_net_import

_SQL_DATABASE = python_net_import("SMT.MastaAPI.Utility.Databases", "SQLDatabase")

if TYPE_CHECKING:
    from mastapy.utility.databases import _1828, _1830
    from mastapy.shafts import _25, _39
    from mastapy.nodal_analysis import _49
    from mastapy.materials import _246, _249, _268, _270, _272
    from mastapy.gears import _343
    from mastapy.gears.rating.cylindrical import _453, _469
    from mastapy.gears.materials import (
        _584,
        _586,
        _588,
        _589,
        _590,
        _592,
        _593,
        _595,
        _599,
        _600,
        _607,
    )
    from mastapy.gears.manufacturing.cylindrical import _610, _615, _626
    from mastapy.gears.manufacturing.cylindrical.cutters import _705, _711, _716, _717
    from mastapy.gears.manufacturing.bevel import _800
    from mastapy.gears.gear_set_pareto_optimiser import (
        _919,
        _921,
        _922,
        _924,
        _925,
        _926,
        _927,
        _928,
        _929,
        _930,
        _931,
        _932,
        _934,
        _935,
        _936,
        _937,
    )
    from mastapy.gears.gear_designs import _941, _943, _946
    from mastapy.gears.gear_designs.cylindrical import _1016, _1022
    from mastapy.electric_machines import _1286, _1304, _1317
    from mastapy.cycloidal import _1459, _1466
    from mastapy.bolts import _1469, _1471, _1473, _1478
    from mastapy.math_utility.optimisation import _1542, _1554
    from mastapy.bearings import _1882, _1895
    from mastapy.bearings.bearing_results.rolling import _1977
    from mastapy.system_model.optimization import _2230, _2238
    from mastapy.system_model.part_model.gears.supercharger_rotor_set import _2566


__docformat__ = "restructuredtext en"
__all__ = ("SQLDatabase",)


Self = TypeVar("Self", bound="SQLDatabase")
TKey = TypeVar("TKey", bound="_1828.DatabaseKey")
TValue = TypeVar("TValue", bound="_0.APIBase")


class SQLDatabase(_1826.Database[TKey, TValue]):
    """SQLDatabase

    This is a mastapy class.

    Generic Types:
        TKey
        TValue
    """

    TYPE = _SQL_DATABASE
    _CastSelf = TypeVar("_CastSelf", bound="_Cast_SQLDatabase")

    class _Cast_SQLDatabase:
        """Special nested class for casting SQLDatabase to subclasses."""

        def __init__(self: "SQLDatabase._Cast_SQLDatabase", parent: "SQLDatabase"):
            self._parent = parent

        @property
        def database(self: "SQLDatabase._Cast_SQLDatabase") -> "_1826.Database":
            return self._parent._cast(_1826.Database)

        @property
        def shaft_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_25.ShaftMaterialDatabase":
            from mastapy.shafts import _25

            return self._parent._cast(_25.ShaftMaterialDatabase)

        @property
        def shaft_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_39.ShaftSettingsDatabase":
            from mastapy.shafts import _39

            return self._parent._cast(_39.ShaftSettingsDatabase)

        @property
        def analysis_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_49.AnalysisSettingsDatabase":
            from mastapy.nodal_analysis import _49

            return self._parent._cast(_49.AnalysisSettingsDatabase)

        @property
        def bearing_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_246.BearingMaterialDatabase":
            from mastapy.materials import _246

            return self._parent._cast(_246.BearingMaterialDatabase)

        @property
        def component_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_249.ComponentMaterialDatabase":
            from mastapy.materials import _249

            return self._parent._cast(_249.ComponentMaterialDatabase)

        @property
        def lubrication_detail_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_268.LubricationDetailDatabase":
            from mastapy.materials import _268

            return self._parent._cast(_268.LubricationDetailDatabase)

        @property
        def material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_270.MaterialDatabase":
            from mastapy.materials import _270

            return self._parent._cast(_270.MaterialDatabase)

        @property
        def materials_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_272.MaterialsSettingsDatabase":
            from mastapy.materials import _272

            return self._parent._cast(_272.MaterialsSettingsDatabase)

        @property
        def pocketing_power_loss_coefficients_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_343.PocketingPowerLossCoefficientsDatabase":
            from mastapy.gears import _343

            return self._parent._cast(_343.PocketingPowerLossCoefficientsDatabase)

        @property
        def cylindrical_gear_design_and_rating_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_453.CylindricalGearDesignAndRatingSettingsDatabase":
            from mastapy.gears.rating.cylindrical import _453

            return self._parent._cast(
                _453.CylindricalGearDesignAndRatingSettingsDatabase
            )

        @property
        def cylindrical_plastic_gear_rating_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_469.CylindricalPlasticGearRatingSettingsDatabase":
            from mastapy.gears.rating.cylindrical import _469

            return self._parent._cast(_469.CylindricalPlasticGearRatingSettingsDatabase)

        @property
        def bevel_gear_abstract_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_584.BevelGearAbstractMaterialDatabase":
            from mastapy.gears.materials import _584

            return self._parent._cast(_584.BevelGearAbstractMaterialDatabase)

        @property
        def bevel_gear_iso_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_586.BevelGearISOMaterialDatabase":
            from mastapy.gears.materials import _586

            return self._parent._cast(_586.BevelGearISOMaterialDatabase)

        @property
        def bevel_gear_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_588.BevelGearMaterialDatabase":
            from mastapy.gears.materials import _588

            return self._parent._cast(_588.BevelGearMaterialDatabase)

        @property
        def cylindrical_gear_agma_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_589.CylindricalGearAGMAMaterialDatabase":
            from mastapy.gears.materials import _589

            return self._parent._cast(_589.CylindricalGearAGMAMaterialDatabase)

        @property
        def cylindrical_gear_iso_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_590.CylindricalGearISOMaterialDatabase":
            from mastapy.gears.materials import _590

            return self._parent._cast(_590.CylindricalGearISOMaterialDatabase)

        @property
        def cylindrical_gear_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_592.CylindricalGearMaterialDatabase":
            from mastapy.gears.materials import _592

            return self._parent._cast(_592.CylindricalGearMaterialDatabase)

        @property
        def cylindrical_gear_plastic_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_593.CylindricalGearPlasticMaterialDatabase":
            from mastapy.gears.materials import _593

            return self._parent._cast(_593.CylindricalGearPlasticMaterialDatabase)

        @property
        def gear_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_595.GearMaterialDatabase":
            from mastapy.gears.materials import _595

            return self._parent._cast(_595.GearMaterialDatabase)

        @property
        def isotr1417912001_coefficient_of_friction_constants_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_599.ISOTR1417912001CoefficientOfFrictionConstantsDatabase":
            from mastapy.gears.materials import _599

            return self._parent._cast(
                _599.ISOTR1417912001CoefficientOfFrictionConstantsDatabase
            )

        @property
        def klingelnberg_conical_gear_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_600.KlingelnbergConicalGearMaterialDatabase":
            from mastapy.gears.materials import _600

            return self._parent._cast(_600.KlingelnbergConicalGearMaterialDatabase)

        @property
        def raw_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_607.RawMaterialDatabase":
            from mastapy.gears.materials import _607

            return self._parent._cast(_607.RawMaterialDatabase)

        @property
        def cylindrical_cutter_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_610.CylindricalCutterDatabase":
            from mastapy.gears.manufacturing.cylindrical import _610

            return self._parent._cast(_610.CylindricalCutterDatabase)

        @property
        def cylindrical_hob_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_615.CylindricalHobDatabase":
            from mastapy.gears.manufacturing.cylindrical import _615

            return self._parent._cast(_615.CylindricalHobDatabase)

        @property
        def cylindrical_shaper_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_626.CylindricalShaperDatabase":
            from mastapy.gears.manufacturing.cylindrical import _626

            return self._parent._cast(_626.CylindricalShaperDatabase)

        @property
        def cylindrical_formed_wheel_grinder_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_705.CylindricalFormedWheelGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _705

            return self._parent._cast(_705.CylindricalFormedWheelGrinderDatabase)

        @property
        def cylindrical_gear_plunge_shaver_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_711.CylindricalGearPlungeShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _711

            return self._parent._cast(_711.CylindricalGearPlungeShaverDatabase)

        @property
        def cylindrical_gear_shaver_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_716.CylindricalGearShaverDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _716

            return self._parent._cast(_716.CylindricalGearShaverDatabase)

        @property
        def cylindrical_worm_grinder_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_717.CylindricalWormGrinderDatabase":
            from mastapy.gears.manufacturing.cylindrical.cutters import _717

            return self._parent._cast(_717.CylindricalWormGrinderDatabase)

        @property
        def manufacturing_machine_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_800.ManufacturingMachineDatabase":
            from mastapy.gears.manufacturing.bevel import _800

            return self._parent._cast(_800.ManufacturingMachineDatabase)

        @property
        def micro_geometry_design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_919.MicroGeometryDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _919

            return self._parent._cast(
                _919.MicroGeometryDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_921.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _921

            return self._parent._cast(
                _921.MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
            )

        @property
        def micro_geometry_gear_set_duty_cycle_design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_922.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _922

            return self._parent._cast(
                _922.MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
            )

        @property
        def pareto_conical_rating_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_924.ParetoConicalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _924

            return self._parent._cast(
                _924.ParetoConicalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_925.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _925

            return self._parent._cast(
                _925.ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_926.ParetoCylindricalGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _926

            return self._parent._cast(
                _926.ParetoCylindricalGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_cylindrical_rating_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_927.ParetoCylindricalRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _927

            return self._parent._cast(
                _927.ParetoCylindricalRatingOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_928.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _928

            return self._parent._cast(
                _928.ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_face_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_929.ParetoFaceGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _929

            return self._parent._cast(
                _929.ParetoFaceGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_face_rating_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_930.ParetoFaceRatingOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _930

            return self._parent._cast(_930.ParetoFaceRatingOptimisationStrategyDatabase)

        @property
        def pareto_hypoid_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_931.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _931

            return self._parent._cast(
                _931.ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_hypoid_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_932.ParetoHypoidGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _932

            return self._parent._cast(
                _932.ParetoHypoidGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_934.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _934

            return self._parent._cast(
                _934.ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_spiral_bevel_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_935.ParetoSpiralBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _935

            return self._parent._cast(
                _935.ParetoSpiralBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_duty_cycle_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_936.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _936

            return self._parent._cast(
                _936.ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
            )

        @property
        def pareto_straight_bevel_gear_set_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_937.ParetoStraightBevelGearSetOptimisationStrategyDatabase":
            from mastapy.gears.gear_set_pareto_optimiser import _937

            return self._parent._cast(
                _937.ParetoStraightBevelGearSetOptimisationStrategyDatabase
            )

        @property
        def bevel_hypoid_gear_design_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_941.BevelHypoidGearDesignSettingsDatabase":
            from mastapy.gears.gear_designs import _941

            return self._parent._cast(_941.BevelHypoidGearDesignSettingsDatabase)

        @property
        def bevel_hypoid_gear_rating_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_943.BevelHypoidGearRatingSettingsDatabase":
            from mastapy.gears.gear_designs import _943

            return self._parent._cast(_943.BevelHypoidGearRatingSettingsDatabase)

        @property
        def design_constraint_collection_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_946.DesignConstraintCollectionDatabase":
            from mastapy.gears.gear_designs import _946

            return self._parent._cast(_946.DesignConstraintCollectionDatabase)

        @property
        def cylindrical_gear_design_constraints_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1016.CylindricalGearDesignConstraintsDatabase":
            from mastapy.gears.gear_designs.cylindrical import _1016

            return self._parent._cast(_1016.CylindricalGearDesignConstraintsDatabase)

        @property
        def cylindrical_gear_micro_geometry_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1022.CylindricalGearMicroGeometrySettingsDatabase":
            from mastapy.gears.gear_designs.cylindrical import _1022

            return self._parent._cast(
                _1022.CylindricalGearMicroGeometrySettingsDatabase
            )

        @property
        def magnet_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1286.MagnetMaterialDatabase":
            from mastapy.electric_machines import _1286

            return self._parent._cast(_1286.MagnetMaterialDatabase)

        @property
        def stator_rotor_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1304.StatorRotorMaterialDatabase":
            from mastapy.electric_machines import _1304

            return self._parent._cast(_1304.StatorRotorMaterialDatabase)

        @property
        def winding_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1317.WindingMaterialDatabase":
            from mastapy.electric_machines import _1317

            return self._parent._cast(_1317.WindingMaterialDatabase)

        @property
        def cycloidal_disc_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1459.CycloidalDiscMaterialDatabase":
            from mastapy.cycloidal import _1459

            return self._parent._cast(_1459.CycloidalDiscMaterialDatabase)

        @property
        def ring_pins_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1466.RingPinsMaterialDatabase":
            from mastapy.cycloidal import _1466

            return self._parent._cast(_1466.RingPinsMaterialDatabase)

        @property
        def bolted_joint_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1469.BoltedJointMaterialDatabase":
            from mastapy.bolts import _1469

            return self._parent._cast(_1469.BoltedJointMaterialDatabase)

        @property
        def bolt_geometry_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1471.BoltGeometryDatabase":
            from mastapy.bolts import _1471

            return self._parent._cast(_1471.BoltGeometryDatabase)

        @property
        def bolt_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1473.BoltMaterialDatabase":
            from mastapy.bolts import _1473

            return self._parent._cast(_1473.BoltMaterialDatabase)

        @property
        def clamped_section_material_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1478.ClampedSectionMaterialDatabase":
            from mastapy.bolts import _1478

            return self._parent._cast(_1478.ClampedSectionMaterialDatabase)

        @property
        def design_space_search_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1542.DesignSpaceSearchStrategyDatabase":
            from mastapy.math_utility.optimisation import _1542

            return self._parent._cast(_1542.DesignSpaceSearchStrategyDatabase)

        @property
        def pareto_optimisation_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1554.ParetoOptimisationStrategyDatabase":
            from mastapy.math_utility.optimisation import _1554

            return self._parent._cast(_1554.ParetoOptimisationStrategyDatabase)

        @property
        def named_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1830.NamedDatabase":
            from mastapy.utility.databases import _1830

            return self._parent._cast(_1830.NamedDatabase)

        @property
        def bearing_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1882.BearingSettingsDatabase":
            from mastapy.bearings import _1882

            return self._parent._cast(_1882.BearingSettingsDatabase)

        @property
        def rolling_bearing_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1895.RollingBearingDatabase":
            from mastapy.bearings import _1895

            return self._parent._cast(_1895.RollingBearingDatabase)

        @property
        def iso14179_settings_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_1977.ISO14179SettingsDatabase":
            from mastapy.bearings.bearing_results.rolling import _1977

            return self._parent._cast(_1977.ISO14179SettingsDatabase)

        @property
        def conical_gear_optimization_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_2230.ConicalGearOptimizationStrategyDatabase":
            from mastapy.system_model.optimization import _2230

            return self._parent._cast(_2230.ConicalGearOptimizationStrategyDatabase)

        @property
        def optimization_strategy_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_2238.OptimizationStrategyDatabase":
            from mastapy.system_model.optimization import _2238

            return self._parent._cast(_2238.OptimizationStrategyDatabase)

        @property
        def supercharger_rotor_set_database(
            self: "SQLDatabase._Cast_SQLDatabase",
        ) -> "_2566.SuperchargerRotorSetDatabase":
            from mastapy.system_model.part_model.gears.supercharger_rotor_set import (
                _2566,
            )

            return self._parent._cast(_2566.SuperchargerRotorSetDatabase)

        @property
        def sql_database(self: "SQLDatabase._Cast_SQLDatabase") -> "SQLDatabase":
            return self._parent

        def __getattr__(self: "SQLDatabase._Cast_SQLDatabase", name: str):
            try:
                return self.__dict__[name]
            except KeyError:
                class_name = "".join(n.capitalize() for n in name.split("_"))
                raise CastException(
                    f'Detected an invalid cast. Cannot cast to type "{class_name}"'
                ) from None

    def __init__(self: Self, instance_to_wrap: "SQLDatabase.TYPE"):
        super().__init__(instance_to_wrap)
        self._freeze()

    @property
    def allow_network_database(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.AllowNetworkDatabase

        if temp is None:
            return False

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
    def uses_database(self: Self) -> "bool":
        """bool

        Note:
            This property is readonly.
        """
        temp = self.wrapped.UsesDatabase

        if temp is None:
            return False

        return temp

    @enforce_parameter_types
    def delete(self: Self, key: "TKey"):
        """Method does not return.

        Args:
            key (TKey)
        """
        self.wrapped.Delete(key)

    def reload(self: Self):
        """Method does not return."""
        self.wrapped.Reload()

    @enforce_parameter_types
    def save(self: Self, item: "TValue"):
        """Method does not return.

        Args:
            item (TValue)
        """
        self.wrapped.Save(item)

    @property
    def cast_to(self: Self) -> "SQLDatabase._Cast_SQLDatabase":
        return self._Cast_SQLDatabase(self)
