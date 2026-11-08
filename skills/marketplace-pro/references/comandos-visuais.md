# Comandos visuais: Clean Flyer e Hero Offer Minimal

Estes são **atalhos textuais da skill**, não comandos nativos do ChatGPT. Um pedido que comece com `/cleanflyer` ou `/herooffer-minimal` deve acionar a respectiva rotina quando a skill estiver disponível.

## Regra de ouro: imagem fiel ao item vendido

- Use sempre foto(s) enviada(s) pelo vendedor como base. Prefira **edição da fotografia** à síntese de um objeto parecido. Sem foto, só forneça roteiro/prompt, a menos que o usuário peça explicitamente uma imagem conceitual; não representar uma geração como sendo o produto real.
- Preserve marca, logotipo, lettering, botões, portas, conectores, material, cor, reflexos reais, embalagem, forma, dimensões relativas e itens inclusos. Não alucinar detalhes de ângulos invisíveis.
- Se a geração mudar algum detalhe, tente corrigir usando a referência; se persistir, avise que é **mockup ilustrativo, não pronto para publicação**.
- Sempre que o pedido for pela imagem final e houver ferramenta de imagem no ambiente, **use-a**, em vez de apenas mostrar prompt. Se inexistente, entregue prompt utilizável.
- Proporção 1:1 e **alvo de exportação 1200×1200 px**. Se a ferramenta não permitir pixel exato, não diga que a resolução foi alcançada; recomendar ajuste/exportação posterior sem distorção.
- Não inventar provas sociais, certificações, especificações, selos, desconto, preço, conectividade ou acessórios.
- Realismo natural: imperfeições plausíveis de fotografia, textura não plastificada, sombras fisicamente coerentes, direção única de luz, reflexos consistentes, sem nitidez exagerada e sem gradientes artificiais. Objetivo: visual de estúdio autêntico, não imitação de documentação fotográfica falsa.
- Inspirar-se em **minimalismo esportivo premium** e linguagem clean/high contrast, **sem copiar marca, campanha, tipografia proprietária ou identidade visual de terceiros**.

## `/cleanflyer` — imagem de produto SEM texto

**Aplicação:** capa/galeria limpa, produto isolado, fundo branco puro ou cinza muito claro conforme categoria. Quando houver exigência de fundo branco puro, **priorizar a regra do Mercado Livre sobre a opção de mesa ou flutuação**. Evitar acessórios de contexto, marca d'água, bordas, selos, textos e ícones.

**Entradas aceitas:** foto original (preferencial), nome/modelo, cor, opção `fundo=branco|cinza-claro`, `mesa=sim|nao` (padrão nao na capa), `flutuando=sim|nao` (padrão nao na capa), `posicao=capa|secundaria`. Se usuário só disser `/cleanflyer` com foto, aplicar defaults sem interromper.

**Prompt operacional adaptável (não mostrar ao usuário se for executar ferramenta):**

> Edit the **provided original product photo** into premium realistic commercial studio photography for a Brazilian marketplace, square composition with 1200×1200 px delivery target. Product: {PRODUTO}; confirmed color: {COR}. Preserve the EXACT original product identity and all visible hardware, shape, color, surfaces, logos, labels, buttons, connections, packaging, dimensions and included objects. No redrawing or replacing product parts. Position it large and centered, with clean margins, on a plain pure-white seamless background {or very light neutral gray only if permitted}. Add soft directional professional studio illumination and one physically consistent subtle contact shadow. {Optional: simple neutral tabletop only for a secondary image if allowed}. Refined athletic-tech minimalism, realistic optical detail, photographic grain so subtle it does not degrade clarity; no CGI look, no plastic shine, no unrealistic edges, no excessive HDR, no props. **No text, no graphic icons, no watermark, no border, no labels, no added products.** Preserve the original visible orientation; do not fabricate unseen surfaces.

**Checklist:** sem texto de marketing; produto original íntegro; aparência de foto real; proporção 1:1; nada fora da embalagem anunciada; enquadramento amplo sem cortes. Se o usuário pedir produto flutuando, só sugerir para foto secundária e se permitida.

## `/herooffer-minimal` — banner visual COM texto em pt-BR

**Aplicação:** **peça promocional/galeria secundária somente quando a política aplicável permitir texto e ícones**; não presumir que o Mercado Livre permite texto em qualquer categoria ou imagem; **não usar como capa**. Se a categoria for restritiva ou não for verificada, oferecer o banner como criativo para redes sociais/Ads ou como conceito separado, **não marcar como pronto para usar no anúncio**.

**Entradas aceitas:** foto original, `produto`, `cor`, `tema`, até 3 benefícios técnicos **verificados**, `titulo`, `subtitulo`, `posicao=secundaria|social`. Se o usuário não fornecer fatos para o tema, pedir comprovação para uma alegação técnica ou criar visual com frases neutras; nunca fabricar.

**Prompt operacional adaptável:**

> Create a premium photographic commercial banner in a square layout (1200×1200 px target) with the exact product preserved from the supplied original photo. Product: {PRODUTO}. Color: {COR}. Main communication theme: {TEMA_COMPROVADO}. Text language: **Brazilian Portuguese**, with correct spelling, diacritics and numbers. Aesthetic: modern clean athletic-tech minimalist studio ad, light gray or white neutral background, realistic directional studio lighting, high contrast, tasteful shadows, naturally photographed product, no CGI look, no plastic or synthetic artifacts. Make the product large, central or slightly offset for a clear typographic grid. Create a strong readable headline **{TITULO_COMPROVADO}**, concise subheading **{SUBTITULO_COMPROVADO}**, and up to three simple consistent line icons representing **{BENEFICIOS_COMPROVADOS}**. Typography hierarchy similar to Montserrat Black for headline, Montserrat Medium for subheadline and Montserrat Regular/SemiBold for supporting copy **only if available and licensed**; otherwise a similar clear sans serif. Large/medium legible copy, ample whitespace, no microtext. Keep text and product from obstructing each other: avoid overlap; if unavoidable, never obscure important features or more than 10% of copy. No fake badges, discounts, certificates, brand logos, claims, accessories or connectors. **Never edit the physical product**. Make icons visually secondary to the original product. Proofread every visible letter before delivery.

**Checklist:** revisar texto palavra por palavra, inclusive diacríticos; checar fatos e ícones; hierarquia tipográfica legível em miniatura; nenhum componente físico modificado; não exibir como capa; verificar política de texto da categoria antes de usar em galeria.

## Roteamento e resposta

- `/cleanflyer` + foto: gerar **uma imagem sem texto**. Não adicionar copy ou ícones, mesmo que o agente normalmente faça descrições.
- `/herooffer-minimal` + foto + tema: gerar **um banner com texto**, se os dados forem confiáveis. Se o tema mencionar tecnologia não comprovada, explicitar necessidade de validação antes de incluir como fato.
- `/cleanflyer` + `/herooffer-minimal` no mesmo pedido: se pedir as duas peças, gerar **duas imagens separadas**; nunca colocar textos na peça sem texto.
- `imagem de capa`: aplicar primeira rotina limpa, mesmo se o usuário mencionar banner, e explicar a separação.
- Sem pedido de imagem final: apenas elaborar/revisar os prompts e conceitos.
- Ao fim, fazer uma revisão visual comparativa com a foto real (se visível); não afirmar fidelidade perfeita sem inspecionar.

## Exemplo — GameSir T4 Nova Lite

`/cleanflyer Produto: controle GameSir T4 Nova Lite. Foto anexada. 1200×1200, sem textos, branco, iluminação de estúdio, sem alterar botões ou conexões.`

## Exemplo — Mchose V9 Pro

`/herooffer-minimal Produto: headset Mchose V9 Pro, preto, foto anexada. Tema: conexão tri-mode 2.4G + Bluetooth + USB-C. Confirme as especificações com embalagem/manual antes de exibi-las. Texto pt-BR, 1200×1200, Montserrat-like, 3 ícones discretos.`

Se o usuário não forneceu especificações oficiais do headset, a conectividade no exemplo acima é **uma afirmação fornecida para verificação**, e não algo que a skill deve presumir como verdade.

## Regras oficiais a conferir

- Mercado Livre — trabalhar com imagens: https://developers.mercadolivre.com.br/pt_br/api-docs-pt-br/trabalhar-com-imagens
- Mercado Livre — diagnóstico de imagens: https://developers.mercadolivre.com.br/pt_br/diagnostico-de-imagens
- Mercado Livre — fotos de qualidade: https://vendedores.mercadolivre.com.br/aprender/nota/fotos-de-qualidade-o-segredo-para-se-destacar-e-vender-mais

## Padrão universal de briefing (versão beta 1.2)

O usuário pode enviar somente:

```text
/herooffer-minimal
Product: Mouse Attack Shark X11
Color: Black
Theme1: Mouse super leve
Theme2: 63g
Image: img.png
```

`Theme1` e `Theme2` são ideias de comunicação e podem exigir verificação. O conteúdo do arquivo não é acessível só por escrever o nome; precisa ser anexado. Modificadores podem ser passados em `Options: /pixel-lock, /quality-check`. Consulte o catálogo com 100 comandos para outros estilos e verificadores.
