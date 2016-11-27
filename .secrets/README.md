# Secrets

Files required for running ansible and terraform:

- `bastion-ingress-ip.txt`
- `cloudflare-api-key.txt`
- `vault-password.txt`

Also required for terraform and packer are aws credentials at `~/.aws/credentials`.

Generate the bastion ingress IP by running:

```bash
curl icanhazip.com --silent -o .secrets/bastion-ingress-ip.txt
```
