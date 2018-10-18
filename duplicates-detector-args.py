#!/usr/bin/env python
# dupFinder.py
import os, sys
import hashlib
import optparse
import re

VERSION = "0.1"

#global debug
 
#def findDup(parentFolder,exclude_fld):
def findDup(parentFolder):
    # Dups in format {hash:[names]}
    dups = {}
    for dirName, subdirs, fileList in os.walk(parentFolder, topdown=True):
      for ex in exclude_folder:
        if ex in dirName or ex in subdirs:
          break
        if debug:
          print 'Scanning ' +  dirName
        else:
          print('Scanning %s...' % dirName)
        for filename in fileList:
            # Get the path to the file
            path = os.path.join(dirName, filename)
            debugit("         " + path)
            # Calculate hash
            #if len(exclude_folder) != 0 and '' not in exclude_folder[0] :
            if len(exclude_folder) != 0 :
              for ex in exclude_folder:
                debugit("          Excluded " + ex)
                if ex not in path:
                  file_hash = hashfile(path)
                  debugit(file_hash)
                  # Add or append the file path
                  if file_hash in dups:
                    dups[file_hash].append(path)
                  else:
                    dups[file_hash] = [path]
		else:
                  print '\033[1m' +  "Skipping .......... " + path + " " + "Found" + " " + ex + '\033[0m'
            else:
               file_hash = hashfile(path)
               debugit(file_hash)
               # Add or append the file path
               if file_hash in dups:
                 dups[file_hash].append(path)
               else:
                 dups[file_hash] = [path]
    return dups
 
 
# Joins two dictionaries
def joinDicts(dict1, dict2):
    for key in dict2.keys():
        if key in dict1:
            dict1[key] = dict1[key] + dict2[key]
        else:
            dict1[key] = dict2[key]
 
 
def hashfile(path, blocksize = 524288):
#40960   real	41m50.104s user	31m48.214s sys	4m20.584s
#1048576 real	53m19.223s user	39m32.505s sys	7m5.617s
#3145728 real	53m52.577s user	39m16.684s sys	8m5.347s
    try:
      afile = open(path, 'rb')
      hasher = hashlib.sha1()
      buf = afile.read(blocksize)
      while len(buf) > 0:
        hasher.update(buf)
        buf = afile.read(blocksize)
      afile.close()
      return hasher.hexdigest()
    except: 
      print '\033[91m' + path + " <- File not found" + '\033[0m' 
 
 
def printResults(dict1):
    results = list(filter(lambda x: len(x) > 1, dict1.values()))
    if len(results) > 0:
        print('Duplicates Found:')
        print('The following files are identical. The name could differ, but the content is identical')
        for result in results:
            #if filtred_file_size:
            #    debugit(os.path.getsize(result[0]))
 	    #	 debugit(sizeof_fmtreverse(filtred_file_size)) 
            #    if os.path.getsize(result[0]) >= sizeof_fmtreverse(filtred_file_size):
            #       try:
            #         file_size = sizeof_fmt(os.path.getsize(result[0]))
            #       except:
            #         file_size = "Not found"
            #       print '__________' + file_size + ' _________'

            for subresult in result:
              print('\033[93m%s\033[0m' % subresult)
            print('___________________')
            #else:
             #   try:
             #     file_size = sizeof_fmt(os.path.getsize(result[0]))
             #   except:
             #     file_size = "Not found"
             #   print '__________' + file_size + ' _________'

             #   for subresult in result:
             #       print('\033[93m%s\033[0m' % subresult)
             #   print('___________________')

    else:
        print('No duplicate files found.')

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix) 

def sizeof_fmtreverse(num):
    d = {'K': 1024, 'M': 1048576, 'G': 1073741824, 'T': 1099511627776, 'P': 1125899906842624} 
    for unit in d:
        debugit(unit + ' ' + str(d[unit]) + ' ' + num)
        if unit in num:
          value = re.sub(' +','',num).strip(unit)
          value = float(value) * float(d[unit])
          debugit("-----------------" + str(value))
          return value 
        else:
          return False

def debugit(action):
    if debug:
      print action
      return action 

parser = optparse.OptionParser(
    "%prog [options]", version="%prog " + VERSION)
parser.add_option('-F', '--Folders',
                  action="append",
                  dest="folders", 
                  help='folders to parse')
parser.add_option('-E', '--exclude',
                  action="append",
                  dest="exclude",
                  help='Folder or subfolder to not fetch')
parser.add_option('-S', '--file-size',
                  dest="file_size",
                  help='Folder or subfolder to not fetch')

parser.add_option("-d", "--debug", action="store_true", dest="debug")
parser.add_option("-v", "--verbose", action="store_true", dest="verbose")
parser.add_option("-q","--quiet", action="store_false", dest="verbose")
 
if __name__ == '__main__':

    # Ok first job : parse args
    opts, args = parser.parse_args()
    if args:
        parser.error("Does not accept any argument.")
    
    verbose = opts.verbose
    debug = opts.debug

    #sys.exit()
    folders = opts.folders
    exclude_folder = opts.exclude or []
    #filtred_file_size = int(float(opts.file_size or '0' ))
    filtred_file_size = opts.file_size or '0' 
    debugit(folders)
    
    if len(sys.argv) > 1:
        dups = {}
#        folder = er[:-1]
#>>> folder
#[1, 2, 3, 4, 5, 6, 7, 8]
#>>> exculude = er[-1]
#>>> exculude
#9

        #print folders
        #print exclude_folder
        #sys.exit()
        for i in folders:
            # Iterate the folders given
            if os.path.exists(i):
                # Find the duplicated files and append them to the dups
                #joinDicts(dups, findDup(i,exclude_folder))
                joinDicts(dups, findDup(i))
            else:
                print('%s is not a valid path, please verify' % i)
                sys.exit()
        printResults(dups)
    else:
        print('Usage: python dupFinder.py folder or python dupFinder.py folder1 folder2 folder3')
