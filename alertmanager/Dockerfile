FROM prom/alertmanager:latest

COPY alertmanager.yml /etc/alertmanager/alertmanager.yml

# Добавляем скрипт для замены переменных
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]