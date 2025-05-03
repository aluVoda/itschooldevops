
##  `README.md` — DevOps Docker + Ansible Project

###  Overview

This project demonstrates how to:
- Monitor system info using Bash and Python scripts
- Containerize them with Docker and Docker Compose
- Automate deployment and cleanup using Ansible

---

##  Project Structure

```
monitoring-project/
├── bash/
│   ├── Dockerfile
│   └── bash_monitor.sh
├── python/
│   ├── Dockerfile
│   └── python_monitor.py
├── docker-deployment/
│   └── docker-compose.yml
├── ansible/
│   ├── add_docker_user.yml
│   ├── deploy_docker_compose.yml
│   ├── cleanup_deployment.yml
├── hosts.ini
└── README.md
```

---

##  Step A: Create Scripts

Create two scripts that run in an infinite loop and print system information every **X seconds**.

### Bash Script

```bash
# bash/bash_monitor.sh
#!/bin/bash

```

### Python Script

```python
# python/python_monitor.py

```

---

##  Step B: Dockerize Scripts

### Bash Dockerfile

```dockerfile

    will copy the Bash script into the container, and run it as the command.
```

### Python Dockerfile

```dockerfile

    will copy the Python script into the container, and run it as the command.
```

### Build & Run

```bash

```

---

##  Step C: Docker Compose

### docker-deployment/docker-compose.yml
    run both containers together using Docker Compose
```yaml

```

### Run

```bash
docker-compose build

docker-compose up

```

> Use `docker logs` to view output.

```bash
docker logs -f bash_script_container
docker logs -f python_script_container

```

---

##  Step D: Ansible - Add User with Docker Access

### ansible/add_docker_user.yml

```yaml

```

### Run It

```bash

```

---

##  Step E: Deploy Docker Compose with Ansible

### ansible/deploy_docker_compose.yml

```yaml

```

### Run It

```bash

```

---

##  Step F: Cleanup Playbook

### ansible/cleanup_deployment.yml

```yaml

```

### Run It

```bash

```

---

##  Requirements

- Docker & Docker Compose installed on target host
- Ansible installed on your control machine
- SSH access to the host
- `community.docker` collection:  
  `ansible-galaxy collection install community.docker`

---

##  Testing Tips

- Use `docker ps` and `docker logs` to verify running containers.
- Use `id devopsuser` to check user and group membership.
- Ensure `docker-compose` commands work as expected under `devopsuser`.

---
