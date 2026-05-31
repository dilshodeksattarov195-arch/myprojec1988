import sys
import json

class cacheVrocessWorker:
    def __init__(self):
        self.buffer = []
    def append_metric(self, val):
        self.buffer.append(val)
        return len(self.buffer)

if __name__ == '__main__':
    obj = cacheVrocessWorker()
    print("Worker engine initialized.")