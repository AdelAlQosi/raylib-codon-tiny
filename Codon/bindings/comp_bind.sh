#!bin/bash

gcc -shared -fPIC -lm -lraylib ./bindings.c -o shared/bindings.so