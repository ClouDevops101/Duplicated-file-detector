# Duplicated-file-detector
<a href="http://bitly.com/2grT54q"><img src="https://cdn.codementor.io/badges/i_am_a_codementor_dark.svg" alt="I am a codementor" style="max-width:100%"/></a><a href="http://bitly.com/2grT54q"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/48px-Python.svg.png" height="50">[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=WX4EKLLLV49WG)



Description : A quick python script to free up disk space by comparing the sha1sum of all file existing in differents folder.

HOW It WORKS
================
```bash
python duplicates-detector-args.py -F /Users/heddar/ /Volumes/Data -E lib
```
CLI PARAMETERS
================
```bash
-F  or --Folders   : folders to fetch
-E  or --exclude   : Folder or subfolder to not fetch
-S  or --file-size : Search file by size
-d  or --debug     : Debug mode
-v  or --verbose"  : verbose mode
-q or --quiet"     : Silent mode
```

Requierements
================
The scipt is built with standard library

Installation
================
Add the script to a user who've got the right access 

Run it 
================
The output shows the skipped file or folder specified within the exclude parameter -E 
```bash
python duplicates-detector-args.py -F /Users/heddar/ /Volumes/Data -E lib
Scanning /USR/XXXX/...
Scanning /USR/XXXX/.eclipse...
Scanning /USR/XXXX/.eclipse/org.eclipse.oomph.jreinfo...
Skipping .......... /USR/XXXX/.eclipse/1846248522_macosx_cocoa_x86_64/configuration/org.eclipse.osgi/143/0/.cp/libswt-pi-cocoa-4758.jnilib Found lib
```

Known issues
================
the -E (exclude parameter ) may show some limites due the for loop, a fix is planed to avoid this issue


Caution 
================


