#!/usr/bin/env python

import sys
import rospy
from ros_essentials_cpp.srv import RectangleAreaService
from ros_essentials_cpp.srv import RectangleAreaServiceRequest
from ros_essentials_cpp.srv import RectangleAreaServiceResponse

def find_area_client(x, y):
    rospy.wait_for_service('find_area')
    try:
        find_area = rospy.ServiceProxy('find_area', RectangleAreaService)
        resp1 = find_area(x, y)
        return resp1.area
    except rospy.ServiceException(e):
        print ("Service call failed: %s"%e)

def usage():
    return 

if __name__ == "__main__":
    if len(sys.argv) == 3:
        x = int(sys.argv[1])
        y = int(sys.argv[2])
    else:
        print ("%s [x y]"%sys.argv[0])
        sys.exit(1)
    print ("Requesting %sx%s"%(x, y))
    s = find_area_client(x, y)
    print ("%s x %s = %s"%(x, y, s))
