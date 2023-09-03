FROM node:19-alpine

WORKDIR /app

COPY ./package*.json .
RUN npm install npm@latest -g && npm install

COPY . .

RUN npm rebuild esbuild
CMD npm run dev --host