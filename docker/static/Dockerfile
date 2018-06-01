FROM hyperbola/app:latest as static-build

FROM nginx:stable-alpine
LABEL maintainer="Ryan Lopopolo <rjl@hyperbo.la>"

RUN rm /etc/nginx/conf.d/default.conf

COPY docker/static/hyperbola.conf /etc/nginx/conf.d/hyperbola.conf
COPY docker/static/nginx-base-config /etc/nginx/conf.d/nginx-base-config
COPY --from=static-build /opt/document-root /opt/static
COPY docker/static/humans.txt docker/static/robots.txt /opt/static/

EXPOSE 80
EXPOSE 8888
