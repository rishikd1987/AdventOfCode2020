import sys
from itertools import combinations
from collections import defaultdict, Counter, deque
# import time
from time import perf_counter

def read_data():
    with open("input.txt") as f:
        contents = f.read().splitlines()
    return list(map(int,contents))

#part 1
def find_pair(input_list:list):
    pointer = 0
    while pointer<len(input_list):
        num1 = input_list[pointer]
        list_to_loop = input_list[pointer+1:]
        for j in list_to_loop:
            if num1 + j == 2020:
                return num1*j
        pointer += 1

#part 2 - option 1
def find_three(input_list:list):
    pointer = 0
    while pointer<len(input_list):
        num1 = input_list[pointer]
        list_to_loop_1 = input_list[pointer+1:]
        for idx,val in enumerate(list_to_loop_1):
            num2 = list_to_loop_1[idx]
            list_to_loop_2 = list_to_loop_1[idx+1:]
            for i in list_to_loop_2:
                if num1 + num2 + i == 2020:
                    return num1,num2,i,num1*num2*i
        pointer += 1

#paart 2 - option 2
def find_three_fast(input_list:list):
    for a,b,c in combinations(input_list,3):
        if a+b+c==2020:
            return a,b,c,a*b*c

def main():
    data = read_data()
    # print(find_pair(data))
    #Option 1
    start = perf_counter()
    print(find_three(data))
    print(f"Elapsed time: {perf_counter()-start}")

    #Option 2
    start = perf_counter()
    print(find_three_fast(data))
    print(f"Elapsed time: {perf_counter()-start}")
if __name__ == "__main__":
    main()
