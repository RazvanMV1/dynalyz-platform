📌 Etapa 1 – Fundamentare
 Proiect structurat backend + frontend

 Docker funcțional pentru local dev

 .env.example, .gitignore, etc.

 Health check endpoint (/api/v1/health)

 Conexiune la DB verificată

🔐 Etapa 2 – Autentificare și utilizatori
 Endpoint register/login/logout

 JWT auth + refresh token

 Role management (user/admin/manager)

 CRUD pentru utilizatori

📊 Etapa 3 – Date și modele AI
 Structura modelelor AI în DB

 Upload + versionare modele

 Endpoint pentru testare model (dummy inference)

 Colectare date OHLC (fake data la început)

📈 Etapa 4 – Generare semnale
 Definirea endpoint generate signal

 Legătură cu AIModel + OHLC

 Scheduler task (Celery)

📣 Etapa 5 – Notificări
 Sistem de notificări email + Telegram

 Preferințe utilizator

 Digest zilnic (task periodic)

🧾 Etapa 6 – Plăți & abonamente
 Modele Subscription, Plan, Payment

 Integrare Stripe/Paypal (dummy inițial)

 Restricții pe funcționalitate în funcție de abonament

🖥️ Etapa 7 – Frontend MVP
 Auth UI

 Dashboard cu semnale

 Pagină profil & setări

 Mobile responsive

🚀 Etapa 8 – Lansare alpha
 CI/CD

 Deploy Docker pe server (Railway, Render, VPS)

 Manuale + README

