FROM hyperbola/app:latest as static-build

FROM nginx:stable-alpine
LABEL maintainer="Ryan Lopopolo <rjl@hyperbo.la>"

RUN rm /etc/nginx/conf.d/default.conf

COPY hyperbola.conf /etc/nginx/conf.d/hyperbola.conf
COPY nginx-base-config /etc/nginx/conf.d/nginx-base-config
COPY --from=static-build /opt/document-root /opt/static
COPY humans.txt robots.txt /opt/static/

EXPOSE 80
EXPOSE 8888
