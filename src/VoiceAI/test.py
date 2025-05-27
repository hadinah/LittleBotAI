import tts_handler as tts
import os
tts.speak2("Hello I am not AN AI")
out = tts.process2("Hello I am AN AI")
out.save("motto.mp3")