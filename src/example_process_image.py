from dog_face_cropper import DogFaceCropper
import cv2

# creamos una instancia de la clase (esta instancia luego puede utilizarse indefinidamente)
dfc = DogFaceCropper('detectors')

# cargamos la imagen en memoria y la preprocesamos
img = cv2.imread('example_image.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# generamos la imagen recortada
img_processed = dfc.process_image(img)

# guardamos la imagen recortada
img_out = cv2.cvtColor(img_processed, cv2.COLOR_RGB2BGR)
cv2.imwrite('processed_image.jpg', img_out)
