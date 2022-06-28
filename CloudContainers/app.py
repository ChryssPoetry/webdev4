#Code monkey

import numpy as np
import cv2


#setting up a global variables

x = 0
y = 0
drawing = False



canvas = np.zeros((800, 600), np.uint8)
#Make canvas white
canvas.fill(255)
#binding mose
def draw(event, current_x, current_y, flags, params):
    #hooking up the global variables
    global x, y, drawing
    #mouse down event
    if event == cv2.EVENT_LBUTTONDOWN:
      x = current_x
      y = current_y
      drawing = True
    elif event == cv2.EVENT_MOUSEMOVE:
      if drawing:
        cv2.line(canvas, (current_x, current_y), (x, y), 0, thickness =2)
        x,y = current_x, current_y
    elif event == cv2.EVENT_LBUTTONUP:
       drawing = False
cv2.setMouseCallback("Draw", draw)

cv2.imshow("Draw", canvas)
while True:
    cv2.imshow("Draw", canvas)
    if cv2.waitKey(1) & 0xFF == 27: break

cv2.destroyAllWindows()

