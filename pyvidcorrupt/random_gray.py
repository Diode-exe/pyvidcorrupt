import cv2
import random

src = "video.mp4"
out = "output_video.mp4"

cap = cv2.VideoCapture(src)
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(out, fourcc, fps, (w, h))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    # add a few random gray patches per frame
    for _ in range(3):
        rw, rh = random.randint(20, w//3), random.randint(20, h//3)
        x, y = random.randint(0, w-rw), random.randint(0, h-rh)
        gray = random.randint(0, 255)
        frame[y:y+rh, x:x+rw] = (gray, gray, gray)
    writer.write(frame)

cap.release()
writer.release()