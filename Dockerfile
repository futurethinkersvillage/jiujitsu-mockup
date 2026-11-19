FROM nginx:1.27-alpine
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY site/ /usr/share/nginx/html/
# Optional private page, injected at build time from Coolify build variables so that
# neither its address nor its content is stored in this (public) repository.
ARG PRIVATE_PAGE_PATH=""
ARG PRIVATE_PAGE_B64=""
RUN mkdir -p /etc/nginx/private && if [ -n "$PRIVATE_PAGE_PATH" ] && [ -n "$PRIVATE_PAGE_B64" ]; then \
      mkdir -p "/usr/share/nginx/html/$PRIVATE_PAGE_PATH" && \
      echo "$PRIVATE_PAGE_B64" | base64 -d > "/usr/share/nginx/html/$PRIVATE_PAGE_PATH/index.html" && \
      printf 'location ^~ /%s/ {\n  add_header X-Robots-Tag "noindex, nofollow" always;\n  add_header Referrer-Policy "no-referrer" always;\n  add_header Cache-Control "no-store" always;\n  try_files $uri $uri/ =404;\n}\n' "$PRIVATE_PAGE_PATH" > /etc/nginx/private/page.conf; \
    fi
EXPOSE 80
