FROM node:20-alpine

WORKDIR /web/cimax/client/

COPY . .

RUN rm -rf node_modules

RUN npm install

COPY entrypoint.js /usr/local/bin/entrypoint.js

RUN chmod +x /usr/local/bin/entrypoint.js

RUN apk add bash

EXPOSE 5173

ENTRYPOINT ["node", "/usr/local/bin/entrypoint.js"]