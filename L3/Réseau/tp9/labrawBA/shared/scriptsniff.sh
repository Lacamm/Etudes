#!/bin/bash

iptables -t filter -A FORWARD -j DROP
/shared/sniff.py
