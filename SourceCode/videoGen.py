import os
import random
from moviepy.editor import *

TRANSITIONS = ['crossfade', 'slide', 'zoom']

def generate_slideshow(image_paths, music_dir, output_path="output/final_video.mp4", duration_per_image=3):
    clips = []

    # Step 1: Create a video clip from each image
    for path in image_paths:
        clip = ImageClip(path).set_duration(duration_per_image).resize(width=720).set_fps(24)
        clips.append(clip)

    # Step 2: Apply randomized transitions
    transitioned_clips = [clips[0]]
    for i in range(1, len(clips)):
        transition_type = random.choice(TRANSITIONS)
        if transition_type == "crossfade":
            transition = clips[i - 1].crossfadeout(1)
            transitioned_clips[-1] = transition
        # More transitions can be implemented here
        transitioned_clips.append(clips[i])

    # Step 3: Concatenate all clips
    final_clip = concatenate_videoclips(transitioned_clips, method="compose")

   # Step 4: Add random background music
    song_files = [f for f in os.listdir(music_dir) if f.endswith(".mp3")]
    if song_files:
        selected_song = random.choice(song_files)
        song_path = os.path.join(music_dir, selected_song)
        audio_clip = AudioFileClip(song_path)

    if audio_clip.duration > final_clip.duration:
        margin = (audio_clip.duration - final_clip.duration) / 2
        start_time = random.uniform(margin * 0.75, margin * 1.25)
        end_time = start_time + final_clip.duration
        audio_clip = audio_clip.subclip(start_time, end_time)

    audio_clip = audio_clip.audio_fadein(1).volumex(1.5)
    final_clip = final_clip.set_audio(audio_clip)

    # Step 5: Export video
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    final_clip.write_videofile(output_path, codec="libx264", audio_codec="aac")
