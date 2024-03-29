from typing import List, Tuple, Optional, Union
from threading import Thread
from queue import Queue
import cv2
import numpy as np


class VideoReader(object):
    """
    Class for video reading using opencv.

    Attributes
    ----------
    source : Union[str, int]
        Video source.

    batch_size : int, default=1
        Number of frames, which will be returned.

    buffer_size : int, default=1
        Number of frames in internal buffer.

    Examples
    --------
    >>> from xvideos import VideoReader
    ...
    ... reader = VideoReader(source=0, batch_size=32, buffer_size=128)
    ... while True:
    ...     flag, batch = reader.get()
    ...     if not flag:
    ...         break

    You can read video in while true loop and stop him when video has ended.

    >>> from xvideos import VideoReader
    ...
    ... reader = VideoReader(source='./test.mp4')
    ... reader.fps
    ... reader.frame_count
    ... reader.frame_duration
    ... reader.video_duration

    Using property "fps", "frame_count", "frame_duration", "video_duration" you can get information about video.

    """
    def __init__(
            self,
            source: Union[str, int],
            batch_size: int = 1,
            buffer_size: int = 1,
            *,
            bgr2rgb: bool = False
    ):
        self._capture = cv2.VideoCapture(source)

        if not self._capture.isOpened():
            raise FileNotFoundError

        self._batch_size = batch_size
        self._buffer = Queue(maxsize=buffer_size)
        self._bgr2rgb = bgr2rgb
        self._is_alive = True
        Thread(target=self._read_video, daemon=True).start()

    def _read_video(self) -> None:
        while True:
            flag, frame = self._capture.read()

            if not flag:
                self._is_alive = False
                self._buffer.put(None)
                break

            if self._bgr2rgb:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            self._buffer.put(frame)

        self._capture.release()

    def get(self) -> Tuple[bool, Optional[List[np.ndarray]]]:
        batch = []

        while (self._is_alive or not self._buffer.empty()) and len(batch) != self._batch_size:
            frame = self._buffer.get()

            if frame is None:
                break

            batch.append(frame)

        if not batch:
            return False, None

        return True, batch

    @property
    def fps(self):
        return self._capture.get(cv2.CAP_PROP_FPS)

    @property
    def frame_count(self):
        return self._capture.get(cv2.CAP_PROP_FRAME_COUNT)

    @property
    def frame_duration(self):
        return 1000 / self.fps

    @property
    def video_duration(self):
        return self.frame_duration * self.frame_count
