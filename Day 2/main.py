from typing import List


def spreadsheet_checksum(spreadsheet: List[List[int]]):
    checksum = 0
    for row in spreadsheet:
        row_diff = max(row) - min(row)
        checksum += row_diff
    return checksum



def spreadsheet_reader(input_spreadsheet:str)->List[List[int]]:
    output_spreadsheet = []
    input_rows = input_spreadsheet.split('\n')
    for input_row in input_rows:
        output_row = []
        input_cells = input_row.split('\t')
        for input_cell in input_cells:
            output_row.append(int(input_cell))
        output_spreadsheet.append(output_row)
    return output_spreadsheet


with open('challenge_input','r') as f:
    challenge_input = f.read()

print(spreadsheet_checksum(spreadsheet_reader(challenge_input)))

test_spreadsheet = [[5,1,9,5],[7,5,3],[2,4,6,8]]
assert(spreadsheet_checksum(test_spreadsheet) == 18)