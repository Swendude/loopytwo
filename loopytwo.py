"""
Loopy 2 - recreation of loopy for python
"""

class BasicLoopyDiagram:
    nodes = {}
    edges = {}
    events = []
    steps = 0

    def addNode(self, nodeName, initial=0):
        self.nodes[nodeName] = initial # nodes are just values
    
    def addEdge(self, fromNode, toNode, positive = True):
        if fromNode in self.edges:
            self.edges[fromNode].append((toNode, positive)) # an edge is directed (from -> to) so we just keep a list of connected nodes for each node
        else:
            self.edges[fromNode] = [(toNode, positive)]

    def addEvent(self, nodeName, positive = True):
        self.events.append((nodeName, positive)) # an event can either be triggered manually or by using the step function
    
    def step(self):
        if len(self.events) != 0: # If there are events
            current_event = self.events.pop() # Get the oldest event
            self.handle_event(current_event)
        self.steps += 1
        return ((self.nodes))

    def handle_event(self, current_event):
        event_node, event_type = current_event
        if event_type == True: # if the event was a positive chance
            self.nodes[event_node] += 1 # the node the event was placed on increases in value
        else:
            self.nodes[event_node] -= 1 # the node the event was placed on decreases in value
        if event_node in self.edges: # if the node has edges
            for connected_node, connection_type in self.edges[event_node]:
                if connection_type == True: # if the relation is positive
                    self.addEvent(connected_node, event_type) # keep the event the same
                else: # if the relation is not positive (== negative)
                    self.addEvent(connected_node, not(event_type)) #flip the event type

    def print(self):
        print("------------")
        print("MODEL STATUS:")
        print("------------")
        print()

        for node in self.nodes:
            print(node + "\t\t -> " + str(self.nodes[node]))
        print()    