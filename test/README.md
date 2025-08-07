For basic testing purposes to see if this actually works we will need to
create this small a small test program that has a sysblk structure created.
The structure for our purposes will have only a max_cpu_threads member. We
can add additional members as needed but I only want to do a 'info zthreads'
to show that the extension would actually work in a full SDM environment.

* if not aready done create a symlink to the gdb extension directory
* * ln -s ${HOME}/workspaces/gdb-zos-disassembler-plugin/gdb /opt/lzlabs/debug/gdb
* compile the test.c code
* * clang -o tsdm -g test.c
* execute the gdb debugging script
* * gdb -ex test.gdb -r "tsdm"
