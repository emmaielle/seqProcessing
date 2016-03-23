#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on Wed Mar 23 14:45:15 2016

@author: mlasserre
"""

from __future__ import division

__author__ = "MOIRA LASSERRE"
__credits__ = ["MOIRA_LASSERRE"]
__license__ = "MIT"
__version__ = "1.0dev"
__maintainer__ = "MOIRA_LASSERRE"
__email__ = "mlasserre@pasteur.edu.uy"
__status__ = "Development"

from subprocess import PIPE, Popen
from cogent.util.option_parsing import parse_command_line_parameters, make_option

script_info = {}
script_info['brief_description'] = "GC Content"
script_info['script_description'] = "Count GC content for each sliding window. Input must be a fasta file in one single line.\n\n"\
"REQUIREMENTS: It uses the script infoseq, so you need to have it previously installed\n"\
"http://emboss.sourceforge.net/apps/cvs/emboss/apps/infoseq.html"
"It outputs a bed file with the following format:\n"\
    "chr1\tWindowStart\tWindowEnd\tGC%"
script_info['script_usage'] = [\
 ("",
  "Counts GC content with a sliding window defined by user",
  "%prog -f in.fasta -win int > outfile.bed")]
script_info['output_description']= "Tab file with the following format:"\
    "chr1\tWindowStart\tWindowEnd\tGC%"
script_info['required_options'] = [\
    make_option('-i','--fasta',type="existing_filepath",help='Fasta file to count the GC by sliding windows'),\
    make_option('-w','--window',help='(int) Sliding window size')
]

script_info['version'] = __version__


def count(args):
    win = int(args.window)
    fileInput = open(args.fasta, 'r')
    genome = fileInput.readlines()[1]
    fileOut = open("GC_density.csv", "w")

    for i in xrange(0,len(genome)-1, int(win)): 
         #print(i)
         subString = genome[i:i+win-1]
         #print(len(subString))
         tempSubstringFile = open("tmp.substring", 'w')
         tempSubstringFile.writelines(">substring" + str(i) + "\n")
         tempSubstringFile.writelines(subString)
         tempSubstringFile.close()
         GCraw = Popen("infoseq tmp.substring | awk '{print $7}' | tail -1", shell=True, stdout=PIPE)
         GCcontent = GCraw.communicate()[0][:-1] # take \n out
         #print(GCcontent)
         
         print("chr1\t" + str(i) + "\t"+ str(i + len(subString)) + "\t" + str(GCcontent))
         fileOut.writelines( "chr1\t" + str(i) + "\t"+ str(i + len(subString)) + "\t" + str(GCcontent) + "\n")

    fileOut.close()
   
def main():
    option_parser, opts, args =\
       parse_command_line_parameters(**script_info)
   
    
    count(opts)


if __name__ == '__main__':
    main()
    
    
    
