from typing import Callable

from app.utils.dev.http_status_code import HttpStatusCode

success_message: Callable[..., dict] = lambda json=None, array=None, **kwargs: dict(
    code=str(HttpStatusCode.OK.value),
    success=True,
    message=str(HttpStatusCode.OK.name),
    **kwargs,
    json=json or {},
    array=array or []
)

error_message: Callable[..., dict] = lambda status_code, message, **kwargs: dict(
    code=str(status_code),
    success=False,
    message=str(message),
    **kwargs,
    json={},
    array=[]
)

not_found_message: Callable[..., dict] = lambda **kwargs: dict(
    code=str(HttpStatusCode.NOT_FOUND.value),
    success=False,
    message=str(HttpStatusCode.NOT_FOUND.name),
    **kwargs,
    json={},
    array=[]
)
