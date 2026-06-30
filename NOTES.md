## Current Architecture

Frontend:
- Next.js

Backend:
- No cloud backend yet

Desktop Integration:
- electron/

Claude Code Execution:
- Not found yet

Database:
- Prisma

Authentication:
- Yet to investigate

## Investigation

Found:
pages/api/ws

Likely Purpose:
- WebSocket endpoint
- Streams responses between frontend and backend

Next:
Inspect pages/api/ws

## Day 3

- Installed Docker Desktop and WSL 2
- Verified Docker Engine
- Created Docker service using Docker SDK
- Tested Docker container creation
- Integrated Docker with the /projects API
- Each project now creates:
  - a workspace folder
  - a dedicated Docker container