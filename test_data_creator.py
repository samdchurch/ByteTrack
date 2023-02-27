import cv2


def convert_video_to_frames(path, frame_names):
    cap = cv2.VideoCapture(path)

    i = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if ret == False:
            break
        cv2.imwrite('test_data/' + frame_names + '_' + str(i) + '.jpg', frame)
        i += 1

    cap.release()
    cv2.destroyAllWindows()


def bounding_box_labeler(start_idx, end_idx):
    for i in range(start_idx, end_idx):
        name = 'kitten_' + str(i)
        with open(name + '.txt', 'w') as f:
            img = cv2.imread('test_data/' + name + '.jpg')
            r = (-1, -1, -1, -1)
            while r != (0, 0, 0, 0):
                r = cv2.selectROI('kitten frame', img)
                tl_x = r[0]
                tl_y = r[1]
                br_x = r[0] + r[2]
                br_y = r[1] + r[3]

                if r != (0, 0, 0, 0):
                    f.write(str(tl_x) + ',' + str(tl_y) + ',' + str(br_x) + ',' + str(br_y) + '\n')


def draw_bounding_boxes():
    for i in range(1, 6):
        name = 'kitten' + str(i)
        img = cv2.imread('test_frames/' + name + '.jpg')
        with open(name + '.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                coord = line.split(',')
                for j in range(len(coord)):
                    coord[j] = int(coord[j])

                cv2.rectangle(img, coord[:2], coord[2:], (0, 255, 0), 1)

        cv2.imshow(name, img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


bounding_box_labeler(2910, 2970)
