from mininet.node import Controller, OVSKernelAP
from mininet.log import setLogLevel, info
from mininet.wifi.net import Mininet_wifi
from mininet.wifi.link import wmediumd, mesh
from mininet.wifi.propagationModels import propagationModel

def topology():
    net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP)
    
    info("*** Setting propagation model\n")
    net.setPropagationModel(model="logDistance", exp=3)

    info("*** Creating nodes\n")
    ap1 = net.addAccessPoint("ap1", ssid="ssid1", mode="g", channel="1", position="10,20,0")
    ap2 = net.addAccessPoint("ap2", ssid="ssid2", mode="g", channel="6", position="30,20,0")
    sta1 = net.addStation("sta1", position="15,25,0")
    sta2 = net.addStation("sta2", position="35,25,0")
    
    info("*** Configuring wifi nodes\n")
    net.configureWifiNodes()

    info("*** Starting network\n")
    net.start()
    
    info("*** Running simulation\n")
    # Simulate a network disruption in access point 1
    ap1.cmd("ifconfig ap1 down")
    info("*** AP1 is down. STA1 reconnecting to AP2...\n")
    sta1.cmd("iw dev sta1-wlan0 connect ssid2")

    # Add additional simulation code for dynamic reconfiguration here
    
    info("*** Stopping network\n")
    net.stop()

if __name__ == "__main__":
    setLogLevel("info")
    topology()
