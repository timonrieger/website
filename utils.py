import os
from PIL import Image, ExifTags
from fractions import Fraction

PHOTOS_DIR = 'static/images/photography'


def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data is not None:
        exif = {
            ExifTags.TAGS.get(tag): value
            for tag, value in exif_data.items()
            if tag in ExifTags.TAGS
        }
        return exif
    else:
        return None

def get_exposure_info(exif):
    aperture = exif.get("FNumber")
    shutter_speed = exif.get("ExposureTime")
    iso = exif.get("ISOSpeedRatings")
    if aperture and shutter_speed and iso:
        aperture_value = aperture.numerator / aperture.denominator
        shutter_speed_value = Fraction(shutter_speed).limit_denominator()
        exposure_info = f" | f{aperture_value} | {shutter_speed_value}s | ISO {iso}"
        return exposure_info
    return ""

def get_camera_info(exif):
    lens = exif.get("LensModel")
    model = exif.get("Model", "").strip()
    lens_mm = round(exif.get("FocalLength"), 0)
    if model and lens:
        return f" | {lens} | {model} | {lens_mm}mm"
    return ""

def build_photo_list():
    all_photos = []
    for filename in os.listdir(PHOTOS_DIR):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(PHOTOS_DIR, filename)
            exif = get_exif_data(image_path)
            exposure_info = get_exposure_info(exif) if exif else None
            camera_info = get_camera_info(exif) if exif else None
            photo_info = {
                "filename": filename,
                "camera": camera_info,
                "exposure": exposure_info,
                "date": exif['DateTimeOriginal']
            }
            all_photos.append(photo_info)
    return all_photos

