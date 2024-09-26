set autoscale
unset log
unset label
set xtics scale 3
set ytics scale 3
set xtic font ", 25"
set ytic font ", 25"
set key font ", 20"
set xlabel "E-Ef (eV)"
set xlabel font ", 25"
set ylabel "DOS"
set ylabel font ", 25"
set xzeroaxis linetype 3 lc rgb 'black'
set xtic axis

plot 'TDOS.dat' using ($1):2 notitle with filledcurves above fs transparent solid 0.1 lc rgb 'blue',\
     'TDOS.dat' using ($1):($3*1) notitle with filledcurves below fs transparent solid 0.1 lc rgb "blue"

pause -1 'Hit any key to continue\n'
