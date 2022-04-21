import cv2
import logging
from typing import Union, Callable, Optional, Tuple, List, Dict

from xvideos.utils import *


class VideoReader(object):
    '''
    Class for video reading using opencv
    '''

    def __init__(
            self,
            source: Union[str, int],
            batch_size: int = 1,
            buffer_size: int = 1,
            transform: Optional[Callable] = None,
            workers: int = 1
    ):
        '''
        :param source: video source
        :param batch_size: number of frames, which will be returned
        :param buffer_size: number of frames in internal buffer
        :param transform: function or none, which be applied before frame returning
        :param workers: number of workers for transform frames in buffer
        '''
        self.capture = cv2.VideoCapture(source)
        self.capture_info = self.__info()
        self.batch_size = batch_size
        self.buffer_size = buffer_size
        self.transform = transform
        self.workers = workers

    def get(self) -> Tuple[bool, List]:
        '''
        Get batch of frames from buffer
        :return: pair (bool flag, list of frames). If capture has ended, then flag = False, else flag = True
        '''
        ...

    def __info(self) -> Dict:
        '''
        Return information of capture
        :return: dict with attributes of capture
        '''
        info = {}
        try:
            info['fps'] = get_fps(self.capture)
        except Exception as e:
            logging.warning(f'Failed to calculate fps: {e}')
        try:
            info['num_frames'] = count_frames(self.capture)
        except Exception as e:
            logging.warning(f'Failed to calculate number of frames: {e}')
        try:
            info['duration'] = video_duration(self.capture)
        except Exception as e:
            logging.warning(f'Failed to calculate duration of video: {e}')
        return info

    @property
    def info(self):
        '''
        Info of video capture
        '''
        return self.capture_info
