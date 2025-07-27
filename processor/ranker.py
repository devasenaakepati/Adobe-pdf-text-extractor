# processor/ranker.py
from difflib import SequenceMatcher

def similarity(a, b):
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()

def rank_sections(sections, persona, job):
    context = f"{persona} {job}"
    ranked = []

    for sec in sections:
        score = similarity(context, sec["text"])
        ranked.append({
            "document": sec["document"],
            "page": sec["page"],
            "section_title": sec["title"],
            "importance_rank": round(score, 3),
            "refined_text": sec["text"]
        })

    ranked.sort(key=lambda x: -x["importance_rank"])
    return ranked[:10]  # Top 10 relevant
