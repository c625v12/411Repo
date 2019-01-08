import zlib, sys, lzma, json, bz2, time

class Compress:

    def zlib_compress(self, data):
        return zlib.compress(data)

    def lzma_compress(self, data):
        lzc = lzma.LZMACompressor(check=lzma.CHECK_CRC32)
        return lzc.compress(data) + lzc.flush()

    def bz2_compress(self, data):
        return bz2.compress(data)

class Decompress:

    def zlib_decompress(self, data):
        return zlib.decompress(data)

    def lzma_decompress(self, data):
        lzcd = lzma.LZMADecompressor()
        return lzcd.decompress(data=payloadcompress)

    def bz2_decompress(self, data):
        return bz2.decompress(data)


if __name__ == '__main__':
    c = Compress()
    d = Decompress()

    print("Opening Json file to compress and decompress!!")
    time.sleep(2)
    payload = open('jsonWebsite.json', 'rb')
    data = payload.read()
    print("Json file opened and read!")
    time.sleep(1)
    print("Getting data")
    time.sleep(2)
    print(data)
    print("Time to compress your feelings!")
    print("Compressing :(")
    zlibcompressed = c.zlib_compress(data)
    time.sleep(1)
    print("Compressed :'(")
    print(zlibcompressed)
    checksum = zlib.crc32(data)
    time.sleep(1)
    print("Time to decompress those bad feelings!")
    time.sleep(1)
    print(":)")
    print("Decompressing")
    zlibdecompressed = d.zlib_decompress(zlibcompressed)
    checksumGen = zlib.crc32(zlibdecompressed)
    if checksum == checksumGen:
        print("Checksum matches")

    else:
        print("Checksum mismatch")
    print("You have been decompressed!")
    print(zlibdecompressed)
    time.sleep(2)
    print("Oh no! Here comes lady lzma to ruin your life!!!!")
    print("Compressing :(")
    time.sleep(1)
    lzmacompressed = c.lzma_compress(data)
    print("She has compressed your feelings and here they are!")
    time.sleep(1)
    print(lzmacompressed)
    time.sleep(1)
    print("After life hits you, you finally find a way to decompress those feelings! LET THEM OUT")
    time.sleep(1)
    d.lzma_decompress(lzmacompressed)

    #c.lzma()



#try:
 #           print("Reading the file Payload to compress")
   #         payload = open('payloadJSON.json', 'rb')
  #          data = payload.read()
    #        print("Compressing")

     #       lzc = lzma.LZMACompressor(check=lzma.CHECK_CRC32)
      #      payloadcompress = lzc.compress(data) + lzc.flush()
       #     print(payloadcompress)
#
 #           lzcd = lzma.LZMADecompressor()
  #          payloaddecompress  = lzcd.decompress(data=payloadcompress)
   #         prin lzcd = lzma.LZMADecompressor()
  #          payloaddecompress  = lzcd.decompress(data=payloadcompress)
   #         print(payloaddecompress)
    #        if data == payloaddecompress:
     #           print("Checksum matches")

      #      else:
       #          print("Checksum mismatch")
        #except Exception as e:
         #   print(e)
   # c.bz2()
#try:
 #           print("Reading the file Payload to compress")
  #          payload = open('payloadJSON.json', 'rb')
   #         data = payload.read()
    #        print("Compressing")
     #       payloadComp = zlib.compress(data)
      ##      print(payloadComp)
        #    checksum = zlib.crc32(data)
         #   print(checksum)
          #  payloadComp = zlib.decompress(payloadComp)
           # print(payloadComp)
#            checksumGen = zlib.crc32(payloadComp)
 #           print(checksumGen)
  #          if checksum == checksumGen:
   #             print("Checksum matches")
#
 #           else:
  #               print("Checksum mismatch")
   #     except Exception as e:
    #        print(e)
#def bz2(self):
 #      try:
  #          print("Reading in file Payload to compress")
   #         payload = open('payloadJSON.json', 'rb')
    #        data = payload.read()
     #       print("Compressing")
      #      compressed = bz2.compress(data)
       ##     print(compressed)
         #   decompressed = bz2.decompress(compressed)
     #       print(decompressed)
      #      if data == decompressed:
       #         print("Checksum matches")

        #    else:
         #        print("Checksum mismatch")
      # except Exception as e:
       #     print(e)
