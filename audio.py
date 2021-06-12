from gtts import gTTS
from playsound import playsound
audio="speech.mp3"
language='en'
sp=gTTS(text='im umeshchandra i love coding',lang=language,slow=False)
sp.save(audio)
playsound(audio)
print("======audio is playing======")
