# Sitio público de insurehub

Página de inicio estática (sin servidor). Se publica en Cloudflare como un proyecto aparte de la app.

- `public/`: lo que se publica (index.html, logos, íconos).
- `src/index.html`: el contenido y el diseño de la página (con marcadores para el logo y el número de WhatsApp).
- `construir.py`: arma `public/index.html`. Uso: `python3 construir.py 593991234567` (número de WhatsApp).

## Cambiar el número de WhatsApp
En `public/index.html`, busca `const WHATSAPP = "593000000000";` y reemplaza el número:
código de país 593 y el celular sin el 0 inicial (ej. 0991234567 → 593991234567).

## Publicar en Cloudflare
1. Crea un repositorio nuevo en GitHub (`insurehub-landing`) y sube el contenido de esta carpeta.
2. En Cloudflare: Workers y Pages → Crear → Importar un repositorio → elige `insurehub-landing`. No hace falta comando de compilación; usa el `wrangler.jsonc` incluido.
3. Cuando compres insurehub.ec: en el proyecto, Configuración → Dominios → agrega `insurehub.ec` y `www.insurehub.ec`.
 
