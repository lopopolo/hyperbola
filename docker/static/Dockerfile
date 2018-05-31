FROM node as dist-build

COPY package.json yarn.lock webpack.config.js /opt/
COPY src /opt/src

RUN mkdir /opt/dist && \
    mkdir /opt/document-root && \
    cd /opt && \
    yarn install
RUN cd /opt && ls && $(yarn bin)/webpack --mode production

FROM hyperbola-app as static-build

COPY --from=dist-build /opt/document-root /opt/document-root
COPY --from=dist-build /opt/dist /opt/dist

RUN /opt/venv/bin/python /opt/manage.py collectstatic --no-input

FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf

COPY docker/static/hyperbola.conf /etc/nginx/conf.d/hyperbola.conf
COPY docker/static/nginx-base-config /etc/nginx/conf.d/nginx-base-config
COPY --from=static-build /opt/document-root /opt/static
COPY docker/static/humans.txt docker/static/robots.txt /opt/static/

EXPOSE 8888
