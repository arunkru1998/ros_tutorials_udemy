#!/usr/bin/env python

from ros_essentials_cpp.srv import RectangleAreaService
from ros_essentials_cpp.srv import RectangleAreaServiceRequest
from ros_essentials_cpp.srv import RectangleAreaServiceResponse

import rospy

def handle_find_area(req):
    print ("Returning [%s x %s = %s]"%(req.width, req.height, (req.width * req.height)))
    return RectangleAreaServiceResponse(req.width * req.height)

def find_area_server():
    rospy.init_node('find_area_server')
    s = rospy.Service('find_area', RectangleAreaService, handle_find_area)
    print ("Ready find the area of the rectangle.")
    rospy.spin()
    
if __name__ == "__main__":
    find_area_server()
