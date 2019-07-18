FROM node:10
ARG FILE_VERSION=1
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
COPY routes/account${FILE_VERSION}.js routes/account.js
EXPOSE 5002
ENTRYPOINT [ "node", "server.js" ]
