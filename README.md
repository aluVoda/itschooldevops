
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
# bash/Dockerfile.bash
    will copy the Bash script into the container, and run it as the command.
```

### Python Dockerfile

```dockerfile
# python/Dockerfile.python
    will copy the Python script into the container, and run it as the command.
```

### Build & Run

```bash
cd bash && docker build -t bash-monitor .
cd ../python && docker build -t python-monitor .
```

```bash
docker run --name bash-container bash-monitor
docker run --name python-container python-monitor
```

---

##  Step C: Docker Compose

### docker-deployment/docker-compose.yml
    run both containers together using Docker Compose
```yaml

```

### Run

```bash
cd docker-deployment
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
ansible-playbook -i hosts.ini ansible/add_docker_user.yml
```

---

##  Step E: Deploy Docker Compose with Ansible

### ansible/deploy_docker_compose.yml

```yaml

```

### Run It

```bash
ansible-playbook -i hosts.ini ansible/deploy_docker_compose.yml
```

---

##  Step F: Cleanup Playbook

### ansible/cleanup_deployment.yml

```yaml

```

### Run It

```bash
ansible-playbook -i hosts.ini ansible/cleanup_deployment.yml
```

---

## Requirements
- Docker & Docker Compose installed on host
- Ansible installed
- Python 3.8+ for running Ansible
- SSH access to target host (localhost in this case)

## Testing Tips
- Use `docker logs <container_name>` to view script output
- Adjust interval in scripts to change monitoring frequency
- Use `htop`, `df -h`, and `free -h` on host to verify output matches actual state
- After Compose deploy, run `docker ps` to verify containers are running


---
