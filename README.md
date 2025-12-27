# Hackathon II — The Evolution of Todo

## Project Overview

This project implements a todo application that evolves through 5 phases: CLI → Full-stack → AI chatbot → Local K8s → Cloud/event-driven, following spec-driven development principles.

## Phase I: CLI Todo Application

This is the first phase of the project: a command-line todo application that stores tasks in memory with no persistence. The application provides a menu-driven interface for users to add, view, update, delete, and toggle completion status of tasks.

### Features
- Add tasks with title and optional description
- View all tasks with status indicators
- Update existing tasks
- Delete tasks by ID
- Toggle task completion status
- Input validation and error handling

### Prerequisites
- Python 3.13+ (Phase I)
- Node.js (Phase II+)
- Docker (Phase IV+)
- Kubernetes (Phase V)

### Phase I: CLI Application Setup & Run
```bash
# Clone the repository
git clone <repository-url>
cd hackhathone2-todo-app

# Setup for Phase I with UV (recommended)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt

# Or using standard Python
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### Running the Application
```bash
# From the project root directory
cd src
python -m todo_app

# Or if you have it set up as a module
python -m todo_app.main
```

### Usage
1. The application will display a menu with options 1-6
2. Select an option by entering the corresponding number
3. Follow the prompts to perform the desired action
4. Use option 6 to exit the application

### Phase II: Full-Stack Web Application
```bash
# Frontend setup
cd frontend
npm install
npm run dev

# Backend setup
cd backend
pip install -r requirements.txt
python main.py
```

### Phase III: AI Chatbot Integration
```bash
# Setup MCP tools for AI agent integration
# Configuration for OpenAI ChatKit UI
```

### Phase IV: Kubernetes Deployment (Local)
```bash
# Using Minikube and Helm
minikube start
helm install todo-app ./charts/todo-app
```

### Phase V: Cloud Deployment
```bash
# Cloud Kubernetes with Kafka and Dapr
kubectl apply -f k8s/
```

## Deploy

### Phase II+ Deployment
- Frontend: Deployed on Vercel (or similar platform)
- Backend: Deployed on cloud platform with environment configuration

### Phase IV+ Deployment
- Helm charts available in `/charts/`
- Kubernetes manifests in `/k8s/`

## Demo Steps

### Phase I Demo
1. Run CLI application
2. Add, list, update, delete, and mark tasks complete
3. Verify basic functionality

### Phase II Demo
1. Access web UI
2. Create account and authenticate
3. Perform todo operations with proper user isolation
4. Verify JWT authentication

### Phase III Demo
1. Interact with AI chatbot
2. Perform todo operations via natural language
3. Verify MCP tool integration

### Phase IV+ Demo
1. Deploy to Kubernetes
2. Verify scalability and health checks
3. Test containerized deployment

## Environment Variables

### Required Environment Variables
```env
# Backend Authentication
BETTER_AUTH_SECRET=your_secret_here
DATABASE_URL=postgresql://user:pass@host:port/db

# Frontend Configuration
NEXT_PUBLIC_API_URL=http://localhost:8000

# Phase III+ AI Integration
OPENAI_API_KEY=your_openai_key
```

### Example .env File
Create `.env.example` with all required environment variables for local development.

## Architecture

### Tech Stack by Phase
- **Phase I**: Python 3.13+, UV, console app, in-memory storage
- **Phase II**: Next.js (App Router), FastAPI, SQLModel, Neon Postgres, Better Auth (JWT)
- **Phase III**: OpenAI ChatKit UI, OpenAI Agents SDK, Official MCP SDK
- **Phase IV**: Docker, Minikube, Helm, kubectl-ai
- **Phase V**: Kafka + Dapr, cloud Kubernetes (DigitalOcean DOKS), CI/CD

### Security & User Isolation
- JWT authentication required for all API endpoints
- User data isolation enforced at database query level
- Role-based access control (RBAC)
- Secure secret management

## Contributing

### Development Workflow
1. Create feature branch: `git checkout -b feature/###-feature-name`
2. Create spec in `/specs/[feature]/spec.md`
3. Generate plan with `/sp.plan`
4. Generate tasks with `/sp.tasks`
5. Implement following tasks in priority order
6. Create PHR for significant changes
7. Submit PR with constitution compliance verification

### Code Standards
- Follow spec-driven development principles
- Maintain traceability: `[From]: spec §X.Y + plan §A.B`
- Write testable, independent user stories
- Ensure cross-cutting concerns are addressed

## Project Structure
```
/
├── .specify/           # SpecKit configuration
├── specs/             # Feature specifications, plans, tasks
├── frontend/          # Next.js application (Phase II+)
├── backend/           # FastAPI application (Phase II+)
├── history/           # Prompt History Records and ADRs
├── charts/            # Helm charts (Phase IV+)
├── k8s/               # Kubernetes manifests (Phase V)
├── CLAUDE.md          # Claude Code instructions
├── AGENTS.md          # Agent behavior rules
└── README.md          # This file
```

## Documentation Standards
- All PRs require constitution compliance verification
- PHRs created for significant changes
- ADRs for architecturally significant decisions
- Traceability maintained from requirements to implementation

## Success Criteria
- All 5 phases implemented with spec-driven approach
- Demonstrable working app at each checkpoint
- AI chatbot performs todo operations via MCP tools
- Deployments reproducible via documented commands
- Complete spec history and traceability maintained