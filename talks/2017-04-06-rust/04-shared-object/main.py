import ctypes

lib = ctypes.cdll.LoadLibrary('target/debug/libshared_object.so')
buf = b"foo bar baz"

print(lib.max_byte(buf, len(buf)))
