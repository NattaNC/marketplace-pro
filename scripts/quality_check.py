#!/usr/bin/env python3
"""Auditoria local *heurística* de texto/metadata de anúncio. Não consulta o Mercado Livre.

Uso:
    python scripts/quality_check.py examples/anuncio_exemplo.json
    python scripts/quality_check.py examples/anuncio_exemplo.json --title-limit 60 --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path


PROMOTIONAL_PATTERNS = [
    (r"\bimperdivel\b", "Evite apelo promocional no título."),
    (r"\bpromocao\b", "Evite a palavra 'promoção' no título."),
    (r"\boferta\b", "Evite a palavra 'oferta' no título."),
    (r"\bmelhor\s+(?:do\s+brasil|do\s+mercado|preco)\b", "Afirmação comparativa requer comprovação."),
    (r"\b100\s*%\s*original\b", "Confirme evidências de originalidade antes de afirmar."),
]


def normalize(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return value.casefold()


def validate_listing(data: dict, title_limit: int | None = None) -> list[dict]:
    """Return findings with severity (P0-P3) and suggested action.

    No external facts are assumed. Images are checked ONLY from their supplied
    metadata; this function does not actually inspect image pixels.
    """
    findings: list[dict] = []

    def add(priority: str, field: str, message: str):
        findings.append({"priority": priority, "field": field, "message": message})

    title = data.get("title", "")
    description = data.get("description", "")
    brand = data.get("brand", "")
    model = data.get("model", "")
    attributes = data.get("attributes", {})
    images = data.get("images", [])

    if not isinstance(title, str) or not title.strip():
        add("P1", "title", "Preencha um título descritivo do produto.")
        title = ""
    if not isinstance(description, str) or not description.strip():
        add("P1", "description", "Preencha uma descrição fiel e informativa.")
        description = ""
    if not isinstance(images, list):
        add("P1", "images", "O campo images deve ser uma lista de metadados de fotos.")
        images = []
    if not isinstance(attributes, dict):
        add("P2", "attributes", "O campo attributes deve ser um objeto com atributos confirmados.")
        attributes = {}

    if title_limit is not None and len(title) > title_limit:
        add("P1", "title", f"Título tem {len(title)} caracteres; limite informado: {title_limit}.")

    if title and title == title.upper() and any(ch.isalpha() for ch in title):
        add("P2", "title", "Evite título inteiramente em maiúsculas.")

    normalized = normalize(title)
    for pattern, message in PROMOTIONAL_PATTERNS:
        if re.search(pattern, normalized):
            add("P2", "title", message)

    tokens = re.findall(r"[a-z0-9]+", normalized)
    common = [(word, count) for word, count in Counter(tokens).items() if count >= 3 and len(word) >= 4]
    if common:
        add("P2", "title", f"Possível repetição excessiva: {', '.join(w for w, _ in common)}.")

    if brand and isinstance(brand, str) and normalize(brand).strip() not in normalized:
        add("P2", "title", "Marca informada não aparece no título; verifique se deveria aparecer.")
    if model and isinstance(model, str) and normalize(model).strip() not in normalized:
        add("P2", "title", "Modelo informado não aparece no título; verifique a pertinência.")
    if 0 < len(description.strip()) < 100:
        add("P2", "description", "Descrição curta; confira se responde às dúvidas essenciais.")
    if not attributes:
        add("P2", "attributes", "Sem atributos informados; confira a ficha técnica no cadastro.")
    if not images:
        add("P1", "images", "Nenhuma imagem declarada; inclua fotos reais do produto.")
    else:
        covers = [im for im in images if isinstance(im, dict) and im.get("role") == "cover"]
        if not covers:
            add("P1", "images", "Indique a foto de capa no metadado role='cover'.")
        for idx, image in enumerate(images, start=1):
            if not isinstance(image, dict):
                add("P2", f"images[{idx}]", "Imagem deve ter metadados em formato objeto.")
                continue
            if image.get("role") == "cover" and image.get("contains_overlay") is True:
                add("P1", f"images[{idx}]", "Capa tem overlay; verifique as regras da categoria.")
            if image.get("ai_generated") is True and image.get("product_fidelity_verified") is not True:
                add("P0", f"images[{idx}]", "Imagem de IA ainda não foi conferida contra o produto real. Não publique sem validação.")
            w, h = image.get("width"), image.get("height")
            if isinstance(w, int) and isinstance(h, int) and w != h:
                add("P3", f"images[{idx}]", "Foto não é quadrada; revise enquadramento/requisitos da categoria.")

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("listing", type=Path, help="Arquivo JSON com o anúncio")
    parser.add_argument("--title-limit", type=int, default=None, help="Limite confirmado da categoria (opcional)")
    parser.add_argument("--json", action="store_true", help="Saída estruturada")
    args = parser.parse_args()
    if args.title_limit is not None and args.title_limit < 1:
        parser.error("--title-limit deve ser maior que zero")

    try:
        data = json.loads(args.listing.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        parser.error(f"Não foi possível ler JSON válido: {exc}")
    if not isinstance(data, dict):
        parser.error("A raiz do JSON deve ser um objeto")

    findings = validate_listing(data, args.title_limit)
    if args.json:
        print(json.dumps({
            "title_characters": len(data.get("title", "")) if isinstance(data.get("title"), str) else 0,
            "title_limit_verified_by_user": args.title_limit,
            "image_pixels_checked": False,
            "findings": findings,
        }, ensure_ascii=False, indent=2))
    else:
        title = data.get("title", "")
        print(f"Título: {len(title) if isinstance(title, str) else 0} caracteres")
        if args.title_limit is None:
            print("Limite da categoria: NÃO verificado (forneça --title-limit se souber)")
        else:
            print(f"Limite informado: {args.title_limit}")
        print("Imagens: só metadados; análise de pixels NÃO realizada.")
        print(f"Alertas: {len(findings)}")
        for item in findings:
            print(f"- {item['priority']} [{item['field']}] {item['message']}")
    # Findings are suggestions requiring human review, not a promise of compliance.
    return 0


if __name__ == "__main__":
    sys.exit(main())
