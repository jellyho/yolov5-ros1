# yolov5-ros1-wrapper

아주 간단하게 만든 yolov5 wrapper입니다. 

webcam 노드를 만들어서 이미지를 쏴주고 yolo 노드에서 이것을 읽어 dectection 하는 구조입니다. 


1) workspace/src 에 패키지 다운로드

```jsx
cd catckin_ws/src
git clone https://github.com/jellyho/yolov5-ros1-wrapper.git
```

2) yolov5 다운로드

```jsx
cd yolo/src
git clone https://github.com/ultralytics/yolov5.git
```

3) python 패키지 설치

```jsx
cd yolov5
pip install -r requirements.txt
```

4) 패키지 빌드 후 실행
