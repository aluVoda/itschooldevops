# Use Ubuntu as the base image
FROM ubuntu:20.04

# Set environment variables to avoid interaction during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && apt-get install -y \
    bash \
    lsb-release \
    procps \
    coreutils \
    && rm -rf /var/lib/apt/lists/*

# Copy the Bash script into the container
COPY bash_monitor.sh /usr/local/bin/bash_monitor.sh

# Make the script executable
RUN chmod +x /usr/local/bin/bash_monitor.sh

# Set the default command to run the Bash script
CMD ["/usr/local/bin/bash_monitor.sh"]
