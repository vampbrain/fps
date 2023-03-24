import cv2

# Open input video file
input_video = cv2.VideoCapture("rickroll_5s.mp4")

# Get input video properties
fps = input_video.get(cv2.CAP_PROP_FPS)
width = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Define output video file properties
output_fps = fps * 0.75  
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
output_video = cv2.VideoWriter("output_video.mp4", fourcc, output_fps, (width, height))

frame_count = 0
while True:
    e, frame = input_video.read()
    if not e:
        break
    if frame_count % 4 == 0:
        output_video.write(frame)
    frame_count += 1

# Release resources
input_video.release()
output_video.release()
cv2.destroyAllWindows()
