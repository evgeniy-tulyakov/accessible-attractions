'''
Utility tools for the application
'''

from functools import wraps
from os.path import join as join_paths
from typing import Any, Callable, NewType
from uuid import uuid4

from django.db import Error as DBError
from django.db.models import Model
from markdown import markdown
from result import Err, Result



# This type is returned by the result object in case of an error
ErrorReason = NewType('ErrorReason', str)


def build_upload_path(instance: Model, source_file_name: str, base_path: str | None=None) -> str:
    '''
    Generates a new path for uploaded media files
    '''

    file_suffix = source_file_name.split('.')[-1]
    new_file_name = f'{uuid4().hex}.{file_suffix}'
    if base_path is not None:
        return join_paths(base_path, new_file_name)
    else:
        return new_file_name


def md_to_html(source: str) -> str:
    '''
    Translates markdown into html markup
    '''

    return markdown(source)


def catch_database_errors(func: Callable[..., Any]):
    '''
    Wraps a function that interacts with database
    to transform database exceptions into a result type
    '''

    @wraps(func)
    def wrapper(*args, **kwargs) -> Result[Any, ErrorReason]:
        try:
            result_value = func(*args, **kwargs)
        except DBError as catched_exception:
            msg = str(catched_exception)
            return Err(ErrorReason(msg))
        return result_value

    return wrapper
