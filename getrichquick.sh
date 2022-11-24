#!/bin/bash

echo "What is your name?"

read name

echo "How old are you?"

read age
echo ""
echo "Calculating"
sleep 2

echo "*.........."
sleep 1

echo "****........"
sleep 1

echo "********...."
sleep 1

echo "***********."
sleep 3

echo "************"
sleep 1

echo ""
echo ">>COMPLETE<<"
sleep 2

getrich=$((( $RANDOM % 15 ) + $age ))

echo "Hello $name, you'll be rich at the age $getrich."
