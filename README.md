Software-defined networking (SDN) is an approach to networking in which control is decoupled from hardware and given to a software application called a controller. It allows network administrators to manage network services through abstraction of lower level functionality. This is done by isolating the system that makes decisions about where traffic is sent (the control plane) from the underlying systems that forwards traffic to the selected destination (the data plane).

Description : I provided a graphical interface that uses mininet to create a virtual network. POX is a python based openflow controller and I use this controller to populate the flow-tables of virtual switches. And finally the controller learnt network is shown graphically to the user. 

Motivation : 

-No existing GUI tool to create a network with custom topology
-No tool to save the custom topology and recreate the networkusing the saved file.

Approach And Tools

-I built a tool in python that enables the user to create custom topology using drag and drop feature.
-The tool, built on top of Miniedit, can be used to save the user defined topology in a file. This file can be used later to edit the topology.
-I use Mininet to simulate the user specified network.
-I use POX as controller, that learns the network and populates the flow-tables at all the switches.
-I repesent this newly learnt control flow using NetworkX.
-The packet traffic between hosts can be seen using wireshark.

Features

-Ability to drag and drop switchs/hosts and create virtual topology.
-Ability to use custom controller like POX.
-Provides mininet CLI.
-Ability to save the custom topology in a file and create topology again using this file.
-Visualize the network learned by controller using NetworkX.

Applications:

-Can be used by network administrator to graphically create and manage network topology
-Useful to visualize the exiting network.
