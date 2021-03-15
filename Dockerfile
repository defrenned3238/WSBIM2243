FROM ubuntu
RUN apt-get update
RUN apt-get install -y git python-virtualenv
RUN git clone https://github.com/defrenned3238/WSBIM2243.git
