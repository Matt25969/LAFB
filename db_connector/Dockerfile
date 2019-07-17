FROM node:10 as node-build
WORKDIR /build
COPY . .
RUN npm install
RUN npm start
ENTRYPOINT ["/usr/local/bin/serve", "-l", "5001"]
