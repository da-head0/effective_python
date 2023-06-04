from functools import wraps

def trace(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__}({args!r}, {kwargs!r}) ' # args!r = repr(args) -> 객체의 인쇄 가능한 표현이 포함된 문자열을 반환
              f'-> {result!r}')
        return result
    return wrapper

@trace
def fibonacci(n):
    """return nth number of fibonnacci"""
    if n in (0, 1):
        return n
    return (fibonacci(n-2) + fibonacci(n-1))

fibonacci(4)
print(fibonacci)
help(fibonacci)