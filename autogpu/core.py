
import gpustat
import numpy as np
import torch

def freest():
    stats = gpustat.core.GPUStatCollection.new_query()
    idx = np.argmax(list(map(lambda s: s.memory_free, stats)))
    return torch.device(f"cuda:{idx}")