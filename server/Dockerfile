# Use Node 20.11 alpine as parent image
FROM node:20

# Change the working directory on the Docker image to /app
WORKDIR /app

# Install Python
RUN apt-get update && apt-get install -y python3 python3-pip python3-venv python-is-python3 ffmpeg

# Copy package.json and package-lock.json to the /app directory
COPY package.json package-lock.json ./

# Install dependencies
RUN npm install

# Copy the rest of project files into this image
COPY . .

# Install Python dependencies
RUN pip install --break-system-packages -r requirements.txt

# Expose application port
EXPOSE 8080

# Start the application
CMD npm start
