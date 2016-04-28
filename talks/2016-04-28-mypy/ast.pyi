from typing import List, Union, Optional  # noqa


class AST:
    lineno = ...  # type: int
    col_offset = ...  # type: int


# ****************
identifier = str


# ****************
class boolop(AST):
    pass


class And(boolop):
    pass


class Or(boolop):
    pass


# ****************
class operator(AST):
    pass


class Add(operator):
    pass


class Sub(operator):
    pass


class Mult(operator):
    pass


class MatMult(operator):
    pass


class Div(operator):
    pass


class Mod(operator):
    pass


class Pow(operator):
    pass


class LShift(operator):
    pass


class RShift(operator):
    pass


class BitOr(operator):
    pass


class BitXor(operator):
    pass


class BitAnd(operator):
    pass


class FloorDiv(operator):
    pass


# ****************
class unaryop(AST):
    pass


class Invert(unaryop):
    pass


class Not(unaryop):
    pass


class UAdd(unaryop):
    pass


class USub(unaryop):
    pass


# ****************
class expr_context(AST):
    pass


class Load(expr_context):
    pass


class Store(expr_context):
    pass


class Del(expr_context):
    pass


class AugLoad(expr_context):
    pass


class AugStore(expr_context):
    pass


class Param(expr_context):
    pass


# ****************
class slice_(AST):
    pass


class Slice(slice_):
    lower = ...  # type: Optional[expr]
    upper = ...  # type: Optional[expr]
    step = ...  # type: Optional[expr]


class ExtSlice(slice_):
    dims = ...  # type: List[slice]


class Index(slice_):
    value = ...  # type: expr


# ****************
class cmpop(AST):
    pass


class Eq(cmpop):
    pass


class NotEq(cmpop):
    pass


class Lt(cmpop):
    pass


class LtE(cmpop):
    pass


class Gt(cmpop):
    pass


class GtE(cmpop):
    pass


class Is(cmpop):
    pass


class IsNot(cmpop):
    pass


class In(cmpop):
    pass


class NotIn(cmpop):
    pass


# ****************
class expr(AST):
    pass


class BoolOp(expr):
    op = ...  # type: boolop
    values = ...  # type: List[expr]


class BinOp(expr):
    left = ...  # type: expr
    op = ...  # type: operator
    right = ...  # type: expr


class UnaryOp(expr):
    op = ...  # type: unaryop
    operand = ...  # type: expr


class IfExp(expr):
    test = ...  # type: expr
    body = ...  # type: expr
    orelse = ...  # type: expr


class Compare(expr):
    left = ...  # type: expr
    ops = ...  # type: List[cmpop]
    comparators = ...  # type: List[expr]


class Num(expr):
    n = ...  # type: Union[int, float]


class Str(expr):
    s = ...  # type: str


class Bytes(expr):
    s = ...  # type: bytes


class Attribute(expr):
    value = ...  # type: expr
    attr = ...  # type: identifier
    ctx = ...  # type: expr_context


class Subscript(expr):
    value = ...  # type: expr
    slice = ...  # type: slice_
    ctx = ...  # type: expr_context


class Name(expr):
    id = ...  # type: identifier
    ctx = ...  # type: expr_context


# ****************
class Expression(AST):
    body = ...  # type: expr


# ****************
def dump(node: AST,
         annotate_fields: bool = ...,
         include_attributes: bool = ...) -> str: ...


def parse(expr: str, mode: str = ...) -> expr: ...
