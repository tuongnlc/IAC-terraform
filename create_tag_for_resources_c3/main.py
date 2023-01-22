import json

"""
    We create tag then reference to other class (Factory Class)
    -> propotype pattern
"""


class StandardTags():
    def __init__(self):
        self.resource = {
            'customer': 'my-company',
            'automated': True,
            'cost_center': 123456,
            'business_unit': 'ecommerce'
        }


class ServerFactory:
    def __init__(self, name, network, zone='asia-southeast1-a', tags={}):
        self.name = name
        self.network = network
        self.zone = zone
        self.tags = tags #define tags
        self.resource = self._build()

    def _build(self):
        return {
            'resource': [
                {
                    'google_compute_instance': [
                        {
                            self.name: [
                                {
                                    'allow_stopping_for_update': True,
                                    'boot_disk': [
                                        {
                                            'initialize_params': [
                                                {
                                                    'image': 'ubuntu-1804-lts'
                                                }
                                            ]
                                        }
                                    ],
                                    'machine_type': 'e2-micro',
                                    'name': self.name,
                                    'network_interface': [
                                        {
                                            'network': self.network
                                        }
                                    ],
                                    'zone': self.zone,
                                    'labels': self.tags
                                }
                            ]
                        }
                    ]
                }
            ]
        }


if __name__ == "__main__":
    config = ServerFactory(
        name='test-database-server', network='default',
        tags=StandardTags().resource)

    with open('main.tf.json', 'w') as outfile:
        json.dump(config.resource, outfile,
                  sort_keys=True, indent=4)
