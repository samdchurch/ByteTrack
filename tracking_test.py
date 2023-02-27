import numpy as np
import cv2

from BYTE.byte_tracker import Tracker, NearestNeighborDistanceMetric
from BYTE.detection import Detection
import torch

metric = NearestNeighborDistanceMetric(metric='cosine', matching_threshold=.7)
tracker = Tracker(metric=metric, n_init=3)
detections = []

for i in range(2910, 2970):
    file_name = 'test_data/kitten_' + str(i) + '.txt'
    lines = []
    with open(file_name, 'r') as f:
        lines = np.array(f.readlines())

    detections = []

    for line in lines:
        vals = line.split(',')
        for j in range(len(vals)):
            vals[j] = float(vals[j])

        tlwh = [vals[0], vals[1], vals[2] - vals[0], vals[3] - vals[1]]

        det = Detection(tlwh=tlwh, confidence=np.random.rand(), feature=[1, 1])

        detections.append(det)

    classes = torch.tensor([1]*len(lines))

    tracker.predict()
    tracker.update(detections, classes)

    img = cv2.imread('test_data/kitten_' + str(i) + '.jpg')
    tracks = tracker.get_current_tracks()

    for t in tracks:
        color = None

        if t[4] == 1:
            color = [255, 0, 0]
        elif t[4] == 2:
            color = [0, 255, 0]
        elif t[4] == 3:
            color = [0, 0, 255]
        elif t[4] == 4:
            color = [255, 255, 0]
        elif t[4] == 5:
            color = [255, 0, 255]

        cv2.rectangle(img, (t[0], t[1]), (t[2], t[3]), color, 1)

    cv2.imshow('kittens', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()



