# Architecture Decisions

## ADR-001

### Decision

The GUI layer must not directly access the database.

### Reason

To separate presentation from business logic.

---

## ADR-002

### Decision

Every GUI component will be its own reusable widget.

### Reason

Improves testing and reuse.

---

## ADR-003

### Decision

MainWindow is responsible only for assembling components.

### Reason

Keeps the application modular.