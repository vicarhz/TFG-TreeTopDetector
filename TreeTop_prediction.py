#import keras as Keras
#import tensorflow as tf

#Keras.DisablePySysConsoleLog = True

# tf.keras.utils.disable_interactive_logging()

""" import logging

logging.getLogger('tensorflow').disabled = True """


from mrcnn.config import Config
from mrcnn.model import MaskRCNN

from matplotlib import pyplot as plt

from mrcnn.visualize import display_instances

import skimage

import os
import sys


#config_name = 'myapp.cfg'
#config_path = os.path.join(sys.path[0], config_name)


# define the prediction configuration
class PredictionConfig(Config):
    # define the name of the configuration
    NAME = "marble_cfg_coco"
    # number of classes (background + Blue Marbles + Non Blue marbles)
    NUM_CLASSES = 1 + 1  # fondo + treetops
    # Set batch size to 1 since we'll be running inference on
    # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
    GPU_COUNT = 1
    IMAGES_PER_GPU = 1

# calculate the mAP for a model on a given dataset


""" def evaluate_model(dataset, model, cfg):
    APs = list()
    for image_id in dataset.image_ids:
        # load image, bounding boxes and masks for the image id
        image, image_meta, gt_class_id, gt_bbox, gt_mask = load_image_gt(
            dataset, cfg, image_id, use_mini_mask=False)
        # convert pixel values (e.g. center)
        scaled_image = mold_image(image, cfg)
        # convert image into one sample
        sample = expand_dims(scaled_image, 0)
        # make prediction
        yhat = model.detect(sample, verbose=0)
        # extract results for first sample
        r = yhat[0]
        # calculate statistics, including AP
        AP, _, _, _ = compute_ap(
            gt_bbox, gt_class_id, gt_mask, r["rois"], r["class_ids"], r["scores"], r['masks'])
        # store
        APs.append(AP)
    # calculate the mean AP across all images
    mAP = mean(APs)
    return mAP """

# create config
cfg = PredictionConfig()
# define the model
model = MaskRCNN(mode='inference', model_dir='logs', config=cfg)
# load model weights


# print('# of Trees detected: ', len(results['rois']))
#print("Ruta donde esta el file: ", sys.path[0])
#print("Ruta donde esta el file: ", sys.path[1])
#print("PATH OTRO: ", os.path.abspath("./"))
config_name = os.path.abspath("./")
model_name = "\Treetop_mask_rcnn_trained_DE.h5"
config_path = config_name + model_name

""" Just for test purpose """
#config_path = r"C:\Users\vicar\Downloads\test TFG con Rafa\maskrcnn\Treetop_mask_rcnn_trained_DE.h5"  # comentar para prod

#config_path = os.path.join(config_name, model_name)
""" print("MAIN PATH: ", config_path) """

# Model con 15 Epoch y 20 steps por epoch
model.load_weights(config_path, by_name=True)
