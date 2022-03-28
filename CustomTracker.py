class CustomTracker:
    def __init__(self, tracker):
        self.tracker = tracker
        self.bbox = None
        self.status = None
        self.w = None
        self.h = None

    def init(self, frame, bbox):
        self.status = self.tracker.init(frame, bbox)
        self.h, self.w = frame.shape[:2]
        return self.status

    def update(self, frame):
        self.status, self.bbox = self.tracker.update(frame)
        return self.status, self.bbox
