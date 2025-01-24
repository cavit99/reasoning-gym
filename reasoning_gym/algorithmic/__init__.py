"""
Algorithmic tasks for training reasoning capabilities:
- Text processing
- Counting
- Sorting
- Pattern matching
"""

from .base_conversion import BaseConversionConfig, BaseConversionDataset
from .letter_counting import LetterCountingConfig, LetterCountingDataset
from .number_filtering import NumberFilteringConfig, NumberFilteringDataset
from .number_sorting import NumberSortingConfig, NumberSortingDataset
from .word_reversal import WordReversalConfig, WordReversalDataset

__all__ = [
    "BaseConversionConfig",
    "BaseConversionDataset",
    "LetterCountingConfig",
    "LetterCountingDataset",
    "NumberFilteringConfig",
    "NumberFilteringDataset",
    "NumberSortingConfig",
    "NumberSortingDataset",
    "WordReversalConfig",
    "WordReversalDataset",
]
