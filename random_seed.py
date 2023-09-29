import random
import numpy as np 
import torch

def update_seed_number(SEED_NUMBER):
    random.seed(SEED_NUMBER)
    np.random.seed(SEED_NUMBER)
    torch.manual_seed(SEED_NUMBER)
    torch.cuda.manual_seed_all(SEED_NUMBER)