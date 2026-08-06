# xgen_contextifier/chunking/strategies/__init__.py
"""
Chunking Strategies

Each strategy implements one approach to splitting text into chunks.
The TextChunker selects and applies the appropriate strategy based
on the content characteristics and configuration.
"""

from xgen_contextifier.chunking.strategies.base import BaseChunkingStrategy
from xgen_contextifier.chunking.strategies.page_strategy import PageChunkingStrategy
from xgen_contextifier.chunking.strategies.table_strategy import TableChunkingStrategy
from xgen_contextifier.chunking.strategies.protected_strategy import (
    ProtectedChunkingStrategy,
)
from xgen_contextifier.chunking.strategies.plain_strategy import PlainChunkingStrategy

__all__ = [
    "BaseChunkingStrategy",
    "PageChunkingStrategy",
    "TableChunkingStrategy",
    "ProtectedChunkingStrategy",
    "PlainChunkingStrategy",
]
