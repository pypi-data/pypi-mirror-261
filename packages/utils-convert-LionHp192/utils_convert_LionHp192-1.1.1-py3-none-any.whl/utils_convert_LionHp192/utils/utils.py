from datetime import datetime, date, timedelta, timezone
import pytz


def to_timezone(dt, tz_name='Asia/Ho_Chi_Minh'):
    """ Convert datetime to timezone datetime

    Args:
        dt (datetime) - The datetime object
        tz_name (str) - The name of timezone

    Returns:
        datetime - The datetime object with new timezone, invalid timezone
                   name make no effect

    """
    try:
        tz = pytz.timezone(tz_name)
    except pytz.UnknownTimeZoneError:
        return dt

    return dt.astimezone(tz)


def naive_datetime_to_local(dt, tz_name='Asia/Ho_Chi_Minh'):
    if not dt:
        return
    local_timezone = pytz.timezone(tz_name)
    return local_timezone.localize(dt)


def set_time_to_begin_of_the_day(dt):
    return dt.replace(hour=0, minute=0, second=0)


def set_time_to_end_of_the_day(dt):
    return dt.replace(hour=23, minute=59, second=59)


def convert_date_format_vietnamese(date):
    format_date = date.strftime("%d %m %Y")
    return f"{format_date[:3]}Th{format_date[3:]}"


def remove_multi_space_to_one_space(str_content):
    return ' '.join([item for item in str_content.split(" ") if item != ''])
