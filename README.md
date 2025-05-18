# Climate Data System

## Quick Start with Docker Compose

1. **Prerequisites**:
   - Docker
   - Docker Compose

2. **Run the full stack**:

   ```bash
   docker-compose up --build
   ```

   - Frontend: <http://localhost:3000>
   - Backend API: <http://localhost:8000/docs>

## Individual Service Control

### Frontend (Next.js)

```bash
# Build and run
docker-compose up frontend

# Stop
docker-compose stop frontend

# View logs
docker-compose logs -f frontend
```

### Backend (FastAPI)

```bash
# Build and run
docker-compose up backend

# Stop
docker-compose stop backend

# View logs
docker-compose logs -f backend
```

## Development Tips

1. **Rebuild specific service**:

   ```bash
   docker-compose up --build frontend
   ```

2. **Clean up**:

   ```bash
   docker-compose down -v
   ```

3. **Environment Variables**:
   - Edit `.env` files in each service directory
   - Frontend connects to backend via `NEXT_PUBLIC_API_URL`
