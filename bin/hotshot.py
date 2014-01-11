#!/usr/bin/env bash

python <<EOF

import hotshot.stats

stats = hotshot.stats.load('$1')
stats.sort_stats('time', 'calls')
stats.print_stats(20)
EOF
