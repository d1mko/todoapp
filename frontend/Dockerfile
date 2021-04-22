FROM node

WORKDIR /app/frontend
COPY package.json /app/frontend

RUN npm install -g npm
RUN npm install

COPY ./src ./src
COPY ./public ./public

RUN npm run dev

EXPOSE 5000
