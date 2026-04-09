#!/bin/bash
for i in {1..10}; do
    touch "test$i.txt"
done

echo "Все файлы созданы. Начинаем удаление в обратном порядке..."

counter=10
while [ $counter -ge 1 ]; do
    rm "test$counter.txt"
    counter=$((counter - 1))
done

echo "Операция завершена: все файлы созданы и удалены"
