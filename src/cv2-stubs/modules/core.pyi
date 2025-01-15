import builtins
from abc import abstractmethod
from typing import Any, overload, TypeAlias

retval: TypeAlias = Any
rects: TypeAlias = Any
dst: TypeAlias = Any

__all__ = ["Algorithm", "FileNode", "FileStorage"]

class FileNode(builtins.object):
    def at(self, i) -> retval:
        r"""
        @overload
        @param i Index of an element in the sequence node.
        """

    def empty(self) -> retval:
        r""""""

    def getNode(self, nodename) -> retval:
        r"""
        @overload
        @param nodename Name of an element in the mapping node.
        """

    def isInt(self) -> retval:
        r""""""

    def isMap(self) -> retval:
        r""""""

    def isNamed(self) -> retval:
        r""""""

    def isNone(self) -> retval:
        r""""""

    def isReal(self) -> retval:
        r""""""

    def isSeq(self) -> retval:
        r""""""

    def isString(self) -> retval:
        r""""""

    def keys(self) -> retval:
        r"""
        @brief Returns keys of a mapping node.
        @returns Keys of a mapping node.
        """

    def mat(self) -> retval:
        r""""""

    def name(self) -> retval:
        r""""""

    def rawSize(self) -> retval:
        r""""""

    def real(self) -> retval:
        r"""
        Internal method used when reading FileStorage.
        Sets the type (int, real or string) and value of the previously created node.
        """

    def size(self) -> retval:
        r""""""

    def string(self) -> retval:
        r""""""

    def type(self) -> retval:
        r"""
        @brief Returns type of the node.
        @returns Type of the node. See FileNode::Type
        """

class FileStorage(builtins.object):
    def endWriteStruct(self) -> None:
        r"""
        @brief Finishes writing nested structure (should pair startWriteStruct())
        """

    def getFirstTopLevelNode(self) -> FileNode:
        r"""
        @brief Returns the first element of the top-level mapping.
        @returns The first element of the top-level mapping.
        """

    def getFormat(self) -> int:
        r"""
        @brief Returns the current format.
        * @returns The current format, see FileStorage::Mode
        """

    def getNode(self, nodename) -> retval:
        r"""
        @overload
        """

    def isOpened(self) -> bool:
        r"""
        @brief Checks whether the file is opened.

        @returns true if the object is associated with the current file and false otherwise. It is a
        good practice to call this method after you tried to open a file.
        """

    def open(self, filename: str, flags: int, encoding: str = ...) -> bool:
        r"""
        @brief Opens a file.

        See description of parameters in FileStorage::FileStorage. The method calls FileStorage::release
        before opening the file.
        @param filename Name of the file to open or the text string to read the data from. Extension of the file (.xml, .yml/.yaml or .json) determines its format (XML, YAML or JSON respectively). Also you can append .gz to work with compressed files, for example myHugeMatrix.xml.gz. If both FileStorage::WRITE and FileStorage::MEMORY flags are specified, source is used just to specify the output file format (e.g. mydata.xml, .yml etc.). A file name can also contain parameters. You can use this format, "*?base64" (e.g. "file.json?base64" (case sensitive)), as an alternative to FileStorage::BASE64 flag.
        @param flags Mode of operation. One of FileStorage::Mode
        @param encoding Encoding of the file. Note that UTF-16 XML encoding is not supported currently and you should use 8-bit encoding instead of it.
        """

    def release(self) -> None:
        r"""
        @brief Closes the file and releases all the memory buffers.

        Call this method after all I/O operations with the storage are finished.
        """

    def releaseAndGetString(self) -> retval:
        r"""
        @brief Closes the file and releases all the memory buffers.

        Call this method after all I/O operations with the storage are finished. If the storage was
        opened for writing data and FileStorage::WRITE was specified
        """

    def root(self, streamidx: int = ...) -> FileNode:
        r"""
        @brief Returns the top-level mapping
        @param streamidx Zero-based index of the stream. In most cases there is only one stream in the file. However, YAML supports multiple streams and so there can be several. @returns The top-level mapping.
        """

    @overload
    def startWriteStruct(self, name: str, flags: int, typeName: str = ...) -> None:
        r"""
        @brief Starts to write a nested structure (sequence or a mapping).
        @param name name of the structure. When writing to sequences (a.k.a. "arrays"), pass an empty string.
        @param flags type of the structure (FileNode::MAP or FileNode::SEQ (both with optional FileNode::FLOW)).
        @param typeName optional name of the type you store. The effect of setting this depends on the storage format. I.e. if the format has a specification for storing type information, this parameter is used.
        """

    @overload
    def startWriteStruct(self, name, flags, typeName=...) -> None:
        r"""
        * @brief Simplified writing API to use with bindings.
        * @param name Name of the written object. When writing to sequences (a.k.a. "arrays"), pass an empty string.
        * @param val Value of the written object.
        """

    def writeComment(self, comment: str, append: bool = ...) -> None:
        r"""
        @brief Writes a comment.

        The function writes a comment into file storage. The comments are skipped when the storage is read.
        @param comment The written comment, single-line or multi-line
        @param append If true, the function tries to put the comment at the end of current line. Else if the comment is multi-line, or if it does not fit at the end of the current line, the comment starts a new line.
        """

class Algorithm(builtins.object):
    @abstractmethod
    def clear(self) -> None:
        r"""
        @brief Clears the algorithm state
        """

    @abstractmethod
    def empty(self) -> bool:
        r"""
        @brief Returns true if the Algorithm is empty (e.g. in the very beginning or after unsuccessful read
        """

    @abstractmethod
    def getDefaultName(self) -> str:
        r"""
        Returns the algorithm string identifier.
        This string is used as top level xml/yml node tag when the object is saved to a file or string.
        """

    def read(self, fn: FileNode) -> None:
        r"""
        @brief Reads algorithm parameters from a file storage
        """

    @abstractmethod
    def save(self, filename: str) -> None:
        r"""
        Saves the algorithm to a file.
        In order to make this method work, the derived class must implement Algorithm::write(FileStorage& fs).
        """

    @overload
    def write(self, fs: FileStorage) -> None:
        r"""
        @brief Stores algorithm parameters in a file storage
        """

    @overload
    def write(self, fs: FileStorage, name: str) -> None:
        r""""""
