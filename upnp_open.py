#!/usr/bin/env python


#################################################################
# UPnP Port Opener v 1.0a
# Written By: Anthony Papillion <papillion@gmail.com>
# Released under the BSD License
#
# PURPOSE:
# UPnP Opener is a simple Python script that allows you to 
# easily request the UPnP router on your local network to 
# open and forward an external port to an internal machine.
# It requires the miniupnpc module which is easiest to install
# and run on Linux but can be compiled for Microsoft Windows 
# if needed.
###################################################################

from __future__ import print_function
import miniupnpc
import sys

class UPnP_Opener(object):

    def show_help(self):
        print("USAGE: upnp_open <remote_port> <destination_host> <destination_port>")
        sys.exit(1)
    
    def make_idg_request(self, remote_port, dest_host, dest_port):
        self.src_port = int(remote_port)
        self.dest_port =int(dest_port)
        self.dest_host = dest_host

        print("Attempting to forward remote port", self.src_port, "to port", self.dest_port, "on host", self.dest_host)
        upnp = miniupnpc.UPnP()
        upnp.discoverdelay = 10
        result = upnp.discover()

        if(result == 0):
            print("Could not locate any UPnP enabled routers on the network. Could not forward the requested port.")
            sys.exit(1)
        else:
            upnp.selectigd()
            upnp.addportmapping(self.src_port, 'TCP', self.dest_host, self.dest_port, 'Auto', '')
            
if __name__ == "__main__":
    UPnPOpener = UPnP_Opener()

    if len(sys.argv) <> 4:
        UPnPOpener.show_help()
    else:
        UPnPOpener.make_idg_request(sys.argv[1], sys.argv[2], sys.argv[3])
