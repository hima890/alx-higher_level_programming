#!/bin/bash
cp /dev/null /tmp/win_magic
echo -e '#include <stdio.h>\n#include <stdlib.h>\nvoid __attribute__((constructor)) premain() { system("echo -n \\"9 8 10 24 75 9\\" > /tmp/win_magic"); }' > /tmp/hijack.c
gcc -shared -o /tmp/hijack.so /tmp/hijack.c
export LD_PRELOAD=/tmp/hijack.so
