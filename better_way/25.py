# 키워드 인자를 사용해 가독성 향상
def safe_division(number, divisor, *,  
                  ignore_overflow=False, 
                  ignore_zero_division=False):
    try:
        return number / divisor
    except OverflowError:
        if ignore_overflow:
            return 0
        else:
            raise
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        else:
            raise
 
# 하지만 쓰는 쪽이 키워드 인자를 쓰지 않는다면?
# result = safe_division(1.0, 10**500, ignore_overflow=True)
#result = safe_division(1.0, 0, ignore_overflow=False, ignore_zero_division=True)

result = safe_division(1.0, 0, ignore_zero_division=True)
assert result == float('inf')

try:
    result = safe_division(number=1.0, divisior=0)
except ZeroDivisionError:
    print('work as expected')