import rpa as r

def main():
    # mouse move to 100, 100
    r.init(visual_automation=True)
    r.mouse_move(100, 100)
    r.mouse_down()
    r.mouse_up()


if __name__ == "__main__":
    main()
