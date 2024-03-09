"""__init__.py"""

import sys
from typing import TYPE_CHECKING

from lazy_imports import LazyImporter


if TYPE_CHECKING:
    from ._1090 import FinishStockSpecification
    from ._1091 import FinishStockType
    from ._1092 import NominalValueSpecification
    from ._1093 import NoValueSpecification
else:
    import_structure = {
        "_1090": ["FinishStockSpecification"],
        "_1091": ["FinishStockType"],
        "_1092": ["NominalValueSpecification"],
        "_1093": ["NoValueSpecification"],
    }

    sys.modules[__name__] = LazyImporter(
        __name__,
        globals()["__file__"],
        import_structure,
    )

__all__ = (
    "FinishStockSpecification",
    "FinishStockType",
    "NominalValueSpecification",
    "NoValueSpecification",
)
