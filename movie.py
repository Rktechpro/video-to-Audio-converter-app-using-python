import moviepy.editor
from tkinter.filedialog import *

var=askopenfilename()
vid=moviepy.editor.VideoFileClip(var)

aud=vid.audio
aud.write_audiofile("deko.mp3")

print("----End----")