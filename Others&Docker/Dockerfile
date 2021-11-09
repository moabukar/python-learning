FROM golang:1.16.0

# Run update
RUN apt update &&\
    apt upgrade

# Install system modules
RUN apt install -y \
    wget\
    curl

# Set working folder
WORKDIR /usr/src/app

COPY src/go.mod /usr/src/app

# Install modules
RUN go mod download

EXPOSE 80