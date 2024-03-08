# https://docs.chia.net/harvester-rpc/
from chiarpc.client import Client
import os.path


class HarvesterClient:

    def __init__(self, base_url=None, private_cert_file=None, private_key_file=None):
        if base_url is None:
            base_url = 'https://localhost:8560'
        if private_cert_file is None or private_key_file is None:
            home_path = os.path.expanduser("~")
            ssl_path = os.path.join(home_path, '.chia', 'mainnet', 'config', 'ssl')
            if private_cert_file is None:
                private_cert_file = os.path.join(ssl_path, 'harvester', 'private_harvester.crt')
            if private_key_file is None:
                private_key_file = os.path.join(ssl_path, 'harvester', 'private_harvester.key')
        self.client = Client(base_url, private_cert_file, private_key_file)

    def call(self, endpoint, data):
        return self.client.call(endpoint, data)

    def add_plot_directory(self, dirname: str):
        return self.client.call('add_plot_directory',
                                data={'dirname': dirname})

    def delete_plot(self, filename: str):
        return self.client.call('delete_plot',
                                data={'filename': filename})

    def get_plots(self):
        return self.client.call('get_plots')

    def get_plot_directories(self):
        return self.client.call('get_plot_directories')

    def get_routes(self):
        return self.client.call('get_routes')

    def refresh_plots(self):
        return self.client.call('refresh_plots')

    def get_harvester_config(self):
        return self.client.call('get_harvester_config')

    def update_harvester_config(self):
        return self.client.call('update_harvester_config')

    def get_connections(self):
        return self.client.call('get_connections')

    def open_connection(self, host: str, port: int):
        return self.client.call('open_connection', {
            'host': host,
            'port': port
        })

    def close_connection(self, node_id):
        return self.client.call('close_connection', {
            'node_id': node_id
        })

    def healthz(self):
        return self.client.call('healthz')

    def stop_node(self):
        return self.client.call('stop_node')

    def remove_plot_directory(self, dirname: str):
        return self.client.call('remove_plot_directory', {
            'dirname': dirname
        })


if __name__ == '__main__':
    hc = HarvesterClient()

    res = hc.healthz()
    print(res)
