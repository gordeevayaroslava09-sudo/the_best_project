#!/bin/bash
read -p "Введите массу (в кг): " WEIGHT
read -p "Введите рост (в см): " HEIGHT
BMI=$((WEIGHT * 1000 / (HEIGHT * HEIGHT)))
echo "Ваше ИМТ равно $BMI"

