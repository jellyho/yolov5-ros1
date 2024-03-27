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

There are three options when execute launch file.
- image(string) : Image topic name that you want to apply yolov5.
- verbose(bool) : Open popup window that shows the annotated results.
- publish(bool) : Publish the annotated image
- weights(stirng) : Pretrained weight name in src/ folder

Default setting is verbose:=false, publish:=true

If you don't put any option about weights, defuault yolov5n.pt will applied.

.

1. Subscribe existing image topic and yolo
```jsx
roslaunch yolov5 yolo.launch image:='/topic_name' verbose:=false publish:= true weights:=yolov8m.pt
```

2. Use webcam as an image publisher
```jsx
roslaunch yolov5 yolo_webcam.launch vebose:=false publish:=true
```

### 5) Topic lists

```jsx
/yolo_image - Image - Annotated inferenced image when publish:=true
/yolo_results - String - Bounding box information encoded into json format
```

> How to use /yolo_results ?

```python
# define String msg subscriber
rospy.Subscriber('/yolo_results', String, yolo_cb)
```

```python
# In callback, convert to json
import json

def yolo_cb(msg):
    result = json.loads(msg.data)
    print(result)
```

```bash
[{'xmin': 140.4574737549, 'ymin': 1.7290496826, 'xmax': 509.8947143555, 'ymax': 480.0, 'confidence': 0.5377990603, 'class': 0, 'name': 'person'},
 {'xmin': 25.5067329407, 'ymin': 366.9152832031, 'xmax': 146.5026702881, 'ymax': 455.7973632812, 'confidence': 0.520999074, 'class': 64, 'name': 'mouse'}]
```
