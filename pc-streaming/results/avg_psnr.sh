


BW="50 60 70 80 90"
METHOD="CSP HYBRID LAG EQUAL"
SCENE="1 2 3 4"
avg_psnr_index="5"

mkdir avg_psnr

for sc in $SCENE
do
	mkdir avg_psnr/scene${sc}
	echo "bw ${METHOD}" > avg_psnr/scene${sc}/plot_scene${sc}.txt
	for bw in $BW
	do
		echo -n "${bw} " >> avg_psnr/scene${sc}/plot_scene${sc}.txt
		for med in $METHOD
		do
			python3 stats_log.py "test-*/VIDEO/APSNR/${med}-Scene${sc}-bw${bw}.psnr.log" avg_psnr/scene${sc}/${med}-Scene${sc}-bw${bw} ${avg_psnr_index} >> avg_psnr/scene${sc}/plot_scene${sc}.txt
		done
		echo "" >> avg_psnr/scene${sc}/plot_scene${sc}.txt
	done
done
