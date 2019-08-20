# PulsewayDockerContainerMonitor
A simple workaround to allow Pulseway to monitor Docker containers by using a generic systemd service

To use this solution properly:

1. Copy one of the scripts to `/opt/` (or other location if you want) and give it permission of exection (`chmod +x script`)
2. Copy the special service file (`pulseway-docker@.service`) to one of the valid systemd locations (e.g. `/lib/systemd/system`)
3. Enable the service for each specific Docker container you want to monitor using the following notation:

```
$ systemctl enable pulseway-docker@nameofcontainer
$ systemctl start pulseway-docker@nameofcontainer
```

4. Include the entry in the Pulseway XML config file as a systemd service inside of the section `MonitoredServices`:

```
<MonitoredServices>
  <Service Name="pulseway-docker@nameofcontainer.service" DisplayName="Container Name" IsDaemon="true" DaemonType="SYSTEMD" Path="" StartParameters="" CanBeStopped="false" Enabled="true"/>
</MonitoredServices>

```

5. Restart the Pulseway agent.
