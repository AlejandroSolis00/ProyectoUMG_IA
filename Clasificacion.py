import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import os

def classify_frames(model_path, frames_folder, batch_size=32):
    model = load_model(model_path)
    frame_files = sorted(os.listdir(frames_folder))
    scene_intervals = []
    current_scene = None

    def process_batch(batch_files):
        batch_images = []
        for frame_file in batch_files:
            img_path = os.path.join(frames_folder, frame_file)
            img = load_img(img_path, target_size=(224, 224))
            img_array = img_to_array(img) / 255.0
            batch_images.append(img_array)
        return np.array(batch_images)

    for i in range(0, len(frame_files), batch_size):
        batch_files = frame_files[i:i + batch_size]
        batch_images = process_batch(batch_files)
        predictions = model.predict(batch_images)
        predicted_classes = np.argmax(predictions, axis=1)

        for j, scene_class in enumerate(predicted_classes):
            frame_index = i + j
            if current_scene is None:
                current_scene = (scene_class, frame_index, frame_index)
            else:
                if current_scene[0] == scene_class:
                    current_scene = (scene_class, current_scene[1], frame_index)
                else:
                    scene_intervals.append(current_scene)
                    current_scene = (scene_class, frame_index, frame_index)
    
    if current_scene:
        scene_intervals.append(current_scene)

    return scene_intervals

model_path = 'scene_classification_model.h5'
frames_folder = 'path/to/frames'
scene_intervals = classify_frames(model_path, frames_folder)
