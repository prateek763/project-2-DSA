import sys
import collections


class Node(object):

    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    @staticmethod
    def fusion_nodes(node_1, node_2):
        combined_node = Node()

        if node_1.freq <= node_2.freq:
            combined_node.left = node_1
            combined_node.right = node_2
        else:
            combined_node.left = node_1
            fcombined_node.right = node_2

        combined_node.freq = node_1.freq + node_2.freq

        return combined_node

    def __repr__(self):
        return "Node of character: {} | frequency: {}".format(self.char, self.freq)


class Queue(object):
    def __init__(self, string):
        _c = collections.Counter(string)
        self.arr = [Node(char=letter, freq=_c[letter]) for letter in _c]
        self.sort()

    def sort(self) -> None:
        self.arr = sorted(self.arr, key=lambda x: x.freq, reverse=True)

    def fuse_step(self) -> None:
        node1 = self.arr.pop()
        node2 = self.arr.pop()

        self.arr.append(Node.fusion_nodes(node_1=node1, node_2=node2))
        self.sort()


class Tree(object):
    def __init__(self, queue):
        while len(queue.arr) > 1:
            queue.fuse_step()

        self.root = queue.arr[0]

    def binaryze(self) -> None:
        self.root = self._add_binary_code(self.root)
        self.root.freq = 0

    @staticmethod
    def _add_binary_code(node: Node) -> Node:
        if (node.left is None) and (node.right is None):
            return node

        if node.left is not None:
            node.left.freq = 1
            node.left = Tree._add_binary_code(node.left)

        if node.right is not None:
            node.right.freq = 0
            node.right = Tree._add_binary_code(node.right)

        return node


class HuffmanEncoder(object):
    def __init__(self, tree: Tree):
        self.table = self._create_encoding_table(base_code='', node=tree.root)
        self.encode_dict = None
        self.decode_dict = None

        self._create_encoder()
        self._create_decoder()

    def _create_encoder(self) -> None:
        encoder_dict = dict()

        for i, element in enumerate(self.table):
            encoder_dict[element[0]] = element[1]

        self.encode_dict = encoder_dict

    def _create_decoder(self) -> None:
        decoder_dict = dict()

        for i, element in enumerate(self.table):
            decoder_dict[element[1]] = element[0]

        self.decode_dict = decoder_dict

    def encode(self, text: str) -> str:
        coded_text = ''
        for char in text:
            coded_text += self.encode_dict[char]

        return coded_text

    def decode(self, encoded_text: str) -> str:
        decoded_text = ''

        while len(encoded_text) > 0:
            i_decoder = 1
            while True:
                if encoded_text[:i_decoder] in self.decode_dict.keys():
                    decoded_text += self.decode_dict[encoded_text[:i_decoder]]
                    encoded_text = encoded_text[i_decoder:]
                    break
                i_decoder += 1

        return decoded_text

    @staticmethod
    def _create_encoding_table(base_code: str, node: Node) -> list:
        if (node.left is None) and (node.right is None):
            return [(node.char, base_code + str(node.freq))]

        if node.freq == -1:
            current_code = ''
        else:
            current_code = base_code + str(node.freq)

        coding_dict = []

        if node.char is not None:
            coding_dict.append((node.char, current_code + str(node.freq)))

        if node.left is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(current_code, node.left))

        if node.right is not None:
            coding_dict.extend(HuffmanEncoder._create_encoding_table(current_code, node.right))

        return coding_dict


def huffman_encoding(data: str) -> (str, HuffmanEncoder):
    if len(data) == 0:
        print("Please introduce a non null string")
        return

    else:
        temp_queue = Queue(string=data)
        temp_tree = Tree(queue=temp_queue)
        temp_tree.binaryze()
        temp_encoder = HuffmanEncoder(temp_tree)

        return temp_encoder.encode(data), temp_encoder


def huffman_decoding(data: str, encoder: HuffmanEncoder) -> str:
    return encoder.decode(data)


#%% Testing official
if __name__ == "__main__":
    # Case 1

    a_great_sentence = "My name is prateek"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output:-The size of the data is: 43
    print("The content of the data is: {}\n".format(a_great_sentence))
    # Output:-The content of the data is: My name is prateek

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output:-The size of the encoded data is: 24
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # Output:-The content of the encoded data is: 0001011011101000111001010010011000000001000011101110100110001111010010

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output:-The size of the decoded data is: 43
    print("The content of the decoded data is: {}\n".format(decoded_data))
    # Output:-The content of the decoded data is: My name is prateek

    # Case 2

    a_great_sentence = "I love coding a lot"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output:-The size of the data is: 44
    print("The content of the data is: {}\n".format(a_great_sentence))
    # Output:-The content of the data is: I love coding a lot

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output:-The size of the encoded data is: 24
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # Output:-The content of the encoded data is: 00110110011100010010010111001011000000010111101100111010101000010110100
    # 0110100100010000110111010010111101100000001101

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output:-The size of the decoded data is: 44
    print("The content of the decoded data is: {}\n".format(decoded_data))
    # Output:-The content of the decoded data is: I love coding a lot

    # Case 3

    a_great_sentence = "The sun shines and I go to the beach"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Output:-The size of the data is: 61
    print("The content of the data is: {}\n".format(a_great_sentence))
    # Output:-The content of the data is: The sun shines and I go to the beach

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output:-The size of the encoded data is: 36
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # Output:-The content of the encoded data is: 0100100110011100100001010011000100
    #01000010110010000000100111000010010001100010010001001010110001010111000000001000
    #001000000001000001011001110010101000111000110101010110

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output:-The size of the decoded data is: 61
    print("The content of the decoded data is: {}\n".format(decoded_data))
    # Output:-The content of the decoded data is: The sun shines and I go to the beach

    # Edge Cases
    # Case 4

    a_not_so_great_sentence = "aaa"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_not_so_great_sentence)))
    # Output:-The size of the data is: 28
    print("The content of the data is: {}\n".format(a_not_so_great_sentence))
    # Output:-The content of the data is: aaa

    encoded_data, tree = huffman_encoding(a_not_so_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Output:-The size of the encoded data is: 12
    print("The content of the encoded data is: {}\n".format(encoded_data))
    # Output:-The content of the encoded data is: 000

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Output:-The size of the decoded data is: 28
    print("The content of the decoded data is: {}\n".format(decoded_data))
    # Output:-The content of the decoded data is: aaa

    # Case 5
    a_not_so_great_sentence = ""

    print("The size of the data is: {}\n".format(sys.getsizeof(a_not_so_great_sentence)))
    # Output:-The size of the data is: 25
    print("The content of the data is: {}\n".format(a_not_so_great_sentence))
    # Output:-The content of the data is:

    huffman_encoding(a_not_so_great_sentence)
    # Output:-Please introduce a non null string
