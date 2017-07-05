# Hyperbola media

This directory contains an identifier (symlink or directory)
that points to or contains media for a given installation of
hyperbola.

`hyperbola.settings` automatically configures the media root
to be:

```python
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media', ENVIRONMENT)
```
