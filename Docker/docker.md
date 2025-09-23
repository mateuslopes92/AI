# Docker

## What is docker?
- Platform to consistently build, run and ship applications in a consistent matter(run on same way on diff machines)
- Package with defined versions
- Isolated environments

## Container vs Virtual Machine
- Container is an isolated environment for running application
    - Containers are lightweight and
    - allow running multiple apps in isolation
    - Start faster as use the OS of the host
    - Need less hardware resources
- Virtual Machine is abstraction of a machine or physical hardware (Hypervisor like Virtualbox VMware and Hyper-V for windows)
    - Slow startup

## Docker Architecture
- Use Client - Server architecture
- Uses rest api to talk with docker engine
- Containers are process and share kernel of the host

## Registry (Docker Hub)
- Is like a github to git
- All is written in the docker file
- We can push image to docker hub in the registry then we can put on any machine to run like prod or test and have same image as dev

## Development workflow
### Real example

Creating folder project and opening on vscode
```
mkdir hello-docker
cd hello-docker
code .
```
