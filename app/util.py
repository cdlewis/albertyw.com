# Various utility functions


def cached_function(func, should_cache):
    data = {}

    def wrapper(*args):
        if not should_cache:
            return func(*args)
        cache_key = ' '.join([str(x) for x in args])
        if cache_key not in data:
            data[cache_key] = func(*args)
        return data[cache_key]

    return wrapper
