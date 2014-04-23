from pox.core import core
import pox.openflow.libopenflow_01 as of
import re
from pox.lib.util import dpidToStr
import tool 
from graph1 import parse,draw_graph 
import time
log = core.getLogger()

class Tutorial (object):
  def __init__ (self, connection):
    self.connection = connection
    connection.addListeners(self)
    # Use this table to keep track of which ethernet address is on
    # which switch port (keys are MACs, values are ports).
    self.mac_to_port = {} 
    self.matrix={} # This will keep track of the traffic matrix. 
                   # matrix[i][j]=number of times a packet from i went to j
    """print "tutorial vars"
    print vars(self)
    print "connection vars"
    print vars(self.connection)
    """	
      
 
  def send_packet (self, buffer_id, raw_data, out_port, in_port):
    #Sends a packet out of the specified switch port.
    msg = of.ofp_packet_out()
    msg.in_port = in_port
    msg.data = raw_data
    # Add an action to send to the specified port
    action = of.ofp_action_output(port = out_port)
    msg.actions.append(action)
    # Send message to switch
    self.connection.send(msg)


  def act_like_hub (self, packet, packet_in):
    #flood packet on all ports
    self.send_packet(packet_in.buffer_id, packet_in.data,
                     of.OFPP_FLOOD, packet_in.in_port)


  def act_like_switch (self, packet, packet_in):
    """
    Implement switch-like behavior.
    """
    """ print "packet vars"
    print vars(packet)
    print "packet_in vars"
    print vars(packet_in)
    print "self"	
    print vars(self) 
    """
    # Learn the port for the source MAC
    self.mac_to_port[packet.src]=packet_in.in_port
    #print "packet_in " 
    #print packet_in.in_port
    if(self.matrix.get((packet.src,packet.dst))==None):
            self.matrix[(packet.src,packet.dst)]=0
    self.matrix[(packet.src,packet.dst)]+=1
    if self.mac_to_port.get(packet.dst)!=None:
      #send this packet
      self.send_packet(packet_in.buffer_id, packet_in.data,self.mac_to_port[packet.dst], packet_in.in_port)
      #create a flow modification message
      msg = of.ofp_flow_mod()
      #set the fields to match from the incoming packet
      msg.match = of.ofp_match.from_packet(packet)

      #print "SENDING  TO PORT " + str(self.mac_to_port[packet.dst])
      # send the rule to the switch so that it does not query the controller again.
      msg.actions.append(of.ofp_action_output(port=self.mac_to_port[packet.dst]))
      # push the rule
      self.connection.send(msg)
      print "DPID. is it a Jaaakpot"
      dpid=dpidToStr(self.connection.dpid)
      l=[]
      l=dpid.split('-');
      final_dpid=''
      for i in l:
	final_dpid=final_dpid+i
      final_dpid="0000"+final_dpid
      print "blah";
      print final_dpid;
     # print dpidToStr(self.connection.dpid) 
      my_dict = {}
      with open("/home/saumya/Downloads/SwitchMapping.txt","r") as f:
	for line in f:
		items = line.split(',')
		key , value = items[1],items[0]
		key=key.rstrip();
		my_dict[key]=value
      print my_dict
      mdict2 = {}
      with open("/home/saumya/Downloads/MacHost.txt","r") as f:
	for line in f:
		print "l",line;
		items = line.split(' ')
		key , value = items[1],items[0]
		key=key.rstrip();
		mdict2[key]=value
      print "my";
      print mdict2;
      #tool.addRuleToGUI(dpidToStr(self.connection.dpid),self.mac_to_port[packet.dst])
      print "packet",packet.dst;
      tool.addRuleToGUI(my_dict.get(final_dpid),self.mac_to_port[packet.dst],mdict2.get(str(packet.dst)));
      #parse("asdjhaksh");
      #draw_graph()
      #time.sleep(5); 
      #print "self connection vars"
      #print vars(self.connection)
      #print str(self.connection)
      #print "msg match vars"
      #print vars(msg.match)
    else:
      # Flood this packet out as we don't know about this node.
      self.send_packet(packet_in.buffer_id, packet_in.data,
                       of.OFPP_FLOOD, packet_in.in_port)

  def _handle_PacketIn (self, event):
    """
    Handles packet in messages from the switch.
    """
    packet = event.parsed # This is the parsed packet data.
    #print "handle pkt self"	
    #print vars(self)
    
    if not packet.parsed:
      log.warning("Ignoring incomplete packet")
      return
    packet_in = event.ofp # The actual ofp_packet_in message.
    #print "KKKKKKKKKKK Switch name from internal port"
    #print event.connection.ports[of.OFPP_LOCAL].name
    #self.act_like_hub(packet, packet_in)
    self.act_like_switch(packet, packet_in)

def launch ():
  """
  Starts the component
  """
  def start_switch (event):
    log.debug("Controlling %s" % (event.connection,))
    print "Witch Switch "
    print dpidToStr(event.dpid)
    print dpidToStr(event.connection.dpid)
    Tutorial(event.connection)
    #print "Main vars"
    #print vars(self)

  core.openflow.addListenerByName("ConnectionUp", start_switch)
