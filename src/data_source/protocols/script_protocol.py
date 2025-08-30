from typing import Protocol, Any


class ScriptProtocol(Protocol):
    async def __call__(self, *args, **kwargs) -> Any : ...
