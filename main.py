# import cv2
# import mediapipe as mp

# cap = cv2.VideoCapture(0)
# mpHands = mp.solutions.hands
# hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils
# while True:
#     success, image = cap.read()
#     imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(imageRGB)

#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks: # working with each hand
#             for id, lm in enumerate(handLms.landmark):
#                 h, w, c = image.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)

#                 if id == 20 :
#                     cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

#                 mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
#                 cv2.imshow("Output", image)
#                 cv2.waitKey(1)
# import cv2
# import mediapipe as mp

# cap = cv2.VideoCapture(0)
# cap.set(3, 640)  # Set lower width resolution
# cap.set(4, 480)  # Set lower height resolution

# mpHands = mp.solutions.hands
# hands = mpHands.Hands()
# mpDraw = mp.solutions.drawing_utils

# while True:
#     success, image = cap.read()
#     imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
#     results = hands.process(imageRGB)

#     if results.multi_hand_landmarks:
#         for handLms in results.multi_hand_landmarks:
#             for id, lm in enumerate(handLms.landmark):
#                 h, w, c = image.shape
#                 cx, cy = int(lm.x * w), int(lm.y * h)

#                 if id == 20:
#                     cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)

#         mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

#     cv2.imshow("Output", image)
#     cv2.waitKey(1)
import cv2
import mediapipe as mp
import pyautogui
import math

wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

screen_width, screen_height = pyautogui.size()
prev_x, prev_y = 0, 0
is_clicking = False

while True:
    success, image = cap.read()
    imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(imageRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                screen_x = int(cx * screen_width)
                screen_y = int(cy * screen_height)

                if id == 20:
                    cv2.circle(image, (cx, cy), 25, (255, 0, 255), cv2.FILLED)
                    dx = cx - prev_x
                    dy = cy - prev_y
                    direction = math.atan2(dy, dx)
                    pyautogui.moveRel(dx, dy)
                    prev_x, prev_y = cx, cy

                    if lm.y < handLms.landmark[17].y and lm.y < handLms.landmark[4].y:
                        if not is_clicking:
                            pyautogui.click(button='left')
                            is_clicking = True
                    else:
                        is_clicking = False

        mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("AI Mouse", image)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
