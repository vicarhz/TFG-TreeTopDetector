###################################################
""" from mrcnn.model import load_image_gt
from mrcnn.model import mold_image
from mrcnn.utils import compute_ap """
#from numpy import expand_dims
#from numpy import mean
#from matplotlib.patches import Rectangle

from mrcnn.config import Config
from mrcnn.model import MaskRCNN

from matplotlib import pyplot as plt
from mrcnn.visualize import display_instances
import skimage


# define the prediction configuration
class PredictionConfig(Config):
	# define the name of the configuration
	NAME = "marble_cfg_coco"
	# number of classes (background + Blue Marbles + Non Blue marbles)
	NUM_CLASSES = 1 + 1 # fondo + treetops
	# Set batch size to 1 since we'll be running inference on
            # one image at a time. Batch size = GPU_COUNT * IMAGES_PER_GPU
	GPU_COUNT = 1
	IMAGES_PER_GPU = 1
 
# calculate the mAP for a model on a given dataset
""" def evaluate_model(dataset, model, cfg):
	APs = list()
	for image_id in dataset.image_ids:
		# load image, bounding boxes and masks for the image id
		image, image_meta, gt_class_id, gt_bbox, gt_mask = load_image_gt(dataset, cfg, image_id, use_mini_mask=False)
		# convert pixel values (e.g. center)
		scaled_image = mold_image(image, cfg)
		# convert image into one sample
		sample = expand_dims(scaled_image, 0)
		# make prediction
		yhat = model.detect(sample, verbose=0)
		# extract results for first sample
		r = yhat[0]
		# calculate statistics, including AP
		AP, _, _, _ = compute_ap(gt_bbox, gt_class_id, gt_mask, r["rois"], r["class_ids"], r["scores"], r['masks'])
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

#Model con 15 Epoch y 20 steps por epoch
model.load_weights(r"C:\Users\vicar\Downloads\Mask-RCNN-TF2\Treetop_mask_rcnn_trained_DE.h5", by_name=True)

#Model con 5 Epoch y 1 steps por epoch
#model.load_weights(r"C:\Users\vicar\Downloads\Mask-RCNN-TF2\Treetop_mask_rcnn_trained.h5", by_name=True)

# evaluate model on training dataset

## Victor, por ahora no necesito evaluar el modelo -----------------
#train_mAP = evaluate_model(dataset_train, model, cfg)
#print("Train mAP: %.3f" % train_mAP)
# ------------------------------------------------------------------
# evaluate model on test dataset
# test_mAP = evaluate_model(dataset_train, model, cfg)
# print("Test mAP: %.3f" % test_mAP)

#################################################
#Test on a single image
#Test img 1
#marbles_img = skimage.io.imread(r"C:\Users\vicar\Downloads\Mask-RCNN-TF2\tree-detection\img\test img\DJI_0400.JPG")

#Test img 2
#marbles_img = skimage.io.imread(r"C:\Users\vicar\Downloads\Mask-RCNN-TF2\tree-detection\img\test img\DJI_0401.JPG")

#Test img 3
#marbles_img = skimage.io.imread(r"C:\Users\vicar\Downloads\Mask-RCNN-TF2\tree-detection\img\test img\DJI_0385.JPG")

#Test img 4
#marbles_img = skimage.io.imread(r"C:\Users\vicar\Downloads\Mask-RCNN-TF2\tree-detection\img\test img\DJI_0354.JPG")

#Test img 5 IMAGEN COMPLETAMENTE DESCONOCIDA
marbles_img = skimage.io.imread(r"C:\Users\vicar\Downloads\Mask-RCNN-TF2\tree-detection\img\test img\DJI_0337.JPG")

# plt.imshow(marbles_img) #Por ahora no necesito ver la imagen a detectar

detected = model.detect([marbles_img])
results = detected[0]
class_names = ['BG', 'tree'] #'Blue_Marble', 'Non_Blue_Marble']

#Comentada por ahora
display_instances(marbles_img, results['rois'], results['masks'], 
                  results['class_ids'], class_names, results['scores'])

print(results)
print(results['rois'])
print('# of elements detected: ', len(results['rois']))

print("\n Done \n")
###############################


##############################################