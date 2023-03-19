import cv2
import time


def ex_1():
    img_1 = cv2.imread('image_1.jpg')
    res = cv2.resize(img_1, dsize=(256, 256))
    cv2.imshow('image', res)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

    big_image = cv2.resize(res, (0, 0), fx=2, fy=2)
    cv2.imshow('image', big_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)


def ex_2_3():
    cap = cv2.VideoCapture(0)
    down_points = (640, 480)
    object_detector = cv2.createBackgroundSubtractorMOG2(varThreshold=100)
    time_start = time.time()
    cnt_left = 0
    cnt_right = 0

    while time.time() - time_start < 25:
        ret, frame = cap.read()
        frame = cv2.resize(frame, down_points)
        height, width, _ = frame.shape

        black = object_detector.apply(frame)
        _, black = cv2.threshold(black, 253, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 900:
                cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 2)
                x, y, w, h = cv2.boundingRect(cnt)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                if x < 320 and x + w < 320:
                    cnt_left += 1
                if x > 320 and x + w > 320:
                    cnt_right += 1

        cv2.imshow("Frame", frame)
        cv2.imshow("Black", black)
        cv2.waitKey(1)

    cap.release()

    print('cnt_left = ', cnt_left)
    print('cnt_right = ', cnt_right)


def extra():
    cap = cv2.VideoCapture(0)
    img_2 = cv2.imread('fly64.jpg')

    down_points = (640, 480)
    object_detector = cv2.createBackgroundSubtractorMOG2(varThreshold=100)
    time_start = time.time()
    cnt_left = 0
    cnt_right = 0

    while time.time() - time_start < 25:
        ret, frame = cap.read()
        frame = cv2.resize(frame, down_points)
        height, width, _ = frame.shape

        black = object_detector.apply(frame)
        _, black = cv2.threshold(black, 253, 255, cv2.THRESH_BINARY)
        contours, _ = cv2.findContours(black, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 900:
                cv2.drawContours(frame, [cnt], -1, (0, 0, 255), 2)
                x, y, w, h = cv2.boundingRect(cnt)

                res = cv2.resize(img_2, dsize=(w, h))
                cv2.imshow("Муха", res);
                cv2.waitKey(1)
                cv2.moveWindow("Муха", x, y)
                time.sleep(0.1)
                cv2.destroyWindow("Муха")

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
                if x < 320 and x + w < 320:
                    cnt_left += 1
                if x > 320 and x + w > 320:
                    cnt_right += 1

        cv2.imshow("Frame", frame)
        cv2.imshow("Black", black)
        cv2.waitKey(1)

    cap.release()


ex_1()
time.sleep(5)
ex_2_3()
time.sleep(2)
# Перед запуском доп. задания я поместил окно в левый верхний угол.
# Понимаю, что сделал не совсем то, что написано в задании.
# Получилось реализовать лишь вариант с новым окном, в котором появляется изображение мухи.
# Бывают ситуации, когда изображение мухи не в центре метки. Это связано с тем, что условия неидеальные.
# В лучшем случае муха в рамке большого квадрата будет перекрывать изображения мух в более маленьком.
# Поскольку иногда распознаются внутренние контуры метки, а не внешние, получается "муха в метке" или смещенная муха.
extra()
