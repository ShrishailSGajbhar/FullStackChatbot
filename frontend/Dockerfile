# Stage 1: Install Chakra UI dependencies and build the React application
FROM node:20.11.1 AS build

WORKDIR /app

# Copy package.json and package-lock.json separately to leverage Docker layer caching
COPY package.json package-lock.json ./
RUN npm install

# Install Chakra UI and its peer dependencies
RUN npm install @chakra-ui/react @emotion/react @emotion/styled framer-motion

COPY . .
RUN npm run build

# Stage 2: Serve the React application using Nginx
FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
