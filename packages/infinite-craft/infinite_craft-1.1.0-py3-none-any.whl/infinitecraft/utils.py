import os
import json
import inspect
import uvicorn
from typing import (
    Callable, Coroutine,
    Any, NoReturn,
    Mapping
)
from fastapi import FastAPI

from .      import errors
from .types import *


def session_not_started(*args: Unused, **kwargs: Unused) -> NoReturn:
    raise RuntimeError("Session has not been started")


def check_file(path: str) -> bool:
    """Check if a file exists or not"""
    path = os.path.abspath(path)
    
    if os.path.exists(path):
        if os.path.isfile(path):
            if not os.access(path, os.W_OK):
                raise errors.NotWritableError(f"path '{path}' is not writable")
            
            return True
        
        else:
            raise errors.NotFileError(f"path '{path}' is not a file")
    
    dir = os.path.dirname(path)
    if not os.access(dir, os.R_OK):
        return False
    
    if os.path.isdir(dir):
        os.makedirs(dir, exist_ok=True)
    
    else:
        raise errors.NotDirectoryError(f"path '{dir}' is not a directory")
    
    return False
    

def dump_json(
    file: str,
    data: Any,
    encoding: str = "utf-8",
    indent: int = 2,
    open_args: Mapping[str, Any] = {},
    dump_args: Mapping[str, Any] = {}
) -> None:
    """Dump JSON into a file

    ## Arguments:
        `file` (`str`): Path to file
        `data` (`Any`): JSON data to be dumped
        `encoding` (`str`, optional): Encoding of file to dump the JSON data in. Defaults to `"utf-8"`.
        `indent` (`int`, optional): Number of spaces to use as indents. Defaults to `2`.
        `open_kwargs` (`Mapping[str, Any]`, optional): Keyword arguments to use for `open()`. Defaults to `{}`.
        `dump_kwargs` (`Mapping[str, Any]`, optional): Keyword arguments to use for `json.dump()`. Defaults to `{}`.
    """
    
    with open(file, "w", encoding=encoding, **open_args) as f:
        json.dump(data, f, indent=indent, **dump_args)


async def maybe_coroutine(__func: Callable[..., Coroutine[Any, Any, Any]], *args: Any, **kwargs: Any) -> Any | None:
    """An asynchronous function that runs a callable or a coroutine with the given arguments

    ## Arguments:
        `__func` (`Callable[..., Coroutine[Any, Any, Any]]`): The callable or coroutine
        `*args`: Arguments to be passed to the callable or coroutine
        `**kwargs`: Keyword arguments to be passed to the callable or coroutine

    ## Returns:
        `Any | None`: Returns the returned value of the callable or coroutine
    """
    
    if inspect.iscoroutine(__func):
        return await __func
    elif inspect.iscoroutinefunction(__func):
        return await __func(*args, **kwargs)
    else:
        return __func(*args, **kwargs)


def mock_server(host: str = "127.0.0.1", port: int = 8080) -> None:
    app = FastAPI() 

    @app.get("/api/infinite-craft/pair")
    async def pair(first: str, second: str) -> dict[str, str | bool]: # type: ignore
        print(f"[MOCK API] PAIR: {first} + {second}")
        print(f"[MOCK API] RESULT: 🌌 ???")

        if len(first) == 0 or len(second) == 0:
            return {
                "result": "???",
                "emoji": "🌌",
                "isNew": False
            }
            
        return {
            "result": "???",
            "emoji": "🌌",
            "isNew": False
        }

    uvicorn.run(app, host=host, port=port)