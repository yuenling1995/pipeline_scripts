import os
import sys
import argparse

def msg():
    return '''This script concatenates a list of fastq files for each sample. Please provide a file location. Exiting... '''

def parse_arguments():
    '''adding the command line arguments to be provided while running the script'''
    parser = argparse.ArgumentParser(description='Process command line arguments', usage=msg())
    parser.add_argument('-p', '--path', help='fastq file full path')
    args = parser.parse_args()
    return args

def check_input_path():
    input_path = parse_arguments().path
    if os.path.isdir(input_path):
        print(f"\ndirectory {input_path} exists!")
        return input_path
    else:
        print(f"\n This is not a valid directory, exit now.")
        sys.exit()

def get_files(input_path):
    sample_dict = {}
    for filename in os.listdir(input_path):
        filepath = os.path.join(input_path, filename)
        list = filename.split("_")
        sample_name = list[0] + "_" + list[1]
        if sample_name not in sample_dict.keys():
            sample_dict[sample_name] = [filepath]
        else:
            sample_dict[sample_name].append(filepath)
    return sample_dict

def concat_files(sample_dict):
    for sample_name, file_path in sample_dict.items():
        for file in file_path:
            dirname = os.path.dirname(file)
            outdir_filename = sample_name + ".fastq"
            outdir = os.path.join(dirname, outdir_filename)
            cmd = "cat " + file + " >> " + outdir
            os.system(cmd)

        






def main():
    msg()
    input_path = check_input_path()
    sample_dict = get_files(input_path)
    concat_files(sample_dict)
    print("Finish concatenating the files and saved in: " + input_path )


if __name__ == '__main__':
    main()


