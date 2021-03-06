from Bio import SeqIO
fasta_dict = {}
record_dict = SeqIO.to_dict(SeqIO.parse("/home/irinababkina/Downloads/Polina/Prediction/dedupl.fasta", "fasta"))
out_file = open("/home/irinababkina/Downloads/Polina/Prediction/AA_count.txt", "w")
for key in record_dict:
   a = record_dict[key]
   b = str(a.seq)
   fasta_dict[key] = b

for key in fasta_dict:
   seq = fasta_dict.get(key)
   m = 0
   lys = seq.count("K")
   arg = seq.count("R")
   out_file.write(key + "\t" + str(lys) + "\t" + str(arg) + str('\n'))
      
