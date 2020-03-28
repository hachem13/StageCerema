# import the necessary packages
from keras.preprocessing.image import img_to_array
from keras.models import load_model
import numpy as np
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained model model")
ap.add_argument("-c", "--chemin", required=True,
	help="path to input chemin")
ap.add_argument("-i", "--image", required=True,
	help="path to input image")
ap.add_argument("-r", "--result", required=True,
	help="path to input result")
args = vars(ap.parse_args())

print(ap)

# # load the image
# image = cv2.imread(args["chemin"]+args["image"])
# orig = image.copy()
 
# # pre-process the image for classification
# image = cv2.resize(image, (150, 150))
# image = image.astype("float") / 255.0
# image = img_to_array(image)
# image = np.expand_dims(image, axis=0)

# # load the trained convolutional neural network
# print("[INFO] loading network...")
# model = load_model(args["model"])
 
# # classify the input image
# value_predict = model.predict(image)[0][0]
# print(value_predict)
# formulation = "[INFO] parking = "+str((1-value_predict)*100)+" %" if value_predict < 0.5 else "[INFO] non_parking = "+str(value_predict*100)+" %"
# print(formulation)

# # build the label
# label = "parking" if value_predict < 0.5 else "non_parking"
# label = "{}: {:.2f}%".format(label, (1-value_predict) * 100) if value_predict < 0.5 else "{}: {:.2f}%".format(label, value_predict * 100)

# # draw the label on the image
# output = imutils.resize(orig, width=400)
# cv2.putText(output, label, (10, 25),  cv2.FONT_HERSHEY_SIMPLEX,
# 	0.7, (0, 255, 0), 2)
 
# # show the output image
# cv2.imshow("Output", output)
# cv2.imwrite(args["result"]+args["image"],output)
# #cv2.waitKey(0)# import the necessary packages


