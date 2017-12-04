from typing import List
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
