# Arma public/index.html (para Cloudflare) y una vista previa con el logo embebido.
# Uso: python3 construir.py [numero_whatsapp]   (ej. 593991234567)
import base64, re, sys, pathlib
raiz = pathlib.Path(__file__).parent
numero = sys.argv[1] if len(sys.argv) > 1 else "593000000000"
fuente = (raiz / "src/index.html").read_text().replace("{{WHATSAPP}}", numero)
(raiz / "public/index.html").write_text(fuente.replace("{{LOGO_CLARO}}", "logo-claro.png"))
logo = "data:image/png;base64," + base64.b64encode((raiz / "public/logo-claro.png").read_bytes()).decode()
vista = fuente.replace("{{LOGO_CLARO}}", logo)
cab = vista[vista.index("<head>") + 6 : vista.index("</head>")]
cab = re.sub(r'<meta charset[^>]*>|<meta content="width=device-width[^>]*>|<link href="icono[^>]*>', "", cab)
cuerpo = vista[vista.index("<body>") + 6 : vista.index("</body>")]
(raiz / "vista-previa.html").write_text(cab + "\n" + cuerpo)
print("listo:", numero)
