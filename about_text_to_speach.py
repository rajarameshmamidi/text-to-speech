# below code reply the text in voice
#devdungeon.com/content/text-speech-python-pyttsx3

# using pyttsx3 module
#pip install pywin32 pypiwin32 pyttsx3
# below code will say in default system language id. english is the default language id in this system
import pyttsx3
engine = pyttsx3.init()
engine.say('Good Morning.')
engine.runAndWait()

'''
# Set properties _before_ you add things to say
import pyttsx3
engine = pyttsx3.init()
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
engine.say('Good Morning.')
engine.runAndWait()
'''
'''
# below code is to get vioces availabe
import pyttsx3
engine = pyttsx3.init()
voices  =engine.getProperty('voices')
for voice in voices:
    print("Voice:")
    print(" - ID: %s" % voice.id)
    print(" - Name: %s" % voice.name)
    print(" - Languages: %s" % voice.languages)
    print(" - Gender: %s" % voice.gender)
    print(" - Age: %s" % voice.age)
'''
'''
# Below code is to say in different language based on system availablity language id's 
import pyttsx3
engine = pyttsx3.init()
# These will be system specific
en_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Anna-1033-20-DSK'
chinese_voice_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\MS-Lili-2052-20-DSK'
engine.setProperty('voice',en_voice_id) # to deliver in particuar voice
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
engine.say('Good Morning.')
engine.runAndWait()
# chinese language
engine.setProperty('voice',en_voice_id) # to deliver in particuar voice
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1
engine.say('Zaoshang hao')
engine.runAndWait()
'''

'''
# using win32com.client API
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
#speaker.Speak("Jumpman Jumpman Jumpman Them boys up to something!")
speaker.Speak('Good morning.')
'''