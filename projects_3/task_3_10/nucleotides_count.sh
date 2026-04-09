#!/bin/bash
for file in *.fasta; do
    if [ ! -f "$file" ]; then
        continue
    fi
    sequence=$(grep -v "^>" "$file" | tr -d '\n')
    A=$(echo "$sequence" | grep -o "A" | wc -l)
    T=$(echo "$sequence" | grep -o "T" | wc -l)
    G=$(echo "$sequence" | grep -o "G" | wc -l)
    C=$(echo "$sequence" | grep -o "C" | wc -l)
    printf "%-15s %-7s %-7s %-7s %-7s\n" "$file" "$A" "$T" "$G" "$C"
done
