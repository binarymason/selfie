import argparse
import cv2
import datetime
import pathlib

def take_selfie(cam):
    ret_val, img = cam.read()
    return img

def put_text(img, text, point=(10,10)):
    height, width = img.shape[:2]

    font                   = cv2.FONT_HERSHEY_SIMPLEX
    bottomLeftCornerOfText = (10,height-20)
    fontScale              = 0.5
    fontColor              = (255,255,255)
    lineType               = 1

    cv2.putText(img, text, bottomLeftCornerOfText, font, fontScale, fontColor, lineType)

    return img

def save(im, output=None):
    assert output is not None
    cv2.imwrite(str(output), im)
    print("saved selfie to:", output)

def display(im, title=None):
    if title is None:
        title = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    cv2.imshow(title, im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_timestamp():
    return datetime.datetime.now().strftime("%D %T")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Take selfies of yourself')
    parser.add_argument("-d", "--device", default=0, help="Video device to take picture")
    parser.add_argument("-o", "--output", default=".", help="Directory to dump selfie")
    parser.add_argument("--show", default=False, action="store_true" , help="Display image after taking selfie")
    parser.add_argument("--skip-save", default=False, action="store_true" , help="Skip saving the image")

    args = parser.parse_args()

    img = take_selfie(cv2.VideoCapture(args.device))
    ts = get_timestamp()
    put_text(img, ts)
    title = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")

    if not args.skip_save:
        output_dir = pathlib.Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        filename = title + ".png"
        save(img, output=output_dir/filename)

    if args.show:
        display(img, title=title)
