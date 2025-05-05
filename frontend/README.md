frontend/
├── public/                        # Fișiere statice
├── src/
│   ├── assets/                    # Resurse
│   │   ├── images/
│   │   ├── styles/                # Stiluri globale
│   │   └── fonts/
│   ├── components/                # Componente React
│   │   ├── common/                # Componente comune
│   │   │   ├── Button/
│   │   │   ├── Input/
│   │   │   └── ...
│   │   ├── layout/                # Componente layout
│   │   │   ├── Header/
│   │   │   ├── Sidebar/
│   │   │   └── ...
│   │   ├── features/              # Organizate pe feature
│   │   │   ├── auth/
│   │   │   ├── signals/
│   │   │   ├── charts/
│   │   │   └── ...
│   │   └── modals/                # Dialoguri modale
│   ├── config/                    # Configurări frontend
│   │   ├── api.js                 # Configurare API
│   │   ├── routes.js              # Definire rute
│   │   └── constants.js           # Constante aplicație
│   ├── contexts/                  # React Context
│   │   ├── AuthContext.js
│   │   ├── ThemeContext.js
│   │   └── ...
│   ├── hooks/                     # Custom hooks
│   │   ├── useAuth.js
│   │   ├── useSignals.js
│   │   └── ...
│   ├── lib/                       # Librării și utilități
│   │   ├── api.js                 # Client API
│   │   ├── socket.js              # Configurare WebSocket
│   │   ├── storage.js             # Local storage utils
│   │   └── ...
│   ├── pages/                     # Pagini aplicație
│   │   ├── Dashboard/
│   │   ├── SignalList/
│   │   ├── SignalDetails/
│   │   ├── Profile/
│   │   └── ...
│   ├── services/                  # Servicii comunicare API
│   │   ├── auth.service.js
│   │   ├── signals.service.js
│   │   ├── users.service.js
│   │   └── ...
│   ├── store/                     # State management (Redux)
│   │   ├── actions/
│   │   ├── reducers/
│   │   ├── selectors/
│   │   ├── middlewares/
│   │   └── store.js
│   ├── types/                     # Type definitions
│   │   ├── user.types.js
│   │   ├── signal.types.js
│   │   └── ...
│   ├── utils/                     # Funcții utilitare
│   │   ├── format.js              # Formatare date
│   │   ├── validators.js          # Validare formulare
│   │   └── ...
│   ├── App.jsx                    # Componenta principală
│   ├── index.jsx                  # Punct de intrare
│   └── routes.jsx                 # Configurare routing
├── .eslintrc.js                   # Configurare ESLint
├── tailwind.config.js             # Configurare Tailwind
├── jest.config.js                 # Configurare teste
├── package.json
└── README.md