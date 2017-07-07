# hyperbola systemd units

All services run in the foreground—no daemon mode.

Use instantiated instances to avoid code duplication. `hyperbola-wiki@.service`
is parameterized on backend number. `hyperbola-app@.service` is parameterized
on environment.

## Deploy

### wiki

```bash
sudo cp systemd/hyperbola-wiki@.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable hyperbola-wiki@{0,1,2}.service
sudo systemctl start 'hyperbola-wiki@*'
```

### hyperbola app

```bash
sudo cp systemd/hyperbola-app@.service /etc/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable hyperbola-app@{production,staging}.service
sudo systemctl start 'hyperbola-app@*'
```
