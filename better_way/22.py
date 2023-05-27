# 로그에 남길 값이 없을 때도 빈 리스트를 넘겨야 한다면
def log(sequence, message, *values):
    if not values:
        print(f'{sequence}-{message}')
    else:
        values_str = ', '.join(str(x) for x in values)
        print(f'{sequence}-{message}: {values_str}')

log(1, '좋아하는 숫자는', 7, 33)
log(1, '안녕') # 뒤 인자를 생략할 수 있음

log('좋아하는 숫자는', 7, 33) # sequence 가 주어지지 않아 7을 parameter로 사용... 예외가 발생하지 않고 코드가 작동할 수도 있어 추적하기 어려운 버그

# 그러나 문제점이 있음... 
# 1. 선택적인 위치 인자가 함수에 전달되기 전에 튜플로 변환됨

def my_generator():
    for i in range(10):
        yield i

# *args를 받는 함수는 가변 인자의 개수가 처리하기 좋을 정도로 작은 경우에 가장 적합함.  
# 아니면 메모리를 모두 소진하고 중단될 수도... 

def my_func(*args):
    print(args)

it = my_generator()
my_func(*it)