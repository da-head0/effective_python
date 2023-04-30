from collections import defaultdict

class Visits:
    def __init__(self):
        self.data = defaultdict(set)
    
    def add(self, country, city):
        self.data[country].add(city)
        
visits = Visits()
visits.add('영국', '바스')
visits.add('영국', '런던')
print(visits.data)