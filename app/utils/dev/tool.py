import hashlib
import imghdr
import io
import re
from _decimal import Decimal
from typing import Callable, Union, Annotated, Any

from fastapi import UploadFile


def to_camel_case(text):
    parts = re.split(pattern=r"[\s_]+", string=text)
    return parts[0] + "".join(part.title() for part in parts[1:])


to_camel_case_dict: Callable[[dict], dict] = lambda data: {to_camel_case(key): value for key, value in data.items()}


def hide_name_with_aster(name):
    length = len(name)
    if length == 2:  # 이름이 두 글자인 경우
        covered_name = name[0] + "*"
    else:  # 이름이 세 글자 이상인 경우
        covered_name = name[0] + "*" * (length - 2) + name[length - 1]
    return covered_name


def mask_string(s):
    if s is None:
        return None
    if len(s) <= 2:  # 문자열 길이가 2 이하이면 변환하지 않음
        return s
    return s[0] + '*' * (len(s) - 2) + s[-1]


def print_on_console(*messages):
    print("#" * 100)
    print(*messages)
    print("#" * 100)


def format_number(value):
    if value is not None:
        value = float(value)
        return str(int(value)) if value.is_integer() else str(round(value, 1))
    return None


def remove_point_zero(value):
    if value is not None:
        value = float(value)
        return str(int(value)) if value.is_integer() else str(value)
    return None


def get_file_info(upload_file: UploadFile) -> tuple[Union[str, None], int]:
    contents = upload_file.file.read()
    file_size = len(contents)
    file_like = io.BytesIO(contents)
    image_type = imghdr.what(file_like)
    upload_file.file.seek(0)
    return image_type, file_size


sha256_hash: Callable[[str], str] = lambda data: hashlib.sha256(data.encode()).hexdigest()
sha512_hash: Callable[[str], str] = lambda data: hashlib.sha512(data.encode()).hexdigest()


def convert_bytes(num):
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if num < 1024.0:
            return f"{num:3.1f}{unit}"
        num /= 1024.0


def get_supply_cost(total_amount: Annotated[Any, lambda x: x.isdecimal()]) -> str:
    return str(round(Decimal(str(total_amount)) * Decimal("0.909")))


def get_tax(total_amount: Annotated[Any, lambda x: x.isdecimal()]) -> str:
    return str(round(Decimal(total_amount) * Decimal("0.091")))
