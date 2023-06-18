import cv2
import os

"""
https://github.com/opencv/opencv-python
"""


def get_image_from_rtsp(rtsp_url):
    video_capture = cv2.VideoCapture(rtsp_url)
    if not video_capture.isOpened():
        print("Video Capture cannot open.")
        return
    retval, video_image = video_capture.read()
    if video_image is not None:
        print("frame.shape[1]: {}".format(video_image.shape[1]))
        print("frame.shape[0]: {}".format(video_image.shape[0]))
    return video_image


def save_image_from_rtsp(save_path, image_filename, rtsp_url):
    video_capture = cv2.VideoCapture(rtsp_url)
    if not video_capture.isOpened():
        print("Video Capture cannot open.")
        return
    retval, video_image = video_capture.read()
    if video_capture.isOpened():
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        save_image_path = os.path.join(save_path, image_filename)
        cv2.imwrite(save_image_path, video_image)
        video_capture.release()
    else:
        save_image_path = None
    return save_image_path


if __name__ == "__main__":
    rtsp_url = "rtsp://Input your rtsp url here"
    frame = get_image_from_rtsp(rtsp_url)
    image_path = save_image_from_rtsp("./", "image.jpg", rtsp_url)
