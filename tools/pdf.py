'''
Created on 13-05-2014

@author: leonardo jofre
'''

from unpdfer import Unpdfer

# set an input filename
filename = 'myfile.pdf'

# conver to text
worker = Unpdfer()
(created, pdftext, pdfhash, success) = worker.unpdf(filename, SCRUB=False, verbose=False)
