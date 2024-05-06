import cv2
import os

input_folder = "processed_images"
output_video = "output_video.mp4"
image_files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if f.endswith('.jpg')]
image_files.sort(key=lambda x: int(x.split('_')[-1].split('.')[0]))
image = cv2.imread(image_files[0])
height, width, _ = image.shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Choose the codec according to the file extension, here it's MP4
out = cv2.VideoWriter(output_video, fourcc, 30.0, (width, height))

for image_file in image_files:
    img = cv2.imread(image_file)
    out.write(img)

out.release()
print(f"Video created: {output_video}")
