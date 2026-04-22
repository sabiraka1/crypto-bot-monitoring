FROM grafana/grafana:latest
ENV GF_SECURITY_ADMIN_USER=admin
ENV GF_SECURITY_ADMIN_PASSWORD=admin123
ENV GF_INSTALL_PLUGINS=
ENV GF_PATHS_PROVISIONING=/etc/grafana/provisioning

COPY provisioning/datasources /etc/grafana/provisioning/datasources
COPY provisioning/dashboards /etc/grafana/provisioning/dashboards
COPY dashboards /var/lib/grafana/dashboards
