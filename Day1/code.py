import sys
import itertools
from collections import defaultdict, Counter, deque


def read_data():
    with open("sample.txt") as f:
        contents = f.read().splitlines()
    return contents

def cust_sum(s:str):
    return sum(map(int,list(s)))


def main():
    data = read_data()
    final_list = []
    processed_data = list(map(cust_sum,data))
    print(processed_data)
    x = [data[processed_data.index(n)] for n in processed_data if n==2020]
    print(x)
if __name__ == "__main__":
    main()
