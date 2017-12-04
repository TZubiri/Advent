from typing import List
from input_reader import spreadsheet_reader


def spreadsheet_checksum(spreadsheet: List[List[int]]):
    checksum = 0
    for row in spreadsheet:
        row_diff = max(row) - min(row)
        checksum += row_diff
    return checksum



with open('challenge_input','r') as f:
    challenge_input = f.read()

print(spreadsheet_checksum(spreadsheet_reader(challenge_input)))

test_spreadsheet = [[5,1,9,5],[7,5,3],[2,4,6,8]]
assert(spreadsheet_checksum(test_spreadsheet) == 18)