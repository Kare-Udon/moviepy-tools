from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip

def openv(file):
    clipv = VideoFileClip(file)
    return clipv

def opena(file):
    clipa = AudioFileClip(file)
    return clipa

def cut(clip,start,end):
    clip = clip.subclip(start,end)
    return clip

def resize(clip,hei=720):
    clip = clip.resize(height=hei)
    return clip

def writev(clip,file_name="output.mp4"):
    clip.write_videofile(file_name)

def writea(clip,bit_rate,file_name="output.mp3"):
    clip.write_audiofile(file_name,bitrate=str(bit_rate))

def writeg(clip,myfps=15,file_name="output.gif"):
    clip.write_gif(file_name,fps=int(myfps))