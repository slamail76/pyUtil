from heic2png import HEIC2PNG

if __name__ == '__main__':
    heic_img = HEIC2PNG('original.heic', quality=90)  # Specify the quality of the converted image
    heic_img.save()  # The converted image will be saved as `test.png`