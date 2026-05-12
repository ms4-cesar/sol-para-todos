# 🌿 Tutorial Básico de Git — Projeto Sol para Todos

Este guia apresenta os comandos básicos de Git utilizados no projeto.

Cada integrante terá sua própria branch para desenvolver suas alterações de forma organizada.

---

# ✅ 1. Clonar o repositório

Execute o comando abaixo no terminal:

```bash
git clone URL_DO_REPOSITORIO
```

Exemplo:

```bash
git clone https://github.com/seu-repo/sol-para-todos.git
```

---

# ✅ 2. Entrar na pasta do projeto

```bash
cd sol-para-todos
```

---

# ✅ 3. Verificar as branches disponíveis

```bash
git branch -a
```

---

# ✅ 4. Trocar para sua branch

Cada integrante deverá utilizar sua própria branch.

Exemplo:

```bash
git checkout nome-da-sua-branch
```

Exemplos reais:

```bash
git checkout mariana
```

```bash
git checkout joao
```

---

# ✅ 5. Verificar arquivos alterados

Após realizar alterações no projeto:

```bash
git status
```

Esse comando mostra:
- arquivos modificados;
- arquivos novos;
- arquivos preparados para commit.

---

# ✅ 6. Adicionar alterações

## Adicionar todos os arquivos alterados

```bash
git add .
```

---

## Adicionar apenas um arquivo específico

```bash
git add nome-do-arquivo
```

Exemplo:

```bash
git add README.md
```

---

# ✅ 7. Criar commit

Após adicionar os arquivos:

```bash
git commit -m "Descrição da alteração"
```

Exemplo:

```bash
git commit -m "Adiciona CRUD de usuário"
```

---

# ✅ 8. Enviar alterações para o GitHub

```bash
git push
```

---

# ✅ 9. Atualizar a branch principal (`main`) com merge

Quando uma funcionalidade estiver pronta e funcionando, as alterações da branch individual devem ser integradas à branch principal (`main`).

O merge deve ser feito:
- ao finalizar uma funcionalidade;
- quando o código estiver estável;
- após testar as alterações realizadas.

---

# 📌 Como fazer o merge (GitHub)

1. Acesse o repositório no GitHub;
2. Vá até a branch enviada;
3. Clique em:

```text
Compare & pull request
```

4. Crie o Pull Request;
5. Revise as alterações;
6. Clique em:

```text
Merge pull request
```

---

# ⚠️ Importante

A branch `main` deve representar sempre a versão mais estável do projeto.

Por isso:
- não desenvolver diretamente na `main`;
- utilizar branches individuais;
- fazer merge apenas de funcionalidades concluídas.

---

# ✅ Atualizar sua branch antes de começar novas alterações

Antes de iniciar novas tarefas:

```bash
git checkout main
git pull
```

Depois volte para sua branch:

```bash
git checkout sua-branch
```

Isso evita conflitos e mantém sua branch atualizada com a versão mais recente do projeto.

---

# 📌 Fluxo básico resumido

```bash
git checkout sua-branch

git status

git add .

git commit -m "Descrição"

git push
```

Depois:
- abrir Pull Request no GitHub;
- realizar merge na `main`.

---

# ⚠️ Boas práticas

- Sempre trabalhar na própria branch;
- Fazer commits pequenos e organizados;
- Utilizar mensagens claras nos commits;
- Verificar o `git status` antes do commit;
- Não alterar arquivos de outros colegas sem alinhamento;
- Fazer merge apenas de funcionalidades finalizadas.

---

# 🚫 Evite

- Trabalhar diretamente na branch principal;
- Fazer commit de arquivos desnecessários;
- Subir senhas ou arquivos `.env`;
- Fazer commit sem verificar alterações;
- Deixar branches muito desatualizadas.

---

# ✅ Exemplo completo

```bash
git checkout mariana

git status

git add .

git commit -m "Adiciona modelagem da tabela usuario"

git push
```

Depois:
- abrir Pull Request;
- revisar alterações;
- realizar merge na `main`.
