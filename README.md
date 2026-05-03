# 🏥 Lacrei Saúde API

API RESTful de Gerenciamento de Consultas Médicas desenvolvida para o desafio técnico voluntário da Lacrei Saúde.

## 🛠️ Tecnologias

- Python 3.11
- Django 4.2 + Django REST Framework
- PostgreSQL 15
- Docker + Docker Compose
- GitHub Actions (CI/CD)
- JWT Authentication
- Poetry (gerenciamento de dependências)

## 📋 Requisitos

- Docker Desktop instalado e rodando
- Git

## 🚀 Setup local com Docker

```bash
# Clone o repositório
git clone https://github.com/HigorSantos0/lacrei-saude-api.git
cd lacrei-saude-api

# Suba os containers
docker compose up --build

# Em outro terminal, crie um superusuário
docker compose exec web python manage.py createsuperuser
```

A API estará disponível em: `http://localhost:8000`

## 🧪 Rodando os testes

```bash
docker compose exec web python manage.py test
```

## 🔐 Autenticação

A API usa JWT. Para obter o token:

```bash
POST /api/token/
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Use o token retornado no header:


## 📌 Endpoints

### Profissionais
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /api/profissionais/ | Lista todos |
| POST | /api/profissionais/ | Cria novo |
| GET | /api/profissionais/{id}/ | Busca por ID |
| PUT | /api/profissionais/{id}/ | Atualiza |
| DELETE | /api/profissionais/{id}/ | Remove |

### Consultas
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| GET | /api/consultas/ | Lista todas |
| POST | /api/consultas/ | Cria nova |
| GET | /api/consultas/{id}/ | Busca por ID |
| GET | /api/consultas/?profissional_id={id} | Filtra por profissional |
| PUT | /api/consultas/{id}/ | Atualiza |
| DELETE | /api/consultas/{id}/ | Remove |

### Autenticação
| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | /api/token/ | Obter token |
| POST | /api/token/refresh/ | Renovar token |

## ⚙️ CI/CD

O pipeline do GitHub Actions roda automaticamente a cada push na branch `main`:

1. **Lint** — verifica qualidade do código com flake8
2. **Testes** — roda todos os testes automatizados
3. **Build** — verifica se o Docker builda corretamente

## 🔄 Rollback

Em caso de falha no deploy, o rollback pode ser feito via GitHub Actions:

1. Acesse a aba **Actions** no GitHub
2. Encontre o último pipeline com sucesso
3. Clique em **Re-run all jobs**

Ou via git:
```bash
git revert HEAD
git push origin main
```

## 🔒 Segurança

- Autenticação JWT em todos os endpoints
- Proteção contra SQL Injection via ORM do Django
- CORS configurado
- Variáveis sensíveis via `.env` (nunca commitadas)
- Sanitização de inputs via serializers do DRF

## 📝 Decisões técnicas

- **Django 4.2 LTS** — versão com suporte longo, estável e compatível com Python 3.11
- **JWT** — autenticação stateless, mais segura e escalável que sessões
- **Poetry** — gerenciamento de dependências com lock file, garantindo reprodutibilidade
- **Docker** — ambiente idêntico em desenvolvimento e produção
- **PostgreSQL** — banco robusto e adequado para produção
- **ModelViewSet** — reduz código repetitivo mantendo todos os endpoints REST
