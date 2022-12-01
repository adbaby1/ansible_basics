#!/usr/bin/env python
#
# Dynamic inventory script for  simple binds
# 
# 
# Copyright 2017 Red Hat, Inc.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
#    1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#
#    2. Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.




# THIS SOFTWARE IS PROVIDED BY RED HAT, INC. ``AS IS'' AND ANY EXPRESS
# OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL RED HAT, INC. BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
# HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
# STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING
# IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

##
# Configuration settings
##


from subprocess import Popen,PIPE
import sys
import json

result = {}
result['webservers'] = {}
result['webservers']['hosts'] = []
result['webservers']['vars'] = {}
result['lbservers'] = {}
result['lbservers']['hosts'] = []
result['lbservers']['vars'] = {}

pipe = Popen(['getent', 'hosts'], stdout=PIPE, universal_newlines=True)

for line in pipe.stdout.readlines():
   s = line.split()
   if s[1].startswith('servere'):
      result['webservers']['hosts'].append(s[1])
   if s[1].startswith('serverf'):
      result['webservers']['hosts'].append(s[1])
   if s[1].startswith('serverd'):
      result['lbservers']['hosts'].append(s[1])


if __name__ == '__main__':
   if len(sys.argv) == 2 and sys.argv[1] == '--list':
      print(json.dumps(result))
   elif len(sys.argv) == 3 and sys.argv[1] == '--host':
      print(json.dumps({}))
   else:
      print("Requires an argument, please use --list or --host <host>")
