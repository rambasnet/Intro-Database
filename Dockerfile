FROM python:3

RUN apt update \
  && apt install -y \
  sqlite3 build-essential time curl cmake git nano dos2unix \
  net-tools iputils-ping iproute2 sudo gdb less 

ARG USER=user
ARG UID=1000
ARG GID=1000

# Set environment variables
ENV USER                ${USER}
ENV HOME                /home/${USER}

# Create user and setup permissions on /etc/sudoers
RUN useradd -m -s /bin/bash -N -u $UID $USER && \
    echo "${USER} ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers && \
    chmod 0440 /etc/sudoers && \
    chmod g+w /etc/passwd 

WORKDIR ${HOME}

RUN pip install --upgrade pip

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt


#WORKDIR /app

# Uses "Bira" theme with some customization. Uses some bundled plugins and installs some more from github
RUN sh -c "$(wget -O- https://github.com/deluan/zsh-in-docker/releases/download/v1.1.5/zsh-in-docker.sh)" -- \
    -t bira \
    -p git \
    -p ssh-agent \
    -p https://github.com/zsh-users/zsh-autosuggestions \
    -p https://github.com/zsh-users/zsh-completions

ENV PATH="${HOME}:${HOME}/.local/bin:${HOME}/kattis-cli:${PATH}"
#RUN echo export PATH="${HOME}:${HOME}/.local/bin:${PATH}" >> ${HOME}/.zshrc
ENV KATTIS_CLI="${HOME}/kattis-cli"

USER user

CMD zsh
