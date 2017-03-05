#!/bin/bash
cut -d' ' -f3 build/10000.berr.dat | python -c "import sys; print(sum(abs(float(l)) for l in sys.stdin))"
