# -*- coding: utf-8 -*-
import argparse, dicom, os, time
start = time.time()

parser = argparse.ArgumentParser(
    description='''this code takes the Pt age and gender to save these
    institution PTdata.txt file. This code will work in each directory
    in pwd.
    Please execute this code in one level higher directory than the
    each patient directory or execute with -indir option to specify
    the directory one level higher.
    The result is saved in each directory with the name 'PTdata.txt'
    (or the name specified with the - outfile option).
    This code depends on argparse, dicom, os and time''' ,
    )
parser.add_argument("-indir", nargs= 1, help=": the name of the dir_root where dicom datas are, default: '.'  ")
parser.add_argument("-outfile", nargs= 1, help=": name of file to save. default: PTdata.txt.  ")
parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1, Oct/23/2017')
args = parser.parse_args()

try:
    in_dir = args.indir[0]
except:
    in_dir = '.' # defaul target directory
try:
    out_file = args.outfile[0]
except:
    out_file = 'PTdata.txt'

print("\nin_dir is '" + in_dir + "'\nout_file is '" + out_file + "'\n")

def main():
    data_list = []
    PatientName, PatientID, PatientSex = 'Nodata', 'Nodata', 'Nodata'#str(), str(), str()
    PatientAge, PatientSize, PatientWeight = 'Nodata', 'Nodata', 'Nodata'#0, 0, 0#str(), str(), str()

    for root, dirs, files in os.walk(in_dir):
        for file_name in files:
            file_path = root + "/" + file_name
            try:
                ds = dicom.read_file(file_path)
                if PatientName == 'Nodata':#str():
                    PatientName = str(ds.PatientName)
                if PatientID == 'Nodata':#str():
                    PatientID = str(ds.PatientID)
                if PatientSex == 'Nodata':#str():
                    PatientSex = str(ds.PatientSex)
                if PatientAge == 'Nodata':#str():
                    PatientAge = str(ds.PatientAge)
                if PatientSize == 'Nodata':#str():
                    PatientSize = str(ds.PatientSize)
                if PatientWeight == 'Nodata':#str():
                    PatientWeight = str(ds.PatientWeight)
            except:
                pass

    PatientName = ('Name:_' + PatientName)
    PatientID = ('ID:_' + PatientID)
    PatientSex = ('Sex:_' + PatientSex)
    PatientAge = ('Age:_' + PatientAge)
    PatientSize = ('Size:_' + PatientSize)
    PatientWeight = ('Weight:_' + PatientWeight)

    data_list.append(PatientName)
    data_list.append(PatientID)
    data_list.append(PatientSex)
    data_list.append(PatientAge)
    data_list.append(PatientSize)
    data_list.append(PatientWeight)
    print(data_list)

    f = open(out_file, 'w')
    for x in data_list:
        f.write(str(x) + "\n")
    f.close()

total, n = len(os.listdir('.')), 0
for move_dir in os.listdir('.'):
    n += 1
    if os.path.isdir(move_dir):
        os.chdir(move_dir)
        main()
        elapsed_time = time.time() - start
        est_total = (elapsed_time/n) * total
        if est_total < 600:
            print("elapsed/est_total: {0:1.1f}/{1} sec\n".format(
              elapsed_time, int(est_total)))
        elif est_total < 6000:
            print("elapsed/est_total: {0}/{1} min\n".format(
              elapsed_time//60, int(est_total//60)))
        else:
            print("elapsed/est_total: {0:1.2f}/{1:1.2f} hr\n".format(
              elapsed_time/3600, est_total/3600))
        os.chdir('..')
    else:
        pass

elapsed_time = time.time() - start
print("finished in {0} sec".format(str(elapsed_time)))
