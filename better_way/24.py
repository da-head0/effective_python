from time import sleep
from datetime import datetime

def log(message, when=None):
    """_summary_

    Args:
        message (_type_): _description_
        when (_type_, optional): _description_. Defaults to None.
    """
    # 디폴트 인자 값으로 None을 사용하는 것은 인자가 가변적인 경우 특히 중요
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')
    
log('hello!')
sleep(0.1)
log('Hello again!')

import json

def decode(data, default=None):
    try:
        return json.loads(data)
    except ValueError:
        if default is None:
            default = {}
        return default
    
foo = decode('wrong data')
foo['stuff'] = 5
bar = decode('again wrong data')
bar['meep'] = 1
print('Foo: ', foo) 
print('Bar:', bar) # foo와 bar는 동일한 딕셔너리 객체

# assert foo is bar


from typing import Optional

def log_typed(message: str,
              when: Optional[datetime]=None) -> None:
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')

        
log_typed('뭐라뭐라')
