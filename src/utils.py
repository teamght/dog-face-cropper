import urllib
import imghdr
import time
import shutil
import cv2
import matplotlib.pyplot as plt
from imutils import face_utils
import os

def download_image(img_url):
  tmp_path, _ = urllib.request.urlretrieve(img_url)
  ext = imghdr.what(tmp_path)
  to = str(time.time()).replace('.', 's') + '.' + ('unknown' if ext is None else ext)
  shutil.copyfile(tmp_path, to)
  return to

def show_with_points(img, points, figsize=(16, 16)):
  img_result = img.copy()
  for i, p in enumerate(points):
    p = (round(p[0]), round(p[1]))
    cv2.circle(img_result, center=p, radius=3, color=(0,0,255), thickness=-1, lineType=cv2.LINE_AA)
    cv2.putText(img_result, str(i), p, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1, cv2.LINE_AA)
  plt.figure(figsize=figsize)
  plt.imshow(img_result)

def get_detection_and_shape(detector, predictor, img):
  dets = detector(img, upsample_num_times=1)
  assert len(dets) == 1, f"Se necesitaba 1 cara, se encontraron {len(dets)}" # Ver qué hago en estos casos... (quedarme con la mas grande? la que tiene mayor confidence?)
  d = dets[0]
  shape = predictor(img, d.rect)
  shape = face_utils.shape_to_np(shape)
  return d, [tuple(x) for x in shape]

def eliminar_archivos_temporales(filename):
  try:
    print('Eliminar el archivo temporal {}'.format(filename))
    os.remove(filename)
  except AssertionError as error:
    print(error)
    print('Error al eliminar el archivo temporal {}'.format(filename))