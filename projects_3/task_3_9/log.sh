#!/bin/bash
FILE_PATH="./system.log"
ERROR_CODE=1
case $ERROR_CODE in
    0)
        echo "Статус: Ошибок нет." ;;
    1)
        echo "Статус: Критическая ошибка!" ;;
    *)
        echo "Статус: Неизвестный код." ;;
esac
