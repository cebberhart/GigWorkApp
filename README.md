# Gig Work App 

A local gig jobs platform connecting clients with workers for short-term opportunities.

[![Status](https://img.shields.io/badge/Status-In%20Development-yellow)]()
[![Backend](https://img.shields.io/badge/Backend-Python%20%7C%20Flask-green)]()
[![Frontend](https://img.shields.io/badge/Frontend-HTML%20%7C%20CSS%20%7C%20JS-blue)]()

## About

The Gig Work App is a web-based platform that connects people offering short-term work (clients) with people seeking work (workers). Users can post gigs, browse opportunities, apply for jobs, and build credibility through reviews and badges.

## Key Features

- 🔐 Secure user registration and authentication
- 📝 Post and manage gig opportunities
- 🔍 Browse and search available gigs
- ✅ Apply for jobs with application tracking
- ⭐ Review and badge system for workers
- 🔔 Notifications for gig activities
- 📱 Responsive design for mobile and desktop

## Tech Stack

**Frontend:** HTML, CSS, JavaScript  
**Backend:** Python / Flask  
**Database:** SQLite (development), MySQL (production)  
**Authentication:** JWT with bcrypt password hashing  

## Quick Start

### Prerequisites
- Python 3.8+  
- Git  
- VS Code or another code editor 

### Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/cebberhart/GigWorkApp
   cd gig-work-app
   ```

2. **Set up backend**
   
   *Flask:*
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env      # Edit .env with your settings
   python app.py
   ```
3. **Set up frontend**
   ```bash
   cd frontend
   # Open index.html in your browser
   # OR use Live Server in VS Code

Backend runs on `http://localhost:5000`  
Frontend can be accessed via your browser or live server.

## Documentation

- [Software Requirements Specification (SRS)](./docs/SRS.md) - Full requirements
- [Project Management Plan (SPMP)](./docs/SPMP.md) - Timeline & planning
- [API Documentation](./docs/API.md) - Endpoint reference

## Team

| Name | Role |
|------|------|
| Cordero | Backend Developer, UI/UX Designer, Database, Documentation |
| Sean | Backend Developer, UI/UX Designer, Documentation |
| Melissa | Frontend Developer,UI/UX Designer, Documentation |
| Tamara | Frontend Developer,UI/UX Designer, Documentation |
| Luca | Documentation |

## Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and commit: `git commit -m "feat: add feature"`
3. Push to your branch: `git push origin feature/your-feature`
4. Open a Pull Request

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed guidelines.

## License

Academic project for CIS 1512. Educational use only.

## Contact

**Instructor:** Professor Hadi Nasser  
**Course:** CIS 1512: Software Engineering  

---

**Last Updated:** November 30, 2025  
**Version:** 0.1.0 (Prototype)
