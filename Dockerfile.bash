FROM ubuntu:22.04

RUN apt-get update && apt-get install -y \
    procps lscpu coreutils grep awk util-linux \
    && apt-get clean

COPY bash_monitor.sh /usr/local/bin/bash_monitor.sh
RUN chmod +x /usr/local/bin/bash_monitor.sh

CMD ["/usr/local/bin/bash_monitor.sh"]
