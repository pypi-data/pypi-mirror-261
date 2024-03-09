"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._941 import BevelHypoidGearDesignSettingsDatabase
    from ._942 import BevelHypoidGearDesignSettingsItem
    from ._943 import BevelHypoidGearRatingSettingsDatabase
    from ._944 import BevelHypoidGearRatingSettingsItem
    from ._945 import DesignConstraint
    from ._946 import DesignConstraintCollectionDatabase
    from ._947 import DesignConstraintsCollection
    from ._948 import GearDesign
    from ._949 import GearDesignComponent
    from ._950 import GearMeshDesign
    from ._951 import GearSetDesign
    from ._952 import SelectedDesignConstraintsCollection
else:
    import_structure = {
        "_941": ["BevelHypoidGearDesignSettingsDatabase"],
        "_942": ["BevelHypoidGearDesignSettingsItem"],
        "_943": ["BevelHypoidGearRatingSettingsDatabase"],
        "_944": ["BevelHypoidGearRatingSettingsItem"],
        "_945": ["DesignConstraint"],
        "_946": ["DesignConstraintCollectionDatabase"],
        "_947": ["DesignConstraintsCollection"],
        "_948": ["GearDesign"],
        "_949": ["GearDesignComponent"],
        "_950": ["GearMeshDesign"],
        "_951": ["GearSetDesign"],
        "_952": ["SelectedDesignConstraintsCollection"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "BevelHypoidGearDesignSettingsDatabase",
    "BevelHypoidGearDesignSettingsItem",
    "BevelHypoidGearRatingSettingsDatabase",
    "BevelHypoidGearRatingSettingsItem",
    "DesignConstraint",
    "DesignConstraintCollectionDatabase",
    "DesignConstraintsCollection",
    "GearDesign",
    "GearDesignComponent",
    "GearMeshDesign",
    "GearSetDesign",
    "SelectedDesignConstraintsCollection",
)
