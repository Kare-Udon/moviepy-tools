from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip
from moviepy_tools import *
from eyed3 import mp3

print("选择功能：\n 1.剪切视频 \n 2.剪切音频")
func = input()
if func == "1":
    print("请输入需要剪切的视频的路径：")
    file = input()
    clip = openv(file)
    print("请输入剪切起始时间(秒 整数)：")
    start = input()
    print("请输入剪切终止时间(秒 整数)：")
    end = input()
    clip = cut(clip,start,end)
    print("请输入输出文件名(默认为 output.mp4)")
    file_name = input()
    if file_name == "":
        writev(clip)
    else:
        writev(clip,file_name)
elif func == "2":
    print("请输入需要剪切的音频的路径：")
    file = input()
    clip = opena(file)
    print("请输入剪切起始时间(秒 整数)：")
    start = input()
    print("请输入剪切终止时间(秒 整数)：")
    end = input()
    clip = cut(clip,start,end)
    print("请输入输出文件名(默认为 output.mp3)")
    file_name = input()
    f = mp3.Mp3AudioFile(file)
    bit_rate = f.info.bit_rate[1] * 1000
    if file_name == "":
        writea(clip,bit_rate)
    else:
        writea(clip,file_name,bit_rate)


