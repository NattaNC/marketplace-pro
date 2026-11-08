# Marketplace Pro

**Skill open source para SEO, títulos, descrições, análise competitiva e fotografia de produto para marketplaces, com foco no Mercado Livre Brasil.**

> **Status:** v1.2.0-beta.1 — versão para teste com catálogo de 100 comandos, template de prompt e utilitário de verificação. Não é uma integração automática com a conta Mercado Livre, não publica anúncios sozinho e não inclui um modelo de IA próprio.

## O que faz

- Criar anúncios completos com título, descrição e ficha técnica baseada em dados reais.
- Auditar anúncios e recomendar mudanças por prioridade.
- Preparar três títulos com contagem de caracteres, sem inventar o limite da categoria.
- Fazer pesquisa e comparação de concorrentes **se o agente tiver navegação disponível**.
- Orientar ou executar edição/geração de fotos **quando o ChatGPT tiver ferramenta de imagem disponível e o usuário pedir**; preferir fotos originais, respeitar fidelidade do produto e regras da categoria.
- Conduzir checklist de conformidade, confiança e riscos.
- Aceitar os **atalhos textuais** `/cleanflyer` (foto sem texto) e `/herooffer-minimal` (banner em pt-BR com ícones, somente quando permitido); ver `skills/marketplace-pro/references/comandos-visuais.md`.

### Catálogo de 100 comandos — versão beta

A biblioteca inclui **100 aliases textuais**, em 10 grupos, para proteção da foto, edição, fotografia de estúdio, cenas, estilos por categoria, banners, identidade visual, galerias, SEO e auditoria.

- [Consultar todos os 100 comandos](skills/marketplace-pro/references/catalogo-100-comandos.md)
- [Metadados JSON dos 100 comandos](skills/marketplace-pro/references/catalogo-100-comandos.json)
- Comandos principais: `/marketplace-pro`, `/auto-gallery`, `/cleanflyer`, `/herooffer-minimal`, `/catalog-white`, `/pixel-lock`, `/quality-check`, `/title-pro`, `/listing-audit`.
- Funciona para **eletrônicos, calçados, moda, beleza, utensílios, casa, brinquedos, produtos pet, alimentos embalados** e outras categorias.
- Diferencie o *comando principal* (primeira linha) dos *modificadores* em `Options: /pixel-lock, /quality-check`.

**Prompt padrão do usuário** (só funciona com `img.png` realmente anexado):

```text
/herooffer-minimal

Product: Mouse Attack Shark X11
Color: Black
Theme1: Mouse super leve
Theme2: 63g
Image: img.png
Options: /pixel-lock, /quality-check
```

`Theme1` e `Theme2` são pautas fornecidas pelo usuário. A skill **não presume** que "63g" esteja comprovado. Sem foto anexada, não afirma ter visto ou editado o produto. `/pixel-lock` só preserva pixels originais se houver ferramentas de recorte/máscara e composição; prompts generativos por si não garantem isso.

**Gerador local de prompts** (somente Python padrão; não gera imagens):

```bash
python scripts/prompt_builder.py --list
python scripts/prompt_builder.py --show /herooffer-minimal
python scripts/prompt_builder.py --command /herooffer-minimal --product "Mouse Attack Shark X11" --color Black --theme1 "Mouse super leve" --theme2 "63g" --image img.png --options /pixel-lock,/quality-check
```

### Dois comandos de imagem

```text
/cleanflyer
Produto: GameSir T4 Nova Lite
[anexar foto real]
Capa limpa, sem texto, 1200x1200, fundo branco, foto realista.
```

```text
/herooffer-minimal
Produto: Mchose V9 Pro Headset, cor preta
[anexar foto real e informações oficiais]
Tema a verificar: TRI-MODE — 2.4 GHz + Bluetooth + USB-C
Arte em português brasileiro com título grande, ícones discretos e visual premium.
```

**Atenção:** são gatilhos interpretados pelas instruções da skill, **não slash commands registrados nativamente** no ChatGPT. A foto sem texto é o padrão para capa; texto e ícones em banners precisam ser compatíveis com a política de imagens da categoria. O comando não garante que um modelo gerador preserve 100% dos detalhes: revisar a imagem final é obrigatório.


## Estrutura

```text
marketplace-pro/
├── plugin.json                            # Plugin portátil skills-only
├── skills/
│   └── marketplace-pro/
│       ├── SKILL.md                       # Entrypoint da skill
│       ├── references/                    # SEO, copywriting, fotos, auditoria
│       └── examples/
├── chatgpt/
│   └── INSTRUCOES_PROJETO.md              # Alternativa no ChatGPT pessoal
├── scripts/quality_check.py              # Verificação local de JSON
├── scripts/prompt_builder.py             # Gerador local de prompts dos 100 comandos
├── tests/                                # Testes unitários
├── examples/anuncio_exemplo.json
├── assets/marketplace-pro-icon.svg
└── README.md
```

## Como usar no ChatGPT agora — via Projetos

A documentação da OpenAI informa que **Projetos** permitem instruções e arquivos, inclusive em contas pessoais elegíveis; ao contrário de skills instaláveis no ChatGPT, reservadas a ambientes de trabalho elegíveis na documentação de novembro de 2026.

1. Abra o ChatGPT e crie um **Novo projeto** chamado `Marketplace Pro`.
2. Nas **Configurações do projeto**, copie o conteúdo de [`chatgpt/INSTRUCOES_PROJETO.md`](chatgpt/INSTRUCOES_PROJETO.md) para as instruções.
3. Adicione **`skills/marketplace-pro/references/catalogo-100-comandos.md`** e os demais arquivos de referências como fontes do projeto (recomendado).
4. Em uma conversa dentro do projeto, envie uma foto do produto, especificações ou link e peça: "Crie meu anúncio para Mercado Livre com SEO e fotos reais".

Esse método **não instala a skill globalmente**; reproduz seu fluxo de trabalho no projeto.

## Como instalar a skill no ChatGPT (contas elegíveis)

Na interface compatível: **Plugins > Habilidades > Criar > Carregar do computador**, enviando a pasta/ZIP da skill conforme a opção exibida. A plataforma verifica arquivos antes de liberar a instalação; permissões e disponibilidade dependem do ambiente. O ZIP `marketplace-pro-skill.zip` da distribuição tem `SKILL.md` na raiz.

Consulte: https://help.openai.com/pt-br/articles/20001066-skills-in-chatgpt

## Como instalar no Codex (Linux, macOS, Kali)

Após clonar ou extrair o repositório:

```bash
mkdir -p ~/.agents/skills
cp -R skills/marketplace-pro ~/.agents/skills/marketplace-pro
```

Reinicie/abra uma sessão do Codex e peça: "Use a skill marketplace-pro para auditar meu anúncio". Caminho por projeto: `.agents/skills/marketplace-pro/` em vez de `~/.agents/skills/marketplace-pro/`.

O pacote também possui `plugin.json` no padrão portátil de plugins para facilitar distribuição futura.

## Uso sugerido

- **Criar:** "Tenho fotos e manual de um produto. Crie anúncio completo para Mercado Livre."
- **Otimizar:** "Analise este link do meu anúncio, identifique problemas de SEO e reescreva título e descrição."
- **Imagens:** "Edite a foto original, capa com fundo branco, 1200x1200, preserve 100% dos detalhes físicos."
- **Concorrentes:** "Compare estes três anúncios com o meu e sugira melhorias verificáveis."

## Verificador local (opcional)

Requer somente Python 3.10+ e não envia dados para internet:

```bash
python scripts/quality_check.py examples/anuncio_exemplo.json
python scripts/quality_check.py examples/anuncio_exemplo.json --title-limit 60 --json
python -m unittest discover -s tests -v
```

**Atenção:** `--title-limit 60` é um **exemplo de limite informado pelo usuário**, não uma afirmação de que todas as categorias do Mercado Livre permitem 60 caracteres. Confira o limite da sua categoria antes de validar. O script só lê textos e metadados, **não avalia pixels das fotos**.

## Publicar no seu GitHub (ação manual até conectar a conta)

1. Crie uma conta e autentique o GitHub CLI se necessário (`gh auth login`).
2. Entre na pasta `marketplace-pro` e execute:

```bash
git init
git add .
git commit -m "feat: Marketplace Pro 100 commands beta"
gh repo create marketplace-pro --public --source=. --remote=origin --push
```

Ou crie um repositório pelo site e envie o conteúdo do ZIP do repositório. Faça revisão antes de publicar. Nunca adicione tokens, credenciais, dados pessoais nem imagens de terceiros sem direitos de uso.

Publicar no GitHub **não equivale** a publicar no diretório de plugins do ChatGPT; essa distribuição possui revisão e permissões próprias.

## Limites da v1

- Sem acesso autônomo a lojas, analytics ou API do Mercado Livre. Não salva/publica anúncios.
- Pesquisa de palavras-chave e concorrentes depende de navegação e fontes atuais.
- Criação de imagens depende das ferramentas de imagem do host e de material de referência. A skill define padrões de trabalho, não entrega um motor próprio de renderização.
- A qualidade de imagens geradas precisa de conferência humana antes da publicação.

## Referências oficiais

- [Skills no ChatGPT — OpenAI](https://help.openai.com/pt-br/articles/20001066-skills-in-chatgpt)
- [Projetos no ChatGPT — OpenAI](https://help.openai.com/pt-br/articles/10169521-projects-in-chatgpt)
- [Como criar skills — OpenAI Developers](https://developers.openai.com/plugins/build/skills)
- [Como empacotar plugins — OpenAI Developers](https://developers.openai.com/plugins/build/plugins)
- [Como criar anúncios eficientes — Mercado Livre](https://vendedores.mercadolivre.com.br/nota/como-criar-anuncios-eficientes-no-mercado-livre)
- [Imagens nos anúncios — Developers Mercado Livre](https://developers.mercadolivre.com.br/pt_br/api-docs-pt-br/trabalhar-com-imagens)
- [Diagnóstico de imagens — Developers Mercado Livre](https://developers.mercadolivre.com.br/pt_br/diagnostico-de-imagens)

## Contribuições

Pull requests e issues são bem-vindos. Atualize referências oficiais antes de propor um limite de título ou regra visual como universal. Leia a [licença MIT](LICENSE).

## Gerar ZIPs depois de editar

Rode `python scripts/package_release.py`. O script criará em `dist/`: um ZIP da **skill isolada**, um ZIP do **plugin portátil** e um ZIP do **repositório completo**.

Uma GitHub Action executa os testes de validação a cada push e pull request.
