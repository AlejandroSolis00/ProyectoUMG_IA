from moviepy.editor import VideoFileClip, concatenate_videoclips

def extract_scenes(video_path, scene_intervals, scene_class_to_extract):
    clips = []
    original_video = VideoFileClip(video_path)
    fps = original_video.fps

    for scene_class, start_frame, end_frame in scene_intervals:
        if scene_class == scene_class_to_extract:
            start_time = start_frame / fps
            end_time = end_frame / fps
            clip = original_video.subclip(start_time, end_time)
            clips.append(clip)

    if clips:
        final_clip = concatenate_videoclips(clips)
        final_clip.write_videofile('extracted_scenes.mp4', codec='libx264', audio_codec='aac')
    else:
        print("No se encontraron escenas de la clase especificada.")

video_path = 'C:\Users\shawa\OneDrive\Documents\Analizador_Escenas\Escenas\EscenaPelea1.mp4'
scene_class_to_extract = 1  # Por ejemplo, la clase de escena de acción
extract_scenes(video_path, scene_intervals, scene_class_to_extract)
