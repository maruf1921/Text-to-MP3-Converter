from gtts import gTTS
import os
from tkinter.filedialog import *

link = askopenfilename()

file = open(link,"r")
myText = file.read().replace("\n"," ")
language = "en"

output = gTTS(text=myText, lang= language, slow=True)
output.save("output.mp3")
file.close()

os.system("start output.mp3")

