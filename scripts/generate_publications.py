#!/usr/bin/env python3
"""Generate the Jekyll publication collection from files/freire.bib."""

import argparse
import calendar
import json
import re
import unicodedata
from datetime import date
from pathlib import Path

from pybtex.database import BibliographyData
from pybtex.database.input import bibtex


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SOURCE = ROOT / "files" / "freire.bib"
DEFAULT_OUTPUT = ROOT / "_publications"
PUBLICATION_TYPES = {"article", "book", "inbook", "incollection", "inproceedings", "phdthesis", "mastersthesis", "techreport"}
MIN_PUBLICATION_YEAR = 2023
MONTHS = {name.lower(): number for number, name in enumerate(calendar.month_name) if name}
MONTHS.update({name.lower(): number for number, name in enumerate(calendar.month_abbr) if name})


class DuplicateKeyParser(bibtex.Parser):
    """Keep duplicate source records instead of letting one abort generation."""

    def process_entry(self, entry_type, key, fields):
        if key in self.data.entries:
            duplicate_number = 2
            duplicate_key = f"{key}-{duplicate_number}"
            while duplicate_key in self.data.entries:
                duplicate_number += 1
                duplicate_key = f"{key}-{duplicate_number}"
            key = duplicate_key
        unique_fields = []
        seen_fields = set()
        for field_name, field_value in fields:
            if field_name.lower() in seen_fields:
                continue
            seen_fields.add(field_name.lower())
            unique_fields.append((field_name, field_value))
        super().process_entry(entry_type, key, unique_fields)


def field(entry, name, default=""):
    value = entry.fields.get(name, default)
    return str(value).strip()


def clean_text(value):
    value = re.sub(r"[{}]", "", value)
    return re.sub(r"\\([&%#])", r"\1", value).strip()


def publication_date(entry):
    year = field(entry, "year")
    if not year.isdigit():
        raise ValueError("missing or invalid year")

    month_value = field(entry, "month").lower().strip("{}")
    month = int(month_value) if month_value.isdigit() else MONTHS.get(month_value[:3], 1)
    month = min(max(month, 1), 12)
    day_value = field(entry, "day")
    day = int(day_value) if day_value.isdigit() else 1
    day = min(max(day, 1), calendar.monthrange(int(year), month)[1])
    return date(int(year), month, day)


def slugify(value):
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", normalized.lower()).strip("-")
    return slug or "publication"


def authors(entry):
    people = entry.persons.get("author", [])
    names = []
    for person in people:
        name = " ".join(person.first_names + person.middle_names + person.last_names)
        names.append(clean_text(name))
    if not names:
        return ""
    if len(names) == 1:
        return names[0]
    return ", ".join(names[:-1]) + ", and " + names[-1]


def venue(entry):
    return clean_text(field(entry, "journal") or field(entry, "booktitle") or field(entry, "publisher") or field(entry, "howpublished"))


def citation(entry, title, publication_year, publication_venue):
    parts = [authors(entry), f'"{title}."']
    if publication_venue:
        parts.append(publication_venue)
    parts.append(publication_year)
    return " ".join(part for part in parts if part)


def render(entry, key):
    title = clean_text(field(entry, "title"))
    published = publication_date(entry)
    publication_venue = venue(entry)
    paper_url = field(entry, "url") or field(entry, "doi")
    if paper_url.startswith("10."):
        paper_url = "https://doi.org/" + paper_url
    abstract = clean_text(field(entry, "abstract") or field(entry, "note"))
    slug = f"{published.isoformat()}-{slugify(title)}"
    metadata = {
        "title": title,
        "collection": "publications",
        "generated_by": "scripts/generate_publications.py",
        "permalink": f"/publication/{slug}",
        "date": published.isoformat(),
        "venue": publication_venue,
        "citation": citation(entry, title, str(published.year), publication_venue),
        "bibtex_key": key,
    }
    if abstract:
        metadata["excerpt"] = abstract
    if paper_url:
        metadata["paperurl"] = paper_url

    lines = ["---"]
    for name, value in metadata.items():
        lines.append(f"{name}: {json.dumps(value, ensure_ascii=False)}")
    lines.extend(["---", "", f"[View publication]({paper_url})" if paper_url else ""])
    return slug + ".md", "\n".join(lines).rstrip() + "\n"


def generate(source, output, clean=True):
    bibliography: BibliographyData = DuplicateKeyParser().parse_file(str(source))
    output.mkdir(parents=True, exist_ok=True)
    generated = {}
    skipped = []

    for key, entry in bibliography.entries.items():
        if entry.type.lower() not in PUBLICATION_TYPES:
            continue
        if field(entry, "year").isdigit() and int(field(entry, "year")) < MIN_PUBLICATION_YEAR:
            continue
        try:
            filename, contents = render(entry, key)
        except ValueError as error:
            skipped.append(f"{key}: {error}")
            continue
        if filename in generated:
            filename = f"{Path(filename).stem}-{slugify(key)}.md"
        generated[filename] = contents

    if clean:
        for existing in output.glob("*.md"):
            existing.unlink()
    for filename, contents in generated.items():
        (output / filename).write_text(contents, encoding="utf-8")

    print(f"Generated {len(generated)} publications in {output}")
    for warning in skipped:
        print(f"Skipped {warning}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument("--keep-existing", action="store_true", help="Do not remove old markdown files")
    args = parser.parse_args()
    generate(args.source, args.output, clean=not args.keep_existing)


if __name__ == "__main__":
    main()