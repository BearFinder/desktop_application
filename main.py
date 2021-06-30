from desktop import run_application
from detector import image_pillow, init


if __name__ == '__main__':
    init("model.pth")
    print("F")
    run_application(image_pillow)