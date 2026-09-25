"""Minimal Book API documentation sync package."""

from .contracts import BookContract
from .documentation_sync import sync_documentation

__all__ = ["BookContract", "sync_documentation"]
