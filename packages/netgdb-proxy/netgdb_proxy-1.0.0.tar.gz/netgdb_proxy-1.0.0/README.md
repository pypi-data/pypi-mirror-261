# netgdb-proxy
This proxy facilitates communication between a client kgdb instance and a remote
panicked FreeBSD machine running NetGDB. This can be started either as a daemon
or as a single process.

## Installation and Execution

### Single Mode
Run `pip install netgdb-proxy` to install, and then `netgdb_proxy` to start
the proxy. Follow the prompts to connect with your FreeBSD machine and your kgdb
client, or follow this guide:

From the `db>` prompt on the panicked machine, run `netgdb -s <proxy ip>`. This
will output a port for you to connect with your kgdb client from.
Then from your client, run `target remote <proxy ip>:<given port>`.

### Daemon Mode
Run `pip install netgdb-proxy[daemon]` to install with the daemon extra. Then
you can run `netgdb_proxy_d` to start the background process. You will then
be able to connect with any number of pairs FreeBSD machines and clients, just
without the helpful prompts from the proxy.

## Development

### Installation
This project uses poetry to manage dependencies and distrobution. After cloning,
set up with `poetry install --with dev`.

### Contribution
Before submitting a pull request, please format your changes with
`poetry run black .` and `poetry run ruff check . --fix`.