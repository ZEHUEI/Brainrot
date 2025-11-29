import cv2
import mediapipe as mp

base = cv2.resize(cv2.imread("images/BASE.jpeg"), (400, 400))
haha = cv2.resize(cv2.imread("images/HAHA.jpeg"), (400, 400))
huh = cv2.resize(cv2.imread("images/HUH.jpeg"), (400, 400))
yes = cv2.resize(cv2.imread("images/YES.jpeg"), (400, 400))

cap = cv2.VideoCapture(0)