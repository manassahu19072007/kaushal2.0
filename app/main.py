import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings
from app.core.database import Base, engine, migrate_sqlite_schema
from app.routers import (
    auth,
    communities,
    intelligence,
    certification,
    gaps,
    reports,
    jobs,
    platform,
)

# Automatically create all SQL tables on boot
Base.metadata.create_all(bind=engine)
migrate_sqlite_schema()

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url=f"{settings.API_V1_STR}/docs",
)

# Dynamically parse CORS origins from Environment Variable or settings
# Strips whitespace and trailing slashes (e.g., https://site.com/ -> https://site.com)
raw_origins = os.getenv("CORS_ORIGINS", "")
if raw_origins:
    origins = [origin.strip().rstrip("/") for origin in raw_origins.split(",") if origin.strip()]
else:
    origins = [str(origin).strip().rstrip("/") for origin in getattr(settings, "cors_origins_list", [])]

# Fallback to allow all if no explicit origins configured
if not origins:
    origins = ["*"]

# Enable CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True if origins != ["*"] else False,  # Browser safety requirement
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount all domain routers under /api
app.include_router(auth.router, prefix=settings.API_V1_STR)
app.include_router(communities.router, prefix=settings.API_V1_STR)
app.include_router(intelligence.router, prefix=settings.API_V1_STR)
app.include_router(certification.router, prefix=settings.API_V1_STR)
app.include_router(gaps.router, prefix=settings.API_V1_STR)
app.include_router(reports.router, prefix=settings.API_V1_STR)
app.include_router(jobs.router, prefix=settings.API_V1_STR)
app.include_router(platform.router, prefix=settings.API_V1_STR)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": settings.PROJECT_NAME}
