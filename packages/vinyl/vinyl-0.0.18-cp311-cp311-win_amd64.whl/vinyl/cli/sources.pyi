from _typeshed import Incomplete
from vinyl.cli.events import Event as Event, EventLogger as EventLogger
from vinyl.lib.connect import DatabaseFileConnector as DatabaseFileConnector, SourceInfo as SourceInfo
from vinyl.lib.project import Project as Project

console: Incomplete
sources_cli: Incomplete

def list_sources(tables: bool = False):
    """Caches sources to a local directory (default: .turntable/sources)"""
def table_to_python_class(table_name) -> str: ...
def source_to_class_string(source: SourceInfo, saved_attributes: dict[str, str], generate_twin: bool = False, root_path: str | None = None, sample_size: int = 1000) -> str: ...
def generate_sources(twin: bool = ..., resources: list[str] = ...):
    """Generates schema files for sources"""
