import rustworkx as rx
from ibis.backends.base import BaseBackend as BaseBackend
from rich.text import Text as Text
from textual.app import ComposeResult as ComposeResult
from vinyl.lib.utils.graphics import TurntableTextualApp as TurntableTextualApp

class VinylGraph(rx.PyDiGraph): ...
