import Node

class MCTS:
    def __init__(self,root_node:Node.Node,search_const,no_iter) -> None:
        self.root = root_node
        self.c = search_const
        self.no_iter = no_iter
    
    def generate_distribution(self):
        for i in range(self.no_iter):
            selected_node = self.root.select(self.c)
            if selected_node.is_leaf_node() and selected_node.is_fully_expanded():
                continue 
            selected_node.expand()
            selected_node.children[-1].simulate()
        scores =[]
        for node in self.root.children:
            scores.append(node.wins/self.root.visits*100)
        
        return (self.root.children_moves,scores)

