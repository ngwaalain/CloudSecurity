import os
from pathlib import Path
from datetime import datetime

SITE_ROOT = "/CloudSecurity"

SECTIONS = {
    "cspm/runbooks":      ("docs/cspm/runbooks/index.md",      "PLACEHOLDER_RUNBOOKS"),
    "cspm/exceptions":    ("docs/cspm/exceptions/index.md",    "PLACEHOLDER_EXCEPTIONS"),
    "cspm/risk-register": ("docs/cspm/risk-register/index.md", "PLACEHOLDER_RISK"),
}

ICONS = {
    ".pdf":  ("PDF",         "#E24B4A"),
    ".html": ("HTML",        "#1D9E75"),
    ".docx": ("Word",        "#7F77DD"),
    ".xlsx": ("Excel",       "#1D9E75"),
    ".pptx": ("PowerPoint",  "#BA7517"),
}

def sp(f):
    return SITE_ROOT + "/" + str(f.relative_to(Path("docs"))).replace("\\", "/")

def render(section_key):
    fdir = Path("docs") / section_key / "files"
    if not fdir.exists():
        return '<p class="cs-no-files">No files uploaded yet.</p>'
    all_f = sorted([f for f in fdir.iterdir() if f.is_file() and not f.name.startswith(".")])
    if not all_f:
        return '<p class="cs-no-files">No files uploaded yet.</p>'
    src_stems = {f.stem for f in all_f if f.suffix.lower() in (".docx", ".pptx")}
    show = [f for f in all_f if not (f.suffix.lower() == ".pdf" and f.stem in src_stems)]
    L = ['<div class="cs-file-list">']
    for i, f in enumerate(show):
        ext  = f.suffix.lower()
        name = f.stem.replace("-", " ").replace("_", " ").title()
        uid  = section_key.replace("/", "-") + "-" + str(i)
        tag, col = ICONS.get(ext, (ext.upper(), "#888780"))
        if ext in (".docx", ".pptx"):
            pf = fdir / (f.stem + ".pdf")
            view_sp = sp(pf) if pf.exists() else None
        else:
            view_sp = sp(f) if ext in (".pdf", ".html") else None
        h = "950" if ext == ".html" else "820"
        L.append('<div class="cs-file-item">')
        L.append('  <div class="cs-file-row" onclick="csT(\'' + uid + '\')">')
        L.append('    <div class="cs-file-icon"><svg width="14" height="14" viewBox="0 0 14 14" fill="none"><rect x="2" y="1" width="10" height="12" rx="1.5" stroke="currentColor" stroke-width="1.2"/><path d="M4 5h6M4 7.5h6M4 10h4" stroke="currentColor" stroke-width="1" stroke-linecap="round"/></svg></div>')
        L.append('    <div class="cs-file-name">' + name + '</div>')
        L.append('    <span class="cs-file-tag" style="background:' + col + '22;color:' + col + '">' + tag + '</span>')
        L.append('    <a class="cs-file-btn" href="' + sp(f) + '" target="_blank" onclick="event.stopPropagation()">Download</a>')
        if view_sp:
            L.append('    <a class="cs-file-btn" href="' + view_sp + '" target="_blank" onclick="event.stopPropagation()">View</a>')
        L.append('    <div class="cs-chev" id="chev-' + uid + '">&#9662;</div>')
        L.append('  </div>')
        if view_sp:
            L.append('  <div class="cs-file-viewer" id="viewer-' + uid + '">')
            L.append('    <iframe src="' + view_sp + '" width="100%" height="' + h + '" frameborder="0" title="' + name + '"></iframe>')
            L.append('  </div>')
        L.append('</div>')
    L.append('</div>')
    L.append('<script>function csT(u){var v=document.getElementById("viewer-"+u),c=document.getElementById("chev-"+u);if(!v)return;var o=v.style.display==="block";v.style.display=o?"none":"block";c.innerHTML=o?"&#9662;":"&#9652;";}</script>')
    L.append('<p class="cs-ts">Last updated: ' + datetime.utcnow().strftime("%d %B %Y at %H:%M") + ' UTC</p>')
    return "\n".join(L)

for sk, (mp, ph) in SECTIONS.items():
    p = Path(mp)
    if not p.exists():
        print("SKIP: " + mp); continue
    txt = p.read_text()
    p.write_text(txt.replace(ph, render(sk)))
    print("OK: " + mp)
print("Done.")
