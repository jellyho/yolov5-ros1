#!/usr/bin/env python3

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

def webcam_publisher():
    rospy.init_node('webcam_publisher', anonymous=True)
    image_pub = rospy.Publisher('/webcam', Image, queue_size=1)
    rate = rospy.Rate(10)  # 발행 주기를 설정합니다 (여기서는 10Hz로 설정되었습니다).

    capture = cv2.VideoCapture(0)

    bridge = CvBridge()

    while not rospy.is_shutdown():
        ret, frame = capture.read()  # 웹캠에서 프레임을 읽습니다.

        if ret:
            # 읽은 프레임을 ROS 메시지 형식으로 변환합니다.
            ros_image = bridge.cv2_to_imgmsg(frame, encoding="rgb8")
            image_pub.publish(ros_image)  # ROS 토픽으로 프레임을 발행합니다.
        rate.sleep()
    capture.release()  # 캡처 객체를 해제합니다.

if __name__ == '__main__':
    try:
        webcam_publisher()
    except rospy.ROSInterruptException:
        pass
