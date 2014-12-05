"""
    Download files from specified url addresses and save them to the local disk.
"""

import urllib

testfile = urllib.URLopener()
print 'downloading'
for i in range(2,27):

    urlLink = "http://www.cse.sc.edu/~tongy/csce350/lecture/lect" + str(i) + ".pdf"
    testfile.retrieve(urlLink, "lect" + str(i) + ".pdf")
    print 'lect' + str(i) + ' downloaded'