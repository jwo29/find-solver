FROM node:16.16.0

WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

RUN npm install @vue/cli@5.0.8 --location=global

COPY package.json .
COPY package-lock.json .
RUN npm install

CMD ["npm", "run", "serve"]
