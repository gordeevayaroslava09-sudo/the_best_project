#!/bin/bash
df -h | awk 'NR>1 {print $1, $5}' | while read fs percent; do
    echo "$fs $percent"
    if [ ${percent%\%} -gt 90 ]; then
        echo "ПРЕДУПРЕЖДЕНИЕ: $fs заполнена на $percent"
    fi
done
