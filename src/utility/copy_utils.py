import shutil
import os
import sys
import multiprocessing
import copy_func

class Copier:
    def divide_chunks(self, l, n):
        for i in range(0, len(l), n):
            yield l[i:i + n]

    def __init__(self):
        self.source = None
        self.destination = None
        self.to_copy = []
        self.starting_size = 0

    def array_to_size(self, array):
        size = 0
        for item in array:
            size += item[1]
        return size

    def scan(self, source):
        # r=root, d=directories, f = files
        for root, _, files in os.walk(source):
            for file in files:
                path = os.path.join(root, file)
                file_stats = os.stat(path)
                self.to_copy.append([path, file_stats.st_size]) # size in bytes

    def start(self, source, destination):
        self.source = source
        self.destination = destination

        self.scan(source)
        self.starting_size = self.array_to_size(self.to_copy)
        split_to_do = list(self.divide_chunks(self.to_copy, len(self.to_copy)//multiprocessing.cpu_count()))

        processes = []
        for process in range(multiprocessing.cpu_count()):
            proc = multiprocessing.Process(target=copy_func.copy_process, args=(split_to_do[process], self.source, self.destination,))
            proc.start()
            processes.append(proc)

        for process in processes:
            process.join()

        print("Done!")