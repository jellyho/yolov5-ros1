#!/usr/bin/env python3

import rospy, rospkg
import cv2, torch
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

rospack = rospkg.RosPack()

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
    rospy.init_node('yolov5_node', anonymous=True)
    
    weights = rospy.get_param('~weights')
    if weights == "None":
        rospy.loginfo("USE Default pretrained weights - yolov5s.pt")
        weightPath = 'yolov5s.pt'
    else:
        weightPath = rospack.get_path('yolov5') + f'/src/{weights}'
        
    yoloPath = rospack.get_path('yolov5') + '/yolov5'

    model = torch.hub.load(yoloPath, 'custom', weightPath, source='local')
    model.iou = 0.1

    topic = rospy.get_param('~image')
    rospy.Subscriber(topic, Image, image_subscriber)
    verbose = rospy.get_param('~verbose')
    publish = rospy.get_param('~publish')

    json_publisher = rospy.Publisher('/yolo_results', String, queue_size=1)

    if publish:
        publisher = rospy.Publisher('/yolo_image', Image, queue_size=1)

    while not rospy.is_shutdown():
        if latest_image is not None:
            frame = latest_image
            results = model(frame)
            results.render()
            json_publisher.publish(String(results.pandas().xyxy[0].to_json(orient="records")))

            if verbose:
                cv2.imshow("Received Image", frame)
                cv2.waitKey(1)

            if publish:
                bridge = CvBridge()
                publisher.publish(bridge.cv2_to_imgmsg(frame, encoding="bgr8"))

if __name__ == '__main__':
    try:
        image_subscriber_node()
    except rospy.ROSInterruptException:
        pass
