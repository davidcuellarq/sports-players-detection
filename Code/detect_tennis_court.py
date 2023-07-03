import cv2
import numpy as np

def detect_tennis_court(path):
    """
    Detects the tennis court in a video file and saves the output video.

    Parameters:
    path: The path to the video file.
    """

    cap = cv2.VideoCapture(path)

    # Create a new video file called `video_output#.mp4` in the `VideoOutput` folder.
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    output_video = cv2.VideoWriter('VideoOutput/video_output8.mp4', fourcc, 20.0, (640, 480))

    while cap.isOpened:
        ret, frame = cap.read()

        if not ret:
            break

        gray = _threshold(frame)

        # Apply Canny edge detection.
        edges = cv2.Canny(gray, 100, 200)

        # Find the lines of the tennis court.
        lines = cv2.HoughLinesP(edges, rho=1, theta=np.pi / 180, threshold=100, minLineLength=25, maxLineGap=50)

                # Choose the strongest edges.
        strongest_lines = []
        for line in lines:
            votes = np.sum(line, axis=0)
            if np.max(votes) > 500:
                strongest_lines.append(line)

        # Draw the strongest lines of the tennis court on the frame.
        for line in strongest_lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        # Show the frame.
        cv2.imshow('Tennis Court Detection', frame)
        output_video.write(frame)

        # Quit if the user presses `q`.
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    output_video.release()

def _threshold(frame):
    """
    Simple thresholding for white pixels
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)[1]
    return gray

if __name__ == '__main__':
    path = 'VideoInput/video_input8.mp4'
    detect_tennis_court(path)