import collections
import functools


def filter_and_text_type_assertions(func):
    """Decorates all functions with the filter and text signature to confirm the types of """
    @functools.wraps(func)
    def decorator(*args, **kwargs):
        try:
            args = list(args)
            filters = args[0]
            assert args[0] is not None or args[1] is not None, "Arguments must not be empty"
            assert isinstance(args[0], collections.Iterable) and isinstance(args[1], collections.Iterable), "Filters and objects to filter must be iterable."
        except IndexError:
            filters = kwargs.get('filter')
            assert kwargs.get('filter') is not None or kwargs.get('text') is not None, "Arguments or Key Word Arguments must not be empty"
            assert isinstance(kwargs.get('filter'), collections.Iterable) and isinstance(kwargs.get('text'), collections.Iterable), "Filters and objects to filter must be iterable."

        if isinstance(filters, str):
            try:
                delimiter = args[2]
            except IndexError:
                delimiter = kwargs.get('delimiter', ',')
            args[0] = filters.split(delimiter)

        return func(*args, **kwargs)
    return decorator
