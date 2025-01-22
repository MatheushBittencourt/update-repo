# Update Repositories Script 🛠️

Automatize a atualização de múltiplos repositórios Git com este script Python simples e eficiente. Ideal para quem trabalha com vários projetos e deseja economizar tempo mantendo tudo atualizado automaticamente. 

---

## 🚀 Funcionalidades
- Atualiza todos os repositórios Git em uma pasta específica (e suas subpastas).
- Verifica se o repositório está na branch **master** antes de executar `git pull`.
- Gera um resumo das atualizações realizadas ao final da execução.

---

## 🧰 Pré-requisitos
Certifique-se de que você tenha as seguintes ferramentas instaladas:
- **Python 3.6+**
- **Git**
---

## 📦 Instalação
1. Clone este repositório:
   ```bash
   git clone https://github.com/MatheushBittencourt/update-repo.git
   ```
2. Acesse o diretório do projeto:
   ```bash
   cd update-repos
   ```
3. Instale as dependências necessárias (se houver):
   ```bash
   pip install -r requirements.txt
   ```
4. Certifique-se de que o script está apontando para o diretório correto contendo seus repositórios:
   Edite a linha no script Python:
   ```python
   PROJECTS_DIR = "/caminho/para/sua/pasta/com/repositorios"
   ```

---

## 🏃 Uso
Execute o script manualmente:
```bash
python3 update_projects.py
```

### Exemplo de saída:
```
Repositório: my-project
Branch atual: master
Atualizações realizadas com sucesso! 🎉

Repositório: other-project
Branch atual: dev
Ignorado (não está na branch master). ⚠️
```

---

## 📌 Dicas
- Use **cron** ou o Agendador de Tarefas para executar o script em horários específicos automaticamente.
- Certifique-se de que o WSL ou ambiente Linux esteja sempre ativo se estiver usando essa integração.

---

## 📖 Contribuindo
Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar um **pull request** com melhorias e novas funcionalidades.

---
Se precisar de ajustes ou quiser adicionar algo, é só avisar! 😊
