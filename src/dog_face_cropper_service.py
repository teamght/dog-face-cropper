#import numpy as np
#from PIL import Image
#from datetime import datetime

from .dog_face_cropper import DogFaceCropper

dfc = DogFaceCropper('./src/detectors')

class DogFaceCropperService():

    def __init__(self):
        pass

    #def recortar_imagen_mascota(self, data):
    #    print('Inicio de Service para recortar imagen ({})'.format(datetime.now()))
    #    try:
    #        predict_image_array = np.array(Image.open(data))
    #        flag, new_image_array = dfc.process_image(predict_image_array)
    #        print('Fin de Service para recortar imagen ({})'.format(datetime.now()))
    #        if flag:
    #            return True, new_image_array
    #    except Exception as e:
    #        print('Hubo un error al procesar imagen ({})'.format(datetime.now()))
    #        print('Hubo un error. {}'.format(e))
    #    return False, None
    def recortar_imagen_mascota(self, image_path, new_name_image_path):
        dfc.process_file(image_path, new_name_image_path)
