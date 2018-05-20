
import argparse
from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord
from Bio.Seq import Seq


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Blast')

    parser.add_argument('-p', '--program', help='blastn, blastp, blastx, tblastn, or tblastx', metavar='Str', type=str, default="blastn")
    parser.add_argument('-d', '--database', help='Which database to search against (e.g. "nr")', metavar='Str', type=str, default="nt")
    parser.add_argument('-t', '--treshold', help='Evalue threshold', type=float, default=1)
    parser.add_argument('-i', '--input', help='Input filename (with extension)', metavar='FILE', required=True)
    parser.add_argument('-o', '--output', help='Results filename (with extension)', metavar='FILE', required=True)
    args = parser.parse_args()

    evalue = args.treshold
    filename = args.input
    fileout = args.output
    prog = args.program
    database = args.database

    elements = []
    for seq_record in SeqIO.parse(filename, format="fasta"):
        result_handle = NCBIWWW.qblast(prog, database, seq_record.seq, alignments = 1, descriptions = 1)
        blast_records = NCBIXML.parse(result_handle)
        for blast_record in blast_records:
            if (blast_record.alignments[0].hsps[0].expect < evalue) & (len(blast_record.alignments) > 0): #Если evalue больше трешхолда и найдено хоть одно выравниание
                element = SeqRecord(Seq(str(seq_record.seq)), id=blast_record.descriptions[0].title, description='')
            else:
                element = SeqRecord(Seq(str(seq_record.seq)), id=seq_record.id, description='')
        elements.append(element)

    output_handle = open(fileout, "w")
    for seq in elements:
        SeqIO.write(seq, output_handle, "fasta"),
    output_handle.close()



filename = "sequence.fasta"
