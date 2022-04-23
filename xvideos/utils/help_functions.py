import cv2


def get_fps(capture: cv2.VideoCapture) -> int:
    """

    Get fps from video capture.

    Parameters
    ----------
    capture: cv2.VideoCapture
        Opencv video capture.

    Returns
    -------
    int

    """
    return int(capture.get(cv2.CAP_PROP_FPS))


def count_frames(capture: cv2.VideoCapture) -> int:
    """

    Get number of frames from video capture.

    Parameters
    ----------
    capture: cv2.VideoCapture
        Opencv video capture.

    Returns
    -------
    int

    """
    return int(capture.get(cv2.CAP_PROP_FRAME_COUNT))


def video_duration(capture: cv2.VideoCapture) -> int:
    """

    Get video duration in milliseconds

    Parameters
    ----------
    capture: cv2.VideoCapture
        Opencv video capture.

    Returns
    -------
    int

    """
    fps = get_fps(capture)
    num_frames = count_frames(capture)
    return int(num_frames * 1000 / fps)
