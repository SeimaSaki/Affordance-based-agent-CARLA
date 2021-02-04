# Affordance-based-agent-CARLA

## Introduction
There are three approaches in the end-to-end driving model:
 1. Imitation Learning: During the training phase, the user manually drives the car and the model captures the camera images and tries to map it with the driving the driving actions such as, accelarator, break and steering angle.  
 2. Mediated Perception: During the training phase, individual objects are detected, such as traffic light, humans or other vehicles on the lane and the model tries to calculate the distance to the particular object to take the necessary driving actions.
 3. Direct Perception: In direct perception, the complexity of the object detection is avoided instead the model is trained to calculate the features such as the distance to the object in the front, lane angle, traffic light, etc, directly from the camera images.
 
 The goal of this project is to implement an affordance based end-to-end driving model and simulate it in the urban simulator called CARLA.
