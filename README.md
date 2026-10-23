# TaskTracker

Aplicação de linha de comando (CLI) para gerenciamento de tarefas, desenvolvida como
projeto cumulativo do Bootcamp II.

## 📋 Descrição

O TaskTracker permite cadastrar tarefas com título, descrição, prioridade e data
limite, visualizar todas as tarefas organizadas por prioridade e acompanhar quantas
estão pendentes ou concluídas, tudo direto pelo terminal.

O projeto evoluiu em três fases:

| Fase | Foco | Resultado |
|---|---|---|
| 1 | Planejamento lógico | `docs/planejamento_logico.pdf` |
| 2 | Git, GitHub e Python | `src/main.py` |
| 3 | Containerização com Docker | `Dockerfile` e `docker-compose.yml` |

## 🚀 Funcionalidades

- Cadastrar nova tarefa (título obrigatório, descrição, prioridade e data limite)
- Validação estrita de prioridade (aceita apenas Alta, Média ou Baixa)
- Validação de título (não aceita campos vazios)
- Visualizar tarefas cadastradas, ordenadas por prioridade
- Contagem de tarefas pendentes e concluídas

## 🛠️ Tecnologias utilizadas

- Python 3.11
- Docker e Docker Compose

## 📁 Estrutura do projeto

```
tasktracker-projeto/
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf   # Planejamento lógico da Fase 1
├── src/
│   └── main.py                   # Código-fonte da aplicação (Fase 2)
├── Dockerfile                    # Receita da imagem (Fase 3)
├── docker-compose.yml            # Orquestração da execução interativa (Fase 3)
└── README.md
```

## 🐳 Como executar com Docker

**Pré-requisito:** ter o [Docker](https://www.docker.com/products/docker-desktop/)
instalado e **em execução**. Rode os comandos abaixo na raiz do projeto.

**Como construir a imagem:**

```bash
docker build -t tasktracker .
```

**Como rodar o container em modo isolado:**

```bash
docker run -it tasktracker
```

**Como rodar via orquestração (Recomendado):**

```bash
docker compose run --rm tasktracker-app
```

> A aplicação usa `input()`, por isso precisa de um terminal interativo. A flag `-it`
> (no `docker run`) e as opções `stdin_open: true` e `tty: true` (no
> `docker-compose.yml`) cumprem esse papel.

## 💻 Como executar sem Docker (opcional)

```bash
python3 src/main.py
```

## 👤 Autor

[Seu Nome Completo], Bootcamp II, [Polo/Turma]
