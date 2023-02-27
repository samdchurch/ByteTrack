# ByteTrack

Official ByteTrack github: https://github.com/ifzhang/ByteTrack

tracking_test.py shows a byte being used on the files found in test_data

1. Create a tracker object (Byte/byte_tracker.py)
2. Store every detection in a Detection object (Byte/detection.py)
3. Call tracker.predict()
4. Call tracker.update(detections, classes) for the detections for that frame
5. Call tracker.get_current_tracks() to get tracking information
