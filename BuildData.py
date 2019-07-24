from matplotlib import pyplot as plt
import numpy as np
import pickle
import os
import cv2
from tqdm import tqdm

# CATEGORY = ["Dog","Cat"]
# directory = "./kagglecatsanddogs/PetImages"

def create_data(CATEGORY, directory, size, x_name, y_name):
  training_data=[]

  for category in CATEGORY:
    path = os.path.join(directory, category)
    class_num = CATEGORY.index(category)

  for img in tqdm(os.listdir(path)):
    try:
      img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_COLOR)
      new_array = cv2.resize(img_array, (size, size))
      training_data.append([new_array, class_num])
      # plt.imshow(img_array)
      # plt.show()
    except:
      pass
  save_data_to_pickle(training_data, x_name, y_name)


def save_data_to_pickle(training_data, x_name, y_name):
  X =[]
  y =[]

  for features, label in training_data:
    X.append(features)
    y.append(label)

  pickle_in = open(x_name, "wb")
  pickle.dump(X, pickle_in)
  pickle_in.close()

  pickle_in = open(y_name, "wb")
  pickle.dump(y, pickle_in)
  pickle_in.close()


def read_data_in_pickle(x_name, y_name):
  X =[]
  y =[]

  pickle_out = open(x_name, "rb")
  X= pickle.load(pickle_out)  

  pickle_out = open(y_name, "rb")
  y =pickle.load(pickle_out)

  print(X[0])

  # plt.imshow(X[0])
  
# create_data(["Dog", "Cat"], "./kagglecatsanddogs/PetImages", 120, "X.pickle", "y.pickle")
read_data_in_pickle("X.pickle", "y.pickle")