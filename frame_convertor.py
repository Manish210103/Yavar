import os
import cv2 

def FrameCapture(path, output_dir): 
    vidObj = cv2.VideoCapture(path) 
    count = 0
    success = 1
    os.makedirs(output_dir, exist_ok=True)

    while success: 
        success, image = vidObj.read() 
        if success:
            output_path = os.path.join(output_dir, f"frame_{count}.jpg")
            cv2.imwrite(output_path, image) 
            count += 1

if __name__ == '__main__': 
    video_path = "sample2.mp4"
    output_dir = "frames"
    FrameCapture(video_path, output_dir) 
