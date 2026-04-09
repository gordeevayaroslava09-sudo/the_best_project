#!/bin/bash
check_root() {
    if [ $EUID -ne 0 ]; then
        echo "Ошибка: Требуются права root."
        exit 1
    fi
}
check_root
echo "Скрипт запущен от root"
