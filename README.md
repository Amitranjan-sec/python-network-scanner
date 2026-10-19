# Python Network Scanner

A lightweight command-line network scanning tool built from scratch in Python using *Scapy*. This tool sends custom ARP requests to discover live hosts on a local network and maps their IP and MAC addresses.

---

## Features
**ARP Packet Crafting:** Uses Scapy to broadcast ARP requests and capture responses.
**Command-Line Interface:** Uses 'argparse' to accept target IP ranges directly from the terminal.
**Structured Output:** Cleans up raw packet data to display active IP and MAC pairs neatly in a table format.

---

## Prerequisites & Dependencies

Make sure you have **Python 3** installed on your system. This tool also requires **Scapy**, which may need administrative/root privileges to send and receive raw network packets.

Install the required library via pip:
```bash
pip install scapy
