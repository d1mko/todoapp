FROM node:latest

WORKDIR /app/frontend

COPY package-lock.json package-lock.json
COPY package.json package.json

RUN npm install

COPY . .

EXPOSE 5000
ENV HOST 0.0.0.0

