def gifmaster(imgin,imgout):
    imgs = (Image.open(f) for f in sorted(glob.glob(imgin)))
    img = next(imgs)  # extract first image from iterator
    img.save(fp=imgout, format='GIF', append_images=imgs,save_all=True, duration=200, loop=0)