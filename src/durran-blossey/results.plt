set cbrange [0:1]
set palette defined ( 0 "white", 1 "black" )
set xrange [-100e3:100e3]
set yrange [0:25e3]
unset colorbox

set multiplot layout 3,1

set title "t = 0"
plot 'build/0.dat' using 1:2:3 notitle with points palette pt 7 ps 0.5

set title "t = 5000"
plot 'build/5000.dat' using 1:2:3 notitle with points palette pt 7 ps 0.5

set title "t = 10000"
plot 'build/10000.dat' using 1:2:3 notitle with points palette pt 7 ps 0.5
