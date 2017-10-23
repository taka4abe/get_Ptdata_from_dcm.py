usage: get_data_from_dcm.py [-h] [-indir INDIR] [-outfile OUTFILE] [-v]

this code takes the Pt age and gender to save these institution PTdata.txt
file. This code will work in each directory in pwd. Please execute this code
in one level higher directory than the each patient directory or execute with
-indir option to specify the directory one level higher. The result is saved
in each directory with the name 'PTdata.txt' (or the name specified with the -
outfile option). This code depends on argparse, dicom, os and time

optional arguments:
  -h, --help        show this help message and exit
  -indir INDIR      : the name of the dir_root where dicom datas are, default:
                    '.'
  -outfile OUTFILE  : name of file to save. default: PTdata.txt.
  -v, --version     show program's version number and exit
