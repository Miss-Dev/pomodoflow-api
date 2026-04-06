# 🚀 PomodoFlow API

**PomodoFlow API** é um sistema de produtividade focado em **gestão de tarefas + técnica Pomodoro**, com automação de notificações para tarefas não concluídas.

> Automate your focus. Never forget unfinished tasks again.

---

## 📌 Status do Projeto

🚧 Em desenvolvimento

Funcionalidades já implementadas:

* ✅ Estrutura inicial do projeto
* ✅ Configuração do banco de dados (SQLite + SQLAlchemy)
* ✅ Modelagem inicial de tarefas

Próximas etapas:

* ⏳ CRUD de tarefas
* ⏳ Sistema de Pomodoro
* ⏳ Scheduler para verificação de tarefas pendentes
* ⏳ Notificações por e-mail
* ⏳ Reagendamento de tarefas

---

## 💡 Objetivo

Criar uma API backend que permita:

* Gerenciar tarefas com prazos
* Executar sessões de foco (Pomodoro)
* Automatizar notificações de tarefas pendentes
* Permitir reagendamento inteligente de atividades

---

## 🧱 Arquitetura

O projeto segue uma arquitetura modular baseada em camadas:

```
app/
 ├── api/        # Rotas da API (FastAPI)
 ├── domain/     # Modelos e regras de negócio
 ├── services/   # Lógica da aplicação
 ├── infra/      # Banco de dados e configurações
 └── main.py     # Ponto de entrada
```

---

## ⚙️ Tecnologias

* Python 3.11+
* FastAPI
* SQLAlchemy
* SQLite
* APScheduler (planejado)
* SMTP (para envio de e-mails - planejado)

---

## 🗄️ Banco de Dados

Atualmente o sistema utiliza SQLite para persistência de dados.

Exemplo de entidade:

* **Task**

  * id
  * title
  * status
  * due_date
  * created_at

---

## 🚀 Como rodar o projeto

### 1. Clonar repositório

```bash
git clone https://github.com/seu-usuario/pomodoflow-api.git
cd pomodoflow-api
```

### 2. Criar ambiente virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/Mac
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Rodar aplicação

```bash
uvicorn app.main:app --reload
```

---

## 🔮 Roadmap

* [ ] CRUD completo de tarefas
* [ ] Implementação do Pomodoro
* [ ] Scheduler para automação diária
* [ ] Integração com envio de e-mail
* [ ] Endpoint para reagendamento de tarefas
* [ ] Dashboard de produtividade

---

## 📈 Futuras melhorias

* Integração com Google Calendar
* Autenticação de usuários
* Deploy em cloud (AWS ou similar)
* Containerização com Docker

---

## 🤝 Contribuição

Este é um projeto em desenvolvimento para estudo e portfólio.
Sugestões e melhorias são bem-vindas.

---

## 📄 Licença

MIT
