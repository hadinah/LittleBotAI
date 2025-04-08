import os
from mqtt_handler import publish

'''
ADD MORE FEATURES
'''

def led(state: bool) -> None:
    if state:
        print('LED Turned On!!')
        publish('on')
        #easygui.msgbox("LED Turned On!!", title="Function Output")
    else:
        print('LED Turned Off!')
        publish('off')
        #easygui.msgbox('LED Turned Off!', title="Function Output")

def run_command(*args, **kwargs) -> None:
    exec(*args, **kwargs)
