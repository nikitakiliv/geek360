import numpy as np

INPUT_DIM = 4
OUT_DIM = 102
H_DIM = 300

x = np.array()

W1 = np.array()

b1 =  np.array()

W2 = np.array()

b2 =  np.array()

def relu(t):
    return np.maximum(t, 0)

def softmax(t):
    out = np.exp(t)
    return out / np.sum(out)

def predict(x):
    t1 = x @ W1 + b1
    h1 = relu(t1)
    t2 = h1 @ W2 + b2
    z = softmax(t2)
    return z

probs = predict(x)
pred_class = np.argmax(probs)
class_names = ['Setosa', 'Versicolor', 'Virginica']
print('Predicted class:', class_names[pred_class])
