import os
from moviepy.editor import VideoFileClip, AudioFileClip, TextClip, CompositeVideoClip
IMAGEMAGICK_BINARY = r'C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\convert.exe'

org_video_path = input("Enter path to video: ")
audio_path = input("Enter path to the audio: ")
watermark = input("Enter the watermark: ")
final_video_folder = input("Enter path to the output folder: ")
final_video_name = input("Enter name for the final video (use only .mp4 extension): ")
final_video_path = os.path.join(final_video_folder, final_video_name)

video_clip = VideoFileClip(org_video_path)
audio_clip = AudioFileClip(audio_path)
final_audio = audio_clip.subclip(25, 40)

# Define width, height, and fps
w, h = video_clip.size      
fps = video_clip.fps

# Specify properties of intro text
intro_duration = 5      
intro_text = TextClip("Hello world", fontsize=70, color='white', size=video_clip.size)
intro_text = intro_text.set_duration(intro_duration)
intro_text = intro_text.set_fps(fps)
intro_text = intro_text.set_position("center")

# Set up intro music and intro text
intro_music = audio_clip.subclip(25, 30)        
intro_text = intro_text.set_audio(intro_music)

# Specify watermark properties
watermark_size = 50    
watermark_text = TextClip(watermark, fontsize=watermark_size, color='black', align='East', size=(w, watermark_size))
watermark_text = watermark_text.set_fps(fps)
watermark_text = watermark_text.set_duration(video_clip.duration)
watermark_text = watermark_text.margin(left=10, right=10, bottom=2, opacity=0)
watermark_text = watermark_text.set_position(("bottom"))
watermarked_clip = CompositeVideoClip([video_clip, watermark_text.set_duration(video_clip.duration)])
watermarked_clip = watermarked_clip.set_fps(fps)
watermarked_clip = watermarked_clip.set_audio(final_audio)

# Specify watermark properties
final_clip = CompositeVideoClip([intro_text.set_duration(intro_duration), watermarked_clip]) 
final_clip = final_clip.set_duration(video_clip.duration + intro_duration)
final_clip.write_videofile(final_video_path, codec='libx264', audio_codec='aac', fps=fps)