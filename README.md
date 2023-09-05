# yolov5-wrapper-ros1-noetic

simple yolov5 wrapper.

This is a structure that creates a webcam node that publishes an image, and the yolo node that subscribes the image and inferece yolov5.


1) download this repository to workspace/src

```jsx
cd catckin_ws/src
git clone https://github.com/jellyho/yolov5-ros1-wrapper.git
```

2) download yolov5 repository

```jsx
cd yolo/src
git clone https://github.com/ultralytics/yolov5.git
```

3) install python dependencies of yolov5

```jsx
cd yolov5
pip install -r requirements.txt
```

4) build the package and run!

```jsx
cd ~/catkin_ws
catkin build
source devel/setup.bash
roslaunch yolo yolo.launch
```
