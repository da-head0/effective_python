# 이렇게 쓰지 마라
def get_stats(numbers):
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    average = sum(numbers) / count
    
    
    sorted_numbers = sorted(numbers)
    middle = count // 2
    
    if count % 2 == 0:
        lower = sorted_numbers[middle-1]
        upper = sorted_numbers[middle]
        median = (lower + upper) / 2
    else:
        median = sorted_numbers[middle]
        
    return minimum, maximum, average, median, count

# PEP8에도 어긋나고
# 실수하기가 쉽다



lengths = [63, 73, 72, 60, 67, 66, 71, 61, 72, 70]

minimum, maximum = get_stats(lengths)

print(f'MIN: {minimum}, MAX: {maximum}')


def get_avg_ratio(numbers):
    average = sum(numbers) / len(numbers)
    scaled = [x / average for x in numbers]
    scaled.sort(reverse=True)
    return scaled

# 이렇게 3개까지만 언패킹해라
longest, *middle, shortest = get_avg_ratio(lengths)

print(f'MAX LENGTH: {longest:>4.0%}')
print(f'MIN LENGTH: {shortest:>4.0%}')


# 아니면 NamedTuple이나 작은 클래스로 반환하기