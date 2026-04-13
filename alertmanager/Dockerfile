FROM prom/alertmanager:latest

COPY alertmanager.yml /etc/alertmanager/alertmanager.yml

# entrypoint.sh substitutes TELEGRAM_BOT_TOKEN_PLACEHOLDER and
# TELEGRAM_CHAT_ID_PLACEHOLDER in alertmanager.yml at container start
# from Railway env vars, then launches alertmanager.
# --chmod=755 avoids a separate RUN chmod which fails on the minimal
# alertmanager image (no shell utilities for file permission changes).
COPY --chmod=755 entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
