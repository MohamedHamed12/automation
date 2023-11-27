import ast
import astor

# Define a simple Python code snippet
code = "def fun(a, b):\n    return a + b"

# Parse the code and create an AST
tree = ast.parse(code)

class FunctionNameVisitor(ast.NodeVisitor):
    def visit_FunctionDef(self, node):
        print(f"Found function: {node.name}")

visitor = FunctionNameVisitor()
visitor.visit(tree)

# Define a simple AST transformer to replace addition with multiplication
class MultiplyTransformer(ast.NodeTransformer):
    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            return ast.BinOp(left=node.left, op=ast.Mult(), right=node.right)
        return node

# Use the transformer to modify the AST
transformer = MultiplyTransformer()
new_tree = transformer.visit(tree)

# Print the modified AST
print(ast.dump(new_tree))

print(astor.to_source(new_tree))