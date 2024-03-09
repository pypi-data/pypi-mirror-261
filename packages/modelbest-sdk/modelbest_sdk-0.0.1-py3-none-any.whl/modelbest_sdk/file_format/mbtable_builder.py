import ctypes
import os

from modelbest_sdk.file_format.mbtable import ByteArray

lib_path = os.path.normpath(os.path.join(os.path.dirname(__file__), 'lib', 'libsstable_sdk_shared.so'))
lib = ctypes.CDLL(lib_path)

lib.CreateSSTableBuilder.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
lib.CreateSSTableBuilder.restype = ctypes.c_void_p

lib.SetKV.argtypes = [ctypes.c_void_p, ByteArray, ByteArray]
lib.SetKV.restype = None

lib.SetMetaData.argtypes = [ctypes.c_void_p, ctypes.c_char_p, ctypes.c_char_p]
lib.SetMetaData.restype = None

lib.BuildSSTable.argtypes = [ctypes.c_void_p]
lib.BuildSSTable.restype = None

def create_byte_array(data):
    return ByteArray(ctypes.cast(ctypes.c_char_p(data), ctypes.POINTER(ctypes.c_char)), len(data))

class MbTableBuilder:
    def __init__(self, path: str, codec: str = 'kZlib'):
        """
        Initializes an instance of the class, setting up the underlying MbTable builder with the specified path and compression codec.

        The `codec` parameter specifies the compression method to be used for the MbTable. It must be a string that matches one of the predefined compression codec names. The available codecs are as follows:
        - 'kLzo': LZO compression.
        - 'kZlib': zlib compression.
        - 'kUnCompress': No compression.
        - 'kGzip': Gzip compression.
        - 'kSnappy': Snappy compression.
        - 'kUnknown': Represents an unknown or unsupported compression codec. It's recommended to use one of the supported codecs for compatibility.

        Args:
            path (str): The file system path where the MbTable will be created.
            codec (str, optional): The name of the compression codec to use. Defaults to 'kZlib'.

        Note:
            The path and codec arguments are encoded in UTF-8 before being passed to the underlying `CreateSSTableBuilder` function of the `lib` library.
        """
        self.builder = lib.CreateSSTableBuilder(path.encode('utf-8'), codec.encode('utf-8'))

    def add(self, key, value):
        if isinstance(key, str):
            key = key.encode('utf-8')
        if isinstance(value, str):
            value = value.encode('utf-8')
        key_ba = create_byte_array(key)
        value_ba = create_byte_array(value)
        lib.SetKV(self.builder, key_ba, value_ba)

    def add_metadata(self, key: str, value: str):
        lib.SetMetaData(self.builder, key.encode('utf-8'), value.encode('utf-8'))    

    def flush(self):
        lib.BuildSSTable(self.builder)

if __name__ == '__main__':
    builder = MbTableBuilder('test/data/test.mbt', 'kLzo')
    builder.add('key1', '{"name": "Alice", "age": 25}')
    builder.add('key2', 'value2')
    builder.add('key3', b'value3')
    builder.add_metadata('meta1', 'value1')
    builder.add_metadata('meta2', 'value2')
    builder.flush()

