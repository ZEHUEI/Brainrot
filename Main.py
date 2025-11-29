import cv2
import mediapipe as mp
import numpy as np

base = cv2.imread("images/BASE.jpeg")
haha = cv2.imread("images/HAHA.jpeg")
huh = cv2.imread("images/HUH.jpeg")
yes = cv2.imread("images/YES.jpeg")

base = cv2.resize(base, (400, 400))
haha = cv2.resize(haha, (400, 400))
huh = cv2.resize(huh, (400, 400))
yes = cv2.resize(yes, (400, 400))

mp_face = mp.solutions.face_mesh
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

def mouth_open(landmarks, img_w, img_h):
    top_lip = landmarks[13]
    bot_lip = landmarks[14]

    top = np.array([top_lip.x * img_w, top_lip.y * img_h])
    bot = np.array([bot_lip.x * img_w, bot_lip.y * img_h])
    return np.linalg.norm(top - bot)

with mp_face.FaceMesh(refine_landmarks=True) as face_mesh, \
     mp_hands.Hands(max_num_hands=1) as hands:

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        img_h, img_w, _ = frame.shape
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        face_results = face_mesh.process(rgb)
        hand_results = hands.process(rgb)

        # FACE detection block
        if face_results.multi_face_landmarks:
            lm = face_results.multi_face_landmarks[0].landmark
            ratio = mouth_open(lm, img_w, img_h)

            if ratio > 20:
                cv2.imshow("MOUTH MEME", haha)

        if hand_results.multi_hand_landmarks:
            cv2.imshow("HAND MEME", yes)

        cv2.imshow("nothing",base)

        frame_small = cv2.resize(frame, (320, 240))
        cv2.imshow("Camera", frame_small)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
