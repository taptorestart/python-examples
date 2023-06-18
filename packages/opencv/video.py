import cv2
import os

"""
https://github.com/opencv/opencv-python
"""


def save_video_from_rtsp(save_path, video_filename, rtsp):
    recording_time_second = 10
    frame_per_second = 30
    video_path = os.path.join(save_path, video_filename)
    video_capture = cv2.VideoCapture(rtsp)
    if not video_capture.isOpened():
        print("Video Capture cannot open.")
        return
    video_codec = cv2.VideoWriter_fourcc(*"avc1")
    retval, video_frame = video_capture.read()
    if video_frame is not None:
        video_writer = cv2.VideoWriter(
            video_path, video_codec, frame_per_second, (video_frame.shape[1], video_frame.shape[0])
        )
        frame_index = 0

        while video_capture.isOpened():
            if frame_index == frame_per_second * recording_time_second:
                break
            retval, frame = video_capture.read()
            if not retval:
                break
            video_writer.write(frame)
            frame_index += 1

        if video_writer.isOpened():
            video_writer.release()
        video_capture.release()
        return video_path


if __name__ == "__main__":
    rtsp_url = "rtsp://Input your rtsp url here"
    video_path = save_video_from_rtsp("./", "video.mp4", rtsp_url)
