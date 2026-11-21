"""Question content registry. Importing the chapter modules registers their templates."""
from . import ch09, ch09b, ch09w, ch10, ch10b, ch11, ch11b, ch12, ch12b, ch13, ch13b, ch13w  # noqa: F401  (registration side effects)
from .base import TEMPLATES, Question, Template

__all__ = ["TEMPLATES", "Question", "Template"]
