# Crypto Bot Monitoring

Monitoring stack for crypto-ai-bot on Railway.

## Services
- **Prometheus** — metrics collection (scrapes `crypto-ai-bot.railway.internal:8080/metrics` every 30s)
- **Grafana** — visualization (4 provisioned dashboards: decision-funnel, exits, signal-quality, system-health)
- **Alertmanager** — notifications (Telegram via env-substituted bot token / chat id)

## Deployment
Each folder deploys as a separate service in Railway.

## Required Railway env vars

### `grafana` service
- `GF_SECURITY_ADMIN_USER` — admin username (required; no default)
- `GF_SECURITY_ADMIN_PASSWORD` — admin password (required; no default)

### `alertmanager` service
- `TELEGRAM_BOT_TOKEN` — bot token for alert delivery (substituted by `entrypoint.sh`)
- `TELEGRAM_CHAT_ID` — target chat id (substituted by `entrypoint.sh`)

## Editing dashboards

Dashboards are **file-provisioned** from `grafana/dashboards/*.json` (Dockerfile `COPY`s them into
the container at `/var/lib/grafana/dashboards`). The provisioning config sets
`allowUiUpdates: true`, which means the Grafana UI lets you edit, but those edits are
**ephemeral** — any redeploy rebuilds the container from the JSON in this repo and overwrites them.

Workflow:
1. Tweak in Grafana UI.
2. `Share → Export → Save to file` or copy the model JSON from the panel inspector.
3. Commit the resulting JSON under `grafana/dashboards/`.
4. Push → Railway redeploys → dashboards persist.

