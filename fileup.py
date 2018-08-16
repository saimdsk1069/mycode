import pandas as pd


def files(getlinuxfilename, getsolarisfilename, getonesourcefilename):
    excelFiles = [getlinuxfilename, getsolarisfilename]
    for files in excelFiles:
        if 'xls' in files or 'xlsx' in files:
            data_xls = pd.read_excel(files)
            data_xls.to_csv(files.split('.')[0] + '.csv', encoding='utf-8')
            files = files.split('.')[0] + '.csv'
        elif 'csv' not in files or 'csv' not in getonesourcefilename:
            raise Exception('This is the not the expected file format,please pass xlsx/xls/csv files only.')
        print "Please wait while processing the file:" + files
        df1 = pd.read_csv(files, index_col=0)
        df1.Hostname = df1.Hostname.astype(str).str.lower()
        df2 = pd.read_csv(getonesourcefilename, index_col=0)
        df2.Hostname = df2.Hostname.astype(str).str.lower()
        if 'solaris' in files:
            df2 = df2[(df2['OS'] != 'AIX') & (df2['OS'] != 'Red Hat(Linux)') & (df2['OS'] != 'RedHat Linux 7.x') & (
                    df2['OS'] != 'SuSE(Linux)')]
            common = df1.merge(df2, on=['Hostname'])
            not_in_oneSource_solaris = df1[(~df1.Hostname.isin(common.Hostname))]
            not_in_oneSource_solaris.to_csv('not_in_oneSource_Solaris.csv', encoding='utf-8')
            not_in_solaris = df2[(~df2.Hostname.isin(common.Hostname))]
            not_in_solaris.to_csv('not_in_Solaris.csv', encoding='utf-8')
        else:
            df2 = df2[(df2['OS'] != 'AIX') & (df2['OS'] != 'SunOS')]
            common = df1.merge(df2, on=['Hostname'])
            not_in_oneSource_linux = df1[(~df1.Hostname.isin(common.Hostname))]
            not_in_oneSource_linux.to_csv('not_in_oneSource_linux.csv', encoding='utf-8')
            not_in_linux = df2[(~df2.Hostname.isin(common.Hostname))]
            not_in_linux.to_csv('not_in_linux.csv', encoding='utf-8')


getlinuxfilename = str(raw_input(
    "please give the path off DATA LINUX xlsx/xls file,Please make sure their are no spaces between filename--->"))
getsolarisfilename = str(raw_input(
    "please give the path off DATA Solaris xlsx/xls file,Please make sure their are no spaces between filename-->"))
getonesourcefilename = str(
    raw_input("please give the path off OneSOURCE csv file,Please make sure their are no spaces between filename-->"))
# Pass the field paths as arguments.
files(getlinuxfilename, getsolarisfilename, getonesourcefilename)
