# Gig Work App 

A local gig jobs platform connecting clients with workers for short-term opportunities.

[![Status](https://img.shields.io/badge/Status-In%20Development-yellow)]()
[![Backend](https://img.shields.io/badge/Backend-Python%20%7C%20Flask-green)]()
[![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-blue)]()

## About

The Gig Work App is a web-based platform that connects people offering short-term work (clients) with people seeking work (workers). Users can post gigs, browse opportunities, apply for jobs, and build credibility through reviews and badges.

**Project Info:**
- **Course:** CIS 1512: Software Engineering
- **Instructor:** Professor Hadi Nasser
- **Duration:** Sept 2025 - Dec 2025
- **Type:** Academic Prototype

## Key Features

- 🔐 Secure user registration and authentication
- 📝 Post and manage gig opportunities
- 🔍 Browse and search available gigs
- ✅ Apply for jobs with application tracking
- ⭐ Review and badge system for workers
- 🔔 Notifications for gig activities
- 📱 Responsive design for mobile and desktop

## Team

| Name | Role |
|------|------|
| Cordero | Backend Developer, UI/UX Designer |
| Sean | Backend Developer, UI/UX Designer |
| Melissa | Frontend Developer, Documentation |
| Tamara | Frontend Developer, Documentation |
| Luca | Scrum Master, DevOps, Database |

## Tech Stack

**Frontend:** HTML, CSS, JavaScript  
**Backend:** Node.js/Express OR Python/Flask  
**Database:** SQLite (dev), MySQL (production)  
**Auth:** JWT with bcrypt password hashing  

## Quick Start

### Prerequisites
- Node.js v14+ (or Python 3.8+)
- Git
- VS Code (recommended)

### Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/gig-work-app.git
   cd gig-work-app
   ```

2. **Set up backend**
   
   *Node.js:*
   ```bash
   cd backend
   npm install
   cp .env.example .env
   # Edit .env with your settings
   npm run dev
   ```
   
   *Flask:*
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   # Edit .env with your settings
   python app.py
   ```

3. **Set up frontend**
   ```bash
   cd frontend
   # Open index.html in browser
   # OR use Live Server in VS Code
   ```

4. **Configure environment**
   
   Create `backend/.env`:
   ```env
   PORT=3000
   DATABASE_URL=sqlite:///gig_app.db
   JWT_SECRET=your_secret_key_here
   BCRYPT_ROUNDS=12
   ```

Backend runs on `http://localhost:3000`  
Frontend runs on `http://localhost:8000` (or your live server port)

## Project Structure

```
gig-work-app/
├── backend/          # API server
│   ├── src/
│   │   ├── controllers/
│   │   ├── models/
│   │   ├── routes/
│   │   └── middleware/
│   └── config/
├── frontend/         # Web interface
│   ├── css/
│   ├── js/
│   ├── pages/
│   └── index.html
├── docs/            # Documentation
│   ├── SRS.md
│   ├── SPMP.md
│   └── API.md
└── tests/           # Test files
```

## Documentation

- [Software Requirements Specification (SRS)](./docs/SRS.md) - Full requirements
- [Project Management Plan (SPMP)](./docs/SPMP.md) - Timeline & planning
- [API Documentation](./docs/API.md) - Endpoint reference
- [Contributing Guide](./CONTRIBUTING.md) - Development workflow

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and commit: `git commit -m "feat: add feature"`
3. Push to your branch: `git push origin feature/your-feature`
4. Open a Pull Request

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

**Branch naming:**
- `feature/*` - New features
- `bugfix/*` - Bug fixes
- `docs/*` - Documentation updates

## Timeline

| Phase | Dates | Status |
|-------|-------|--------|
| Proposal | Sept 2-8 | ✅ Done |
| SRS/SPMP | Sept 9-22 | ✅ Done |
| Prototype | Sept 23-29 | ✅ Done |
| Design | Sept 30 - Oct 6 | ✅ Done |
| **Implementation** | **Oct 7 - Nov 3** | 🟡 **Current** |
| Testing | Nov 4-10 | ⏳ Upcoming |
| Final Demo | Dec 1 | ⏳ Upcoming |

## Testing

Testing phase begins Nov 4, 2025.

To run tests (once implemented):
```bash
# Backend tests
cd backend
npm test  # or: python -m pytest

# Frontend tests
cd frontend
npm test
```

## 📝 Current Status

**Sprint:** Implementation Phase (Week 4/4)  
**Focus:** Backend API development, Frontend UI implementation  
**Next:** Testing and validation phase

## Known Issues

- No payment processing (planned future enhancement)
- Notifications may require third-party integration
- Limited to 200 concurrent users in prototype

Track issues: [GitHub Issues](https://github.com/your-username/gig-work-app/issues)

## License

Academic project for CIS 1512. Educational use only.

## Contact

**Instructor:** Professor Hadi Nasser  
**Course:** CIS 1512: Software Engineering  

---

**Last Updated:** October 30, 2025  
**Version:** 0.1.0 (Prototype)
