from PIL import Image
from pillow_heif import register_heif_opener
import os
SourceFolder="E:/100-Photo/Turkish/"
TargetFolder="E:/100-Photo/TurkishJPG/"

register_heif_opener()
heic_photo = [photo for photo in os.listdir(SourceFolder) if '.heic' in photo]
# print(heic_files)
for photo in heic_photo:
  temp_img = Image.open(SourceFolder + photo)
  png_photo = photo.replace('.heic','.jpg')
  temp_img.save(TargetFolder + png_photo)