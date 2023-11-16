from datetime import datetime, timedelta
from typing import Callable

from pytz import timezone

from app.utils.dev.config import QUEENSLAND_TIMEZONE

utc_queensland: Callable[[], datetime] = \
    lambda: datetime.now(timezone(QUEENSLAND_TIMEZONE))

current_time: Callable[[], str] = \
    lambda: datetime.now(timezone(QUEENSLAND_TIMEZONE)).strftime("%Y-%m-%d %H:%M:%S")

current_date: Callable[[], str] = \
    lambda: datetime.now(timezone(QUEENSLAND_TIMEZONE)).strftime("%Y-%m-%d")

# strptime() : string parse time, 문자 -> 시간
# strftime() : string format time, 시간 -> 문자
time_to_date: Callable[[str], str] = \
    lambda time: datetime.strptime(time, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")

datetime_to_string: Callable[[datetime], str] = \
    lambda time: time.strftime("%Y-%m-%d %H:%M:%S")

trim_date_string: Callable[[str], str] = \
    lambda date: datetime.strptime(date, '%Y-%m-%d').strftime('%Y-%m-%d')
trim_date_string_to_next_day: Callable[[str], str] = \
    lambda date: (datetime.strptime(date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')

current_milli_time: Callable[[], int] = \
    lambda: int((datetime.utcnow() - datetime(year=1970, month=1, day=1)).total_seconds() * 1000)

convert_time_to_au_format: Callable[[str], str] = \
    lambda date: datetime.strptime(date, "%Y-%m-%d %H:%M:%S").strftime('%d/%m/%Y')
convert_date_to_au_format: Callable[[str], str] = \
    lambda date: datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')
