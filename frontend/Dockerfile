FROM node:16-alpine

WORKDIR /app

COPY . .
RUN rm -rf node_modules
RUN rm -rf .next

RUN npm install
RUN npm run build

EXPOSE 3000
CMD ["npm", "start"]
