import os
import argparse
import sys

'''should run this in the CLIA pipeline'''
'''usage: create_project_str.py [-h] -p <project path>'''
'''create a list of sub-directories as needed for a project directory'''
subdir_list = ['Raw_fastq', 'QC_report', 'Filtered', 'Primer_trimmed', 'Assembly',
			   'Blast', 'Report', 'Spreadsheets']

def msg():
	return '''This script checks if a project directory and sub-directory exists,
		and creates them if necessary. Please provide a project location. Exiting...'''

def parse_arguments():
	'''Adding the command line arguments to be provided while running the script.'''
	parser = argparse.ArgumentParser(description='Process command line arguments.', usage=msg())
	parser.add_argument('-p', '--path', help='project path')
	args = parser.parse_args()
	return args

def check_proj_dir():
	'''Check if the Project directory exists'''
	dir_path = parse_arguments().path
	if os.path.isdir(dir_path):
		print("Project directory " + dir_path + " exists!\n")
		return dir_path
	else:
		print("Project directory " + dir_path + " doesn't exist. Exit now...")
		sys.exit()

def create_new_dir(subdir_path):
	'''Create sub-directory if needed'''
	if os.path.isdir(subdir_path):
		print("Sub-directory " + subdir_path + "already exists!")
	else:
		try:
			os.mkdir(subdir_path)
			print("Finished creating the " + subdir_path)
		except:
			print("Failed to create the sub-directory " + subdir_path)
		else:
			pass

def copy_config(subdir_path):
	'''Copy the config file (in the current directory) into the current sub-directory'''
	cwd = os.getcwd()
	filename = "config.yml"
	filepath = os.path.join(cwd, filename)
	print("Config file: " + filepath)
	if os.path.isfile(filepath):
		cmd = "cp " + filepath + " " + subdir_path
		print(cmd)
		return_val = os.system(cmd)
		if return_val == 0:
			print("Finished copying the config file to the " + subdir_path)
		else:
			print("Return value: " + str(return_val))
			print("Failed to copy the config file to the " + subdir_path)



################
# Main function:  This function handles menu and flow control.
################
def main():
	dir_path = check_proj_dir()
	print("Project Location: " + dir_path)

	for subdir in subdir_list:
		subdir_path = os.path.join(dir_path, subdir)
		print("\nChecking/Creating sub-directory: " + subdir_path)
		create_new_dir(subdir_path)
		if subdir == "Spreadsheets":
			print("\nCopying the config.yml file")
			copy_config(subdir_path)
		else:
			pass




if __name__ == '__main__':
	main()
