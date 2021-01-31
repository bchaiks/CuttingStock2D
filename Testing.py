import CutStock

test_dict = { '1': [45, 20], '2': [45, 20], '3': [45, 20],
				'4': [55, 25], '5': [35, 23] }
sheet_size = [96.0, 48.0]
				
output = CutStock.CutStock(test_dict, sheet_size)

print(output)