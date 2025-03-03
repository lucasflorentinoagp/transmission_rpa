import pyautogui as r

def main():
    # mouse move to x=100, y=100
    r.moveTo(100, 100)
    # mouse move to x=200, y=200 in 2 seconds
    r.moveTo(200, 200, 2)
    # mouse move to x=300, y=300 in 2 seconds with linear movement
    r.moveTo(300, 300, 2, r.easeInOutQuad)
    # mouse move to x=400, y=400 in 2 seconds with linear movement
    r.moveTo(400, 400, 2, r.easeInOutQuad)


if __name__ == "__main__":
    main()
