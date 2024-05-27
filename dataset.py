import os
import cv2

def preprocess_and_organize_images(source_dir, target_dir, image_size=(224, 224)):
    os.makedirs(target_dir, exist_ok=True)
    
    for class_name in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_name)
        if os.path.isdir(class_path):
            target_class_path = os.path.join(target_dir, class_name)
            os.makedirs(target_class_path, exist_ok=True)
            
            for image_name in os.listdir(class_path):
                image_path = os.path.join(class_path, image_name)
                image = cv2.imread(image_path)
                if image is not None:
                    resized_image = cv2.resize(image, image_size)
                    target_image_path = os.path.join(target_class_path, image_name)
                    cv2.imwrite(target_image_path, resized_image)
                else:
                    print(f"Error loading image {image_path}")

source_dir = 'path/to/your/source/images'
target_dir = 'path/to/organized/dataset'
preprocess_and_organize_images(source_dir, target_dir)
