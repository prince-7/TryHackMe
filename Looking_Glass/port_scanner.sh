#!/bin/bash
for port in {9000..13000}
do
	ssh -o StrictHostKeyChecking=no -p $port $1
	printf $port
done