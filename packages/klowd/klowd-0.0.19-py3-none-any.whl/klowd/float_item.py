import numpy as np

class FloatItem:
    values=[]
    indices=[]

    def __init__(self, blobData, indexType='ByDepth'):
        dto=np.dtype([('index', 'i8'), ('value', 'd')])
        pairs=np.ndarray(int(len(blobData)/16),dto,blobData,0)
        non_nan=pairs[(pairs['value'] == pairs['value'])]
        indices=non_nan['index']
        values=non_nan['value']
        self.values.append(values)
        self.indices.append(indices)
