# Fast API demo

## setup

```bash
git clone https://github.com/okisidentarisu/Fast-API-demo.git
cd Fast-API-demo
```

```bash
docker-compose build
```

```bash
docker-compose run \
  --entrypoint "poetry init \
    --name demo-app \
    --dependency fastapi \
    --dependency uvicorn[standard] \
    --dependency itsdangerous" \
  demo-app
```

Then, answer `n` only to the question `Author [None, n to skip]:` and press <kbd>Enter</kbd> to skip the rest.

```bash
docker-compose run --entrypoint "poetry install --no-root" demo-app
```

```bash
docker-compose build --no-cache
```

```bash
docker-compose up
```
