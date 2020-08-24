### Name: Karin Sinkevitch
### Date: August 24, 2020
### Course: IT FDN 110A

# Binary Files, Pickle Module, and the Exception Class

1.	Introduction
This document provides a brief introduction to binary files, the pickle module to read and write binary files, and using the exception class in Python.  Reference information can be used to learn more and view examples on these topics. An example script is then described to show how these methods can be applied.

2.	Binary Files in Python
Binary files store data in a sequence of bytes grouped into eight bits or sometimes sixteen bits. These bits represent custom data and multiple types of data (images, audio, text, etc) can be stored in a single file. Binary files can have custom file formats that must be well understood by any supporting applications.  A common example of a binary file is the image file types .PNG or .JPG.
(Reference https://www.thecrazyprogrammer.com/2018/05/difference-between-text-file-and-binary-file.html).

2.1.	Binary Versus Text Files
Text files are special subset of binary files that are used to store human readable characters as a rich text document or plain text document. Text files also store data in sequential bytes but the bits in text file represents characters. Text files are of two types: plain text files and rich text files. Both text files store end of line and end of file markers. Figure 1 lists the main differences between binary and text files. (Reference https://www.thecrazyprogrammer.com/2018/05/difference-between-text-file-and-binary-file.html).

 
Figure 1 Differences Between Text and Binary File
