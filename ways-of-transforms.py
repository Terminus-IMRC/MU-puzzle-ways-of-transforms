#!/usr/bin/env python3

import sys

hs = []
max_level = 0
count_all_transforms = 0
count_all_nodes = 0
count_tail = 0

def add_entry(id, s, sn, level):
	global hs, max_level
	global count_all_transforms, count_all_nodes, count_tail

	if id == 0:
		print('%s;' % (sn))
	else:
		count_all_transforms += 1
		print('%s -> %s [label = "r%d"];' % (s, sn, id))
	
	if level == max_level:
		count_tail += 1

	h = hash(sn)
	try:
		hs.index(h)
	except ValueError:
		pass
	else:
		return
	hs.append(h)

	count_all_nodes += 1

	if level < max_level:
		rule_1(sn, level + 1)
		rule_2(sn, level + 1)
		rule_3(sn, level + 1)
		rule_4(sn, level + 1)

def rule_1(s, level):
	if s[-1] != 'I':
		return
	sn = s + 'U'
	add_entry(1, s, sn, level)

def rule_2(s, level):
	if s[0] != 'M':
		return
	sn = s + s[1:]
	add_entry(2, s, sn, level)

def rule_3(s, level):
	i = s.find('III')
	while i != -1:
		sn = s[0:i] + 'U' + s[i + 3:]
		add_entry(3, s, sn, level)
		i = s.find('III', i + 1)

def rule_4(s, level):
	i = s.find('UU')
	while i != -1:
		sn = s[0:i] + s[i + 2:]
		add_entry(4, s, sn, level)
		i = s.find('UU', i + 1)

def main():
	global max_level

	if len(sys.argv) != 1 + 2:
		print('Usage: %s [MUI string] [n]' % (sys.argv[0]), file = sys.stderr)
		exit(1)
	
	s = sys.argv[1]
	max_level = int(sys.argv[2])

	s = s.upper()

	sn = s
	sn = sn.replace('M', '')
	sn = sn.replace('U', '')
	sn = sn.replace('I', '')
	if len(sn) != 0:
		print('error: input string is not MUI-system string', file = sys.stderr)
		exit(1)
	
	print('digraph %s {' % (s))
	add_entry(0, '', s, 0)
	print('}')

	print('count_all_transforms:', count_all_transforms, file = sys.stderr)
	print('count_all_nodes:', count_all_nodes, file = sys.stderr)
	print('count_tail:', count_tail, file = sys.stderr)

if __name__ == '__main__':
	main()
