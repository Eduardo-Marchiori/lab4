import rospy
from std_msgs.msg import String

rospy.init_node('node2')

valor = '0'

def topic_callBack(somatotal):
    global valor
    valor = somatotal.data
    
rospy.subscriber('/matricula',String, topic_callBack)


def timerCallBack(event):
    somatotal = 0
    
    for i in valor:
        somatotal = somatotal + int(i)
    msg = String()
    msg.data = str(somatotal)
    
    pub.publish(msg)
    
pub = rospy.Publisher('/matricula', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)

rospy.spin()
