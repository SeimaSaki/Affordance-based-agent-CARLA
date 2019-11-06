from __future__ import print_function, division
import torch
import torchvision
from torchvision import datasets, models, transforms
import torch.nn as nn
import time
import numpy as np
from torch.autograd import Variable
from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os
import torch.optim as optim
from torch.optim import lr_scheduler
import copy
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random
import sys
from random import randint
from skimage import io, transform

##########################################################
# pytorch util functions 
##########################################################

def load_checkpoint(filename) :
    #print(filename)
    checkpoint = torch.load(filename)
    model_state_dict = checkpoint['model_state_dict']
    optimizer_state_dict = checkpoint['optimizer_state_dict']
    epoch = checkpoint['epoch']
    loss = checkpoint['loss']
    return [model_state_dict, optimizer_state_dict, epoch, loss]

def save_checkpoint(model, optimizer, epoch, loss, filename):
    print("Saving Checkpoint....")
    model_state_dict = model.state_dict()
    optimizer_state_dict = optimizer.state_dict()
#     print("model_state_dict : ", model_state_dict)
#     print("optimizer_state_dict : ", optimizer_state_dict)
#     print("Epoch : ", epoch)
#     print("filename : ", filename)

    torch.save({
            'epoch': epoch,
            'model_state_dict': model_state_dict,
            'optimizer_state_dict': optimizer_state_dict,
            'loss': loss
            }, filename)
    print("Saving Checkpoint Done")

def display_image(image) : 
    plt.show(image)