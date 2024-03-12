# Substrate

# Next apps

- Initial setup: go to dashboard, docs, explore and run `yarn`
- Then go back to the root

```
# (when switching between dashboard/docs/explore)
npx vc link

# (pull new env vars into linked next project)
npx vc pull .env.development.local

# (run linked next project)
npx vc dev
```

# Python

- The preferred way to set up an environment is via `poetry`. [Install poetry by following these instructions](https://python-poetry.org/docs/).
- Install dependencies:
  - `make ensure`
- (Recommended) Set up the git pre-commit hook that runs `ruff check --fix`
  - `poetry run pre-commit install`

## Codegen

- See [`/openapi.json`](/site/public/openapi.json) for our Open API spec
- Some python code is generated automatically from this spec
  - `substrate.run/library` is dynamically rendered based on this spec
- To regenerate code after updating the spec:
  - `make generate`
- To publish `substratecore` to pypi for `substrate-python`:
  - `make _version.py` -> inspect the diff
  - `make publish`

## Local development

- You can develop an individual file locally using `poetry run modal run` with a `local_entrypoint` defined in a file.

```

poetry run modal run sb_models/sdxl/sdxl.py --prompt "cinematic ..."

```

## Staging

Use the `deploy-modal` script to deploy to staging:

```

poetry run ./scripts/deploy-modal.py --apps=usage --env=staging

```

And then use `https://api-staging.substrate.run`

(Note that this also uses the staging deploy of `sb-proxy`)

Commits to main are automatically deployed to `--env=main` via Github action.

## Creating your own modal environment

1. [`poetry run modal environment create`](https://modal.com/docs/guide/environments#environments-beta)
2. update the deploy script with your environment
3. run the deploy script with `--apps=all`
4. update `sb-proxy` with your environment

# Billing

- We use Orb for billing. Managing new prices requires juggling a bunch of scripts.
- See [`billing.md`](/internal-docs/billing.md)
- [`usage.py`](/sb_models/usage.py) is where we report usage to Orb.

# Observability

- `sb-proxy` logs the start and end of requests, and reports overall timing metrics
- [`usage.py`](/sb_models/usage.py) logs more extensive, redacted request info from inference runs

```

```
