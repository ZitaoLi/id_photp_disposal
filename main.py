import id_photo_bg as ipb


def main():
    img = ipb.read_img('img/1436234-36bd210160f15f9f.jpg')
    ipb.change_bg(img, ipb.RED_BG, ipb.BULE_BG)

    img = ipb.read_img('img/d90461920e2a4061b69963252250891f.jpg')
    ipb.change_bg(img, ipb.BULE_BG, ipb.WHITE_BG)

    img = ipb.read_img('img/4034970a304e251fc2868759ad86c9177f3e5319.jpg')
    ipb.change_bg(img, ipb.BULE_BG, ipb.RED_BG)


if __name__ == "__main__":
    main()
