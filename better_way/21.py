def sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0, x)
        return (1, x)
    values.sort(key=helper)
    
numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,6}
sort_priority(numbers, group)
print(numbers)

'''
closure -> 자신이 정의된 영역 밖의 변수를 참조하는 함수 (helper)
- helper 함수가 sort_priority 함수의 group 인자에 접근할 수 있음

파이썬에서 함수는 first-class citizen 객체
- 직접 가리킬 수 있음
- 변수에 대입할 수 있음
- 다른 함수에 인자로 전달할 수 있음
- if 문에서 함수를 비교하거나, 함수에서 반환하는 것 등이 가능
=> sort 메서드가 closure 함수(helper)를 key 인자로 받을 수 있음

파이썬은 시퀀스를 비교할 때 0번 인덱스의 값을 비교한 후, 이 값이 같으면 1번 인덱스에 있는 값을 비교 (순서대로 시퀀스의 모든 원소릴 다 비교하거나 결과가 정해질 때까지 계속)
'''
def sort_priority2(numbers, group):
    found = False           # 영역 : sort+priority2
    def helper(x):
        if x in group:
            nonlocal found  # 클로저(helper) 밖으로 데이터 끌어내기 - 대입할 데이터가 클로저 밖에 있다는 걸 알려줌. 
            found = True
            return (0, x)
        return (1, x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('FIND: ', found) # 잘못된 값을 반환
print(numbers)

# 근데 위 방식도 안 좋음... 함수 동작을 이해하기 힘들어짐

class Sorter:
    def __init__(self, group):
        self.group = group
        self.found = False
        
    def __call__(self, x):
        if x in self.group:
            self.found = True
            return (0, x)
        return (1, x)
    
sorter = Sorter(group)
numbers.sort(key=sorter)
assert sorter.found is True