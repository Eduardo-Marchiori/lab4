import rospy
from std_msgs.msg import String

rospy.init_node('ativ4')
num = 'matricula: 2017020610'

def num_callBack(msg):
    global num
    num = msg.data

def timerCallBack(event):
    print(num)
    msg = String()
    msg.data = '2017020610'
    pub.publish(msg)
    


pub = rospy.Publisher('/matricula', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(1), timerCallBack)
sub = rospy.Subscriber('/soma', String, num_callBack)

rospy.spin()