# Chai Club

Chai Club is a community platform for chai lovers to meet, connect, and build meaningful local relationships. Starting in Munich, it helps people discover others nearby, connect around shared interests, and arrange relaxed in-person or virtual conversations.

## Core experience

- Location-based matching for nearby meetups
- Topic-based matching for shared interests
- Optional video conversations
- Community stories, recipes, and chai culture

## Architecture

- Python and FastAPI backend services
- Python ML sidecar for semantic embeddings and topic matching
- PostgreSQL with PostGIS and pgvector
- Docker for local database setup

## Getting started

Create a Python environment, install the project dependencies, and start the database and matching API:

```bash
cp .env.example .env
# Edit .env and set a private local database password.
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
docker compose --env-file .env -f deployments/docker-compose.yml up --build -d
uvicorn matching_service.main:app --reload --app-dir services/matching-service
```

Do not commit `.env`; it is excluded by `.gitignore`. Keep production credentials in your deployment platform's secret manager instead of a checked-in file.

The matching API currently exposes `GET /health`. Its request and response models are in `services/matching-service/matching_service/domain/match.py`.

## License

This project is licensed under the MIT License. See [LICENSE](./LICENSE).
