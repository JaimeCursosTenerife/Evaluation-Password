contraseña = input("Introduce una contraseña: ")
nivel = 1

if len(contraseña) >= 6:
    nivel += 1
if any(c.islower() for c in contraseña) and any (c.isupper() for c in contraseña):
    nivel += 1
if any(c.isdigit() for c in contraseña):
    nivel += 1
if any(c in "!@#$%&/*()-_=+[]{};:,.<>?/\\|" for c in contraseña) and len(contraseña) >= 10:
    nivel += 1

nivel = min(nivel, 5)

etiquetas = ["Nada segura", "Poco segura", "Segura", "Muy segura", "Perfecta"]
print(f"Seguridad de la contraseña: {etiquetas[nivel-1]} (Nivel {nivel})")

