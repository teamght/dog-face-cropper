import dlib
import cv2
import os
import imutils

from .utils import download_image, show_with_points
from .rotate import DogFaceRotate
from .crop import DogFaceCrop
from .resize import DogFaceResize

class DogFaceCropper():

  def __init__(self, detectors_path):
  
    detector = dlib.cnn_face_detection_model_v1(os.path.join(detectors_path, 'dogHeadDetector.dat'))
    predictor = dlib.shape_predictor(os.path.join(detectors_path, 'landmarkDetector.dat'))
    
    self.rotator = DogFaceRotate(detector, predictor)
    self.cropper = DogFaceCrop(detector, predictor)
    self.resizer = DogFaceResize()

  def process_image(self, img):
  
    tracking = {}
  
    show_with_points(img, [], figsize=(4, 4))
    #img_result = img.copy()

    img_resized = self.resizer.input_resize(img, max_size = 300)
    tracking['ratio'] = img_resized.shape[0]/img.shape[0] # using height

    img_rotated, tracking['angle'] = self.rotator.rotate(img_resized)
    #show_with_points(img_rotated, [])

    img_cropped, tracking['cropping_points'] = self.cropper.crop(img_rotated)
    #show_with_points(img_cropped, [])
    
    img_reprocessed = self.reprocess(img, tracking)

    img_resized = self.resizer.final_resize(img_reprocessed)
    show_with_points(img_resized, [], figsize=(4, 4))
    
    return img_resized
    
  def reprocess(self, img, tracking):
    img = imutils.rotate_bound(img, tracking['angle'])
    adjused_cropping_points = tuple([round(p/tracking['ratio']) for p in tracking['cropping_points']])
    return self.cropper.crop_with_padding(img, *adjused_cropping_points)

  def process_file(self, img_path, save_as_path = None):
    try:
      img = cv2.imread(img_path)
      img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      
      img_processed = self.process_image(img)

      if save_as_path is not None:
        img_out = cv2.cvtColor(img_processed, cv2.COLOR_RGB2BGR)
        cv2.imwrite(save_as_path, img_out)
    except Exception as e:
      print(e)
