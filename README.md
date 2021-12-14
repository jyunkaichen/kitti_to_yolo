# KITTI labels in YOLO label format 
This tool converts KITTI labels to YOLO format.
The generated labels can be directly used to start a Training on the KITTI data for 2D object detection with YOLO.
The attachment is the generated labels, you can download it directly.

## Setup
Install the packages:
```
pip install -r requirements.txt
```

## KITTI dataset
You can make the dataset folder in this architecture:
```
Kitti
   └—————— kitti_to_yolo.py
   |
   └—————— images
   |        └—————— test
   |        └—————— train
   |        └—————— val
   └—————— labels
            └—————— train
            |        └—————— label_2 (Original KITTI labels)          
            └—————— val
```

## Usage
```
python kitti_to_yolo.py --ki ./images/train/ --kl ./labels/train/label_2/ --out ./labels/train/
```

## Input txt file

'''
Pedestrian 0.00 0 -0.20 712.40 143.00 810.73 307.92 1.89 0.48 1.20 1.84 1.47 8.41 0.01
'''

## Output txt file
'''
3 0.622194 0.609351 0.080335 0.445730
'''