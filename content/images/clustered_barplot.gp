#set terminal pdf enhanced
set terminal png size 600,400
set output 'bar.png'

set style data histogram
set style histogram cluster gap 2

set style fill solid border rgb "black"
set auto x
set xlabel " "
set ylabel "Time (s)"
set yrange [0:*]
plot 'benchmark.dat' using 2:xtic(1) title col, \
        '' using 3:xtic(1) title col
