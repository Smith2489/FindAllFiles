This program was written in Python 3.1.3 using Visual Studio Code
<br>
<br>
When you run it, you will be prompted with a sequence of options*. Then, the program will generate a list of files
<br>
relative to a path and print it either to the console or a file.
<br>
If you choose to print to a file, you will be prompted to provide a name for the file after the string is created
<br>
If a file by the provided name already exists, you will be asked if you wish to overwrite it
<br>
<br>
Subdirectories that do not contain any files of interest will not be included
<br>
<br>
*The options are, in order:
<br>
<ul>
    <li>The root of the subdirectory you wish to to explore</li>
    <li>The file type of interest (A blank space or "all" will return all files)</li>
    <li>Whether or not you wish to include the root</li>
    <li>What type of seperator you would like (space or new line)</li>
    <li>Whether or not you want to save to a file or print to the console</li>
    <li>Whether or not you would like to print the subdirectories and their files to the console as it constructs the string</li>
</ul>