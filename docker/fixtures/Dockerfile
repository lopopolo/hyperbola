FROM hyperbola/backend:latest
LABEL maintainer="Ryan Lopopolo <rjl@hyperbo.la>"

RUN apk --no-cache add mariadb-client

ADD fixtures-entrypoint.sh /opt/fixtures-entrypoint.sh

ENTRYPOINT ["/opt/fixtures-entrypoint.sh"]
