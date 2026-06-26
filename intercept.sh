#!/usr/bin/env bash
# (c) J~Net 2026
#
# intercept.sh
#
# /usr/lib/libssl.so.3 for other!

SO_PATH="/lib/aarch64-linux-gnu/libssl.so.3" # ARM64 / RPI OPENSSL

bpftrace -e "
uprobe:${SO_PATH}:SSL_write_ex
{
    printf(\"\n[!] Cleartext Intercepted via SSL_write_ex (PID %d):\n\", pid);
    printf(\"%s\\n\", str(arg1, arg2));
}
"
