# General help functions

def add_linebreak(heading=None, endwith=None):
	if heading is not None:
		print(heading)
	print('-'*50)

	if endwith is not None:
		print(endwith)