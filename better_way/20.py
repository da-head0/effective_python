# None을 반환하기보다는 예외를 발생시켜라

def careful_divide(a, b):
    try:
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('잘못된 입력')
    
    
x, y = 5, 2
try:
    result = careful_divide(x, y)
except ValueError:
    print('잘못된 입력')
else:
    print(f'결과는 {result:.1f} 입니다')
    
# None을 반환하는 함수를 사용하면 0, '' 도 조건문에서 False 가 될 수 있어 실수하기 쉽다.
# 특별한 상황을 표현하기 위해 None을 반환하는 대신 예외를 발생시켜라.