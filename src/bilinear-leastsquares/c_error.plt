set terminal svg size 750,350
set output "c_error.svg"

set cbrange [-0.25:0.25]
set palette defined ( -1 "black", -0.6 "red", -0.3 "yellow", 0 "white", 0.3 "cyan", 0.6 "blue", 1 "purple" )
set xrange [-100e3:0e3]
set yrange [5:15e3]

set title "t = 10000"
plot 'build/cerr.dat' using 1:2:3 notitle with points palette pt 7
