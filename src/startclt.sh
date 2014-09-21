#!/bin/bash

num=3 

while(($num > 0))
do
./client &
num=$(($num - 1))
done


