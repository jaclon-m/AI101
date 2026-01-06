import multiprocessing
import time


def write_file():
    with open("test2.txt", "w") as f:
        while True:
            f.write("hello world\n")
            f.flush()
            time.sleep(0.5)

def read_file():
    with open("test2.txt", "r") as f:
        while True:
            time.sleep(0.5)
            line = f.readline()
            print(line)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=write_file)
    p2 = multiprocessing.Process(target=read_file)
    p1.start()
    p2.start()