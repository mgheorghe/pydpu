import grpc
import importlib


class Dpu():
    def __init__(self, address, version='v1'):
        self._version = version
        self._address = address
        self._api = importlib.import_module(f'.proto.{self._version}')
        self._dpu = grpc.insecure_channel(self._address)
        return self

    @property    
    def api(self):
        # type: () -> types.ModuleType
        '''
        Returns
        -------
        - types.ModuleType: returns the api module coresponding the configured version.
        '''
        return self._api
    
    @api.setter
    def api(self, version):
        # type: (str) -> None
        self._version = version
        self._api = importlib.import_module(f'.proto.{self._version}')

    @property
    def ipsec(self):
        # type: () -> types.ModuleType
        '''
        Returns
        -------
        - types.ModuleType: returns the api module coresponding the configured version.
        '''
        self._ipsec = self.api.ipsec_pb2_grpc.IPsecStub(self.dpu)
        return self._ipsec

    @property
    def storage(self):
        self._storage = self.api.frontend_nvme_pcie_pb2_grpc.FrontendNvmeServiceStub(self.dpu)
        return self._storage

    @property
    def inventory(self):
        self._inventory = 'implement me'
        return self._inventory
    