"""Custom topology example

Two directly connected switches plus a host for each switch:

   host --- switch --- switch --- host

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""

from mininet.topo import Topo
from mininet.net import Mininet
import mininet.util
from mininet.node import Switch, Controller
from mininet.node import Node,RemoteController
from graph1 import parse,draw_graph
import os
import time
#hosts = []
class MyTopo( Topo ):
#    hosts = []
#    switches = []
    "Simple topology example."
    def createTopology(self):
#	global hosts
	with open("ip2.txt","r") as f:
		lines = f.readlines()
		f2=open("SwitchMapping.txt","a");
    		for line in lines:
			l=line;
			if(l[0] is "s"):
				sName=self.addSwitch(l.rstrip());
				f2.write(sName+","+str(Switch(sName).dpid)+"\n")
			elif(l[0] is "h"):
				self.addHost(l.rstrip());

			elif(l[0] is "l"):
				l=line.split(" ");
				self.addLink(l[1].rstrip(),l[2].rstrip());
		#self.addHosts(int(lines[0]))
		#self.addSwitches(int(lines[1]))
		#self.addLinks(lines[2:])
		print "trial\n";
		print type(self.hosts());
		for i in self.hosts():
			#print self.nodeInfo(i);
			print i
#			print type(i);
			#node = Node(hosts[i])
			#print "Blahhhhh"
			#print node
			#mac = i.MAC() 
			#print "Mac"
			#print mac
		f2.close();
	
    def addSwitches(self,n):
	with open("SwitchMapping.txt","a") as f2:
		for i in range(n):
			sName = self.addSwitch('s'+`i+1`)
			#sDpid = getDpidFromName(sName)
			print "DPID"
			print Switch(sName).dpid
			f2.write(sName+","+str(Switch(sName).dpid)+"\n")
        	f2.close()
        #print "Node iNFO"
	#z=self.nodeInfo("s1")
	#print z
	#print type(z)
	#print "End of node info"
        #print vars(self.g)
	#print type(self.g)
	#print type(self.switches)
	#dipids=self.hosts()
	#print dipids
	#print type(dipids)
	#print "Nodes"
	#print self.nodes()[0]
	#print dipids[0]
	#for s in self.switches:
	#	print s

    def addHosts(self,n):
#	global hosts
	#print hosts	
	for i in range(n):
#		hosts.append(self.addHost('h'+`i+1`))
	        print type(self.addHost('h'+`i+1`))	
		#k=node.defaultIntf();
		
		#print "printing K and Node";
		#print k,node;
		#macOfHost = Node.MAC(node,hosts[i]+'-eth0')
		#mac2 = hostName.MAC()
		#mac = Node.MAC(node,k);
		#mac = node.MAC(self,k)
		#m1 = Node.hostName.MAC()
		#print mac
#	print hosts
    def addLinks(self,links):
#	n = int(links[0])
	for i in range(1,len(links)):
		#print links
		nodes = links[i].rstrip().split(' ');
		#print nodes
		self.addLink(nodes[0],nodes[1].rstrip())
	
    def __init__( self ):
        "Create custom topo."
#	global net;
        # Initialize topology
        Topo.__init__( self )

        # Add hosts and switches
#	net = Mininet(MyTopo);
	self.createTopology();
	#for i in (net.hosts):
	#	print i;
	#print net.switches
        """ leftHost = self.addHost( 'h1' )
        rightHost = self.addHost( 'h2' )
        leftSwitch = self.addSwitch( 's3' )
        rightSwitch = self.addSwitch( 's4' )

        # Add links
        self.addLink( leftHost, leftSwitch )
        self.addLink( leftSwitch, rightSwitch )
        self.addLink( rightSwitch, rightHost )
        """
class bridge(Controller):
	def start(self):
		self.pox='%s/pox/pox.py' % os.environ['HOME'];
		print "blah: "+ '%s/pox/pox.py' % os.environ['HOME'];
		self.cmd(self.pox,'tutorial > o.txt &')
	#def stop(self):
	#	self.cmd('kill %'+self.pox);		
controllers ={'poxbridge':bridge}

def simple():
	t=MyTopo();
	#c=Controller(name="c0",command="python ./pox/pox.py")
	#net=Mininet(t,controller=bridge);
	net=Mininet(topo=t,controller=lambda name:RemoteController(name,ip='127.0.0.1'))
	#net.addController(name="c0",port=6633);
	#mininet.node.RemoteController(port=6633)
	net.start();
	
	#print net.host;
	f=open("MacHost.txt","w");
	for i in net.hosts:
		print "i= ";
		print i;
		print Node.MAC(i);
		f.write(str(i)+" "+str(Node.MAC(i))+"\n");
	f.close();
	z=0
	f=open("/home/saumya/pox/output.txt","w")
	f.close()
	for i in net.hosts:
		for j in net.hosts:
			if(i!=j):
				time.sleep(10);
				net.ping([i,j])
				z=z+1;
				parse("/home/saumya/pox/output.txt");
				draw_graph();
				
				
	#net.ping([,'h4']);
#	net.pingAll()
	#net.stop();
def run():
	simple();
topos = { 'dup': ( lambda: MyTopo() ) }
