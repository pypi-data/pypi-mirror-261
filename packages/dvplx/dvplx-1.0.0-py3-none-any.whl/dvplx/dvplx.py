import os
import sys
import time
import lz4.block
import zlib
import argparse

# ANSI escape codes for text coloring
class Color:
    RED = '\033[31m'
    GREEN = '\033[32m'
    BLUE = '\033[34m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'

# Constants related to DVPL format
DVPL_FOOTER_SIZE = 20
DVPL_TYPE_NONE = 0
DVPL_TYPE_LZ4 = 2
DVPL_FOOTER = b"DVPL"

# ANSI escape codes for text coloring
class Meta:
    NAME = 'DVPLX'
    VERSION = '1.0.0'
    DATE = '12/03/2024'
    DEV = 'RifsxD'
    REPO = 'https://github.com/rifsxd/dvplx'
    WEB = 'https://rxd-mods.xyz'
    INFO = 'A CLI Tool Coded In Python To Convert WoTB ( Dava ) SmartDLC DVPL File Based On LZ4 High Compression.'

# DVPLFooter represents the footer structure of a DVPL file
class DVPLFooter:
    def __init__(self, original_size, compressed_size, crc32, type_val):
        self.original_size = original_size
        self.compressed_size = compressed_size
        self.crc32 = crc32
        self.type = type_val

# createDVPLFooter creates a DVPL footer from the provided data.
def createDVPLFooter(input_size, compressed_size, crc32_val, type_val):
    result = bytearray(DVPL_FOOTER_SIZE)
    writeLittleEndianUint32(result, input_size, 0)
    writeLittleEndianUint32(result, compressed_size, 4)
    writeLittleEndianUint32(result, crc32_val, 8)
    writeLittleEndianUint32(result, type_val, 12)
    result[16:] = DVPL_FOOTER
    return result

# readDVPLFooter reads the DVPL footer data from a DVPL buffer.
def readDVPLFooter(buffer):
    if len(buffer) < DVPL_FOOTER_SIZE:
        raise ValueError(Color.RED + "InvalidDVPLFooter: Buffer size is smaller than expected" + Color.RESET)

    footer_buffer = buffer[-DVPL_FOOTER_SIZE:]

    if footer_buffer[16:] != DVPL_FOOTER:
        raise ValueError(Color.RED + "InvalidDVPLFooter: Footer signature mismatch" + Color.RESET)

    original_size = readLittleEndianUint32(footer_buffer, 0)
    compressed_size = readLittleEndianUint32(footer_buffer, 4)
    crc32_val = readLittleEndianUint32(footer_buffer, 8)
    type_val = readLittleEndianUint32(footer_buffer, 12)

    return DVPLFooter(original_size, compressed_size, crc32_val, type_val)

# writeLittleEndianUint32 writes a little-endian uint32 value to a byte array at the specified offset.
def writeLittleEndianUint32(b, v, offset):
    b[offset:offset+4] = v.to_bytes(4, 'little')

# readLittleEndianUint32 reads a little-endian uint32 value from a byte array at the specified offset.
def readLittleEndianUint32(b, offset):
    return int.from_bytes(b[offset:offset+4], 'little')

# CompressDVPL compresses a buffer and returns the processed DVPL file buffer.
def CompressDVPL(buffer):
    # Compress the data
    compressed_block = lz4.block.compress(buffer, store_size=False)

    # Create DVPL footer
    footer_buffer = createDVPLFooter(len(buffer), len(compressed_block), zlib.crc32(compressed_block), DVPL_TYPE_LZ4)

    # Append footer to the compressed data
    return compressed_block + footer_buffer

# DecompressDVPL decompresses a DVPL buffer and returns the uncompressed file buffer.
def DecompressDVPL(buffer):
    footer_data = readDVPLFooter(buffer)

    target_block = buffer[:-DVPL_FOOTER_SIZE]

    if len(target_block) != footer_data.compressed_size:
        raise ValueError(Color.RED + "DVPLSizeMismatch" + Color.RESET)

    if zlib.crc32(target_block) != footer_data.crc32:
        raise ValueError(Color.RED + "DVPLCRC32Mismatch" + Color.RESET)

    if footer_data.type == DVPL_TYPE_NONE:
        if footer_data.original_size != footer_data.compressed_size or footer_data.type != DVPL_TYPE_NONE:
            raise ValueError(Color.RED + "DVPLTypeSizeMismatch" + Color.RESET)
        return target_block

    elif footer_data.type == DVPL_TYPE_LZ4:
        deDVPL_block = lz4.block.decompress(target_block, uncompressed_size=footer_data.original_size)
        if len(deDVPL_block) != footer_data.original_size:
            raise ValueError(Color.RED + "DVPLDecodeSizeMismatch" + Color.RESET)
        return deDVPL_block

    else:
        raise ValueError(Color.RED + "UNKNOWN DVPL FORMAT" + Color.RESET)

def ConvertDVPLFiles(directory_or_file, config):
    # Initialize counters
    success_count = 0
    failure_count = 0
    ignored_count = 0

    info = os.stat(directory_or_file)

    if os.path.isdir(directory_or_file):
        dir_list = os.listdir(directory_or_file)
        for dir_item in dir_list:
            succ, fail, ignored, _ = ConvertDVPLFiles(os.path.join(directory_or_file, dir_item), config)
            success_count += succ
            failure_count += fail
            ignored_count += ignored
    else:
        is_decompression = config.mode == "decompress" and directory_or_file.endswith(".dvpl")
        is_compression = config.mode == "compress" and not directory_or_file.endswith(".dvpl")

        ignore_extensions = config.ignore.split(",") if config.ignore else []

        should_ignore = any(directory_or_file.endswith(ext) for ext in ignore_extensions)

        if not should_ignore and (is_decompression or is_compression):
            file_path = directory_or_file
            try:
                with open(file_path, "rb") as f:
                    file_data = f.read()

                if is_compression:
                    processed_block = CompressDVPL(file_data)
                    new_name = file_path + ".dvpl"
                else:
                    processed_block = DecompressDVPL(file_data)
                    new_name = os.path.splitext(file_path)[0]

                with open(new_name, "wb") as f:
                    f.write(processed_block)

                if not config.keep_originals:
                    os.remove(file_path)

                success_count += 1
                if config.verbose:
                    print(f"{Color.GREEN}\nFile{Color.RESET} {file_path} has been successfully {'{Color.GREEN}compressed{Color.RESET}' if is_compression else '{Color.GREEN}decompressed{Color.RESET}'} into {Color.GREEN}{new_name}{Color.RESET}")
            except Exception as e:
                failure_count += 1
                if config.verbose:
                    print(f"{Color.RED}\nError{Color.RESET} processing file {file_path}: {e}")
        else:
            ignored_count += 1
            if config.verbose:
                print(f"{Color.YELLOW}\nIgnoring{Color.RESET} file {directory_or_file}")

    return success_count, failure_count, ignored_count, None

def VerifyDVPLFiles(directory_or_file, config):
    # Initialize counters
    success_count = 0
    failure_count = 0
    ignored_count = 0

    info = os.stat(directory_or_file)

    if os.path.isdir(directory_or_file):
        dir_list = os.listdir(directory_or_file)
        for dir_item in dir_list:
            succ, fail, ignored, _ = VerifyDVPLFiles(os.path.join(directory_or_file, dir_item), config)
            success_count += succ
            failure_count += fail
            ignored_count += ignored
    else:
        is_dvpl_file = directory_or_file.endswith(".dvpl")

        ignore_extensions = config.ignore.split(",") if config.ignore else []

        should_ignore = any(directory_or_file.endswith(ext) for ext in ignore_extensions)

        if not should_ignore and is_dvpl_file:
            file_path = directory_or_file
            try:
                with open(file_path, "rb") as f:
                    file_data = f.read()

                footer_data = readDVPLFooter(file_data)

                # Extract compressed block
                target_block = file_data[:-DVPL_FOOTER_SIZE]

                # Check if compressed size matches the footer
                if len(target_block) != footer_data.compressed_size:
                    raise ValueError(Color.RED + "DVPLSizeMismatch" + Color.RESET)

                # Check CRC32 checksum
                if zlib.crc32(target_block) != footer_data.crc32:
                    raise ValueError(Color.RED + "DVPLCRC32Mismatch" + Color.RESET)

                if config.verbose:
                    print(f"{Color.GREEN}\nFile{Color.RESET} {file_path} has been successfully {Color.GREEN}verified.{Color.RESET}")

                success_count += 1
            except Exception as e:
                failure_count += 1
                if config.verbose:
                    print(f"{Color.RED}\nError{Color.RESET} verifying file {file_path}: {e}")
        else:
            ignored_count += 1
            if config.verbose:
                print(f"{Color.YELLOW}\nIgnoring{Color.RESET} file {directory_or_file}")

    return success_count, failure_count, ignored_count, None

def PrintElapsedTime(elapsed_time):
    if elapsed_time < 1:
        print(f"\nProcessing took {Color.GREEN}{int(elapsed_time * 1000)} ms{Color.RESET}\n")
    elif elapsed_time < 60:
        print(f"\nProcessing took {Color.YELLOW}{int(elapsed_time)} s{Color.RESET}\n")
    else:
        print(f"\nProcessing took {Color.RED}{int(elapsed_time / 60)} min{Color.RESET}\n")

def ParseCommandLineArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-m", "--mode", help="mode can be 'compress' / 'decompress' / 'help' (for an extended help guide).")
    parser.add_argument("-k", "--keep-originals", action="store_true", help="keep original files after compression/decompression.")
    parser.add_argument("-v", "--verbose", action="store_true", help="shows verbose information for all processed files.")
    parser.add_argument("-p", "--path", help="directory/files path to process. Default is the current directory.")
    parser.add_argument("-i", "--ignore", default="", help="Comma-separated list of file extensions to ignore during compression.")
    args = parser.parse_args()

    if not args.mode:
        raise ValueError("No mode selected. Use '--help' for usage information")

    if not args.path:
        args.path = os.getcwd()

    return args

def PrintHelpMessage():
    print('''dvplx [-mode] [-keep-originals] [-path]

    • mode can be one of the following:

        compress: compresses files into dvpl.
        decompress: decompresses dvpl files into standard files.
        verify: verify compressed dvpl files to determine valid compression.
        help: show this help message.

    • flags can be one of the following:

        --keep-originals: flag keeps the original files after compression/decompression.
        --path: specifies the directory/files path to process. Default is the current directory.
        --ignore: specifies comma-separated file extensions to ignore during compression.
        --verbose: shows verbose information for all processed files.

    • usage can be one of the following examples:

        $ dvplx --mode help

        $ dvplx --mode decompress --path /path/to/decompress/compress

        $ dvplx --mode compress --path /path/to/decompress/compress

        $ dvplx --mode decompress --keep-originals -path /path/to/decompress/compress

        $ dvplx --mode compress --keep-originals -path /path/to/decompress/compress

        $ dvplx --mode decompress --path /path/to/decompress/compress.yaml.dvpl

        $ dvplx --mode compress --path /path/to/decompress/compress.yaml

        $ dvplx --mode decompress --keep-originals --path /path/to/decompress/compress.yaml.dvpl

        $ dvplx --mode dcompress --keep-originals --path /path/to/decompress/compress.yaml

        $ dvplx --mode compress --path /path/to/decompress --ignore .exe,.dll

        $ dvplx --mode compress --path /path/to/decompress --ignore exe,dll

        $ dvplx --mode compress --path /path/to/decompress --ignore test.exe,test.txt
    ''')

def main():
    print("\n")
    print(f"{Color.BLUE}• Name:{Color.RESET} {Meta.NAME}")
    print(f"{Color.BLUE}• Version:{Color.RESET} {Meta.VERSION}")
    print(f"{Color.BLUE}• Commit:{Color.RESET} {Meta.DATE}")
    print(f"{Color.BLUE}• Dev:{Color.RESET} {Meta.DEV}")
    print(f"{Color.BLUE}• Repo:{Color.RESET} {Meta.REPO}")
    print(f"{Color.BLUE}• Web:{Color.RESET} {Meta.WEB}")
    print(f"{Color.BLUE}• Info:{Color.RESET} {Meta.INFO}")
    # print("\n")

    start_time = time.time() # Record start time

    config = ParseCommandLineArgs()

    try:
        if config.mode in ["compress", "decompress"]:
            success_count, failure_count, ignored_count, _ = ConvertDVPLFiles(config.path, config)
            print(f"\n\n{Color.GREEN}{config.mode.upper()} FINISHED{Color.RESET}. Successful conversions: {Color.GREEN}{success_count}{Color.RESET}, Failed conversions: {Color.RED}{failure_count}{Color.RESET}, Ignored conversions: {Color.YELLOW}{ignored_count}{Color.RESET}")
        elif config.mode == "verify":
            success_count, failure_count, ignored_count, _ = VerifyDVPLFiles(config.path, config)
            print(f"\n\n{Color.GREEN}VERIFY FINISHED{Color.RESET}. Successful verifications: {Color.GREEN}{success_count}{Color.RESET}, Failed verifications: {Color.RED}{failure_count}{Color.RESET}, Ignored files: {Color.YELLOW}{ignored_count}{Color.RESET}")
        elif config.mode == "help":
            PrintHelpMessage()
        else:
            raise ValueError("Incorrect mode selected. Use '-help' for information.")
    except Exception as e:
        print(f"\n\n{Color.RED}{config.mode.upper()} FAILED{Color.RESET}: {e}\n")

    elapsed_time = time.time() - start_time # Calculate elapsed time
    PrintElapsedTime(elapsed_time)

if __name__ == "__main__":
    main()
