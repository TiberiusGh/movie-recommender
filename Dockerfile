FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app
ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    PATH="/app/backend/.venv/bin:$PATH"

COPY backend/pyproject.toml backend/uv.lock backend/.python-version backend/
RUN cd backend && uv sync --frozen --no-dev --no-install-project

COPY backend/ backend/
COPY web/ web/
COPY data/ data/

RUN useradd --create-home appuser
USER appuser

EXPOSE 8000
CMD ["gunicorn", "--chdir", "backend", "--bind", "0.0.0.0:8000", "--workers", "2", "app:app"]
