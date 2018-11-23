# -*- coding: cp936 -*-

import os
import sys
from os import listdir
from os.path import isfile, join
import subprocess
import random
 

def getAllFiles(curdir):
        filenames = []
        for dirpath,dirnames,fnames in os.walk(curdir):
                for fn in fnames:
                        filenames.append(os.path.join(dirpath,fn))
                
        return filenames


def main():
    workpath =  r'D:\BaiduPanDownload'
    pl = getAllFiles(workpath) 
    for x in pl: 
        if x.find('.baiduyun.p.downloading')>0:
            targets = join(workpath,x)
            newname =join(workpath, x.split('.baiduyun.p.downloading')[0]   )         
            print 'oldname = %s'% targets
            print 'newname =%s'% newname
            if os.path.exists(newname):
                    newname=join(workpath, str(random.randint(1,5)) + x.split('.baiduyun.p.downloading')[0]   )  
            os.rename(targets,newname)
            
    print '>>>>>>>>>>>>>>>>>'

                    
         

if __name__ == '__main__':
	main()

        

