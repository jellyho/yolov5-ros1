# yolov5-ros1

simple yolov5 wrapper.

This is a structure that creates a webcam node that publishes an image, and the yolo node that subscribes the image and inferece yolov5.


1) download this repository to workspace/src

```jsx
cd catckin_ws/src
git clone --recursive https://github.com/jellyho/yolov5-ros1.git
```

2) install python dependencies of yolov5

```jsx
cd yolov5-ros1
cd yolov5
pip install -r requirements.txt
```

3) put pretrained weights

copy-paste the pretrained weights into catkin_ws/src/yolov5/src

4) build the package and run!

```jsx
cd ~/catkin_ws
catkin build
source devel/setup.bash
roslaunch yolov5 yolo.launch
```
