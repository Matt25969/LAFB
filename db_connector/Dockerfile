
FROM node:10 as node-build
WORKDIR /build
COPY . .
RUN npm install
ENTRYPOINT ["server.js", "-l", "5001"]
