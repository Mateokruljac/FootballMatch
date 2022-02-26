from playsound import playsound
from gtts import gTTS
import time


class Playsound () :
    
    def song (self,audio):
        time.sleep(0.2)
        playsound(audio)
    
    def convert_toaudio(self,text):
        self.my_audio = gTTS(text)
        self.my_audio.save("hello.mp3")
        self.song("hello.mp3")
        
      