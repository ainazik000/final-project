from PIL import Image
from errors import ChoiceError

def make_bw(img_pathes):
    for img_path in img_pathes:
        img = Image.open(img_path).convert('L')
        pathh = img_path.split('/')
        print(pathh)
        fr = pathh[-1].split('.')
        ptr = '/'.join(pathh[:-1])
        new_path = f'{ptr}/{fr[0]}_bw.{fr[1]}'
        img.save(new_path)


def change_contrast(img_pathes, option, level=100):
    if option == 'Contrast':
        for img_path in img_pathes:
            img = Image.open(img_path)
            factor = (259 * (level + 255)) // (255 * (259 - level))
            def contrast(c):
                value = 128 + factor * (c - 128)
                return max(0, min(255, value))
            imgg = img.point(contrast)
            pathh = img_path.split('/')
            fr = pathh[-1].split('.')
            ptr = '/'.join(pathh[:-1])
            new_path = f'{ptr}/{fr[0]}_contrast.{fr[1]}'
            imgg.save(new_path)
    elif option == 'Black and white':
        make_bw(img_pathes=img_pathes)
    else:
        raise ChoiceError()
