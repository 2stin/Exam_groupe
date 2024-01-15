#import time
from pygame import mixer

mixer.init()

tick = mixer.Sound("..\sounds\sound1.mp3")
mixer.music.load('..\sounds\jazz.wav')
mixer.music.set_volume(0.2)

mixer.music.play(-1)

def tick_nouv_jeton():
    tick.play()