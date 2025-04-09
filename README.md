# Doc. Web App TO-DO

***Daniel Augusto N° 04***

***Leonardo Felix N° 19***

***Pedro Ribeiro N° 28***

***Marcos Néfi N° 34***

***Isadora Abreu N° 32***

***João Pincinato N° 15*** 

---

## Como Criar e Ativar um Ambiente Virtual Python no VS Code

Ao trabalhar com Python no VS code o ideal é usar um **ambiente virtual**. Isso evita bagunça nas bibliotecas e garante que cada projeto tenha só o que precisa, sem misturar tudo.

---

### Criando o ambiente virtual

1. **Abre o terminal no VS Code**
    - Atalho no Windows: `Ctrl + aspas (``)`
2. **Vai até a pasta do seu projeto:**
    
    ```bash
    cd caminho/para/seu-projeto
    
    ```
    
3. **Cria o ambiente com esse comando:**
    
    ```bash
    python -m venv venv
    
    ```
    
    - Pode trocar `venv` por qualquer nome que quiser pro seu ambiente.

---

## Ativando o ambiente no PowerShell (Windows)

1. No terminal do VS Code, digite:
    
    ```bash
    .\venv\Scripts\Activate.ps1
    
    ```
    
    - Lembrando: se usou outro nome no lugar de `venv`, tem que trocar no caminho também.
2. **Deu erro falando de permissão?**
    
    Roda isso no PowerShell:
    
    ```bash
    Set-ExecutionPolicy RemoteSigned
    
    ```
    
    Depois tenta ativar de novo
    

---

## Dica extra

Quando o ambiente estiver ativado, você vai ver algo tipo `(venv)` no começo da linha do terminal. Isso significa que tá tudo certo e isolado.

---

## Passo a Passo: Rodando o Web App com Flask + MySQL + Upload de Imagem

### 1. Crie e ative um ambiente virtual

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # No PowerShell do Windows

```

---

### 2. Instale as dependências

```bash
pip install flask mysql-connector-python

```

---

### 3. Configure seu banco de dados MySQL

- Crie o banco no MySQL com esse comando (via terminal ou MySQL Workbench):

```sql
CREATE DATABASE gestor;

```

- Depois, crie a tabela:

```sql
USE gestor;

CREATE TABLE tarefas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  titulo VARCHAR(255),
  descricao TEXT,
  imagem VARCHAR(255)
);

```

---

### 4. Estrutura de pastas esperada

Organize as pastas e arquivos assim:

```
/seu-projeto
├── app.py
├── /templates
│   ├── homepage.html
│   ├── tarefas.html
│   ├── addTarefa.html
│   ├── del_tarefa.html
│   └── editarTarefa.html
├── /static
│   └── /img  ← imagens enviadas vão pra cá

```

---

### 5. Execute o app

```bash
python app.py

```

- Acesse no navegador: [http://localhost:5000](http://localhost:5000/)

---

### 6. Rotas disponíveis

| Rota | O que faz |
| --- | --- |
| `/` | Página inicial |
| `/tarefas` | Lista todas as tarefas |
| `/add_tarefa_form` | Formulário de nova tarefa |
| `/add_tarefa` | Rota de envio do formulário (POST) |
| `/del_tarefa` | Lista tarefas para excluir |
| `/excluir_tarefa` | Apaga a tarefa escolhida (POST) |
| `/edit_tarefa` | Lista tarefas para editar |
| `/editar_tarefa` | Atualiza a tarefa no banco (POST) |

---

## Como visualizar dados no MySQL (via terminal ou Command Line Client)

---

### **Opção 1: Usando o terminal (modo raiz brabo)**

1. **Abra o terminal ou prompt de comando**
2. Digite o seguinte para entrar no MySQL:

```bash
mysql -u root -p

```

- `u root`: você tá dizendo que vai logar como o usuário `root`
- `p`: isso avisa que você vai digitar uma senha depois
1. **Digite sua senha do MySQL** (a mesma que tá no seu código Python, ex: `4975`)

---

1. Agora, dentro do console do MySQL, selecione o banco de dados:

```sql
USE gestor;

```

1. E depois visualize as tarefas:

```sql
SELECT * FROM tarefas;

```

```
+----+---------------+---------------------+------------------------+
| id | titulo        | descricao           | imagem                 |
+----+---------------+---------------------+------------------------+
| 1  | Tarefa Teste  | Isso é um exemplo   | img/nome_da_img.jpg    |
+----+---------------+---------------------+------------------------+

```

---

- Se você quiser **sair do MySQL**, digita:

```sql
exit;

```

---

### **Usando o MySQL Command Line Client**

1. Abre o **MySQL Workbench**
2. Conecta na sua instância local (normalmente `localhost`, user `root`)
3. No painel esquerdo, clique no banco `gestor`
4. Execute esses dois comandos na aba de SQL:

```sql
USE gestor;
SELECT * FROM tarefas;

```

1. Clique no botão (executar), e as tarefas vão aparecer numa tabela bonitinha embaixo.

---

### Visualização dos dados através do MySQL

![image.png](attachment:e3e35d05-1179-4a5e-87c2-b1bcfe05f7dd:image.png)
