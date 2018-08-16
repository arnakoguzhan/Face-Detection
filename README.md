# Face-Detection

The project uses haar-cascade model for Face and eye detection. You can run code on existing video or realtime with your camera.

## Demo 

https://www.youtube.com/watch?v=0Drq7AtuXhQ

## Setup

Clone this project

run
`pip install requirements.txt`


## Running code on your camera

Run face_det-cam.py

`python face_det-cam.py`

for quit press "q" 


## Running code on existing video

You need to change video destination in face_det.py in line 24

`reader = imageio.get_reader('VIDEO-HERE)`

Than run the code

`python face_det.py`






