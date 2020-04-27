BEGIN{
FS=",";         #separateur de champ en entree 
OFS=",";         #separateur de champ en sortie 
time = ""
}
{     
	if ($1=="AAA") { print $0 > $1".csv"} 
	if ($1=="BBBP") { print $0 > $1".csv"} 	
	if (time=="") {time = "Timestamp"}
	if ($1=="ZZZZ")  { time = $4" "$3}
	if ($1=="CPU01") { print time,$3,$4,$5,$6 > $1".csv"} 
	if ($1=="CPU02") { print time,$3,$4,$5,$6 > $1".csv"}
	if ($1=="CPU03") { print time,$3,$4,$5,$6 > $1".csv"}
	if ($1=="CPU04") { print time,$3,$4,$5,$6 > $1".csv"}
	if ($1=="CPU05") { print time,$3,$4,$5,$6 > $1".csv"}
	if ($1=="CPU06") { print time,$3,$4,$5,$6 > $1".csv"}
	if ($1=="CPU_ALL") { print time,$3,$4,$5,$6,$7,$8 > $1".csv"}
	if ($1=="MEM") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16,$17 > $1".csv"}
	if ($1=="PROC") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12 > $1".csv"}
	if ($1=="NET") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12 > $1".csv"}
	if ($1=="NETPACKET") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14,$15,$16 > $1".csv"}
	if ($1=="DISKBUSY") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
	if ($1=="DISKREAD") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
	if ($1=="DISKWRITE") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
	if ($1=="DISKXFER") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
	if ($1=="DISKBSIZE") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
	if ($1=="PROC.csv") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}
	if ($1=="DISKBSIZE") { print time,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13,$14 > $1".csv"}

}
END{
}
