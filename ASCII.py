import cv2, numpy as np, sys, shutil

CHARS = " ,.:-=+*#%)*@"
cap = cv2.VideoCapture(0)
w = min(120, shutil.get_terminal_size().columns - 2)

print("\033[2J", end="")  # clear screen
while True:
    ret, frame = cap.read()
    if not ret: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    h = int(w * gray.shape[0] / gray.shape[1] * 0.5)  # 0.5 = char aspect
    small = cv2.resize(gray, (w, h))
    idx = (small.astype(np.float32) / 255 * (len(CHARS) - 1)).astype(int)
    lines = ["".join(CHARS[i] for i in row) for row in idx]
    sys.stdout.write("\033[H" + "\n".join(lines))
    sys.stdout.flush()
    