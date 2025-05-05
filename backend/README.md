backend/
├── app/                           # Cod aplicație
│   ├── api/                       # API endpoints
│   │   ├── v1/                    # API versiunea 1
│   │   │   ├── endpoints/         # Grupare pe resurse
│   │   │   │   ├── auth.py
│   │   │   │   ├── signals.py
│   │   │   │   ├── users.py
│   │   │   │   └── ...
│   │   │   ├── dependencies.py    # Dependențe shared
│   │   │   └── router.py          # Router principal v1
│   │   ├── v2/                    # Versiuni viitoare API
│   │   └── api.py                 # Agregare toate versiuni
│   ├── core/                      # Nucleul aplicației
│   │   ├── config.py              # Configurări aplicație
│   │   ├── security.py            # JWT, criptare, etc
│   │   ├── exceptions.py          # Excepții personalizate
│   │   └── logging.py             # Setup logging
│   ├── db/                        # Acces baze de date
│   │   ├── base.py                # Setup db principal
│   │   ├── repositories/          # Acces date (repository pattern)
│   │   │   ├── base.py            # Repository abstract
│   │   │   ├── signals.py 
│   │   │   └── users.py
│   │   ├── migrations/            # Alembic migrations
│   │   │   ├── env.py
│   │   │   ├── script.py.mako
│   │   │   └── versions/          # Fișiere migrație
│   │   └── session.py             # Session management
│   ├── models/                    # Modele SQLAlchemy
│   │   ├── base.py                # Model de bază
│   │   ├── user.py
│   │   ├── signal.py
│   │   ├── market_data.py
│   │   └── ...
│   ├── schemas/                   # Modele Pydantic
│   │   ├── base.py                # Schema de bază
│   │   ├── auth.py
│   │   ├── user.py
│   │   ├── signal.py
│   │   └── ...
│   ├── services/                  # Logica de business
│   │   ├── auth.py
│   │   ├── signals.py
│   │   ├── users.py
│   │   └── ...
│   ├── tasks/                     # Task-uri asincrone
│   │   ├── worker.py              # Setări worker
│   │   ├── market_data.py         # Import date
│   │   ├── signal_generation.py   # Generare semnale
│   │   └── notifications.py       # Trimitere notificări
│   ├── utils/                     # Utilități
│   │   ├── constants.py
│   │   ├── helpers.py
│   │   └── validators.py
│   └── main.py                    # Punct intrare aplicație
├── ai/                            # Module AI (separate)
│   ├── models/                    # Implementări modele
│   │   ├── base.py                # Clasă model de bază
│   │   ├── random_forest.py
│   │   ├── lstm.py
│   │   └── ...
│   ├── features/                  # Feature engineering
│   │   ├── technical_indicators.py
│   │   ├── preprocessor.py
│   │   └── ...
│   ├── training/                  # Antrenare modele
│   │   ├── trainer.py
│   │   ├── hyperparameter_tuning.py
│   │   └── ...
│   ├── evaluation/                # Evaluare modele
│   │   ├── metrics.py
│   │   ├── backtesting.py
│   │   └── ...
│   ├── inference/                 # Inferență modele
│   │   ├── predictor.py
│   │   ├── signal_generator.py
│   │   └── ...
│   └── registry/                  # Stocare și versionare modele
│       ├── model_registry.py
│       └── versioning.py
├── config/                        # Configurări
│   ├── settings.py                # Setări aplicație
│   ├── environments/              # Configurări specifice mediului
│   │   ├── base.json
│   │   ├── development.json
│   │   ├── staging.json
│   │   └── production.json
│   └── logging_config.json        # Configurare logging
├── scripts/                       # Scripturi utilitare
│   ├── seed_db.py
│   ├── generate_test_data.py
│   └── ...
├── tests/                         # Teste
│   ├── conftest.py
│   ├── unit/                      # Teste unitare
│   │   ├── api/
│   │   ├── services/
│   │   └── ...
│   ├── integration/               # Teste integrare
│   │   ├── api/
│   │   ├── db/
│   │   └── ...
│   └── e2e/                       # Teste end-to-end
├── docs/                          # Documentație
│   ├── architecture/
│   ├── api/
│   └── development/
├── docker/                        # Fișiere Docker
│   ├── Dockerfile.api
│   ├── Dockerfile.worker
│   ├── Dockerfile.ai
│   └── ...
├── deployment/                    # Configurări deployment
│   ├── kubernetes/
│   ├── terraform/
│   └── ...
├── pyproject.toml                 # Dependențe și build
├── alembic.ini                    # Configurare Alembic
└── README.md