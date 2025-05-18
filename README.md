# Climate Data System (ERA5)

## Project Structure

```bash
project-root/
├── cds-api/       # FastAPI backend
├── cds-ui/        # Next.js frontend (submodule)
└── docker-compose.yml
```

## Setup Instructions

1. **Clone the main project**:

   ```bash
   git clone --recurse-submodules https://github.com/tobslob/ERA5.git
   cd ERA5
   ```

2. **Verify submodules**:

   ```bash
   git submodule status
   # Should show: cds-ui (hash) cds-ui
   ```

## Running with Docker

### Full Stack

```bash
docker-compose up --build
```

- Frontend: <http://localhost:3000>
- Backend API: <http://localhost:8000/docs>

### Individual Services

```bash
# Frontend only (Next.js)
docker-compose up frontend

# Backend only (FastAPI)
docker-compose up backend
```

## Development Workflow

1. **Update submodules**:

   ```bash
   git submodule update --remote
   ```

2. **Rebuild specific service**:

   ```bash
   docker-compose up --build frontend
   ```

3. **Clean up**:

   ```bash
   docker-compose down -v
   ```

## Repository Links

- [Main Project](https://github.com/tobslob/ERA5)
- [Frontend Submodule](https://github.com/tobslob/cds-ui)
- [Backend API](https://github.com/tobslob/ERA5/tree/main/cds-api)

> Note: The frontend is maintained as a separate repository but included as a submodule for development convenience.
