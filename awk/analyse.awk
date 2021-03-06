#! /usr/bin/awk -f

# use : 
# awk -f analyse.awk test.nmon  
# or ./analyse.awk test.nmon

BEGIN{
FS=",";         #separateur de champ en entree 
OFS=",";         #separateur de champ en sortie 
}
{     

if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="CPU01")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="CPU02")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="CPU03")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="CPU04")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="CPU05")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="CPU06")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="CPU_ALL")) { print $3,$4,$5,$6,$7,$8 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="MEM")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="PROC")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="NET")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="NETPACKET")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="DISKBUSY")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="DISKREAD")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="DISKWRITE")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="DISKXFER")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="DISKBSIZE")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="PROC.csv")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)=="the-gibson") && ($1=="DISKBSIZE")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}

if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="CPU01")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="CPU02")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="CPU03")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="CPU04")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="CPU05")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="CPU06")) { print $3,$4,$5,$6 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="CPU_ALL")) { print $3,$4,$5,$6,$7,$8 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="MEM")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="PROC")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="NET")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="NETPACKET")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="DISKBUSY")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="DISKREAD")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="DISKWRITE")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="DISKXFER")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="DISKBSIZE")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="PROC.csv")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
if (( substr($2,length($2)-9,11)!="the-gibson") && ($1=="DISKBSIZE")) { print $3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
}
END{
}
