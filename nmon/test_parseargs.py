import sys
import argparse
import logging as log

debug = False

def parseargs(raw_args):
        parser = argparse.ArgumentParser(description="nmonParser converts NMON monitor files into time-sorted CSV/Spreadsheets for easier analysis, without the use of the MS Excel Macro. Also included is an option to build an HTML report with graphs, which is configured through report.config.")
        parser.add_argument("-x", "--overwrite", action="store_true", dest="overwrite", help="overwrite existing results (Default: False)")
        parser.add_argument("-d", "--debug", action="store_true", dest="debug", help="debug? (Default: False)")
        parser.add_argument("--force", action="store_true", dest="force", help="force using of config (Default: False)")
        parser.add_argument("-i", "--inputfile", dest="input_file", default="test.nmon", help="Input NMON file")
        parser.add_argument("-o", "--output", dest="outdir", default="./report/", help="Output dir for CSV (Default: ./report/)")
        parser.add_argument("-c", "--csv", action="store_true", dest="outputCSV", help="CSV output? (Default: False)")
        parser.add_argument("-b", "--buildReport", action="store_true", dest="buildReport", help="report output? (Default: False)")
        parser.add_argument("-t", "--reportType", dest="reportType", default="interactive", help="Should we be generating a \"static\" or \"interactive\" report (Default: interactive)")
        parser.add_argument("-r", "--reportConfig", dest="confFname", default="./report.config", help="Report config file, if none exists: we will write the default config file out (Default: ./report.config)")
        parser.add_argument("--dygraphLocation", dest="dygraphLoc", default="http://dygraphs.com/1.1.0/dygraph-combined.js", help="Specify local or remote location of dygraphs library. This only applies to the interactive report. (Default: http://dygraphs.com/1.1.0/dygraph-combined.js)")
        parser.add_argument("--defaultConfig", action="store_true", dest="defaultConf", help="Write out a default config file")
        parser.add_argument("-l", "--log", dest="logLevel", default="INFO", help="Logging verbosity, use DEBUG for more output and showing graphs (Default: INFO)")
        args = parser.parse_args(raw_args)
        
        
        if len(sys.argv) == 1:
            # no arguments specified
            parser.print_help()
            sys.exit()
        
        logLevel = getattr(log, args.logLevel.upper())
        if debug : print('logLevel',logLevel)
        if logLevel is None:
            print("ERROR: Invalid logLevel:", args.loglevel)
            sys.exit()
        if args.debug:
            log.basicConfig(
                level=logLevel, format='%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s')
        else:
            log.basicConfig(
                level=logLevel, format='%(levelname)s - %(message)s')
        print(logLevel)
        return args
    
# raw_args = liste de paramètres de commande en ligne :  python3  test_parseargs.py -c -o testReport -i test.nmon -x
if debug :
    raw_args = ['-c', '-o', 'testReport', '-i', 'test.nmon', '-x']
else:
    raw_args = sys.argv[1:]
print(raw_args)

args = parseargs(raw_args)
print(args)
#parser.print_help()


# details de saveReportConfig()
# create report.conf from stdReport
stdReport = [('CPU_ALL', ['user', 'sys', 'wait'], 'stackedGraph: true, fillGraph: true'), ('DISKBUSY', [
        'sda1', 'sdb1'], ''), ('MEM', ['memtotal', 'active'], ''), ('NET', ['eth0'], '')]

for stat, fields, plotOpts in stdReport:
            line = stat + "="
            if len(fields) > 0:
                line += ",".join(fields)
            line += "{%s}\n" % plotOpts
            print(line)
            # save to file
            
import pyNmonParser
import pandas as pd
import matplotlib.pyplot as plt
nmonParser = pyNmonParser.pyNmonParser(args.input_file, args.outdir, args.overwrite, args.debug)
processedData = nmonParser.parse()
#print('AAA', nmonParser.sysInfo)
#print('BBB', nmonParser.bbbInfo)
print(processedData.keys())

#print(processedData['CPU01'])
key = 'CPU01'
data = processedData[key]
filename = 'test.csv'
df = pd.DataFrame(data)
print(df)

# process data before saving to file
dfT = df.T
#key = dfT.keys()[0]
dfT.columns = dfT.iloc[0]    #rename columns from first row
dfT = dfT.drop(index=0)      # delete first row
from dateutil.parser import parse
dfT[dfT.keys()[0]]=dfT[dfT.keys()[0]].apply(lambda x: parse(x))
dfT.set_index(dfT[dfT.keys()[0]],inplace=True)
dfT = dfT.drop(columns=[dfT.keys()[0]])
# before plot, need to convert object in columns to float 
dfT = dfT.astype(float) 
print(dfT)
print(dfT.info())
#r =input('stop')
# save to file
dfT.to_csv(filename)         

# plot from processed data
dfT.plot()
plt.show()

# plot from csv file
df = pd.read_csv(filename, index_col=0)
#print(df)
# when reading from file, columns with numbers are automatically converted to float
print(df.info())      
#ready to be plotted
df.plot()
plt.show()

print(processedData.keys())
table= processedData['CPU01']
for n, col in enumerate(table):
    print(n,col)

print(nmonParser.tStamp.keys())
print(nmonParser.tStamp['T0001']) 