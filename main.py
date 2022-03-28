import time
import cv2
from cv2.legacy import TrackerBoosting_create, TrackerTLD_create, TrackerMedianFlow_create, TrackerMOSSE_create

from CustomTracker import CustomTracker

tracker_types = ['BOOSTING', 'MIL', 'KCF', 'TLD', 'MEDIANFLOW', 'GOTURN', 'MOSSE', 'CSRT']
tracker_type = tracker_types[6]

if tracker_type == 'BOOSTING':
    tracker = TrackerBoosting_create()
elif tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()
elif tracker_type == 'KCF':
    tracker = cv2.TrackerKCF_create()
elif tracker_type == 'TLD':
    tracker = TrackerTLD_create()
elif tracker_type == 'MEDIANFLOW':
    tracker = TrackerMedianFlow_create()
elif tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()
elif tracker_type == 'MOSSE':
    tracker = TrackerMOSSE_create()
elif tracker_type == "CSRT":
    tracker = cv2.TrackerCSRT_create()

custom_tracker = CustomTracker(tracker)
path = '/media/serg/0078-EC6B/1.mp4'
cap = cv2.VideoCapture(path)
status, frame = cap.read()

cv2.namedWindow('image', 0)
bbox = cv2.selectROI('image', frame, False)

# Initialize tracker with first frame and bounding box
ok = custom_tracker.init(frame, bbox)
while status:
    status, frame = cap.read()
    t1 = time.time()
    ok, bbox = custom_tracker.update(frame)
    print(ok)
    t2 = time.time()
    print(t2-t1)
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    cv2.imshow('image', frame)
    cv2.waitKey()
