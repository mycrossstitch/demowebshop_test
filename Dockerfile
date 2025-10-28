FROM python:3.12-alpine

# Install system dependencies
RUN apk add --no-cache \
    chromium \
    chromium-chromedriver \
    openjdk11-jre \
    curl \
    tar \
    bash \
    tzdata \
    wget

# Install latest Allure CLI
ENV ALLURE_VERSION=2.29.0
RUN curl -sL https://repo.maven.apache.org/maven2/io/qameta/allure/allure-commandline/${ALLURE_VERSION}/allure-commandline-${ALLURE_VERSION}.tgz \
    | tar -xz -C /opt/ && \
    ln -s /opt/allure-${ALLURE_VERSION}/bin/allure /usr/local/bin/allure

# Set working directory
WORKDIR /usr/workspace

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure Allure is in PATH
ENV PATH="/usr/local/bin:${PATH}"

# Default command
CMD ["bash"]

