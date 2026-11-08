# Catálogo oficial — 100 comandos

Os comandos abaixo são **atalhos de instrução**, não comandos nativos da interface nem 100 ferramentas instaladas. Para executá-los, o host precisa ter a capacidade correspondente. Alguns só geram um plano/briefing quando não há ferramenta de edição, busca ou publicação.

## Uso rápido

```text
/herooffer-minimal

Product: Mouse Attack Shark X11
Color: Black
Theme1: Mouse super leve
Theme2: 63g
Image: img.png
Options: /pixel-lock, /quality-check
```

Uma referência em `Image` é apenas um nome: o usuário precisa **anexar a foto real**. Informações técnicas dos temas devem ser confirmadas antes de virar afirmações no anúncio.

**Categorias**: `visual` cria/planeja uma peça, `modifier` define restrições/estilo, `workflow` organiza pesquisa, copy ou auditoria. Modificadores em `Options` não exigem geração independente.

**Conflitos**: fidelidade, segurança e regra da plataforma > comando visual > estilo. `/no-text` prevalece sobre um banner com texto; peça confirmação ou gere uma composição sem texto. Não anuncie `pixel-lock` como preservação perfeita se a ferramenta recriar pixels do produto.

## Proteção do produto

- **`/pixel-lock`** · `modifier` — Priorizar preservação dos pixels originais do produto, usando recorte e composição não destrutiva quando viável.
- **`/product-mask`** · `modifier` — Isolar a silhueta real do produto para editar somente fundo e entorno.
- **`/edge-clean`** · `modifier` — Corrigir halos e bordas do recorte sem apagar detalhes do produto.
- **`/detail-guard`** · `modifier` — Proteger costuras, botões, portas, conectores, etiquetas e demais detalhes visíveis.
- **`/color-lock`** · `modifier` — Preservar as cores reais do produto e de suas variações.
- **`/logo-lock`** · `modifier` — Preservar marcas, logotipos e inscrições do item e de sua embalagem.
- **`/texture-lock`** · `modifier` — Preservar a aparência original de material, trama, textura e acabamento.
- **`/geometry-lock`** · `modifier` — Preservar ângulo, forma, perspectiva e proporções do item.
- **`/resolution-safe`** · `modifier` — Evitar ampliação destrutiva, nitidez artificial e exportação com perda desnecessária.
- **`/source-compare`** · `modifier` — Comparar imagem final e foto de referência; sinalizar divergências visíveis.

## Tratamento da foto

- **`/background-remove`** · `modifier` — Remover somente o fundo mantendo o produto intacto.
- **`/background-swap`** · `modifier` — Trocar o cenário sem redesenhar o produto.
- **`/object-center`** · `modifier` — Centralizar o recorte mantendo escala e proporções adequadas.
- **`/canvas-1200`** · `modifier` — Preparar enquadramento quadrado com alvo de exportação de 1200×1200 pixels, sem esticar o item.
- **`/crop-safe`** · `modifier` — Recortar com margens seguras, preservando todas as partes importantes.
- **`/margin-balance`** · `modifier` — Equalizar espaços negativos e respiro visual.
- **`/exposure-safe`** · `modifier` — Ajustar luz do cenário, evitando alterar indevidamente cores do item.
- **`/white-balance-safe`** · `modifier` — Neutralizar o fundo sem mudar a cor real do produto.
- **`/shadow-match`** · `modifier` — Criar sombra externa coerente com o recorte, apoio e direção de luz.
- **`/reflection-control`** · `modifier` — Controlar reflexos do cenário sem reconstruir superfícies originais.

## Estúdio e fotografia

- **`/cleanflyer`** · `visual` — Foto comercial limpa e sem nenhum texto, ícone ou selo.
- **`/catalog-white`** · `visual` — Foto de catálogo com fundo branco puro e nenhum gráfico, sem objetos extras.
- **`/studio-soft`** · `visual` — Cenário simples com luz suave e difusa.
- **`/studio-contrast`** · `visual` — Estúdio com contraste controlado e sombras naturais.
- **`/tabletop-premium`** · `visual` — Produto original sobre mesa ou superfície neutra, se a perspectiva permitir.
- **`/floatstudio`** · `visual` — Composição de flutuação ilustrativa usando o recorte original e sombra plausível.
- **`/premium-podium`** · `visual` — Produto sobre pedestal geométrico sem alterá-lo.
- **`/dark-premium`** · `visual` — Cenário escuro e iluminação lateral coerente.
- **`/pastel-studio`** · `visual` — Estúdio claro em tons pastel e aparência fotográfica.
- **`/macro-crop`** · `visual` — Aproximar região já presente e nítida na foto, sem inventar macrodetalhes.

## Cenas e contexto

- **`/lifestyle-real`** · `visual` — Inserir o produto recortado em contexto cotidiano plausível.
- **`/home-scene`** · `visual` — Criar cenário doméstico sem modificar o item.
- **`/office-scene`** · `visual` — Ambientar em escritório mantendo a fotografia original do item.
- **`/kitchen-scene`** · `visual` — Ambientar em cozinha quando o uso e a escala permitirem.
- **`/bathroom-scene`** · `visual` — Ambientar em banheiro para itens compatíveis.
- **`/outdoor-scene`** · `visual` — Criar ambiente externo coerente com o produto.
- **`/natural-daylight`** · `visual` — Simular luz natural no entorno, respeitando o recorte original.
- **`/flatlay`** · `visual` — Compor vista superior somente se as fotos já sustentarem esse ângulo.
- **`/in-hand`** · `visual` — Mostrar o produto na mão só se houver fotografia de referência e escala plausível; senão criar briefing.
- **`/reference-style`** · `visual` — Adaptar estética de referência secundária sem copiar outro produto ou identidade protegida.

## Estilos por categoria

- **`/fashion-flatlay`** · `visual` — Apresentar roupas em superfície plana quando o ângulo original permitir.
- **`/fashion-hanger`** · `visual` — Apresentar roupa em cabide apenas quando houver imagem compatível com o caimento.
- **`/shoe-studio`** · `visual` — Foto de calçados com ênfase em forma e acabamento reais.
- **`/beauty-packshot`** · `visual` — Compor foto de cosméticos e perfumes sem alterar embalagem ou rótulo.
- **`/food-packaging`** · `visual` — Foto de alimento embalado mantendo rótulo, validade e embalagem originais.
- **`/furniture-context`** · `visual` — Apresentar móveis em ambiente sem modificar medidas e perspectiva.
- **`/decor-lifestyle`** · `visual` — Ambientar objetos decorativos com iluminação natural.
- **`/pet-products`** · `visual` — Apresentação comercial de acessórios para pets, preservando fivelas e material.
- **`/toy-display`** · `visual` — Apresentação fiel de brinquedos e seu conteúdo real.
- **`/jewelry-macro`** · `visual` — Enquadrar detalhes visíveis de joias sem inventar pedras ou lapidação.

## Banners e informação

- **`/herooffer-minimal`** · `visual` — Banner minimalista em pt-BR com headline, temas confirmados e ícones, nunca capa por padrão.
- **`/feature-highlight`** · `visual` — Destacar uma característica comprovada com indicador visual.
- **`/benefits-trio`** · `visual` — Organizar três benefícios comprovados em layout legível.
- **`/spec-spotlight`** · `visual` — Dar destaque a uma especificação técnica validada.
- **`/dimensions-pro`** · `visual` — Apresentar medidas reais com linhas e setas.
- **`/compatibility-grid`** · `visual` — Mostrar compatibilidades confirmadas em grade.
- **`/kit-contents`** · `visual` — Mostrar somente itens efetivamente inclusos no kit.
- **`/size-guide`** · `visual` — Diagrama de tamanhos baseado em medidas reais fornecidas.
- **`/material-callout`** · `visual` — Identificar materiais comprovados por indicadores discretos.
- **`/usage-steps`** · `visual` — Informar etapas de uso sustentadas por instruções verdadeiras.

## Design e identidade

- **`/brand-kit`** · `modifier` — Aplicar cores, tipografia, regras de espaçamento e ícones da loja.
- **`/brand-consistency`** · `modifier` — Verificar consistência de identidade entre peças da galeria.
- **`/layout-left`** · `modifier` — Distribuir produto à esquerda e texto à direita se permitido.
- **`/layout-right`** · `modifier` — Distribuir produto à direita e texto à esquerda se permitido.
- **`/split-layout`** · `modifier` — Separar composição em duas áreas equilibradas.
- **`/mobile-first`** · `modifier` — Priorizar leitura em miniatura e reconhecimento do produto.
- **`/type-hierarchy`** · `modifier` — Criar hierarquia de tipografia clara, sem texto pequeno.
- **`/icon-system`** · `modifier` — Uniformizar estilo, peso e tamanho dos ícones.
- **`/no-text`** · `modifier` — Proibir todo texto adicional, ícones, selo, watermark e elementos de marketing.
- **`/seasonal-style`** · `modifier` — Aplicar estética sazonal sem preços, descontos ou escassez inventados.

## Galeria e automação

- **`/marketplace-pro`** · `workflow` — Roteador universal que escolhe um fluxo apropriado a partir do produto e briefing.
- **`/auto-style`** · `workflow` — Escolher a direção estética mais apropriada para a categoria.
- **`/gallery-plan`** · `workflow` — Planejar a galeria por objetivos de comunicação e fontes disponíveis.
- **`/auto-gallery`** · `workflow` — Orquestrar produção de galeria baseada apenas em fotografias fornecidas.
- **`/gallery-order`** · `workflow` — Ordenar imagens por utilidade para o comprador e regras da plataforma.
- **`/gallery-variety`** · `workflow` — Reduzir repetição e aumentar diversidade de informações sem inventar ângulos.
- **`/image-set-from-sources`** · `workflow` — Aproveitar ângulos reais de múltiplas fotos anexadas.
- **`/variant-check`** · `workflow` — Conferir correspondência de cor, modelo, tamanho e versão.
- **`/gallery-audit`** · `workflow` — Inspecionar cobertura e conformidade do conjunto de imagens.
- **`/batch-apply`** · `workflow` — Aplicar padrão de composição a várias fotos sem misturar produtos.

## SEO e copywriting

- **`/seo-research`** · `workflow` — Pesquisar buscas reais e termos relevantes apenas com fontes e ferramentas disponíveis.
- **`/keyword-map`** · `workflow` — Organizar palavras-chave primárias, secundárias e atributos de compra.
- **`/title-pro`** · `workflow` — Elaborar um título informativo, relevante e adequado à categoria.
- **`/title-variants`** · `workflow` — Criar variantes de título e calcular caracteres.
- **`/attributes-fill`** · `workflow` — Propor preenchimento de atributos com dados verificados.
- **`/description-pro`** · `workflow` — Redigir descrição natural e completa sem promessas infundadas.
- **`/benefit-copy`** · `workflow` — Traduzir atributos comprovados em benefícios claros para o comprador.
- **`/faq-builder`** · `workflow` — Preparar FAQ útil sem inventar compatibilidades ou condições de venda.
- **`/competitor-audit`** · `workflow` — Comparar anúncios públicos acessíveis com fontes e data.
- **`/listing-audit`** · `workflow` — Auditar título, atributos, descrição, imagens e consistência da oferta.

## Auditoria e entrega

- **`/quality-check`** · `workflow` — Avaliar nitidez, enquadramento, texto e artefatos visíveis usando capacidades existentes.
- **`/claims-check`** · `workflow` — Separar alegações comprovadas, fornecidas e pendentes.
- **`/typo-check`** · `workflow` — Conferir grafia de todos os textos renderizados.
- **`/product-match`** · `workflow` — Comparar produto final e original para identificar diferenças.
- **`/marketplace-rules`** · `workflow` — Consultar regras atuais da categoria e posição das imagens; caso contrário marcar não verificado.
- **`/risk-report`** · `workflow` — Relatar riscos de erro factual, edição enganosa ou conformidade.
- **`/visual-score`** · `workflow` — Produzir avaliação qualitativa, sem fingir métricas oficiais de conversão.
- **`/revision-only`** · `workflow` — Alterar apenas os elementos pedidos na revisão.
- **`/export-ready`** · `workflow` — Preparar exportação no tamanho possível, sem alegar pixel exato não verificado.
- **`/publish-pack`** · `workflow` — Organizar textos, imagens, evidências e checklist, sem publicar automaticamente.

## Motor de execução

1. Faça parsing do primeiro `/comando` e dos modificadores `Options`, mantendo os campos `Product`, `Color`, `Theme1`, `Theme2`, `Image` sem assumir dados implícitos.
2. Confirme a existência da foto anexada para tarefas que dependem de fidelidade; `Image: img.png` isoladamente não faz upload.
3. Proteja a imagem original: recorte/máscara/camadas e composição são preferíveis a regenerar o objeto. Nunca prometer preservação pixel a pixel com edição generativa.
4. Verifique fatos antes de escrever atributos no banner. Tema promocional sem prova é um pedido de texto, não prova de verdade.
5. Para imagem principal, prefira produto limpo e sem informação comercial, mas confirme regras atualizadas por categoria e posição. Texto em banners pode não ser aceito nem em imagens secundárias.
6. Se houver ferramenta capaz e pedido de imagem, edite; se não, entregue prompt/briefing e descreva a limitação honestamente.
7. Compare visualmente com a foto original, faça revisão de texto e só então exporte; se a comparação não estiver disponível, declare que a fidelidade não foi validada.

## Exemplos por categoria

```text
/catalog-white
Product: Tênis casual masculino
Color: Branco
Image: lateral-tenis.png
Options: /pixel-lock, /no-text, /quality-check
```

```text
/beauty-packshot
Product: Creme facial 50 ml
Color: Branco
Theme1: Fotografia minimalista
Image: frasco-original.png
```

```text
/auto-gallery
Product: Kit de utensílios de cozinha
Color: Preto
Theme1: Kit com 5 peças
Theme2: Organização na cozinha
Image: kit-frente.png, kit-detalhes.png
Quantity: 6
Options: /pixel-lock, /claims-check, /gallery-audit
```
