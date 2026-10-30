# MosaicChat

A cross-platform social app that stitches together short posts, stories, and voice notes into a personal mosaic.

## Tech Stack
- **Backend**: FastAPI, SQLAlchemy, PostgreSQL
- **Frontend**: Vue 3, Pinia, Tailwind CSS, Lucide Icons

## Setup

### Backend
1. `cd backend`
2. `pip install -r requirements.txt`
3. Set `DATABASE_URL` in `.env` (or use the default provided in config).
4. `uvicorn app.main:app --reload`

### Frontend
1. `cd frontend`
2. `npm install`
3. `npm run dev` (Runs on http://localhost:3000)

## Features
- **Unified Mosaic**: Mix text, images, and voice notes.
- **Privacy Sliders**: Granular control per post.
- **Burnout Detector**: AI-powered suggestions for creators to take breaks.
- **Direct Support**: Subscription-ready architecture.