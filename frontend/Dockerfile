# Stage 1: Install Chakra UI dependencies and build the React application
FROM node:20.11.1 AS build

WORKDIR /app

# Copy package.json and package-lock.json separately to leverage Docker layer caching
COPY package.json package-lock.json ./
RUN npm install

# Install Chakra UI and its peer dependencies
RUN npm install @chakra-ui/react @emotion/react @emotion/styled framer-motion

COPY . .

EXPOSE 3000

CMD ["npm", "start"]
