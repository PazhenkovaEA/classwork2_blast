#BLAST
The script takes fasta-file with unknown sequences, then blasts it in specified database and returns a fasta with renamed sequences according to the best blast score. If no matches are found or e-value is lower than treshhold, query sequence will be written with the initial name. 

##Arguments
### Required
* -i Input filename (with extension in fasta format)
* -o Output filename (with extension in fasta format)
### Optional
* -p Chose blastn, blastp, blastx, tblastn, or tblastx (default blastn)
* -d Which database to search against (default "nr)
* -t E-value threshold (default = 1)

