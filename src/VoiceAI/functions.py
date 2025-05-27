import os
from mqtt_handler import publish

'''
ADD MORE FEATURES
'''
def PASS():
    publish("6")
    #send_http("run/set_pin(save_pin(6), 1)")
    pass

def led(state: bool) -> None:
    if state:
        print('LED Turned On!!')
        #publish('on')
        #easygui.msgbox("LED Turned On!!", title="Function Output")
        #send_http("run/set_pin(save_pin(4), 1)")
    else:
        print('LED Turned Off!')
        #publish('off')
        #easygui.msgbox('LED Turned Off!', title="Function Output")
        #send_http("run/set_pin(save_pin(4), 0)")

def nameAsked() -> None:
    print("ℹ️ Name of Robot has been asked")
    publish("1")
    #send_http("run/set_pin(save_pin(4), 1)")

def whoBuiltYouAsked() -> None:
    print("ℹ️ Builder names has been asked")
    publish("2")
    #send_http("run/set_pin(save_pin(17), 1)")

def whatAllCanYouDoAsked() -> None:
    print("ℹ️ What all can you do? has been asked")
    publish("3")
    #send_http("run/set_pin(save_pin(27), 1)")

def whatAreYourSpecsAsked() -> None:
    print("ℹ️ what are your specs? has been asked")
    publish("4")
    #send_http("run/set_pin(save_pin(22), 1)")

def whereAreYouFromAsked() -> None:
    print("ℹ️ wwhere are you from? has been asked")
    publish("5")
    #send_http("run/set_pin(save_pin(5), 1)")

def run_command(*args, **kwargs) -> None:
    exec(*args, **kwargs)

import time

publish("0")
time.sleep(5)