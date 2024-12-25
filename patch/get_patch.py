def get_patch():
    import openslide

    slide = openslide.OpenSlide('/data1/tdiprima/dataset/PC_058_0_1/PC_058_0_1.svs')
    patch = slide.read_region((119808, 55808), 0, (512, 512))
    # newImg1 = PIL.Image.new('RGB', (512,512))
    patch.save("img1.png")
    slide.close()


def zoom_levels():
    arr = [361.7635036496351, 311.793522783644, 155.896761391822, 77.948380695911, 38.9741903479555, 19.48709517397775,
           9.743547586988875, 4.871773793494437, 2.4358868967472187, 1.2179434483736093, 0.6089717241868047]

    for i in range(len(arr)):
        try:
            print("{} - {} = {}".format(arr[i], arr[i + 1], arr[i] - arr[i + 1]))
        except:
            print('end')


zoom_levels()
