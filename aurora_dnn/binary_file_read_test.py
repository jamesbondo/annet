import numpy as np

if __name__=='__main__':
    # grades = np.load('/tmp/cifar10_data/cifar-10-batches-bin/data_batch_1.bin')
    with open('/tmp/cifar10_data/cifar-10-batches-bin/data_batch_1.bin', 'rb') as f:
        # data = f.read()
        data = f.read(32*32*3+1)
        text = data.decode()
        print text