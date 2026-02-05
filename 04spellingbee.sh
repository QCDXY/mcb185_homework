cd ~/Code/MCB185/data
gunzip -c dictionary.gz | grep -E "^[acinorz]{4,}$" | grep -E "r" -c