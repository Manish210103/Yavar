# Fall Detection

## Files
  1.  Frame_convertor.py (used for converting given input .mp4 video into frames)
  2.  train.py (for training the YOLO model)
  3.  test.py (for testing the given video)
  4.  pretrainedModel.py( used for object detection and pose estimation with inbuilt pretrained model of YOLO)
  5.  trainedModel.py ( used for object detection and pose estimation with trained model of YOLO)
  6.  frame_to_video.py (used for converting back the processed frames into video)

## Input
  1.  sample.mp4
  2.  sample1.mp4

## Folders
  1.  dataset (contains the dataset for YOLO model training for object detection)
  2.  frames (images of frames of the given input video )
  3.  processed_images (images of frames of processed/detected frames)
  4.  run (contains the results of train/val by training the model)

## Models
  1.  yolov8n.pt (pretrained model)
  2.  best.pt (trained model of yolo base model using custom data)

## How To Run 
  1.  Run the frame_convertor.py and convert given input into frames.
  2.  Then use the model needed (pretrainedModel.py or trainedModel.py).
  3.  The images are processed and stored in processed images and then run the frame_to_video.py and the processed images are converted back into video

# Train Custom Model
  1.  if you want to train the model for custom data run the train.py and the model will be created with evaluation metrics in runs folder
  2.  then pick the best model (best.pt) and use it for further testing of input frames and then detect the object fall or not
