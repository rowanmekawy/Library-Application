# Use Node.js as a parent image
FROM node:lts-alpine

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Bundle app source
COPY . .

# Build the app
RUN npm run build

# Install a simple HTTP server to serve static content
RUN npm install -g http-server

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Serve the app
CMD ["http-server", "dist"]
