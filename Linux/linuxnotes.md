https://www.coursera.org/learn/linux-fundamentals/lecture/IpRos/specialization-overview

1. Unix was owned and licensed by Bell Labs.
1. FSF created GNU tools as part of GNU project.
1. Linus Torvalds created Linux Kernel and used the GNU Tools.


Linux Distributions

- Red Hat
- Fedora
- SUSE
- ubuntu

## Linux Command Line

https://www.javatpoint.com/linux-commands

https://www.linuxjournal.com/content/linux-command-line-interface-introduction-guide

> pwd, returns the path of the current working directory
cd, change directory
ls, view the contents of a directory
cat, list the contents of a file
cp, copy 
mv, move or rename
mkdir, create a new directory
rm, remove

## Server and Desktop
Linux servers: it has programs designed around background services that share resources. (background process/ spawned by a parent program)
- Deamon: a linux service runs continually as a background process. Often end with the letter d, for example mysqld.
- Major service types: 
    - File server
    - Web server - Listen on port 80 and 443 for incoming requests and assign the request to a process to return the response. 
        - apache, nginX, Lighttpd
        https://kinsta.com/blog/nginx-vs-apache/
    - Database server (CRUD: Creat, Read, Update, Delete) - listen for request and respond with the data
        - relational: transactional focused, for example: PostgreSQL, MySQL
        - NoSQL: Document focused, for example: MongoDB
    - Print server
    - Network resource server (DHCP, logging, etc)

Linux Desktop: it has programs designed around GUI interactive applications.

Managing services
- Init 
> readlink –f
/usr/sbin/init
- Systemd https://en.wikipedia.org/wiki/Systemd
> sudo systemctl start [application.server]

## Files and Directories

### View, create, move, copy and remove files
> ls [options] [paths]

> Touch - 
Update time and date of file, it can create new files.

> cat > filename creates a new file   
cat filename1 filename2>filename3 joins two files and stores the
output of them in a new file

> pr –m file1.txt file2.txt     
-m: print all files in parallel, one in each column

> grep -i aspen /etc/passwd , Help you find a file line (or lines) that contain certain text strings.  
-i: ignore case

> head, tail, pager

### compare and find files

> diff, locate, find

Hard Link - A file (or directory) with one index (inode) number and at least two different file names.
> Filename1 -> inode #[] <- Filename2

To create a hardlink: `ln [originalfilename] [linkname]`

Soft Link - A file with different index (inode) numbers. The soft link file points to other file.
> Filename1 inode #[] -> Filename2 inode #[]

To create a softlink: `ln –s [originalfilename] [linkname]`

- If you delete the original file with a hardlink, the link still works.
- If you delete the oritinal file with a softlink, the link will be broken.
- You can link both files and folders.
