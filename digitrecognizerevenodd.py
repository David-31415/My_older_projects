import math
import numpy as np
import h5py
import matplotlib.pyplot as plt
from matplotlib.pyplot import imread
from scipy.io import loadmat
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# Load MNIST dataset
mnist = tf.keras.datasets.mnist

(X_train, Y_train), (X_test, Y_test) = mnist.load_data()

# Normalize the pixel values to be between 0 and 1
X_train, X_test = X_train / 255.0, X_test / 255.0

X_train = X_train.reshape(X_train.shape[0], 28*28).T
X_test = X_test.reshape(X_test.shape[0], 28*28).T

# Turn Y into odds or evens and reshape
Y_train = (Y_train % 2).reshape(1, -1)
Y_test = (Y_test % 2).reshape(1, -1)


def sigmoid(z):
    return 1/(1+np.exp(-z))

def layer_sizes(X, Y):

    n_x=np.shape(X)[0]
    n_h=4
    n_y=np.shape(Y)[0]
    # YOUR CODE ENDS HERE
    return (n_x, n_h, n_y)

def initialize_parameters(n_x, n_h, n_y):
  
    W1=np.random.randn(n_h,n_x)*.01
    b1=np.zeros((n_h,1))
    W2=np.random.randn(n_y,n_h)*.01
    b2=np.zeros((n_y,1))
    
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters


def forward_propagation(X, parameters):

    W1=parameters["W1"]
    b1=parameters["b1"]
    W2=parameters["W2"]
    b2=parameters["b2"]
 
    Z1=np.dot(W1,X)+b1
    A1=np.tanh(Z1)
    Z2=np.dot(W2,A1)+b2
    A2=sigmoid(Z2)
        
    assert(A2.shape == (1, X.shape[1]))
    
    cache = {"Z1": Z1,
             "A1": A1,
             "Z2": Z2,
             "A2": A2}
    
    return A2, cache

def compute_cost(A2, Y):

    m = Y.shape[1] # number of examples

    logprobs = np.multiply(np.log(A2),Y)+np.multiply(1-Y,np.log(1-A2))
    cost = -1/m * np.sum(logprobs)
    # YOUR CODE ENDS HERE
    
    cost = float(np.squeeze(cost))  # makes sure cost is the dimension we expect. 
                                    # E.g., turns [[17]] into 17 
    
    return cost


def backward_propagation(parameters, cache, X, Y):

    m = X.shape[1]

    W1=parameters["W1"]
    W2=parameters["W2"]
    

    A1=cache["A1"]
    A2=cache["A2"]
    

    dZ2=A2-Y
    dW2=1/m*np.dot(dZ2,A1.T)
    db2=1/m*np.sum(dZ2, axis=1, keepdims=True)
    dZ1=np.dot(W2.T,dZ2)*(1-A1**2)
    dW1=1/m*np.dot(dZ1,X.T)
    db1=1/m*np.sum(dZ1, axis=1, keepdims=True)
    # YOUR CODE ENDS HERE
    
    grads = {"dW1": dW1,
             "db1": db1,
             "dW2": dW2,
             "db2": db2}
    
    return grads



def update_parameters(parameters, grads, learning_rate = 1.2):
    
    W1=parameters["W1"]
    b1=parameters["b1"]
    W2=parameters["W2"]
    b2=parameters["b2"]
    

    dW1=grads["dW1"]
    db1=grads["db1"]
    dW2=grads["dW2"]
    db2=grads["db2"]
    

    W1=W1-learning_rate*dW1
    b1=b1-learning_rate*db1
    W2=W2-learning_rate*dW2
    b2=b2-learning_rate*db2


    
    parameters = {"W1": W1,
                  "b1": b1,
                  "W2": W2,
                  "b2": b2}
    
    return parameters





def nn_model(X, Y, n_h, num_iterations = 10000, print_cost=False):

    np.random.seed(3)
    n_x = layer_sizes(X, Y)[0]
    n_y = layer_sizes(X, Y)[2]

    parameters=initialize_parameters(n_x,n_h,n_y)
    


    for i in range(0, num_iterations):
         
   
        A2,cache=forward_propagation(X,parameters)
        cost=compute_cost(A2,Y)
        grads=backward_propagation(parameters,cache,X,Y)
        parameters=update_parameters(parameters,grads)
        # YOUR CODE ENDS HERE
        
        # Print the cost every 1000 iterations
        if print_cost and i % 1000 == 0:
            print ("Cost after iteration %i: %f" %(i, cost))

    return parameters


def predict(parameters, X):

    A2,cache=forward_propagation(X,parameters)
    predictions=(A2>.5)
    
    
    return predictions

# Build a model with a n_h-dimensional hidden layer
parameters = nn_model(X_train, Y_train, n_h = 4, num_iterations = 3000, print_cost=True)

predict(parameters,X_test)