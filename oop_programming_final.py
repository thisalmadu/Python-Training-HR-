# program is not complete !!! => Portion 2#

#In this exercise, we'll create a few classes to simulate a server that's taking connections
#from the outside and then a load balancer that ensures that there are enough servers to serve
#those connections. To represent the servers that are taking care of the connections,
#we'll use a Server class. Each connection is represented by an id, that could,
#for example, be the IP address of the computer connecting to the server.
#For our simulation, each connection creates a random amount of load in the server, between 1 and 10.

#Begin Portion 1#
import random

class Server:
    def __init__(self):
        """Creates a new server instance, with no active connections."""
        self.connections = {}

    def add_connection(self, connection_id):
        """Adds a new connection to this server."""
        connection_load = random.random()*10+1
        # Add the connection to the dictionary with the calculated load
        self.connections[connection_id] = connection_load

    def close_connection(self, connection_id):
        """Closes a connection on this server."""
        # Remove the connection from the dictionary
        del self.connections[connection_id]

    def load(self):
        """Calculates the current load for all connections."""
        total = 0
        # Add up the load for each of the connections
        for load in self.connections.values():
            total += load
        return total

    def __str__(self):
        """Returns a string with the current load of the server"""
        return "{:.2f}%".format(self.load())

#End Portion 1#

#Now run the following cell to create a Server instance and add a connection to it, then check the load:
server = Server()
server.add_connection("192.168.1.1")

print(server.load())

# You have successfully coded the close_connection method if the cell above prints 0.
server.close_connection("192.168.1.1")
print(server.load())

# Alright, we now have a basic implementation of the server class. Let's look at the basic
# LoadBalancing class. This class will start with only one server available.
#When a connection gets added, it will randomly select a server to serve that connection,
#and then pass on the connection to the server. The LoadBalancing class also needs to keep
#track of the ongoing connections to be able to close them. This is the basic structure:

#Begin Portion 2#
class LoadBalancing:
    def __init__(self):
        """Initialize the load balancing system with one server"""
        self.connections = {}
        self.servers = [Server()]

    def add_connection(self, connection_id):
        """Randomly selects a server and adds a connection to it."""
        server = random.choice(self.servers)
        # Add the connection to the dictionary with the selected server
        self.connections[connection_id] = server
        # Add the connection to the server
        self.servers


    def close_connection(self, connection_id):
        """Closes the connection on the the server corresponding to connection_id."""
        # Find out the right server
        # Close the connection on the server
        # Remove the connection from the load balancer

    def avg_load(self):
        """Calculates the average load of all servers"""
        # Sum the load of each server and divide by the amount of servers
        return 0

    def ensure_availability(self):
        """If the average load is higher than 50, spin up a new server"""
        pass

    def __str__(self):
        """Returns a string with the load for each server."""
        loads = [str(server) for server in self.servers]
        return "[{}]".format(",".join(loads))
#End Portion 2#

# As with the Server class, this class is currently incomplete. You need to fill in the gaps
#to make it work correctly. For example, this snippet should create a connection
#in the load balancer, assign it to a running server and then the load should be more than zero:
l = LoadBalancing()
l.add_connection("fdca:83d2::f20d")
print(l.avg_load())

#After running the above code, the output is 0. Fill in the missing parts for the
#add_connection and avg_load methods of the LoadBalancing class to make this print
#the right load. Be sure that the load balancer now has an average load more than 0 before proceeding.
# What if we add a new server?
l.servers.append(Server())
print(l.avg_load())

# Closing connections
l.close_connection("fdca:83d2::f20d")
print(l.avg_load())

#Before, we added a server manually. But we want this to happen automatically when
#the average load is more than 50%. To make this possible, fill in the missing code for
#the ensure_availability method and call it from the add_connection method after a
#connection has been added. You can test it with the following code:
for connection in range(20):
    l.add_connection(connection)
print(l)

# The code above adds 20 new connections and then prints the loads for each server
#in the load balancer. If you coded correctly, new servers should have been added
#automatically to ensure that the average load of all servers is not more than 50%.
#Run the following code to verify that the average load of the load balancer is not more than 50%.
print(l.avg_load())
