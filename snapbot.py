# HOW-TO #
# 1. Setup a project Google API at https://console.developers.google.com/apis/
# 2. Request a Google Sheet API
# 3. Get client-email and json file
# 4. Please fill in the [BLANK] in this code to work.

import gspread
from gspread_formatting import *
from oauth2client.service_account import ServiceAccountCredentials
scope = [
'https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive',
]

# URL = [SHEET URL]
# client-email : [YOUR OWN EMAIL]
# json_file_name = [API FILE PATH IN JSON FORMAT]
# sheet_name = [SUB SHEET NAME]

credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file_name, scope)
gc = gspread.authorize(credentials)

# Retreive spreadsheet by url
doc = gc.open_by_url(URL)

# Select sheet
worksheet = doc.worksheet([sheet_name])

# Practice time area ranging from B2:H21 (R2C2:R21C8)
range_list = worksheet.range('B2:H21')
for cell in range_list:
	cell_label = rowcol_to_a1(cell.row, cell.col)
	try:
		cell_fmt = get_effective_format(worksheet, cell_label)
		if ((cell_fmt.backgroundColor.red, cell_fmt.backgroundColor.green, cell_fmt.backgroundColor.blue) == (1,1,1)):
			# This cell is pure (white = RGB (1,1,1)). erase it. 
			print "[ERASE CELL %s] %s" % (cell_label, cell.value)
			worksheet.update_acell(cell_label, "")
		else:
			# This cell is reserved (color filled).
			print "[SAVE MENTORING %s] %s" % (cell_label, cell.value)
			pass
	except:
		# Cell format retrieval error. pass.
		pass
