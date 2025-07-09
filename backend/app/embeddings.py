import numpy as np

def get_embedding(text):
    np.random.seed(abs(hash(text)) % (10 ** 8))
    return np.random.rand(384)