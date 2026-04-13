FROM prom/alertmanager:latest

COPY alertmanager.yml /etc/alertmanager/alertmanager.yml

# entrypoint.sh substitutes TELEGRAM_BOT_TOKEN_PLACEHOLDER and
# TELEGRAM_CHAT_ID_PLACEHOLDER in alertmanager.yml at startup from env vars.
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
