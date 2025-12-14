import win32evtlog
import cv2
import time
import os
from crypto_utils import encrypt_file
from email_alert import send_email

FAILED_LIMIT = 2
SAVE_DIR = "captures"
os.makedirs(SAVE_DIR, exist_ok=True)

def failed_logins():
    server = "localhost"
    logtype = "Security"
    hand = win32evtlog.OpenEventLog(server, logtype)

    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ
    events = win32evtlog.ReadEventLog(hand, flags, 0)

    count = 0
    for event in events:
        if event.EventID == 4625:
            count += 1
    return count

def capture_intruder():
    cam = cv2.VideoCapture(0)
    time.sleep(2)
    ret, frame = cam.read()

    if not ret:
        return

    img = f"{SAVE_DIR}\\intruder_{int(time.time())}.jpg"
    cv2.imwrite(img, frame)
    cam.release()

    enc = encrypt_file(img)
    os.remove(img)
    send_email(enc)

if __name__ == "__main__":
    while True:
        if failed_logins() >= FAILED_LIMIT:
            capture_intruder()
            break
        time.sleep(10)
