class MyClass:
    def __init(self):
        self.alligator = 'hatchling'
        self.elephant = 'calf'
    
a = MyClass()
for key, value in a.__dict__.items():
    print(f'{key} = {value}')
    

from collections.abc import MutableMapping

votes = {
    'otter' : 1281,
    'polar bear' : 587,
    'fox' : 863
}

def populate_ranks(votes, ranks):
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks):
    return next(iter(ranks))

ranks = {}
populate_ranks(votes, ranks)
print(ranks)
winner = get_winner(ranks)
print(winner)

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}
        
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
    
    def __delitem__(self, key):
        del self.data[key]
    
    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key
    
    def __len__(self):
        return len(self.data)
    
# sorted_ranks = SortedDict()
# populate_ranks(votes, sorted_ranks)
# print(sorted_ranks.data)
# winner = get_winner(sorted_ranks)
# print(winner)

from collections.abc import MutableMapping

class SortedDict(MutableMapping):
    def __init__(self):
        self.data = {}
        
    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value
        
    def __delitem__(self, key):
        del self.data[key]
    
    def __iter__(self):
        keys = list(self.data.keys())
        keys.sort()
        for key in keys:
            yield key
    
    def __len__(self):
        return len(self.data)


sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winner = get_winner(sorted_ranks)
print(winner)

# 함수 맨 앞에 타입을 검사하는 코드 추가
def get_winner(ranks):
    if not isinstance(ranks, dict):
        raise TypeError('dict 인스턴스가 필요합니다')
    return next(iter(ranks))

# get_winner(sorted_ranks)

# from typing import Dict, MutableMapping

def populate_ranks(votes: Dict[str, int], ranks: Dict[str, int]) -> None:
    names = list(votes.keys())
    names.sort(key=votes.get, reverse=True)
    for i, name in enumerate(names, 1):
        ranks[name] = i

def get_winner(ranks: Dict[str, int]) -> str:
    return next(iter(ranks))
    

sorted_ranks = SortedDict()
populate_ranks(votes, sorted_ranks)
print(sorted_ranks.data)
winnder = get_winner(sorted_ranks)
print(winner)