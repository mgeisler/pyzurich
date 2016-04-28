from typing import Dict, Any

import ast
import operator


class Evaluator:
    # Unary operators
    unaryop = {
        ast.Invert: operator.invert,
        ast.Not: operator.not_,
        ast.USub: operator.neg,
        ast.UAdd: operator.pos,
    }

    # Binary operators
    binop = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Mod: operator.mod,
    }

    # Boolean operators
    boolop = {
        ast.And: all,
        ast.Or: any,
    }

    # Comparison operators
    cmpop = {
        ast.Lt: operator.lt,
        ast.LtE: operator.le,
        ast.Eq: operator.eq,
        ast.NotEq: operator.ne,
        ast.GtE: operator.ge,
        ast.Gt: operator.gt,
    }

    def __init__(self, env: Dict[str, float]) -> None:
        self.env = env

    def eval(self, expr: str) -> Any:
        self.expr = expr
        node = ast.parse(expr, mode='eval')
        if isinstance(node, ast.Expression):
            node = node.body
        return self._eval(node)

    def _eval(self, node: ast.expr) -> Any:
        if isinstance(node, ast.Num):
            # Expressions like '123'
            return node.n

        if isinstance(node, ast.Name):
            return self.env[node.id]

        if isinstance(node, ast.UnaryOp):
            # Expressions like '+x' and '-y'
            return self.unaryop[type(node.op)](self._eval(node.operand))

        if isinstance(node, ast.BinOp):
            # Expressions like 'x + y'
            return self.binop[type(node.op)](self._eval(node.left),
                                             self._eval(node.right))

        if isinstance(node, ast.BoolOp):
            # Expressions like 'x and y or z'
            return self.boolop[type(node.op)](map(self._eval, node.values))

        if isinstance(node, ast.Compare):
            # Expressions like 'x > 10' but also 'x < y <= z' and similar.
            left = self._eval(node.left)
            for op, right in zip(node.ops, map(self._eval, node.comparators)):
                if not self.cmpop[type(op)](left, right):
                    return False
                # The right operand becomes the next left operand
                left = right
            return True

        if isinstance(node, ast.IfExp):
            # Expressions like 'x if y else z'
            if self._eval(node.test):
                return self._eval(node.body)
            else:
                return self._eval(node.orelse)

        raise ValueError('Unrecognized expression at pos %d: %s'
                         % (node.col_offset, self.expr[node.col_offset:]))


def evaluate(expr: str, **env: float) -> float:
    """Evaluate an expression given an environment.

    The expression must be in Python syntax and can contain variables
    and simple arithmetic operators:

    >>> evaluate('(2 + 3) * 4 - 5')
    15
    """
    evaluator = Evaluator(env)
    return evaluator.eval(expr)
