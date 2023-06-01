from time import sleep
from datetime import datetime

def log(message, when=None):
    """_summary_

    Args:
        message (_type_): _description_
        when (_type_, optional): _description_. Defaults to None.
    """
    if when is None:
        when = datetime.now()
    print(f'{when}: {message}')
    
log('hello!')
sleep(0.1)
log('Hello again!')