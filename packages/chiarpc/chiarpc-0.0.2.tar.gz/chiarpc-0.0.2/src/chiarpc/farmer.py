# https://docs.chia.net/farmer-rpc/
import os.path
from chiarpc.client import Client


class FarmerClient:

    def __init__(self, base_url=None, private_cert_file=None, private_key_file=None):
        if base_url is None:
            base_url = 'https://localhost:8559'
        if private_cert_file is None or private_key_file is None:
            home_path = os.path.expanduser("~")
            ssl_path = os.path.join(home_path, '.chia', 'mainnet', 'config', 'ssl')
            if private_cert_file is None:
                private_cert_file = os.path.join(ssl_path, 'farmer', 'private_farmer.crt')
            if private_key_file is None:
                private_key_file = os.path.join(ssl_path, 'farmer', 'private_farmer.key')
        self.client = Client(base_url, private_cert_file, private_key_file)

    def get_signage_point(self, sp_hash):
        return self.client.call('get_signage_point', data={'sp_hash': sp_hash})

    def get_signage_points(self):
        return self.client.call('get_signage_points')

    def get_reward_targets(self, search_for_private_key, max_ph_to_search: int = 500):
        return self.client.call('get_reward_targets', {
            'search_for_private_key': search_for_private_key,
            'max_ph_to_search': max_ph_to_search
        })

    def set_reward_targets(self, farmer_target: str = None, pool_target: str = None):
        data = {}
        if farmer_target:
            data['farmer_target'] = farmer_target
        if pool_target:
            data['pool_target'] = pool_target
        return self.client.call('set_reward_targets', data)

    def get_pool_state(self):
        return self.client.call('get_pool_state')

    def set_payout_instructions(self, launcher_id: str, payout_instructions: str):
        return self.client.call('set_payout_instructions', {
            'launcher_id': launcher_id,
            'payout_instructions': payout_instructions
        })

    def get_harvesters(self):
        return self.client.call('get_harvesters')

    def get_harvesters_summary(self):
        return self.client.call('get_harvesters_summary')

    def get_harvester_plots_valid(self, node_id, page=0, page_size=5):
        return self.client.call('get_harvester_plots_valid', {
            'node_id': node_id,
            'page': page,
            'page_size': page_size
        })

    def get_harvester_plots_invalid(self, node_id, page=0, page_size=5):
        return self.client.call('get_harvester_plots_invalid', {
            'node_id': node_id,
            'page': page,
            'page_size': page_size
        })

    def get_harvester_plots_keys_missing(self, node_id, page=0, page_size=5):
        return self.client.call('get_harvester_plots_keys_missing', {
            'node_id': node_id,
            'page': page,
            'page_size': page_size
        })

    def get_harvester_plots_duplicates(self, node_id, page=0, page_size=5):
        return self.client.call('get_harvester_plots_duplicates', {
            'node_id': node_id,
            'page': page,
            'page_size': page_size
        })

    def get_pool_login_link(self, launcher_id: str):
        return self.client.call('get_pool_login_link', {
            'launcher_id': launcher_id
        })

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

    def stop_node(self):
        return self.client.call('stop_node')

    def get_routes(self):
        return self.client.call('get_routes')

    def healthz(self):
        return self.client.call('healthz')


if __name__ == '__main__':
    fc = FarmerClient()

    res = fc.healthz()

    print(res)
