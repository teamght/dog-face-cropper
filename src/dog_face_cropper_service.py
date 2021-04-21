from .dog_face_cropper import DogFaceCropper

dfc = DogFaceCropper('./src/detectors')

class DogFaceCropperService():

    def __init__(self):
        pass

    def recortar_imagen_mascota(self, image_path, new_name_image_path):
        dfc.process_file(image_path, new_name_image_path)
