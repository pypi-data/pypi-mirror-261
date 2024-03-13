from __future__ import annotations

from lsprotocol.types import INITIALIZE
from lsprotocol.types import InitializeParams
from lsprotocol.types import MessageType
from pygls.server import LanguageServer

from django_lsp import __version__

server = LanguageServer(
    name="django",
    version=__version__,
)


@server.command(INITIALIZE)
def initialize(params: InitializeParams) -> None:
    server.show_message_log("django-lsp initialized", MessageType.Info)
    server.show_message("django-lsp initialized", MessageType.Info)


def start() -> None:
    server.start_io()


if __name__ == "__main__":
    start()
