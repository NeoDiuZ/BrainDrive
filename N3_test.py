from neuropy3.neuropy3 import MindWave
import time
mw = MindWave(address='A4:DA:32:70:03:4E', autostart=False, verbose=3)
mw.set_callback('eeg', lambda x: print("EEG: ", x))
mw.set_callback('meditation', lambda x: print("Meditation: ", x))
mw.set_callback('attention', lambda x: print("Attention: ", x))
mw.set_callback('blinkStrength', lambda x: print("Blink Strenght: ", x))
mw.start()