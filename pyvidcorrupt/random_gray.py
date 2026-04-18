import random
from pathlib import Path

class RandomGray:
    def __init__(self):
        self.video = "video.mp4"
        self.video_data = None

    def random_gray(self, video):
        """Convert random bytes to gray values in the video."""
        self.video = Path(video)
        
        with self.video.open("rb") as file_handle:
            self.video_data = bytearray(file_handle.read())

        for i in range(len(self.video_data)):
            if random.random() < 0.05:  # 5% chance to modify each byte
                gray_value = random.randint(0, 255)
                self.video_data[i] = gray_value
        print
        return bytes(self.video_data)