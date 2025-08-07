typedef struct SYSBLK {
    int max_cpu_threads;
    int regs[10];
} SYSBLK;

SYSBLK sysblk;

int main( ) {
    return( 0 );
}
