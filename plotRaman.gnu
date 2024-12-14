set terminal pngcairo enhanced size 800,800
set output "b-niooh_raman.png"
set xrange[0:4000]
set style line 1 lt 1 lc -1 lw 3 
#set nokey
set xlabel "Frequency, cm^{-1}"
set ylabel "Intensity"
unset ytics
set xtic font ", 18"
set key font ", 20"
set xlabel font ", 30"
set ylabel font ", 30"
set rmargin at screen 0.95

plot "raman.dat-broaden.dat" u 1:2 notitle w l ls 1
