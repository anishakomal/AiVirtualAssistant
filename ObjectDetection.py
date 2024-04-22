# pip install opencv-contrib-python
# pip install cvlib
# pip3 install PyObjc

# import tkinter as tk
# print(tk.TkVersion)
# import tkinter as tk
#
# root = tk.Tk()
# root.title("Hello Tkinter!")
# label = tk.Label(root, text="Hello, World!")
# label.pack()
#
# root.mainloop()

import cv2
print(cv2.__version__)
# import cvlib as cv
# from cvlib.object_detection import draw_bbox
# from gtts import gTTS
# from playsound import playsound
#
# video = cv2.VideoCapture(1)
#
# while True:
#     ret, frame = video.read()
#     bbox, label, conf = cv.detect_common_objects(frame)
#     output_image = draw_bbox(frame, bbox,label,conf)
#
#     cv2.imshow("Object Detection", output_image)
#
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break
