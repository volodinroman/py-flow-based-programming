# PyFBP (Uncompleted project)

Python Flow Based Programming project, that I wrote in parallel with reading "Flow Based Programming" book written by J. Paul Morrison (http://www.jpaulmorrison.com/fbp/index_old.shtml)

This project has no end and it was a private until now, so I decided to share it with public and hopefully will implement some other ideas here sooner or later.

This is a standalone Python project, that requires no extra packages or specific environment.

I wrote it with Python 2.7, so you might need to change some specific lines of code (usually it's **print** command).

Feel free to fork it, modify it, remove it, explode it, melt it, smash it or cook it \m/_

### What works now

* It actually works now and can be implemented in some other project.
* It runs the stream of nodes in a single thread
* It supports loops 
* In main.py you will see the test setup, where I created nodes, plugs, connected them and run them
* Every node does the same thing - taked all input plugs with numbers passed in, sums it up and pushed forward. So it's a "Node Based Sum Calculator". But in the future every node will be a separate class with it's own computing methods.


### How to run it

* Make sure this project is under the PYTHONPATH
* Just run main.py - it will do the rest and will print some debugging info 
