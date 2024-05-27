import cv2
import os

def extract_frames(video_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        raise Exception("Error: No se puede abrir el video.")
    
    frame_rate = int(cap.get(cv2.CAP_PROP_FPS))
    count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame_path = os.path.join(output_folder, f'frame_{count:04d}.jpg')
        cv2.imwrite(frame_path, frame)
        count += 1

    cap.release()
    print(f"Se extrajeron {count} cuadros del video.")

video_path = 'C:\Users\shawa\OneDrive\Documents\Analizador_Escenas\Escenas\EscenaPelea1.mp4'
output_folder = 'C:\Users\shawa\OneDrive\Documents\Analizador_Escenas\Frames'
extract_frames(video_path, output_folder)
