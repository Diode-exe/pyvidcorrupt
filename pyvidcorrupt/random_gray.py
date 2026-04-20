import cv2
import random


class RandomGray:
    def __init__(self):
        self.src = None
        self.out = None
        self.cap = None
        self.w = None
        self.h = None
        self.fps = None
        self.fourcc = None
        self.writer = None
        self.rw = None
        self.rh = None
        self.x = None
        self.y = None
        self.gray = None
        self.frame = None
        self.ret = None

    def write_random_gray(self, src, out):
        self.src = src
        self.out = out
        self.cap = cv2.VideoCapture(self.src)
        self.w = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.h = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        self.writer = cv2.VideoWriter(self.out, self.fourcc, self.fps, (self.w, self.h))

        while True:
            self.ret, self.frame = self.cap.read()
            if not self.ret:
                break
            # add a few random gray patches per frame
            for _ in range(3):
                self.rw, self.rh = random.randint(20, self.w//3), random.randint(20, self.h//3)
                self.x, self.y = random.randint(0, self.w-self.rw), random.randint(0, self.h-self.rh)
                self.gray = random.randint(0, 255)
                self.frame[self.y:self.y+self.rh, self.x:self.x+self.rw] = (self.gray, self.gray, self.gray)
            self.writer.write(self.frame)

        self.cap.release()
        self.writer.release()
        
if __name__ == "__main__":
    rg = RandomGray()
    rg.write_random_gray("video.mp4", "output_video.mp4")