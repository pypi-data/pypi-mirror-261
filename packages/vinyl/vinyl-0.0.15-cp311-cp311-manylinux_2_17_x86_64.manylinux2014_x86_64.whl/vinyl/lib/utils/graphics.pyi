from ibis import Schema as Schema
from textual.app import App
from typing import Any

def rich_print(obj: Any): ...

class TurntableTextualApp(App):
    def action_reload(self) -> None: ...
