# vulstack-ci-template

A template for CY students to get some hands-on experience integrating security tools into CI/CD pipeline. It's got a frontend and backend with some known vulnerabilities for testing.

## Security tools

- SCA (Software Composition Analysis)
- SAST (Static Application Security Testing)
- DAST (Dynamic Application Security Testing)

## Getting the Services Running
You can spin up the service locally or using docker. Once they're up, hit the frontend at `localhost:3000`

### Local
``` bash
# Frontend
cd frontend
npm install
npm run dev

# Backend
cd backend
python -m venv venv # optional: set up a virtual environment
source venv/bin/activate # optional: if virtual environment is available

pip install -r requirements.txt
python3 app.py
```

### Docker Setup
```bash
docker compose -f docker-compose.yaml up

# handy Docker commands
docker ps                               # list of running containers
docker exec -it <name of container> sh  # hop into a container's shell to run commands
```