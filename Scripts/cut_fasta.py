from Bio import SeqIO
fasta_dict = {}
record_dict = SeqIO.to_dict(SeqIO.parse("/home/irinababkina/Downloads/Polina/Prediction/output_online.fasta", "fasta"))
out_file = open("/home/irinababkina/Downloads/Polina/Prediction/cut_68.fasta", "w")
for key in record_dict:
   a = record_dict[key]
   b = str(a.seq)
   fasta_dict[key] = b

for key in fasta_dict:
   seq = fasta_dict.get(key)
   m = 0
   for x in range(0, len(seq), 4):
       a = seq[x:x + 50]
       if len(a) == 50:
           name = str()
           name = str('>')+key + str('_') + str(x) +str('_') + str(x+50) + str('\n')
           a += str('\n')
           out_file.write(name)
           out_file.write(a)

 
