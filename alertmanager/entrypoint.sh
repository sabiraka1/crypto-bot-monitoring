#!/bin/sh
# Заменяем переменные в конфиге
sed -i "s|TELEGRAM_BOT_TOKEN_PLACEHOLDER|${TELEGRAM_BOT_TOKEN}|g" /etc/alertmanager/alertmanager.yml
sed -i "s|TELEGRAM_CHAT_ID_PLACEHOLDER|${TELEGRAM_CHAT_ID}|g" /etc/alertmanager/alertmanager.yml

# Запускаем Alertmanager
exec /bin/alertmanager --config.file=/etc/alertmanager/alertmanager.yml --storage.path=/alertmanager