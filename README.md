# TBB Chai Club

TBB stands for The Brown Brew. This project is the community-building platform behind The Brown Brew, a company focused on bringing together chai lovers and creating warm, meaningful connection through community.

TBB Chai Club is a community-driven platform for chai lovers to meet, connect, and build meaningful local relationships. The idea is inspired by the spirit of a social club: a welcoming space where people can come together over tea, conversation, and shared experiences.

The project is starting in Munich, with the goal of helping people find like-minded friends, conversations, and casual meetups in a warm and low-pressure way. It is rooted in the mission of The Brown Brew: to build a space for people who love chai, connection, and community.

## Mission

The Brown Brew is built around the idea that chai is more than a drink — it is a ritual of hospitality, creativity, and human connection. TBB Chai Club brings that philosophy into a digital community where people can meet, learn, and share.

We want to create an easy and human way for people to:

- discover other chai lovers nearby
- connect around a shared interest or topic
- meet for a walk and a cup of chai
- arrange a virtual chai conversation when meeting in person is not possible

## Core experience

The platform helps people connect in three main ways:

### 1. In-person meetups
Users can express interest in meeting others nearby, share their location, and find people who are open to a casual walk, coffee, or tea together.

### 2. Video chai calls
If someone is not available to meet in person, they can still connect over a short video call and enjoy a relaxed conversation over chai from anywhere.

### 3. Community stories and knowledge sharing
Users can share reflections, blog posts, short videos, recipes, personal rituals, and creative ideas around chai culture. This creates a space for inspiration, learning, and deeper connection beyond just one-to-one matching.

This blog and vlog area can include:

- chai recipes and brewing guides
- reflections on what chai means to people
- creativity and chai culture
- personal stories and rituals
- slow living, hospitality, and community-building ideas
- recommendations for places, books, music, or experiences connected to the chai lifestyle

## Why this matters

This is more than just a matching app. It is a social community builder designed to reduce isolation, encourage real conversations, and make it easier for people to meet new friends in a comfortable, friendly setting.

## Product vision

The initial focus is Munich, but the long-term aim is to grow into a broader community network where people can connect across cities and cultures through shared hospitality and conversation.

TBB Chai Club is not only a meetup app. It is also a community archive and storytelling platform where members can publish essays, recipes, reflections, short videos, and creative inspiration related to chai, connection, and everyday rituals.

## How the app works

The platform combines:

- location-based matching to find nearby people
- topic-based matching to connect around shared interests
- role-based matching for hosts and guests or community members seeking introductions
- optional video conversation support for digital connection

## Current architecture

This repo is structured as a microservice-based application with:

- a matching service for finding nearby and relevant people
- a Python ML sidecar for semantic embeddings and topic matching
- support for geospatial and vector-based profile matching
- a Postgres database configured with PostGIS and pgvector

## Stack

- Python and FastAPI for backend services
- Python for the ML/embedding service
- PostgreSQL drivers and pgvector Python support
- PostgreSQL + PostGIS + pgvector for location and semantic matching
- Docker for local environment setup

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

Do not commit `.env`; it is excluded by `.gitignore`. Keep real production credentials in your deployment platform's secret manager instead of a checked-in file.

The matching API currently exposes `GET /health`. The matching request and response models are in `services/matching-service/matching_service/domain/match.py`.

The previous Go module directories for user, community, reward, and shared code contained no Go source files, so there was no service behavior in those modules to port. They can be implemented as Python packages when those services are developed.

## Future direction

The next phases for the platform could include:

- user profiles and onboarding
- trust and safety controls
- matching preferences and filters
- event-based community meetups
- blog and vlog publishing
- recipe and ritual sharing spaces
- richer chat and video experiences
- community-led content and discovery features

## Summary

TBB Chai Club is a community app built around friendship, conversation, and shared chai experiences. It is designed to help people meet one another in a relaxed, human way, while also creating a space to share stories, inspiration, creativity, and chai rituals. Starting in Munich, it aims to grow into a welcoming network for chai lovers everywhere.
