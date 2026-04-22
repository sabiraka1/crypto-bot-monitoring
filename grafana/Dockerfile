FROM grafana/grafana:latest
# Admin credentials must be injected via Railway env vars:
#   GF_SECURITY_ADMIN_USER, GF_SECURITY_ADMIN_PASSWORD.
# Defaults are left unset so a missing env fails closed (Grafana refuses
# to start with the stock admin/admin banner on production).
ENV GF_INSTALL_PLUGINS=
ENV GF_PATHS_PROVISIONING=/etc/grafana/provisioning

COPY provisioning/datasources /etc/grafana/provisioning/datasources
COPY provisioning/dashboards /etc/grafana/provisioning/dashboards
COPY dashboards /var/lib/grafana/dashboards
