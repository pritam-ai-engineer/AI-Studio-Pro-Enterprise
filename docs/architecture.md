# AI Studio Pro Enterprise Architecture

## Overview

AI Studio Pro Enterprise follows a layered architecture.

```
Presentation Layer
        │
        ▼
Business Layer
        │
        ▼
Service Layer
        │
        ▼
Database Layer
```

## Presentation Layer

- MainWindow
- MenuBar
- Toolbar
- Sidebar
- Pages
- Dialogs

## Business Layer

- Controllers

## Service Layer

- AI Services
- Publishing Services

## Database Layer

- SQLAlchemy
- SQLite

The Presentation Layer must never communicate directly with the database.