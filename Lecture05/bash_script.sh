 #!/bin/bash

grep -v "#" blastoutput2.out > nohead_blastout2.out

while read myfilename
do
	echo "$(echo "$myfilename" | cut -f 2 >> sub_acc_HSP.txt)" 
done <  nohead_blastout2.out

while read queracc subjacc id length mism gap qstart qend sstart send eval score
do
echo "$(echo $length $id >> id_length_HSP.txt)"
done <  nohead_blastout2.out

