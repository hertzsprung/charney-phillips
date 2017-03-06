set terminal svg size 1000,700
set output "b_error.svg"

set cbrange [-0.25:0.25]
set palette defined ( -1 "black", -0.6 "red", -0.3 "yellow", 0 "white", 0.3 "cyan", 0.6 "blue", 1 "purple" )
set xrange [-50e3:100e3]
set yrange [5:15e3]

set multiplot layout 2,1

set title "t = 5000"
plot 'build/5000.berr.dat' using 1:2:3 notitle with points palette pt 7

set title "t = 10000"
plot 'build/10000.berr.dat' using 1:2:3 notitle with points palette pt 7
