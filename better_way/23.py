def remainder(number, divisor):
    return number % divisor

assert remainder(20, 7) == 6

# 아래는 모두 같은 코드

remainder(20, 7)
# remainder(20, divisor=7)
remainder(number=20, divisor=7)
remainder(divisor=7, number=20)

# 위치 기반 인자는 키워드 인자보다 앞에 지정해야 함
# remainder(number=20, 7)

# 각 인자는 단 한번만 지정해야 함
# remainder(20, number=7)


my_kwargs = {
    'number': 20,
}
other_kwargs = {
    'divisor': 7,
}

# ** 연산자를 여러 번 사용할 수 있음 - 딕셔너리에 겹치는 키가 없다면
assert remainder(**my_kwargs, **other_kwargs) == 6

def print_parameters(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} = {value}')
        
# 키워드 인자 사용        
print_parameters(alpha=1.5, beta=9, 감마=4)

# 디폴트 값을 지정하면 해당 인자는 선택적인 인자가 됨
def flow_rate(weight_diff, time_diff, period=1, units_per_kg=1):
    return ((weight_diff*units_per_kg)/time_diff) * period