from loopytwo import BasicLoopyDiagram

# create a basic diagram
my_diagram = BasicLoopyDiagram()
# create a node named 'Foxes' with initial value of 0
my_diagram.addNode("Foxes") 
# create a node named 'Rabbits' with initial value of 5
my_diagram.addNode("Rabbits", initial=5) 
# create an edge from 'Rabbits' to 'Foxes' with a positive relationship
my_diagram.addEdge('Rabbits', 'Foxes') 
# create an edge from 'Rabbits' to 'Foxes' with a positive relationship
my_diagram.addEdge('Foxes', 'Rabbits', positive=False)
# now add some events to start the run
my_diagram.addEvent('Rabbits', positive=True) # we click the up button on rabbits
my_diagram.addEvent('Rabbits', positive=True) # we click the up button on rabbits

# the model is now ready to run. We need a loop tough:

stopped = False

while not stopped:
    print("Current model:")
    print("--------------")
    print("Nodes:")
    print(my_diagram.nodes)
    print("Edges:")
    print(my_diagram.edges)
    print("--------------")
    print("")
    print("How many loops to run? (input 'q' to quit, enter to submit)")
    user_input = input()
    if user_input == 'q':
        print("Stopping")
        stopped = True
    else:
        amount_loops = int(user_input)
        for i in range(amount_loops):
            print("step " + str(my_diagram.steps))
            my_diagram.step()
            my_diagram.print()
            

