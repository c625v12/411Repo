import zlib 
import sys
import lzma
import json
import bz2
import time
import datetime


class Compress:

    
    def zlib_compress(self, data):
        """
        Build zlib compression

        :param data: json file to be compressed
        :rtype: object
        """

        return zlib.compress(data)

    def lzma_compress(self, data):
        """
        Build lzma compression

        :param data: json file to be compressed
        :rtype: object
        """

        lzc = lzma.LZMACompressor(check=lzma.CHECK_CRC32)
        return lzc.compress(data) + lzc.flush()

    def bz2_compress(self, data):
        """
        Build bz2 compression

        :param data: json file to be compressed
        :rtype: object
        """

        return bz2.compress(data)


class Decompress:



    def zlib_decompress(self, data):
        """
        Build zlib decompression

        :param data: json file to be compressed
        :rtype: object
        """

        return zlib.decompress(data)

    def lzma_decompress(self, data):
        """
        Build lzma decompression

        :param data: json file to be compressed
        :rtype: object
        """

        lzcd = lzma.LZMADecompressor()
        return lzcd.decompress(data)

    def bz2_decompress(self, data):
        """
        Build bz2 decompression

        :param data: json file to be compressed
        :rtype: object
        """

        return bz2.decompress(data)


class Main:

    """
    Main class to run the program
    """

    c = Compress()
    d = Decompress()
    print("Opening Json file to compress and decompress!!")
    time.sleep(2)
    payload = open('json.json', 'rb')
    data = payload.read()
    print("Json file opened and read!")
    time.sleep(1)
    print("Getting data")
    time.sleep(2)
#    print(data)


    def zlib_compress_decompress(self):

        """
        Perform zlib compression/decompression

        :rtype: none
        """

        try:
            print("=============================================")
            print("ZLIB COMPRESSION AND DECOMPRESSION STARTING")
            time.sleep(1)
            print("--------COMPRESSION--------")
            print("Time of zlib compression", datetime.datetime.now())
            zlibcompressed = c.zlib_compress(self.data)
            print("The size of compressed object is:", sys.getsizeof(zlibcompressed))
            time.sleep(1)
            print("COMPRESSED OBJECT")
            print(zlibcompressed)
            checksum = zlib.crc32(self.data)
            time.sleep(1)
            print("--------DECOMPRESSION--------")
            print("Time of zlib decompression", datetime.datetime.now())
            zlibdecompressed = d.zlib_decompress(zlibcompressed)
            print("The size of decompressed object is", sys.getsizeof(zlibdecompressed))
            checksumGen = zlib.crc32(zlibdecompressed)
            print("DECOMPRESSED OBJECT")
            print(zlibdecompressed)
            if checksum == checksumGen:
                print("Checksum matches")

            else:
                print("Checksum mismatch")
        except Exception as e: 
            print ("Error %s" % e.args[0])

    def lzma_compress_decompress(self):
        """
        Perform lzma compression/decompression

        :rtype: none
        """
        try:
            print("=============================================")
            print("LZMA COMPRESSION AND DECOMPRESSION STARTING")
            print("Time of lzma compression", datetime.datetime.now())
            print("--------COMPRESSION--------")
            time.sleep(1)
            lzmacompressed = c.lzma_compress(self.data)
            print("COMPRESSED OBJECT")
            time.sleep(1)
            print(lzmacompressed)
            print("The size of compressed object is:", sys.getsizeof(lzmacompressed))
            time.sleep(1)
            print("--------DECOMPRESSION--------")
            print("Time of lzma decompression", datetime.datetime.now())
            lzmadecompressed = d.lzma_decompress(lzmacompressed)
            print("The size of decompressed object is:", sys.getsizeof(lzmadecompressed))
            print("DECOMPRESSED OBJECT")
            print(lzmadecompressed)
            if self.data == d.lzma_decompress(lzmacompressed):
                print("Checksum matches")

            else:
                print("Checksum mismatch")
        except Exception as e:
            print("Error %s" % e.args[0])
    def bz2_compress_decompress(self):
        """
        Perform bz2 compression/decompression

        :rtype: none
        """
        try:
            
            print("=============================================")
            print("BZ2 COMPRESSION AND DECOMPRESSION STARTING")
            print("Time of bz2 compression", datetime.datetime.now())
            print("--------COMPRESSION--------")
            time.sleep(1)
            bz2compressed = c.bz2_compress(self.data)
            print("COMPRESSED OBJECT")
            print(bz2compressed)
            print("The size of compressed object is:", sys.getsizeof(bz2compressed))
            time.sleep(1)
            print("--------DECOMPRESSION--------")
            time.sleep(1)
            print("Time of bz2 decompression", datetime.datetime.now())

            bz2decompressed = d.bz2_decompress(bz2compressed)
            print("The size of compressed object is:", sys.getsizeof(bz2decompressed))
            print("DECOMPRESSED OBJECT")
            print(bz2decompressed)
            if self.data == bz2decompressed:
                print("Checksum matches")

            else:
                print("Checksum mismatch")
        except Exception as e:
            print ("Error %s" % e.args[0])


if __name__ == '__main__':
    c = Compress()
    d = Decompress()
    m = Main()
    m.zlib_compress_decompress()
    m.lzma_compress_decompress()
    m.bz2_compress_decompress()
