import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture
import matplotlib.pyplot as plt
import numpy as np
directionList = []
totalFrames = 0


def plotGraph ():
    print directionList
    global totalFrames
    print totalFrames
    i=0
    while i < totalFrames:
        plt.scatter(i,directionList[i])
        i+=1
    plt.show()


class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']

    def on_init(self, controller):
        print "Initialized"

    def on_connect(self, controller):
        print "Connected"

        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        print "Disconnected"

    def on_exit(self, controller):
        print "Exited"


    def on_frame(self, controller):
        # Get the most recent frame and report some basic information


        frame = controller.frame()

        for hand in frame.hands:
            handType = "Left Hand" if hand.is_left else "Right Hand"
            global totalFrames
            #print " %s , ID = %d ,position = % s " %(handType,hand.id,hand.palm_position)
            normal = hand.palm_normal
            direction = hand.direction
            directionList.append((normal[2]))
            totalFrames+=1

            print " %s is Normal and %s is direction " % (normal[2],direction[0])
def main():
    # Create a sample listener and controller

    listener = SampleListener()
    controller = Leap.Controller()

    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    
    # Keep this process running until Enter is pressed
    print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)


if __name__ == "__main__":
    main()
    plotGraph()

