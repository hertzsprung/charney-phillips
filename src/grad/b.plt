#set terminal svg size 1200,400
#set output "b.svg"

set cbrange [0:1]
set palette defined ( 0 "white", 1 "black" )
set xrange [-80e3:-20e3]
set yrange [5e3:13e3]
unset colorbox

plot 'build/b.dat' using 1:2:3 notitle with points palette pt 7 ps 3.5, \
     'build/grad_b_analytic.dat' using 1:2:($3*3e7):($4*3e5) with vectors, \
     'build/grad_5_Bilinear.dat' using 1:2:($3*3e7):($4*9e5) with vectors, \
