import inspect
from pprint import pprint

def call_stack():
    "Function to get the current call stack"
    current_frame=inspect.currentframe()
    print('**'*40)
    while current_frame.f_back:
        print(pprint(current_frame.f_locals))
        current_frame=current_frame.f_back
