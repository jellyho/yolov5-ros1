#!/usr/bin/env python3

import rospy, rospkg
import cv2, torch
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospack = rospkg.RosPack()
yoloPath = rospack.get_path('yolov5') + '/yolov5'
weightPath = rospack.get_path('yolov5') + '/src/yolov5s.pt'

model = torch.hub.load(yoloPath, 'custom', weightPath, source='local')
model.iou = 0.5

latest_image = None

def image_subscriber(image_msg):
    bridge = CvBridge()

    try:
        frame = bridge.imgmsg_to_cv2(image_msg, desired_encoding="rgb8")
        global latest_image
        latest_image = frame

    except CvBridgeError as e:
        rospy.logerr(e)

def image_subscriber_node():
    rospy.init_node('yolo_node', anonymous=True)
    rospy.Subscriber('/webcam', Image, image_subscriber)
    while not rospy.is_shutdown():
        if latest_image is not None:
            frame = latest_image
            results = model(frame)
            results.render()

            # for volume in results.xyxy[0]:
            #     xyxy = volume.numpy()
            #     cv2.rectangle(frame, (int(xyxy[0]), int(xyxy[1])), (int(xyxy[2]), int(xyxy[3])), color=(0, 255, 0), thickness=2)
            #     cv2.putText(frame, f'{xyxy[4]:.3f}', (int(xyxy[0]), int(xyxy[1])), fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0), thickness=2)

            cv2.imshow("Received Image", frame)
            cv2.waitKey(1)

if __name__ == '__main__':
    try:
        image_subscriber_node()
    except rospy.ROSInterruptException:
        pass
