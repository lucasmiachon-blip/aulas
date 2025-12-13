# 🚀 Como Usar o Descompactador do Google Drive

## 📋 Passo a Passo

### 1️⃣ Instalar as Bibliotecas Necessárias

Abra o PowerShell e execute:

```powershell
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

### 2️⃣ Configurar Credenciais da API do Google

Você precisa criar credenciais OAuth 2.0 para acessar seu Google Drive:

#### A. Acessar o Console do Google Cloud

1. Vá para: https://console.cloud.google.com/
2. Faça login com sua conta **lucasmiachon87@gmail.com**

#### B. Criar/Selecionar um Projeto

1. No topo da página, clique em "Selecionar projeto"
2. Clique em "Novo Projeto"
3. Nome: `Descompactador Drive` (ou qualquer nome)
4. Clique em "Criar"

#### C. Ativar a API do Google Drive

1. No menu lateral, vá em: **APIs e Serviços** → **Biblioteca**
2. Busque por: `Google Drive API`
3. Clique nela e depois em **"Ativar"**

#### D. Criar Credenciais OAuth 2.0

1. No menu lateral: **APIs e Serviços** → **Credenciais**
2. Clique em **"+ Criar Credenciais"** → **"ID do cliente OAuth"**
3. Se pedir para configurar tela de consentimento:
   - Escolha **"Externo"**
   - Nome do app: `Descompactador`
   - Email de suporte: **lucasmiachon87@gmail.com**
   - Email do desenvolvedor: **lucasmiachon87@gmail.com**
   - Clique em **"Salvar e Continuar"** (pode pular os escopos)
   - Em "Usuários de teste", adicione: **lucasmiachon87@gmail.com**
4. Volte para Credenciais e crie:
   - Tipo de aplicativo: **"App para computador"**
   - Nome: `Descompactador Desktop`
   - Clique em **"Criar"**

#### E. Baixar o Arquivo de Credenciais

1. Após criar, clique no ícone de **download** (⬇️) ao lado da credencial
2. Salve o arquivo como: **`credentials.json`**
3. Coloque na mesma pasta do script:
   ```
   C:\Users\lucas\OneDrive\LM\Documentos\Ignis Animi\Ignis_Animi\Codigos\credentials.json
   ```

### 3️⃣ Executar o Script

```powershell
cd "C:\Users\lucas\OneDrive\LM\Documentos\Ignis Animi\Ignis_Animi\Codigos"
python descompactar_google_drive.py
```

### 4️⃣ Primeira Execução

1. Uma janela do navegador será aberta
2. Faça login com **lucasmiachon87@gmail.com**
3. Autorize o aplicativo (pode aparecer aviso que não é verificado - clique em "Avançado" e "Ir para...")
4. Autorize o acesso ao Google Drive
5. O token será salvo como `token.pickle` para próximas execuções

### 5️⃣ Processamento

O script vai:
- ✅ Buscar TODOS os arquivos ZIP na pasta e subpastas
- ✅ Mostrar a lista completa
- ✅ Pedir confirmação
- ✅ Descompactar cada ZIP no mesmo local
- ✅ Criar uma pasta com o nome do ZIP
- ✅ Extrair todos os arquivos dentro dessa pasta

## 🔧 Arquivos Necessários

```
📁 Codigos/
  ├── descompactar_google_drive.py  ✅ (script principal)
  ├── credentials.json              ⚠️ (você precisa criar)
  └── token.pickle                  ✅ (criado automaticamente)
```

## 💡 Dicas

- O `credentials.json` é necessário apenas uma vez
- O `token.pickle` é criado após primeira autenticação
- Você pode reutilizar o token várias vezes
- Se der erro de autenticação, delete o `token.pickle` e execute novamente

## ⚠️ Solução de Problemas

### "credentials.json não encontrado"
→ Você precisa baixar as credenciais da API (veja passo 2)

### "Bibliotecas do Google não instaladas"
→ Execute: `pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client`

### "Erro de autenticação"
→ Delete o arquivo `token.pickle` e execute novamente

## 📧 Configuração Atual

- **Conta Google**: lucasmiachon87@gmail.com
- **Pasta ID**: 18hZz5gb-897PFIjpcOZeiA4laIFdp6yL
- **Link**: https://drive.google.com/drive/folders/18hZz5gb-897PFIjpcOZeiA4laIFdp6yL
