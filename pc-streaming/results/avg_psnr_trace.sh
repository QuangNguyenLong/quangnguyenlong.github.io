TRACE="1"
METHOD="CSP HYBRID LAG EQUAL"
SCENE="1 2 3 4"
avg_psnr_index="5"

mkdir avg_psnr_trace

for sc in $SCENE
do
	mkdir avg_psnr_trace/scene${sc}
	for trc in $TRACE
	do
		for med in $METHOD
		do
			python3 stats_log.py "test-*/VIDEO/APSNR_TRACE/${med}-Scene${sc}-trace${trc}.psnr.log" avg_psnr_trace/scene${sc}/${med}-Scene${sc}-trace${trc} ${avg_psnr_index}
		done
	done
done
