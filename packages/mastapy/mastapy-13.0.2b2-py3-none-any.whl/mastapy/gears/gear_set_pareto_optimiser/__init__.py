"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._902 import BarForPareto
    from ._903 import CandidateDisplayChoice
    from ._904 import ChartInfoBase
    from ._905 import CylindricalGearSetParetoOptimiser
    from ._906 import DesignSpaceSearchBase
    from ._907 import DesignSpaceSearchCandidateBase
    from ._908 import FaceGearSetParetoOptimiser
    from ._909 import GearNameMapper
    from ._910 import GearNamePicker
    from ._911 import GearSetOptimiserCandidate
    from ._912 import GearSetParetoOptimiser
    from ._913 import HypoidGearSetParetoOptimiser
    from ._914 import InputSliderForPareto
    from ._915 import LargerOrSmaller
    from ._916 import MicroGeometryDesignSpaceSearch
    from ._917 import MicroGeometryDesignSpaceSearchCandidate
    from ._918 import MicroGeometryDesignSpaceSearchChartInformation
    from ._919 import MicroGeometryDesignSpaceSearchStrategyDatabase
    from ._920 import MicroGeometryGearSetDesignSpaceSearch
    from ._921 import MicroGeometryGearSetDesignSpaceSearchStrategyDatabase
    from ._922 import MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase
    from ._923 import OptimisationTarget
    from ._924 import ParetoConicalRatingOptimisationStrategyDatabase
    from ._925 import ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase
    from ._926 import ParetoCylindricalGearSetOptimisationStrategyDatabase
    from ._927 import ParetoCylindricalRatingOptimisationStrategyDatabase
    from ._928 import ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase
    from ._929 import ParetoFaceGearSetOptimisationStrategyDatabase
    from ._930 import ParetoFaceRatingOptimisationStrategyDatabase
    from ._931 import ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase
    from ._932 import ParetoHypoidGearSetOptimisationStrategyDatabase
    from ._933 import ParetoOptimiserChartInformation
    from ._934 import ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._935 import ParetoSpiralBevelGearSetOptimisationStrategyDatabase
    from ._936 import ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase
    from ._937 import ParetoStraightBevelGearSetOptimisationStrategyDatabase
    from ._938 import ReasonsForInvalidDesigns
    from ._939 import SpiralBevelGearSetParetoOptimiser
    from ._940 import StraightBevelGearSetParetoOptimiser
else:
    import_structure = {
        "_902": ["BarForPareto"],
        "_903": ["CandidateDisplayChoice"],
        "_904": ["ChartInfoBase"],
        "_905": ["CylindricalGearSetParetoOptimiser"],
        "_906": ["DesignSpaceSearchBase"],
        "_907": ["DesignSpaceSearchCandidateBase"],
        "_908": ["FaceGearSetParetoOptimiser"],
        "_909": ["GearNameMapper"],
        "_910": ["GearNamePicker"],
        "_911": ["GearSetOptimiserCandidate"],
        "_912": ["GearSetParetoOptimiser"],
        "_913": ["HypoidGearSetParetoOptimiser"],
        "_914": ["InputSliderForPareto"],
        "_915": ["LargerOrSmaller"],
        "_916": ["MicroGeometryDesignSpaceSearch"],
        "_917": ["MicroGeometryDesignSpaceSearchCandidate"],
        "_918": ["MicroGeometryDesignSpaceSearchChartInformation"],
        "_919": ["MicroGeometryDesignSpaceSearchStrategyDatabase"],
        "_920": ["MicroGeometryGearSetDesignSpaceSearch"],
        "_921": ["MicroGeometryGearSetDesignSpaceSearchStrategyDatabase"],
        "_922": ["MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase"],
        "_923": ["OptimisationTarget"],
        "_924": ["ParetoConicalRatingOptimisationStrategyDatabase"],
        "_925": ["ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase"],
        "_926": ["ParetoCylindricalGearSetOptimisationStrategyDatabase"],
        "_927": ["ParetoCylindricalRatingOptimisationStrategyDatabase"],
        "_928": ["ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase"],
        "_929": ["ParetoFaceGearSetOptimisationStrategyDatabase"],
        "_930": ["ParetoFaceRatingOptimisationStrategyDatabase"],
        "_931": ["ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase"],
        "_932": ["ParetoHypoidGearSetOptimisationStrategyDatabase"],
        "_933": ["ParetoOptimiserChartInformation"],
        "_934": ["ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase"],
        "_935": ["ParetoSpiralBevelGearSetOptimisationStrategyDatabase"],
        "_936": ["ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase"],
        "_937": ["ParetoStraightBevelGearSetOptimisationStrategyDatabase"],
        "_938": ["ReasonsForInvalidDesigns"],
        "_939": ["SpiralBevelGearSetParetoOptimiser"],
        "_940": ["StraightBevelGearSetParetoOptimiser"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BarForPareto",
    "CandidateDisplayChoice",
    "ChartInfoBase",
    "CylindricalGearSetParetoOptimiser",
    "DesignSpaceSearchBase",
    "DesignSpaceSearchCandidateBase",
    "FaceGearSetParetoOptimiser",
    "GearNameMapper",
    "GearNamePicker",
    "GearSetOptimiserCandidate",
    "GearSetParetoOptimiser",
    "HypoidGearSetParetoOptimiser",
    "InputSliderForPareto",
    "LargerOrSmaller",
    "MicroGeometryDesignSpaceSearch",
    "MicroGeometryDesignSpaceSearchCandidate",
    "MicroGeometryDesignSpaceSearchChartInformation",
    "MicroGeometryDesignSpaceSearchStrategyDatabase",
    "MicroGeometryGearSetDesignSpaceSearch",
    "MicroGeometryGearSetDesignSpaceSearchStrategyDatabase",
    "MicroGeometryGearSetDutyCycleDesignSpaceSearchStrategyDatabase",
    "OptimisationTarget",
    "ParetoConicalRatingOptimisationStrategyDatabase",
    "ParetoCylindricalGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoCylindricalGearSetOptimisationStrategyDatabase",
    "ParetoCylindricalRatingOptimisationStrategyDatabase",
    "ParetoFaceGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoFaceGearSetOptimisationStrategyDatabase",
    "ParetoFaceRatingOptimisationStrategyDatabase",
    "ParetoHypoidGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoHypoidGearSetOptimisationStrategyDatabase",
    "ParetoOptimiserChartInformation",
    "ParetoSpiralBevelGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoSpiralBevelGearSetOptimisationStrategyDatabase",
    "ParetoStraightBevelGearSetDutyCycleOptimisationStrategyDatabase",
    "ParetoStraightBevelGearSetOptimisationStrategyDatabase",
    "ReasonsForInvalidDesigns",
    "SpiralBevelGearSetParetoOptimiser",
    "StraightBevelGearSetParetoOptimiser",
)
