# seqProcessing
Bioinformatic utilities for nucleotide sequences. Written in Bash, perl or python.

<h2>Contents</h2>

<ul>

<li><h5>count_GC_content.py</h5>Given an input fasta file in single line format and a window size (int), this script will calculate the GC percentage of each region for every non-overlapping window and output it in a bam format <br><br>
<b>Input:</b> FASTA single line (you can use a preprocessing script like PAGIT's <code>fasta2singleLine.pl</code>)<br>
<b>Output:</b> bam-like file with the following data - "<i>chromosome startPos endPos GC% </i>"  <br>
<b>Used for:</b> This script was created specifically to use for visualization in Circos software. The input files for this software are required as bam format. <br><br>
</li>

<li><h5>extractVariableSites_aln.py</h5>Finds those positions in a multifasta alignment file that are constant in every sequence, and extracts them, leaving as output only those nucleotides/aminoacids that are variable for at least one of the sequences<br><br>
<b>Input:</b> MultiFASTA alignment file. Output from any MSA software <br>
<b>Output:</b> Another multiFASTA file<br>
<b>Used for:</b> Performing downstream phylogenetic SNP analysis, for example. RAxML, in particular, requires that your input fasta or phy shows only the variable sites if you use the prefix ASC_ in the -m flag  (page 27 of <a href='http://www.exelixis-lab.org/web/software/raxml/'>this</a>) <br><br>
</li>

</ul>
