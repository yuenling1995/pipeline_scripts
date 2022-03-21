import sys
import argparse
import os


def msg():
    return '''This script called the FastQC program that processes adapter trimmed files, and generates .html reports
        for each sample, and save them to the QC_report folder. exiting...'''

def parse_arguments():
    '''Adding the command line arguments to be provided while running the script.'''
    parser = argparse.ArgumentParser(description='Process command line arguments.', usage=msg())
    parser.add_argument('-p', '--path', help='fastq file path')
    parser.add_argument('-n', '--number', type=int, help='number of threads', default=1, required=False)
    args = parser.parse_args()
    return args


def check_file_path():
    '''Check if the path of input fastq file exists'''
    file_path = parse_arguments().path
    if os.path.isfile(file_path):
        return file_path
    else:
        print("Please provide a fastq file for QC analysis\n")
        sys.exit()



def get_job_info(file_path):
    '''Generates the path where the QC_report will go into'''
    if os.path.isfile(file_path):
        file_path = os.path.abspath(file_path)
        dirname = os.path.dirname(file_path)
        filename = os.path.basename(file_path)
        outfile_dir = os.path.dirname(dirname)
        outdir = os.path.join(outfile_dir, "QC_report/")
        job_name = filename.split(".")[0] + "_fastqc"
        
    return dirname, filename, outdir, job_name




################
# Main function:  This function handles menu and flow control.
################
def main():
    print("Starting Fastqc\n")
    file_path = check_file_path()
    smp = parse_arguments().number
    print("Processing fastq file: " + file_path + "\n")
    dirname, filename, outdir, job_name = get_job_info(file_path)
    fastqc_loc = "/share/data/software/FastQC/fastqc"
    cmd = fastqc_loc + " " + file_path + " -o " + outdir + " -noextract -t " + str(smp) + " -d " + outdir
    os.system(cmd)



if __name__ == '__main__':
    main()
    
