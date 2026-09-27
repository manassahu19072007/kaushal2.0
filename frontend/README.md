# KAUSHAL Frontend

React + Vite frontend starter for the KAUSHAL labour-market intelligence and curriculum-alignment platform.

## Roles

- Candidate
- Recruiter
- Trainer
- Institute Admin
- Policy Officer

## Run

```bash
npm install
npm run dev
```

Open the Vite URL shown in the terminal.

## Authentication

The login screen registers and authenticates accounts through the FastAPI
backend. Supported account roles are Candidate, Recruiter, Trainer,
Institute Admin, and Policy Officer.

## Backend

Set the FastAPI base URL in `.env` for local development:

```env
VITE_API_URL=http://localhost:8000/api
```

Frontend RBAC controls navigation and page access. The backend validates bearer
tokens and enforces access to recruiter jobs and applications.

For production, set the build-time `VITE_API_URL` variable on the static site
to the API base URL, including its `/api` prefix (for example,
`https://kaushal-mo8y.onrender.com/api`). The production build defaults to
that Render API URL when the variable is not set. Add the frontend's exact
origin to the backend's `CORS_ORIGINS` setting; the known Render frontend
origins are included in the backend defaults.

## Naming

React-side state, props and API fields use camelCase, matching the project naming reference.