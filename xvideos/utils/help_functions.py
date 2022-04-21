import cv2


def get_fps(capture: cv2.VideoCapture) -> int:
    '''
    Get fps from video capture
    :param capture: opencv video capture
    :return: fps
    '''
    return int(capture.get(cv2.CAP_PROP_FPS))


def count_frames(capture: cv2.VideoCapture) -> int:
    '''
    Get number of frames from video capture
    :param capture: opencv video capture
    :return: number of frames
    '''
    return int(capture.get(cv2.CAP_PROP_FRAME_COUNT))


def video_duration(capture: cv2.VideoCapture) -> int:
    '''
    Get video duration in milliseconds
    :param capture: opencv video capture
    :return: duration in milliseconds
    '''
    fps = get_fps(capture)
    num_frames = count_frames(capture)
    return int(num_frames * 1000 / fps)
