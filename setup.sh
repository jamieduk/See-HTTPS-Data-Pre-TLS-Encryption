#!/bin/bash
# (c) J~Net 2026
#
# ./setup.sh
#
#
#
sudo apt install -y bpftrace

# TLS self-signed cert generation (c) J~Net 2026

openssl req -x509 -newkey rsa:2048 -nodes \
-keyout key.pem \
-out cert.pem \
-days 3650 \
-subj "/CN=localhost"
