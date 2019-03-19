FROM node:8.15-alpine

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN npm uninstall -g yarn && \
    npm install -g yarn && \
    chmod u+x /usr/local/bin/yarn && \    
    yarn global add nuxt vue-cli create-nuxt-app && \
    yarn install && \
    yarn nuxt build

ENV HOST 0.0.0.0
EXPOSE 3000
CMD ["yarn", "nuxt", "start"]