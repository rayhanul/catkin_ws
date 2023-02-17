#!/usr/bin/env python3
import rospy
from cs576.msg import FloatArray

def callback(msg):
    msg_str = " ".join(map(str, msg.nums))
    rospy.loginfo(rospy.get_caller_id() + " I heard %s", msg_str)

def listener():
    rospy.init_node("listener", anonymous=True)
    msg = rospy.wait_for_message("chatter", FloatArray)
    callback(msg)

if __name__ == '__main__':
    listener()
