import socket
import uuid

class myclass(object):

    def get_pc_name(self):
        pcname = socket.getfqdn(socket.gethostname( ))
        self._pcname=pcname
        return pcname

    def get_pc_pcip(self):
        if(self._pcname==None):self._pcname=self.get_pc_name()
        pcip =socket.gethostbyname(self._pcname)
        return pcip

    def get_mac_address(self):
        mac=uuid.UUID(int = uuid.getnode()).hex[-12:]
        return ":".join([mac[e:e+2] for e in range(0,11,2)])
    def __str__(self):
        print("\n".join([self.get_pc_name(),self.get_pc_pcip(),self.get_mac_address()]))
    

