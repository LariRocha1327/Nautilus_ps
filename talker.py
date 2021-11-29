
import rospy
   4 from std_msgs.msg import String
   5 
   6 def talker():
   7     pub = rospy.Publisher('angulos', String, queue_size=10)
   8     rospy.init_node('talker', anonymous=True)
   9     rate = rospy.Rate(5) # 10hz
  10     while not rospy.is_shutdown():
  11         var_str = "x,y,z %s" % rospy.get_time()
  12         rospy.loginfo(var_str)
  13         pub.publish(var_str)
  14         rate.sleep()
  15 
  16 if __name__ == '__main__':
  17     try:
  18         talker()
  19     except rospy.ROSInterruptException:
  20         pass