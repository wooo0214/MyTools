https://missing.csail.mit.edu/

# Proficiency with your tools

11 lectures, each one centering on a specific topic.

How to master the command-line, use a powerful text editor, use fancy features of version control systems, and much more!

## Topic 1: The shell

`Exercises completed`

Launching the shell from ubuntu that I installed previously for linux. 

### scripts tips

- check if a directory exists
    > $ [ -d "/tmp/missing/" ] && echo yes!
- space matters   
    use `$ cd ..` instead of `$ cd..`
- cat   
    When given file names as arguments, it prints the contents of each of the files in sequence to its output stream. But when cat is not given any arguments, it prints contents from its input stream to its output stream.   
    `cat > a` - print/save the input into file a    
    `cat < a` - print content of file a

### concepts

- ~ vs /    
    You are in the user's home directory when you see ~$ and the "top level" or "root" directory when you see /$. You can use `cd ~` or `cd /` to switch between them.
- sh vs BASH   
    https://stackoverflow.com/questions/5725296/difference-between-sh-and-bash