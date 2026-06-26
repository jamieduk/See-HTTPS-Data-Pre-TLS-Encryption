````markdown
# How Attackers See HTTPS Data Before TLS Encryption

Demonstration showing how plain-text data can be observed **before** TLS encryption by tracing OpenSSL's `SSL_write_ex()` function with **bpftrace**.

> **Educational purposes only.** This project demonstrates why endpoint security matters. TLS protects data **in transit**, but applications must handle sensitive data before it is encrypted.

**GitHub:** https://github.com/jamieduk/See-HTTPS-Data-Pre-TLS-Encryption

**Website:** https://jnetai.com

Inspired by:
https://www.youtube.com/watch?v=n9BD4YxiWqM

---

# Features

- Demonstrates where HTTPS data exists before TLS encryption.
- Uses **bpftrace** to hook OpenSSL's `SSL_write_ex()`.
- Includes a secure Python TLS server and client.
- Supports both x86_64 and ARM64 systems.
- Simple setup scripts included.

---

# Quick Start

Make the scripts executable:

```bash
sudo chmod +x *.sh
````

Run the setup:

```bash
./setup.sh
```

Start the interceptor:

```bash
./ssl_intercept.sh
```

ARM64 systems:

```bash
./ssl_intercept_arm.sh
```

Start the secure server:

```bash
./secure_app_start.sh
```

Run the client:

```bash
./login_start.sh
```

---

# Manual Setup

Install bpftrace:

```bash
sudo apt install -y bpftrace
```

Run the interceptor manually:

```bash
bpftrace -e 'uprobe:/path/to/libssl.so:SSL_write_ex { printf("PID %d: %s\n", pid, str(arg1, arg2)); }'
```

Replace:

```
/path/to/libssl.so
```

with the correct OpenSSL library on your system.

---

# Finding the Correct OpenSSL Library

Locate your installed OpenSSL library:

```bash
ldconfig -p | grep libssl
```

Example output:

```
libssl3.so (libc6,AArch64) => /lib/aarch64-linux-gnu/libssl3.so
libssl3.so (libc6,hard-float) => /lib/arm-linux-gnueabihf/libssl3.so
libssl.so.3 (libc6,AArch64) => /lib/aarch64-linux-gnu/libssl.so.3
libssl.so.3 (libc6,hard-float) => /lib/arm-linux-gnueabihf/libssl.so.3
libssl.so (libc6,AArch64) => /lib/aarch64-linux-gnu/libssl.so
```

Use the appropriate library path in the bpftrace command.

---

# Example Python Programs

The repository includes:

* `secure_app.py`
* `login.py`

These provide a minimal HTTPS server and client for demonstrating the interception.

---

# Testing

## 1. Generate a self-signed certificate

```bash
openssl req -new -x509 -days 365 -nodes -out cert.pem -keyout key.pem
```

## 2. Start the interceptor

Use either:

```bash
./ssl_intercept.sh
```

or

```bash
./ssl_intercept_arm.sh
```

Alternatively run the manual `bpftrace` command.

## 3. Start the HTTPS server

```bash
python3 secure_app.py
```

## 4. Run the client

```bash
python3 login.py
```

## 5. Observe the output

The interceptor will display the plain-text data before OpenSSL encrypts it, for example:

```
PID 12345:
user:mysecretpassword
```

After this point the data is encrypted by TLS and transmitted securely across the network.

---

# How It Works

The client passes application data to OpenSSL.

```
Application
      │
      ▼
SSL_write_ex()
      │
      │  <-- bpftrace intercepts here
      ▼
TLS Encryption
      ▼
Encrypted Network Traffic
```

The demonstration shows that endpoint monitoring can observe sensitive information before encryption occurs.

---

# Requirements

* Linux
* Python 3
* OpenSSL
* bpftrace
* Root privileges (for bpftrace)

---

# Disclaimer

This project is intended **solely for education, security research, and defensive testing** on systems that you own or have explicit permission to analyse.

Do **not** use these techniques on systems or networks without proper authorisation.

---

# License

MIT License

```
```

