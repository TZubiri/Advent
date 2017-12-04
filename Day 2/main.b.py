from typing import List
from input_reader import spreadsheet_reader
from itertools import combinations
def spreadsheet_checksum(spreadsheet: List[List[int]]):
    checksum = 0
    for row in spreadsheet:
        possible_pairs = combinations(row,2)
        for pp in possible_pairs:
            small = min(pp)
            big = max(pp)
            if big % small == 0:
                checksum += big/small
                break
    return checksum


with open('test_input_b','r') as f:
    test_input = f.read()
test_spreadsheet = spreadsheet_reader(test_input)
assert(spreadsheet_checksum(test_spreadsheet) == 9)