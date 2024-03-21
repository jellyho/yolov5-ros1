# yolov5-ros1

Simple yolov5 wrapper.

Subscribes the image topic and inference by yolov5 to get bounding box and annotations.

You can use webcam as an image publisher.


### 1) Download this repository to workspace/src

```jsx
cd catckin_ws/src
git clone --recursive https://github.com/jellyho/yolov5-ros1.git
```

### 2) Install python dependencies of yolov5

```jsx
cd yolov5-ros1
cd yolov5
pip install -r requirements.txt
```

### 3) Put pretrained weights

copy-paste the pretrained weights into catkin_ws/src/yolov5/src



### 4) Build the package and run!

```jsx
cd ~/catkin_ws
catkin build
source devel/setup.bash
```

There are two options when execute launch file.
- verbose(bool) : Open popup window that shows the annotated results.
- publish(bool) : Publish the annotated image

Default setting is verbose:=false, publish:=true

.

1. Subscribe existing image topic and yolo
```jsx
roslaunch yolov5 yolo.launch image:='/topic_name' verbose:=false publish:= true
```

2. Use webcam as an image publisher
```jsx
roslaunch yolov5 yolo_webcam.launch vebose:=false publish:=true
```

### 5) Topic lists

```jsx
/yolo_image - Image - Annotated inferenced image when publish:=true
/yolo_results - tbd
```