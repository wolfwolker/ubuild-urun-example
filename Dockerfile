FROM python:3.8
WORKDIR /app
COPY . /app
RUN pip install prettytable web3 eth-utils
EXPOSE 80
ENV ETH_WALLET 0x1234567890123456789012345678901234567890
CMD ["python", "print_eth_funds.py"]
# use this command to run the container
# docker run -p 4000:80 my-python-app 