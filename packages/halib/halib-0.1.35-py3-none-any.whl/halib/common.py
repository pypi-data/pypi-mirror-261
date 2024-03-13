import arrow
import re
from rich.console import Console

console = Console()
def now_str(sep_date_time="."):
    assert sep_date_time in [
        ".",
        "_",
        "-",
    ], "sep_date_time must be one of '.', '_', or '-'"
    now_string = arrow.now().format(f"YYYYMMDD{sep_date_time}HHmmss")
    return now_string


def norm_str(in_str):
    # Replace one or more whitespace characters with a single underscore
    norm_string = re.sub(r"\s+", "_", in_str)
    # Remove leading and trailing spaces
    norm_string = norm_string.strip()
    return norm_string


def console_rule(msg, do_norm_msg=True, is_end_tag=False):
    msg = norm_str(msg) if do_norm_msg else msg
    if is_end_tag:
        console.rule(f"</{msg}>")
    else:
        console.rule(f"<{msg}>")


def console_log(func):
    def wrapper(*args, **kwargs):
        console_rule(func.__name__)
        result = func(*args, **kwargs)
        console_rule(func.__name__, is_end_tag=True)
        return result

    return wrapper


class ConsoleLog:
    def __init__(self, message):
        self.message = message

    def __enter__(self):
        console_rule(self.message)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        console_rule(self.message, is_end_tag=True)
        if exc_type is not None:
            print(f"An exception of type {exc_type} occurred.")
            print(f"Exception message: {exc_value}")
